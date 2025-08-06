
# Wise Regional Expansion — Analysis Package

This package implements the analysis plan and tips in **AP - Wise regional expansion.md** and **tips.md**.
It enforces the funnel order **Created → Funded → Transferred**, builds clean datasets, and delivers EDA,
logistic regression, and friction/power-usage deep-dives. It also provides an exports notebook for slide assets.

## Structure
- `src/funnel_utils.py` — small utilities for funnel ordering, keys, daily metrics, and palette.
- `01_build_eda.ipynb` — builds datasets (`transfers_level.csv`, `daily_segmented.csv`, `daily_global.csv`), validation, EDA, MA7.
- `02_logistic_regression.ipynb` — unsettled vs others classifier with coefficients for interpretability.
- `03_friction_power.ipynb` — conversion steps, time-to-next-stage, and power-usage analysis.
- `04_exports_for_slides.ipynb` — charts/tables exported to `exports/` for presentations.

## Outputs
- CSVs in the project root (`/mnt/data`): `transfers_level.csv`, `daily_segmented.csv`, `daily_global.csv`, `friction_segmented.csv`, `power_usage.csv`.
- Images/tables for slides in `exports/`: `global_success_rate.png`, `region_share_latest.csv`.
- All charts use the Wise palette specified in the AP.

## How this meets the AP & Tips
- **Validate data**: sanity counts, unique users, profile splits (region/platform/experience).
- **Categorize transactions**: transfer-level dataset with status (settled/partially/unsettled), strict stage order, orphan handling.
- **State of transfers over time**: daily & MA7 success rate, segmented and global.
- **Logistic regression**: target per AP (unsettled=1), with segment features and interpretable coefficients.
- **Friction & recurrency**: step conversions and time deltas; power-usage buckets show intensity vs. success.
- **Deliverables**: CSVs, charts, and notebooks ready for review and slide prep.

## Run order
1. `01_build_eda.ipynb`
2. `02_logistic_regression.ipynb`
3. `03_friction_power.ipynb`
4. `04_exports_for_slides.ipynb`
