# Spend Analyzer (design only)

Static landing page for Spend Analyzer, a TTM Tech product: **Know Your Money (KYM)** through your spends, investments and savings.

## Files

| File | What |
| --- | --- |
| `index.html` | The page: logo, title, subtitle, month/year picker, YTD bubble, income split bar (Spend, Investment, Savings, Unallocated) and the spend-by-category donut |
| `scripts/build_spend_rates.py` | Builds the monthly and yearly figures from the spreadsheet (local, not committed) |
| `logos/` | Light and dark merchant logos for the top purchases list |
| `assets/ttm-tech-logo-light.svg` | Logo for light mode |
| `assets/ttm-tech-logo-dark.svg` | Logo for dark mode |

**Spend Rate** comes from the published page's artifact database: the selected month's spend divided by that month's income, rounded to a whole percent. Spend excludes card payments and nets merchant refunds; months are calendar months of the transaction date. The **YTD** bubble beside the month/year picker opens a year list (2019–2025); picking a year shows that calendar year's spend rate up to today (27 Dec 2021 in this design). Changing the month or year dropdown switches back to the monthly view. Yearly totals are precomputed into the same JSON file under `years`. Investment and Savings rates are still placeholders (24% and 18% of income). The **Income split** bar shows all three as coloured sections of one bar, with the rest of the income as grey "Unallocated"; under it each section shows its title, percentage and dollar amount.

**Spend by category** (below the income split) is a donut of the selected month's or YTD year's spend per Category of Spend, net of refunds. Clicking a slice or its row in the list shows that category's top 7 purchases with the amount and its share of the category. A merchant fills at most 3 of those rows; a merchant with more than 3 purchases gets a small bubble underneath with its other purchases (count and total). Each category keeps a fixed colour: the eight largest categories are solid, the smaller ones (Home Improvement, Services, Travel & Hospitality, Pharmacy, Medical) are striped, and "Other" is striped grey. Categories under 5% of the period's spend are clubbed into one grey **Others (n)** row and slice when there are at least two of them; the + next to it (or clicking the Others slice) expands them in place. Chain restaurants and supermarkets show their logo after the row number in the top purchases list, in a light or dark version to match the theme (see `logos/README.md`). The breakdowns are precomputed into `data/spend-rates.json` under each month's and year's `categories`.

After changing the spreadsheet, regenerate the data (needs `openpyxl`):

```sh
python3 scripts/build_spend_rates.py
```
 The page follows the viewer's light/dark setting until they use the Light/Dark switch in the top right corner, which is remembered in that browser and uses the TTM Tech palette and JetBrains Mono (Google Fonts).

## Data

No financial data is stored in this repo. The figures live in the published artifact's database: collection `months` (one document per `YYYY-MM`) and collection `years` (one per `YYYY`), each holding `spend`, `income`, `spendRate` and `categories`. Only the artifact's owner can write them; anyone the page is shared with can read them.

To update them, put the spreadsheet at `data/Master_Data_V0.1.xlsx` (ignored by git), run `python3 scripts/build_spend_rates.py` to produce `data/spend-rates.json`, and load each month and year into the database (Claude does this with its artifact-data tool).

## Run

The page shows figures only when opened as the published artifact on claude.ai while signed in; opened locally it renders the layout with a notice instead. Serve the folder to preview the layout:

```sh
python3 -m http.server 8000
```
