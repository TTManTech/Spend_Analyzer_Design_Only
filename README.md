# Spend Analyzer (design only)

Static landing page for Spend Analyzer, a TTM Tech product: **Know Your Money (KYM)** through your spends, investments and savings.

## Files

| File | What |
| --- | --- |
| `index.html` | The page: logo, title, subtitle, month/year picker, YTD bubble, income split bar (Spend, Investment, Savings, Unallocated) and the spend-by-category donut |
| `data/Master_Data_V0.1.xlsx` | Source transactions and income |
| `data/spend-rates.json` | Monthly and yearly spend, income and spend rate, generated from the spreadsheet |
| `scripts/build_spend_rates.py` | Regenerates `data/spend-rates.json` |
| `assets/ttm-tech-logo-light.svg` | Logo for light mode |
| `assets/ttm-tech-logo-dark.svg` | Logo for dark mode |

**Spend Rate** comes from `data/spend-rates.json`: the selected month's spend divided by that month's income, rounded to a whole percent. Spend excludes card payments and nets merchant refunds; months are calendar months of the transaction date. The **YTD** bubble beside the month/year picker opens a year list (2019–2025); picking a year shows that calendar year's spend rate up to today (27 Dec 2021 in this design). Changing the month or year dropdown switches back to the monthly view. Yearly totals are precomputed into the same JSON file under `years`. Investment and Savings rates are still placeholders (24% and 18% of income). The **Income split** bar shows all three as coloured sections of one bar, with the rest of the income as grey "Unallocated"; under it each section shows its title, percentage and dollar amount.

**Spend by category** (below the income split) is a donut of the selected month's or YTD year's spend per Category of Spend, net of refunds. Clicking a slice or its row in the list shows that category's top 7 purchases with the amount and its share of the category. A merchant fills at most 3 of those rows; a merchant with more than 3 purchases gets a small bubble underneath with its other purchases (count and total). Each category keeps a fixed colour: the eight largest categories are solid, the smaller ones (Home Improvement, Services, Travel & Hospitality, Pharmacy, Medical) are striped, and "Other" is striped grey. The breakdowns are precomputed into `data/spend-rates.json` under each month's and year's `categories`.

After changing the spreadsheet, regenerate the data (needs `openpyxl`):

```sh
python3 scripts/build_spend_rates.py
```
 The page follows the viewer's light/dark setting until they use the Light/Dark switch in the top right corner, which is remembered in that browser and uses the TTM Tech palette and JetBrains Mono (Google Fonts).

## Run

Serve the folder (the page fetches `data/spend-rates.json`, which browsers block when opening the file directly):

```sh
python3 -m http.server 8000
```
