# Spend Analyzer (design only)

Static landing page for Spend Analyzer, a TTM Tech product: **Know Your Money (KYM)** through your spends, investments and savings.

## Files

| File | What |
| --- | --- |
| `index.html` | The page: logo, title, subtitle, month/year picker and three rate bubbles (Spend, Investment, Savings) |
| `data/Master_Data_V0.1.xlsx` | Source transactions and income |
| `data/spend-rates.json` | Monthly spend, income and spend rate, generated from the spreadsheet |
| `scripts/build_spend_rates.py` | Regenerates `data/spend-rates.json` |
| `assets/ttm-tech-logo-light.svg` | Logo for light mode |
| `assets/ttm-tech-logo-dark.svg` | Logo for dark mode |

**Spend Rate** comes from `data/spend-rates.json`: the selected month's spend divided by that month's income, rounded to a whole percent. Spend excludes card payments and nets merchant refunds; months are calendar months of the transaction date. Investment and Savings rates are still placeholders.

After changing the spreadsheet, regenerate the data (needs `openpyxl`):

```sh
python3 scripts/build_spend_rates.py
```
 The page follows the viewer's light/dark setting and uses the TTM Tech palette and JetBrains Mono (Google Fonts).

## Run

Serve the folder (the page fetches `data/spend-rates.json`, which browsers block when opening the file directly):

```sh
python3 -m http.server 8000
```
