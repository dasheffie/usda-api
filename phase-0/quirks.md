# USDA FoodData Central API — Quirks (Reality vs. Docs)

Format: `endpoint/field — observed behavior — workaround`

---

## Authentication & Rate Limits

**Rate limit header vs. docs** — Docs say 1,000 req/hr; observed `X-Ratelimit-Limit: 3600` header suggests 3,600/hr from the data.gov gateway layer. The discrepancy may reflect per-key vs. per-IP accounting. — Trust the header; budget for 3,600/hr but don't exceed 1,000 to be safe.

**404 body** — GET /food/{fdcId} with a nonexistent ID returns HTTP 404 with an empty body (no JSON, no error object). — Check `response.status_code == 404` before parsing; do not attempt `json.loads()` on the body.

**Empty fdcIds POST /foods** — Submitting `{"fdcIds": []}` returns HTTP 200 with `{}` (empty JSON object), not an array and not an error. — Validate that fdcIds is non-empty before calling; treat `{}` response as a no-op.

---

## /foods/search Endpoint

**Empty query is NOT an error** — GET /foods/search?query= returns HTTP 200 with all 468,382 foods (effectively a full dump). Docs imply query is required. — Always validate `query` is non-empty in the skill; add `query` to required params.

**numberOfResultsPerPage in criteria echo** — The `foodSearchCriteria` in the response always shows `"numberOfResultsPerPage": 50` regardless of the `pageSize` you sent. The `pageSize` field in criteria correctly echoes your value. — Use `pageSize` from criteria, not `numberOfResultsPerPage`.

**dataType repeated query param vs. CSV** — Both `dataType=Branded&dataType=Foundation` (repeated) and `dataType=Branded,Foundation` (CSV) work identically; both are parsed into `["Branded", "Foundation"]` in the response criteria. — Either syntax is acceptable; repeated param is safer for URL encoding.

**Multi-dataType search results skew toward Branded** — When requesting `dataType=Branded&dataType=Foundation`, the first page of results for `query=apple` returned only Branded items despite both types being requested. Foundation items may appear on later pages due to relevance scoring. — Not a bug, just scoring behavior; filter results by `dataType` field if you need a specific type only.

**dataType must be exact strings including spaces** — `SR Legacy` (with space) and `Survey (FNDDS)` (with parentheses) must be sent exactly. Using `SRLegacy` or `SR_Legacy` returns 0 results. — URL-encode as `SR+Legacy` or `SR%20Legacy`; use `Survey+%28FNDDS%29` for FNDDS.

**brandOwner requires exact match** — Sending `brandOwner=McDonalds` (without apostrophe) returns 0 hits even though McDonald's products exist in the database. The field appears to require the exact string as stored. — Use a search-first approach: search without brandOwner, then filter by `brandOwner` field in results; or use POST /foods/search and treat brandOwner as a substring (behavior not confirmed — exact match observed).

**score field** — Search results include a `score` float field (relevance score from Elasticsearch). This is not documented in the OpenAPI spec but is consistently present. — Useful for ranking but not stable across dataset releases.

**aggregations field** — Search envelope includes an `aggregations` key not documented in swagger. Contains facet counts. — Can be ignored safely.

---

## /food/{fdcId} Endpoint

**FDC ID 1750340 is Foundation, not Branded** — The prompt labeled it as a "Branded item" but it is actually a Foundation food (Apples, fuji, with skin, raw). The actual Branded item tested was fdcId 1955793. — Always check `dataType` field in response rather than assuming from fdcId range.

**foodNutrients shape differs between full and abridged** — Full format uses nested `{nutrient: {id, number, name, rank, unitName}, amount, id, type, foodNutrientDerivation, ...}`. Abridged uses flat `{number, name, amount, unitName, derivationCode, derivationDescription}`. Key rename: `amount` → `amount` (same), but `nutrient.number` → `number`. — Check for presence of `nutrient` key to detect format; write separate parsers for each.

**foodNutrients shape also differs from /foods/search** — Search endpoint uses yet another flat shape with `nutrientId`, `nutrientName`, `nutrientNumber`, `value` (not `amount`), `foodNutrientId`, `indentLevel`. — Three distinct nutrient shapes exist across the API; `value` vs `amount` is the critical difference between search and abridged.

**Nutrient group headers in full response** — foodNutrients array in full format includes category header objects (e.g., `{"nutrient": {"number": "951", "name": "Proximates"}, "type": "FoodNutrient"}`) that have NO `amount` field. These are organizational, not nutritional. — Filter nutrients by presence of `amount` key before processing.

**nutrient.number is a STRING, not integer** — Despite looking numeric, `nutrient.number` is always a string (e.g., `"208"`, `"203"`). Same for `nutrientNumber` in flat format. — Use string comparison for nutrient lookups: `nutrient.number === "208"` not `=== 208`.

**publicationDate format inconsistency** — Some foods use `"4/1/2019"` (M/D/YYYY), others use `"2022-10-28"` (ISO 8601). Foundation foods tend toward ISO; SR Legacy and older entries use M/D/YYYY. — Parse both formats; do not assume ISO.

---

## /foods (Batch) Endpoint

**POST /foods returns bare array, not envelope** — Returns `[FoodItem, FoodItem, ...]` directly, not `{"foods": [...]}`. GET /foods also returns a bare array. — Do not wrap in `.foods` accessor; treat response directly as array.

**Batch size limit** — Swagger spec says "1-20 items" for fdcIds. The docs page also says "up to 20". Not stress-tested beyond 3 in this probe. — Cap at 20 fdcIds per batch call.

**GET /foods abridged response keys** — Returns minimal keys: `fdcId`, `description`, `dataType`, `publicationDate`, optionally `brandOwner`, `gtinUpc`, `ndbNumber`, `foodNutrients`. The abridged foodNutrients here uses the flat format (number, name, amount, unitName).

---

## /foods/list Endpoint

**Returns bare array** — Like /foods batch, returns a bare array of AbridgedFoodItem objects, not a paginated envelope. There is no `totalHits` or `currentPage` in the response. — Cannot determine total count from list endpoint alone; use /foods/search for pagination metadata.

**abridged foodNutrients flat format** — /foods/list always returns the flat nutrient format (number, name, amount, unitName, derivationCode, derivationDescription) regardless of any format parameter.

---

## labelNutrients

**Exclusive to Branded dataType** — labelNutrients is absent on Foundation (fdcId 1750340, 2346393) and SR Legacy (fdcId 171706). Confirmed present on Branded (fdcId 1955793). — Check `dataType === "Branded"` before accessing labelNutrients.

**labelNutrients values are per serving** — Values match the nutrition facts label on the package, scaled to `servingSize`. foodNutrients values on the same Branded item are per 100g. — Use labelNutrients for "what's on the box" display; use foodNutrients / 100 * servingSize for calculations.

**labelNutrients.calories vs. foodNutrients energy** — labelNutrients has `calories` key; to get energy from foodNutrients use nutrient number `"208"`. They should match when scaled to serving size but may differ due to rounding.
