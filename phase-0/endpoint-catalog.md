# USDA FoodData Central API — Endpoint Catalog

**Base URL:** `https://api.nal.usda.gov/fdc/v1`  
**Auth:** `?api_key=<key>` query parameter on every request  
**Verified:** 2026-04-18 via live curl calls

---

| Method | Path | Required Params | Optional Params | Auth | Response Envelope | Per 100g or Per Serving | Quirk Notes |
|---|---|---|---|---|---|---|---|
| GET | `/foods/search` | `query`, `api_key` | `dataType[]`, `pageSize` (1–200, def 50), `pageNumber`, `sortBy`, `sortOrder`, `brandOwner` | `api_key` query param | `{totalHits, currentPage, totalPages, pageList, foodSearchCriteria, aggregations, foods: [SearchResultFood]}` | Per 100g (Foundation/SR Legacy); per serving (Branded via LCCS derivation) | Empty query returns 200 + all 468K foods (not an error); `numberOfResultsPerPage` in criteria echo is always 50 regardless of `pageSize`; `dataType` accepts both repeated param and CSV; results skew toward Branded when mixing types; foodNutrients uses flat `value` field (not `amount`) |
| POST | `/foods/search` | `query`, `api_key` | `dataType[]`, `pageSize`, `pageNumber`, `sortBy`, `sortOrder`, `brandOwner`, `tradeChannel[]`, `startDate`, `endDate` | `api_key` query param | Same as GET: `{totalHits, currentPage, totalPages, pageList, foodSearchCriteria, aggregations, foods: [...]}` | Same as GET | POST additionally supports `tradeChannel`, `startDate`, `endDate` (not available on GET); `brandOwner` requires exact stored string match (case-sensitive) |
| GET | `/food/{fdcId}` | `fdcId` (path), `api_key` | `format` (`full`\|`abridged`, def `full`), `nutrients` (array of nutrient numbers, up to 25) | `api_key` query param | Full: typed food object (`BrandedFoodItem`, `FoundationFoodItem`, `SRLegacyFoodItem`, `SurveyFoodItem`); Abridged: `{fdcId, description, dataType, publicationDate, ndbNumber, foodNutrients[flat]}` | Per 100g (Foundation/SR Legacy/Survey); Branded `foodNutrients` derived from per-serving label data (LCCS); `labelNutrients` (Branded only) is per serving | 404 returns empty body (no JSON); full foodNutrients use nested `{nutrient:{number,name,...}, amount}` shape; abridged uses flat `{number, name, amount, unitName}`; category header items have no `amount` field; nutrient numbers are strings; `publicationDate` format inconsistent (M/D/YYYY vs ISO) |
| GET | `/foods` | `fdcIds` (comma-sep or repeated), `api_key` | `format` (`full`\|`abridged`), `nutrients[]` | `api_key` query param | **Bare array** `[FoodItem, ...]` — no envelope | Same as /food/{fdcId} | Max 20 fdcIds; returns bare array (not `{foods:[...]}`); abridged format uses flat nutrient shape |
| POST | `/foods` | `fdcIds` (JSON array), `api_key` | `format`, `nutrients[]` | `api_key` query param | **Bare array** `[FoodItem, ...]` — no envelope | Same as GET /foods | Empty `fdcIds: []` returns `{}` (empty object) with HTTP 200, not an error; max 20 per batch per spec |
| GET | `/foods/list` | `api_key` | `dataType[]`, `pageSize` (1–200, def 50), `pageNumber`, `sortBy`, `sortOrder` | `api_key` query param | **Bare array** `[AbridgedFoodItem, ...]` — no pagination envelope | Per 100g (all types); abridged only | No `totalHits`/`totalPages` in response — cannot determine total count; always returns abridged format; nutrient shape is flat |
| POST | `/foods/list` | `api_key` | Same as GET `/foods/list` via JSON body | `api_key` query param | Same bare array as GET | Same | JSON body mirrors GET params |
| GET | `/json-spec` | `api_key` | — | `api_key` query param | Full OpenAPI 3.0 JSON spec object | N/A | Useful for schema validation and code generation |
| GET | `/yaml-spec` | `api_key` | — | `api_key` query param | Full OpenAPI 3.0 YAML spec | N/A | Alternative format of the spec |

---

## SearchResultFood Fields (from /foods/search)

| Field | Type | Notes |
|---|---|---|
| `fdcId` | integer | Unique FoodData Central ID |
| `description` | string | Food name |
| `dataType` | string | `"Foundation"`, `"SR Legacy"`, `"Branded"`, `"Survey (FNDDS)"` |
| `publishedDate` | string | ISO format |
| `brandOwner` | string | Branded only |
| `gtinUpc` | string | Branded only |
| `ingredients` | string | Branded only |
| `foodNutrients` | array | Flat format: `{nutrientId, nutrientName, nutrientNumber, unitName, value, ...}` |
| `score` | float | Elasticsearch relevance score (undocumented) |
| `foodCategory` | string | Category name |
| `ndbNumber` | string | Foundation/SR Legacy only |
| `allHighlightFields` | string | Raw highlight markup |

## Key Branded-Only Fields on /food/{fdcId} Full

| Field | Type | Notes |
|---|---|---|
| `brandOwner` | string | e.g., `"Original Gourmet Food Company Inc."` |
| `brandName` | string | May be empty string |
| `gtinUpc` | string | Barcode |
| `ingredients` | string | Full ingredient list |
| `servingSize` | float | e.g., `42.5` |
| `servingSizeUnit` | string | e.g., `"g"` |
| `householdServingFullText` | string | e.g., `"1 COOKIE"` |
| `packageWeight` | string | e.g., `"10.5 OZ/298g"` |
| `brandedFoodCategory` | string | Category label |
| `marketCountry` | string | e.g., `"United States"` |
| `labelNutrients` | object | Per-serving: `{fat, saturatedFat, transFat, cholesterol, sodium, carbohydrates, fiber, sugars, protein, calcium, iron, potassium, addedSugar, calories}` each `{value: number}` |
| `discontinuedDate` | string | If product discontinued |

---

## Error Response Shapes

| Scenario | HTTP Status | Body |
|---|---|---|
| Nonexistent fdcId | 404 | Empty string (no JSON) |
| Invalid API key | 200 | `{"error": {"code": "API_KEY_INVALID", "message": "..."}}` |
| Empty fdcIds POST /foods | 200 | `{}` |
| Empty query GET /foods/search | 200 | Full result set (all foods) — not treated as error |
