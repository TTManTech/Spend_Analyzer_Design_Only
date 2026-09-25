"""Build data/spend-rates.json from data/Master_Data_V0.1.xlsx.

Spend rate for a month = total spend that month / total income that month,
rounded to a whole percent (half up). The same is done per calendar year for YTD.

- Spend: Transactions rows by calendar month of Date, excluding card payments
  ("Payment / Credit"); merchant refunds are negative so they net against spend.
- Income: Income sheet rows by calendar month of Date.

Run: python3 scripts/build_spend_rates.py   (needs openpyxl)
"""
import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "Master_Data_V0.1.xlsx"
OUT = ROOT / "data" / "spend-rates.json"


def monthly_totals(ws, skip_category=None):
    totals = defaultdict(Decimal)
    rows = ws.iter_rows(min_row=2, values_only=True)
    for _bank, date, _year, _desc, amount, category, _kind in rows:
        if date is None or amount is None or category == skip_category:
            continue
        totals[f"{date.year}-{date.month:02d}"] += Decimal(str(amount))
    return totals


def by_year(totals):
    years = defaultdict(Decimal)
    for key, amount in totals.items():
        years[key[:4]] += amount
    return years


def summarise(spend, income):
    out = {}
    for key in sorted(set(spend) | set(income)):
        s, i = spend.get(key, Decimal(0)), income.get(key, Decimal(0))
        rate = int((s / i * 100).quantize(Decimal(1), ROUND_HALF_UP)) if i else None
        out[key] = {"spend": float(s.quantize(Decimal("0.01"))), "income": float(i), "spendRate": rate}
    return out


def main():
    wb = load_workbook(SRC, data_only=True)
    spend = monthly_totals(wb["Transactions"], skip_category="Payment / Credit")
    income = monthly_totals(wb["Income"])

    months = summarise(spend, income)
    years = summarise(by_year(spend), by_year(income))

    OUT.write_text(json.dumps({"source": SRC.name, "months": months, "years": years}, indent=2) + "\n")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(months)} months, {len(years)} years)")


if __name__ == "__main__":
    main()
