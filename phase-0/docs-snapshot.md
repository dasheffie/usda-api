# USDA FoodData Central API — Docs Snapshot

**Compiled:** 2026-04-18  
**Sources:** api-guide, fdc_api.html (OpenAPI), swaggerhub spec, download-datasets page, live curl responses

---

## 1. Authentication

- **Method:** Query parameter only — `?api_key=<key>`
- **Header auth:** Not supported (no Bearer / Authorization header)
- **Demo key:** `DEMO_KEY` available for low-volume testing
- **Sign-up:** https://api.data.gov/signup
- **Key security:** The key holder is responsible for keeping it private; sharing it publicly is a policy violation

---

## 2. Rate Limits

- **Default cap:** 1,000 requests per hour per IP address
- **Enforcement:** Exceeding the limit causes the API key to be temporarily blocked for 1 hour
- **Observed headers (live):** `X-Ratelimit-Limit: 3600` and `X-Ratelimit-Remaining: <n>` returned on every response — the 3,600 figure likely means per-hour from the underlying data.gov gateway, not 1,000 as stated in prose docs. This is a quirk (see quirks.md).
- **Higher limits:** Contact FDC to request increased rate settings
- **No `Retry-After` header** observed on rate limit responses

---

## 3. DataType Values

| DataType | Exact API string | Description | Update cadence |
|---|---|---|---|
| Foundation | `Foundation` | USDA ARS analytically measured nutrient profiles; highest data density; includes sub-sample details | Bi-annual (Apr + Dec) |
| SR Legacy | `SR Legacy` | Final release of USDA Standard Reference; frozen at April 2018; not updated | Archived, no updates |
| Branded | `Branded` | Commercial product nutrition from manufacturer labels; largest dataset by volume | Bi-annual |
| Survey (FNDDS) | `Survey (FNDDS)` | Aligned with NHANES dietary surveys; updated every 2 years | Every 2 years |
| Experimental | `Experimental` | Listed in browse menus; no download releases documented | Unknown |

**Critical spelling note:** "SR Legacy" requires a space — `SR+Legacy` or `SR%20Legacy` in URL encoding. "Survey (FNDDS)" requires the parenthetical. These exact strings are case-sensitive in practice.

---

## 4. Response Envelopes

### GET/POST /foods/search
```json
{
  "totalHits": 1,
  "currentPage": 1,
  "totalPages": 1,
  "pageList": [1, 2, ...],
  "foodSearchCriteria": {
    "query": "cheddar",
    "dataType": ["Foundation"],
    "pageNumber": 1,
    "pageSize": 3,
    "numberOfResultsPerPage": 50,
    "requireAllWords": false,
    "generalSearchInput": "cheddar",
    "foodTypes": ["Foundation"]
  },
  "aggregations": { ... },
  "foods": [ { SearchResultFood }, ... ]
}
```
Note: `numberOfResultsPerPage` in criteria always echoes `50` even when `pageSize=3` was requested — `pageSize` controls actual page size, `numberOfResultsPerPage` appears to be a separate internal default.

### GET /food/{fdcId} — full format (non-Branded)
```json
{
  "fdcId": 171706,
  "description": "Avocados, raw, California",
  "dataType": "SR Legacy",
  "publicationDate": "4/1/2019",
  "foodClass": "...",
  "ndbNumber": "...",
  "isHistoricalReference": false,
  "foodNutrients": [ { FoodNutrient (nested) }, ... ],
  "foodPortions": [ ... ],
  "foodComponents": [ ... ],
  "foodAttributes": [ ... ],
  "nutrientConversionFactors": [ ... ],
  "inputFoods": [ ... ],
  "foodCategory": { ... }
}
```

### GET /food/{fdcId} — full format (Branded only, additional fields)
```json
{
  "fdcId": 1955793,
  "dataType": "Branded",
  "brandOwner": "Original Gourmet Food Company Inc.",
  "brandName": "",
  "gtinUpc": "...",
  "ingredients": "ENRICHED FLOUR (WHEAT FLOUR...",
  "servingSize": 42.5,
  "servingSizeUnit": "g",
  "householdServingFullText": "1 COOKIE",
  "packageWeight": "...",
  "brandedFoodCategory": "...",
  "marketCountry": "...",
  "modifiedDate": "...",
  "availableDate": "...",
  "dataSource": "...",
  "labelNutrients": {
    "fat": {"value": 9.0},
    "saturatedFat": {"value": 4.5},
    "transFat": {"value": 0.0},
    "cholesterol": {"value": 5.1},
    "sodium": {"value": 220},
    "carbohydrates": {"value": 27.0},
    "fiber": {"value": 1.02},
    "sugars": {"value": 15.0},
    "protein": {"value": 2.0},
    "calcium": {"value": 10.2},
    "iron": {"value": 0.999},
    "potassium": {"value": 50.2},
    "addedSugar": {"value": 15.0},
    "calories": {"value": 200}
  },
  "foodNutrients": [ ... ],
  "foodUpdateLog": [ ... ]
}
```

### GET /food/{fdcId} — abridged format
```json
{
  "fdcId": 2346393,
  "description": "Nuts, almonds, whole, raw",
  "dataType": "Foundation",
  "publicationDate": "2022-10-28",
  "ndbNumber": "12061",
  "foodNutrients": [
    {"number": "303", "name": "Iron, Fe", "amount": 3.74, "unitName": "MG",
     "derivationCode": "A", "derivationDescription": "Analytical"},
    ...
  ]
}
```
Abridged strips `foodPortions`, `inputFoods`, `nutrientConversionFactors`, `foodNutrientDerivation` objects, and `nutrientAnalysisDetails`. foodNutrients uses a flat shape (number, name, amount, unitName, derivationCode, derivationDescription) — same as the list endpoint.

