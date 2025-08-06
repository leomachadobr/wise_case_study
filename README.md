
---

## 🚀 Getting Started

1. **Place raw data** in `/data/wise_funnel_events.csv`.  
2. **Install dependencies** (e.g., `pandas`, `numpy`, `matplotlib`, `scikit-learn`).  
3. **Run notebooks in order** under `/notebooks`:  
   1. `01_build_eda.ipynb`  
   2. `01b_eda_deep_dive.ipynb`  
   3. `02_logistic_regression.ipynb`  
   4. `03_friction_power.ipynb`  
   5. `04_exports_for_slides.ipynb`  
   6. `05_data_visualizations.ipynb`  
4. **Review outputs** in `/exports` for data tables and charts.

---

## 📄 Notebook Summaries

- **01_build_eda.ipynb**: Creates transfer-level data, validates, and computes daily/MA7 success rates.  
- **01b_eda_deep_dive.ipynb**: Cross-tab pivots, segment summaries, and switching flow analysis.  
- **02_logistic_regression.ipynb**: Predicts unsettled transfers via logistic regression and interprets coefficients.  
- **03_friction_power.ipynb**: Analyzes funnel friction (time deltas) and power-user behavior.  
- **04_exports_for_slides.ipynb**: Exports slide-ready assets (tables/plots) for decks.  
- **05_data_visualizations.ipynb**: Monthly success trends, friction heatmaps, failure decomposition sankeys, and partial-settled profiles.

---

## 🔍 Analysis Coverage

See `analysis_coverage.md` for a detailed checklist ensuring all points in the AP and tips are implemented, including:

- Event & customer counts  
- Frequency of frequencies and failure profiles  
- Success rates (1 - Unsettled) broken down by Region, Platform, Experience  
- Daily + 7-day MA7 tracking  
- Switching flows (New→Existing vs Others)  
- Logistic regression and coefficient analysis  
- Funnel friction and time-to-stage  
- Power-user intensity effects  
- Decomposition of failures and partial-settled profiling

---

## 🎯 Key Outputs

- **`transfers_level.csv`**: Canonical ETL of events into one row per transfer with flags & status.  
- **`daily_*`**: Daily and global funnel metrics with moving averages.  
- **Heatmaps** & **Sankeys** for cross-sectional friction & failure decomposition.  
- **Slide assets** in `/exports/visualizations` ready for presentations.

---

## ☑️ Next Steps & Recommendations

After reviewing the outputs:

1. Focus on segments with highest failure rates for UX or reliability improvements.  
2. Deep-dive into platform-specific friction via error logs.  
3. Enhance onboarding for `Experience = New` cohorts, given lower early success.  
4. Monitor MA7 trends post-launch to measure impact of product optimizations.

---

*Prepared by the Regional Expansion Tribe — Wise*  
