
# Analysis Coverage Checklist

This package covers the analysis points required in **AP - Wise regional expansion.md** and the guidance in **tips.md**.

## EDA (Exploratory)
- ✅ Event and customer counts (`eda_summary_counts.csv`)
- ✅ Frequency of frequencies (transfers per user) (`freq_of_freq.csv`, `freq_transfers_per_user.csv`)
- ✅ Users with ≥1 failure and split New vs Old (`failed_users_summary.csv`)
- ✅ Success Rate = **1 − Unsettled** by:
  - Platform × Region (`success_rate_platform_by_region.csv`, plus counts)
  - Platform × Experience (`success_rate_platform_by_experience.csv`, plus counts)
  - Region × Experience (`success_rate_region_by_experience.csv`, plus counts)
- ✅ Daily trend and **7‑day moving average**:
  - Global (`daily_success_global.csv`, `daily_success_global.png`)
  - Platform × Region (`daily_success_platform_region.csv`)
  - Platform × Experience (`daily_success_platform_experience.csv`)
- ✅ Deeper EDA pivots and switching analysis:
  - Segment summary (`eda_segment_summary.csv`)
  - 2×2 and 3‑way pivots (`pivot_*` CSVs)
  - Dominant group per user/month and **switching flows** (`user_group_*` CSVs)

## Modeling
- ✅ Logistic regression predicting **unsettled** (Notebook: `02_logistic_regression.ipynb`)
  - Train/test split, ROC‑AUC, report, coefficients table

## Friction & Power Usage
- ✅ Step conversions, **Created→Funded**, **Funded→Transferred**, median times (Notebook: `03_friction_power.ipynb` / `friction_segmented.csv`)
- ✅ Power usage buckets and success (`power_usage.csv`)

## Datasets & Repro
- ✅ Clean transfer‑level dataset (`transfers_level.csv`) built with strict order **Created → Funded → Transferred**
- ✅ Helper functions for reproducibility (`funnel_utils.py`)
- ✅ Slide-ready exports and visuals (`*csv`, `global_success_rate.png`)
- ✅ Summary docs (`README.md`, `conclusion.md`, AP & tips included)

> All files are kept at a single directory depth in this `wise_expansion_deliverable` folder.