### GET/POST /foods (batch)
Returns a **bare array** `[FoodItem, FoodItem, ...]` — no envelope object.

### GET /foods/list
Returns a **bare array** `[AbridgedFoodItem, ...]` — no envelope object.

---

## 5. foodNutrients Shape: Two Distinct Formats

### Format A — Full nested (returned by GET /food/{fdcId} full, POST /foods full)
```json
{
  "type": "FoodNutrient",
  "id": 1632926,
  "amount": 167.0,
  "dataPoints": 0,
  "nutrient": {
    "id": 1008,
    "number": "208",
    "name": "Energy",
    "rank": 300,
    "unitName": "kcal"
  },
  "foodNutrientDerivation": {
    "id": 49,
    "code": "NC",
    "description": "Calculated",
    "foodNutrientSource": { "id": 2, "code": "4", "description": "Calculated or imputed" }
  },
  "nutrientAnalysisDetails": [ ... ]
}
```
Some items are category headers (no `amount` field, just `nutrient` + `type`).

### Format B — Flat (returned by /foods/search, /foods/list, /food abridged)
```json
{
  "nutrientId": 1003,
  "nutrientName": "Protein",
  "nutrientNumber": "203",
  "unitName": "G",
  "value": 4.71,
  "derivationCode": "LCCS",
  "derivationDescription": "Calculated from value per serving size measure",
  "derivationId": 70,
  "rank": 600,
  "indentLevel": 1,
  "foodNutrientId": 22735976,
  "dataPoints": null
}
```
Key difference: Format A uses `amount`; Format B uses `value`. Format A uses `nutrient.number`; Format B uses `nutrientNumber`. Format A uses `nutrient.name`; Format B uses `nutrientName`.

---

## 6. labelNutrients vs foodNutrients

- `labelNutrients` is present **only on Branded foods** — confirmed absent on SR Legacy (fdcId 171706), Foundation (fdcId 1750340, 2346393).
- `labelNutrients` values are **per serving** (not per 100g), matching what appears on a product's nutrition facts panel.
- `foodNutrients` values for Foundation/SR Legacy are **per 100g** by convention.
- `foodNutrients` values for Branded use derivation code `LCCS` ("Calculated from value per serving size measure") — they are stored per 100g internally but derived from serving-size data.
- The `labelNutrients` keys: `fat`, `saturatedFat`, `transFat`, `cholesterol`, `sodium`, `carbohydrates`, `fiber`, `sugars`, `protein`, `calcium`, `iron`, `potassium`, `addedSugar`, `calories`. Each is `{"value": <number>}`.

---

## 7. Serving Size Fields (Branded only)

| Field | Type | Example |
|---|---|---|
| `servingSize` | float | `42.5` |
| `servingSizeUnit` | string | `"g"` |
| `householdServingFullText` | string | `"1 COOKIE"` |
| `packageWeight` | string | `"10.5 OZ/298g"` |

---

## 8. Pagination

- Parameters: `pageSize` (1–200, default 50), `pageNumber` (1-based)
- Response includes: `totalHits`, `currentPage`, `totalPages`, `pageList` (array of first ~10 page numbers)
- `pageList` is decorative — it does not limit results
- `/foods/list` and `/foods/search` support pagination; `/food/{id}` and `/foods` (batch) do not

---

## 9. Key Nutrient Numbers

| Number | Name | Unit |
|---|---|---|
| 208 | Energy | kcal |
| 203 | Protein | g |
| 204 | Total lipid (fat) | g |
| 205 | Carbohydrate, by difference | g |
| 269 | Sugars, total | g |
| 291 | Fiber, total dietary | g |
| 307 | Sodium | mg |
| 539 | Sugars, added | g |
| 301 | Calcium | mg |
| 303 | Iron, Fe | mg |
| 418 | Vitamin B-12 | µg |

Canonical number location: `foodNutrients[].nutrient.number` (Format A — string, not integer) or `foodNutrients[].nutrientNumber` (Format B — also string).

---

## 10. POST /foods/search Body Shape

```json
{
  "query": "string",
  "dataType": ["Branded", "Foundation"],
  "pageSize": 50,
  "pageNumber": 1,
  "sortBy": "dataType.keyword | lowercaseDescription.keyword | fdcId | publishedDate",
  "sortOrder": "asc | desc",
  "brandOwner": "string",
  "tradeChannel": ["GROCERY", "FOOD_SERVICE", ...],
  "startDate": "YYYY-MM-DD",
  "endDate": "YYYY-MM-DD"
}
```
POST allows `tradeChannel`, `startDate`, `endDate` — not available on GET.

---

## 11. Error Responses

- **404 Not Found** (nonexistent fdcId): Empty body, HTTP 404 — no JSON error object
- **Invalid API key:** `{"error": {"code": "API_KEY_INVALID", "message": "An invalid api_key was supplied..."}}`
- **Empty query GET /foods/search:** Returns 200 with all foods (totalHits=468,382) — not an error
- **Empty fdcIds POST /foods:** Returns `{}` (empty object) with HTTP 200 — no error
