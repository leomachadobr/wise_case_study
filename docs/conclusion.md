
# Conclusion — Wise Regional Expansion (MXN → USD)

**Executive take:** Based on the current event data, the launch is on-track overall, with success rates stable on a 7‑day moving average.
The primary drivers of friction are concentrated in specific segments by platform and experience, not uniformly across regions.

## Key Findings (backed by the notebooks)
1. **Funnel performance:** The 7‑day MA **Success Rate = 1 − Failure Rate** is stable with modest improvements. See `01_build_eda.ipynb` (Global Success Rate).
2. **Segment deltas:** Platform and Experience segmentations explain most of the variance in unsettled outcomes; Region effects are secondary (see EDA segment tables).
3. **Friction timing:** Median time from Created→Funded and Funded→Transferred differs materially by segment, suggesting UX or payment frictions (see `03_friction_power.ipynb`).
4. **Recurrency & power usage:** Heavier users achieve **higher average success**, indicating value of early activation and education.
5. **Predictive check:** Logistic regression flags **experience** and **platform** as the strongest correlates of an unsettled outcome.

## Recommendations
- **Platform-specific QA**: Deep-dive into the platforms with below-average MA7 success; inspect payment handoff and error telemetry.
- **New-user onboarding**: Add nudges/tooltips for first-time users in segments with high Created-only rates.
- **Payment reliability**: Focus on reducing Created→Funded frictions where median time-to-fund is elevated.
- **Activation loop**: Encourage recurrency among new users; heavy-usage cohorts show better odds of transfer completion.

> Each recommendation maps to evidence and charts in notebooks 01–03 and slide exports from 04.
