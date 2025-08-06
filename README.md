
# Wise MXN→USD Route Analytics Case Study

A comprehensive product analytics case study examining the launch of a new MXN→USD currency route. This project demonstrates data-driven insights for product performance evaluation, funnel optimization, and regional expansion strategy.

## 📋 Project Overview

**Context**: Analysis of a hypothetical MXN→USD route launch for Wise's Regional Expansion Tribe. The study evaluates demand estimation methodologies and provides insights on product performance using real funnel event data.

**Objectives**:
1. Propose demand estimation methodologies for new currency routes
2. Analyze funnel performance and identify optimization opportunities  
3. Provide actionable insights for product and engineering teams

## 🏗️ Project Structure

```
wise_case_study/
├── data/                           # Raw and processed datasets
│   ├── wise_funnel_events.csv     # Source events data
│   ├── transfers_level.csv        # Processed transfer-level data
│   ├── daily_segmented.csv        # Daily metrics by segment
│   └── exports/                   # Analysis outputs and exports
├── notebooks/                      # Analysis notebooks (run in order)
│   ├── 01_build_eda.ipynb         # Data processing & EDA
│   └── 02_logistic_regression.ipynb # Predictive modeling
├── src/                           # Source code and utilities
│   └── funnel_utils.py            # Custom analysis functions
├── deprecated/                    # Archived/experimental notebooks
├── exports/                       # Charts, visualizations, and reports
│   ├── eda/                       # Exploratory analysis outputs
│   └── visualizations/            # Publication-ready charts
└── docs/                          # Documentation and case study materials
    ├── tips.md                    # Analysis guidelines
    └── Regional Product Analyst - Case Study.pdf
```

## 🚀 Getting Started

### Prerequisites
```bash
# Install required Python packages
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Running the Analysis
1. **Data Setup**: Raw event data is already in `/data/wise_funnel_events.csv`
2. **Execute Notebooks**: Run notebooks in sequence:
   - `01_build_eda.ipynb` - Core data processing and exploratory analysis
   - `02_logistic_regression.ipynb` - Predictive modeling for transfer success
3. **Review Outputs**: Check `/exports/` for generated charts and data exports

### Key Functions
The `src/funnel_utils.py` module provides:
- **`normalize_events()`**: Standardizes event data and creates funnel stages
- **`build_transfer_level()`**: Converts events to transfer-centric view
- **`daily_funnel()`**: Computes daily success metrics by segment

## 📊 Key Findings

### 🔍 Performance Highlights
- **Overall Success Rate**: ~45% of transfers reach completion (transferred status)
- **Regional Performance**: North America shows highest success rates (~50%), Europe significantly lower (~25%)
- **Platform Insights**: iOS users demonstrate higher retry behavior with 44.7% platform switching rate
- **User Experience**: New users face substantially higher failure rates across all segments

### 🚨 Critical Issues Identified
1. **Europe Anomaly**: Despite MXN→USD being Mexico-US focused, Europe shows:
   - Highest transfer volumes (spike from 130→439 daily in Feb 2024)
   - Lowest success rates (~25-30%)
   - Suggests potential routing/system issues requiring investigation

2. **New User Friction**: Success rates significantly lower for new customers
   - Indicates onboarding optimization opportunities

3. **Platform-Specific Behavior**: iOS users switch platforms more frequently after failures
   - Points to iOS-specific UX issues

## 🎯 Business Recommendations

### Immediate Actions
1. **Technical Investigation**: Investigate Europe routing issues causing volume surge and poor performance
2. **New User Experience**: Redesign onboarding flow to reduce initial friction
3. **Platform Optimization**: Address iOS-specific pain points leading to switching behavior

### Strategic Opportunities  
1. **Demand Estimation**: Implement cohort-based forecasting using North America performance as baseline
2. **Performance Monitoring**: Establish 7-day MA success rate tracking for early issue detection
3. **Segmentation Strategy**: Tailor user experiences by region and platform characteristics

## 📈 Analysis Methodology

### Data Processing Pipeline
1. **Event Normalization**: Transform raw events into standardized funnel stages
2. **Transfer Construction**: Build transfer-centric dataset with success/failure flags
3. **Segmentation Analysis**: Break down performance by region, platform, and user experience
4. **Time Series Analysis**: Track daily performance with moving averages for trend detection

### Key Metrics
- **Success Rate**: % of transfers reaching "transferred" status
- **Retry Rate**: % of users attempting transfers after failures
- **Recurrence Rate**: % of users with multiple successful transfers
- **Platform Switch Rate**: % of retry attempts using different platforms

## 🔄 Data Flow

```mermaid
graph TD
    A[wise_funnel_events.csv] --> B[normalize_events()]
    B --> C[attach_transfer_keys()]
    C --> D[build_transfer_level()]
    D --> E[transfers_level.csv]
    E --> F[daily_funnel()]
    F --> G[Segmented Analysis]
    E --> H[Cohort Analysis]
    G --> I[Visualizations]
    H --> I
```

## 📚 Additional Resources

- **Case Study Brief**: `/docs/Regional Product Analyst - Case Study.pdf`
- **Analysis Guidelines**: `/docs/tips.md`
- **Generated Charts**: `/exports/visualizations/`
- **Data Exports**: `/data/exports/`

---

*This case study demonstrates end-to-end product analytics capabilities including funnel analysis, segmentation, predictive modeling, and actionable business recommendations.*  
