# RELYNDIA — Visualizing Reliance's Business and Market Footprint in India

**Course:** BISL504 Data Visualization Lab | Department of IS&E, NIE Mysuru  
**Project Platform:** Streamlit Interactive Web Application (`app.py`)  
**Academic Stance:** Academically defensible analysis examining Reliance Industries' growth, business segment transformation, telecom market dynamics, and consumer footprint expansion in relation to Indian macroeconomic indicators (avoiding unsupported causal claims).

---

## 🚀 Quick Start: Launch the Interactive Web Application

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch Streamlit Web Application
python3 -m streamlit run app.py
```

Streamlit will automatically open your browser at:
- **Local URL:** `http://localhost:8501`
- **Network URL:** `http://127.0.0.1:8501`

Detailed user instructions and navigation walkthrough are documented in [`docs/app_run_guide.md`](file:///Users/sj/Desktop/DVP/docs/app_run_guide.md).

---

## 📁 Project Directory Structure

```text
/Users/sj/Desktop/DVP/
├── app.py                                # Streamlit Interactive Web Application
├── components/                           # Modular UI & Analytical Components
│   ├── charts.py                         # Dynamic Plotly chart generation with user filters
│   ├── metrics.py                        # KPI cards, CAGRs, and financial ratio calculations
│   └── explanations.py                   # 7-point Detailed Explanation expandable panels
│
├── data/                                 # 100% Verified primary datasets & audit register
│   ├── verified_ril_financial_segment_growth.csv
│   ├── verified_telecom_market_subscribers.csv
│   ├── verified_reliance_retail_footprint.csv
│   ├── verified_indian_economic_indicators.csv
│   └── data_sources_and_verification.csv
│
├── clean_data/                           # Standardized, normalized & reshaped datasets
│   ├── clean_ril_financial_segment_growth.csv
│   ├── clean_ril_segments_long.csv       # Tidy format for Plotly grouped & stacked charts
│   ├── clean_telecom_market_subscribers.csv
│   ├── clean_telecom_subscribers_long.csv # Tidy format for Plotly multi-line & area charts
│   └── clean_reliance_retail_footprint.csv # With store density & productivity metrics
│
├── scripts/                              # Automated batch processing & visualization pipelines
│   ├── data_profile.py                   # Automated pandas profiling engine
│   ├── data_cleaning.py                  # Cleaning, reshaping & derived metrics engine
│   └── visualizations.py                 # Core Plotly standalone visualization generator
│
├── outputs/                              # 7 Standalone interactive HTML visualizations
│   ├── reliance/                         # Q1: Diversification & segment charts
│   ├── telecom/                          # Q2: Telecom market & subscriber charts
│   └── retail/                           # Q3: Retail footprint & customer reach charts
│
├── docs/                                 # Complete documentation suite
│   ├── app_run_guide.md                  # Comprehensive web app execution guide
│   ├── phase4_freeze_record.md           # Formal implementation freeze record
│   ├── phase4_refinement_audit.md        # Pre-freeze refinement and mapping audit
│   ├── phase4_reproducibility_report.md  # End-to-end reproducibility report
│   ├── visualization_insights.md         # 6-point structured academic commentary
│   ├── code_walkthrough_notes.md         # Oral viva defense walkthrough notes
│   ├── AI_usage_log.md                   # Transparent AI compliance log
│   └── data_profile.md                   # Empirical dataset profiling reports
│
├── requirements.txt                      # Project Python dependencies
└── index.html                            # Standalone static visual explorer
```

---

## ⚙️ Batch Reproducibility Pipeline

If you want to run the underlying data pipeline or regenerate the standalone HTML visualizations:

```bash
# 1. Automated Data Profiling
python3 scripts/data_profile.py

# 2. Data Cleaning & Reshaping
python3 scripts/data_cleaning.py

# 3. Core Visualizations Batch Export
python3 scripts/visualizations.py
```

---

## 🎯 Guiding Analytical Questions & Visualization Mapping

1. **Q1 (Reliance Diversification):** *How has Reliance diversified across its major business segments over time?*
   - `outputs/reliance/q1_segment_revenue_trend.html` (Multi-Line Chart)
   - `outputs/reliance/q1_segment_comparison_grouped_bar.html` (Grouped Bar Chart)
   - `outputs/reliance/q1_business_composition_100pct_stacked.html` (100% Stacked Area)
2. **Q2 (Telecom Market Dynamics):** *How did the growth of Jio coincide with changes in India's telecom market?*
   - `outputs/telecom/q2_telecom_subscribers_multiline.html` (Multi-Line Chart)
   - `outputs/telecom/q2_telecom_market_share_stacked_area.html` (100% Stacked Area)
3. **Q3 (Retail & Consumer Reach):** *How has Reliance expanded its retail footprint and consumer reach over time?*
   - `outputs/retail/q3_retail_revenue_vs_stores_dual_axis.html` (Dual-Axis Bar + Line)
   - `outputs/retail/q3_retail_customers_and_area_trend.html` (Dual-Axis Line Chart)

---

## 📊 Phase 5: Dashboard Creation (Weeks 8–9)

The project has achieved completion of **Phase 5: Dashboard Creation**, transforming the frozen Phase 4 foundation into a polished, interactive, academically defensible data-visualization dashboard.

### Key Phase 5 Deliverables:
- **Streamlit Interactive Web Application:** [`app.py`](file:///Users/sj/Desktop/DVP/app.py) with modular components in `components/`.
- **Phase 5 Initial Audit:** [`docs/phase5_dashboard_audit.md`](file:///Users/sj/Desktop/DVP/docs/phase5_dashboard_audit.md)
- **AI-Assisted Design Critique Log (10 Questions):** [`docs/phase5_design_critique_log.md`](file:///Users/sj/Desktop/DVP/docs/phase5_design_critique_log.md)
- **Dashboard Testing & Verification Report:** [`docs/phase5_testing_report.md`](file:///Users/sj/Desktop/DVP/docs/phase5_testing_report.md)
- **End-User Operational Guide:** [`docs/phase5_user_guide.md`](file:///Users/sj/Desktop/DVP/docs/phase5_user_guide.md)
- **Visual Evidence & Screenshot Register:** [`outputs/phase5/screenshots/README.md`](file:///Users/sj/Desktop/DVP/outputs/phase5/screenshots/README.md)
- **Automated Verification Script:** [`scripts/verify_phase5.py`](file:///Users/sj/Desktop/DVP/scripts/verify_phase5.py)

### Interactive Features Implemented:
1. **5 Comprehensive Views:** Executive Overview, Business Diversification (Q1), Jio & Telecom Dynamics (Q2), Reliance Retail Reach (Q3), Data Sources & Methodology.
2. **Dynamic Section-Level KPIs:** Filter-responsive KPI cards above charts recalculating period CAGRs, ending totals, and shifts based on active user selections.
3. **Interactive Filtering:** Timeline range slider (`FY2017`–`FY2024`), segment multiselect, and operator multiselect.
4. **"🔄 Reset All Filters" Button:** Instantly restores all sliders and multiselects to defaults via Streamlit session state.
5. **Exact `[ Detailed Explanation ]` Panels:** Collapsible panels beneath every chart featuring all 7 mandatory numbered sections.
6. **CSV Data Downloads:** One-click downloads for displayed subset data across all sections.

---

## 🔒 Implementation Freeze & Academic Integrity
The underlying source data (`data/*.csv`) and core analytical calculations remain frozen from Phase 4. All observations adhere to strict academic non-causal framing (coexistence, concurrent growth, and market transition). See [`docs/phase4_freeze_record.md`](file:///Users/sj/Desktop/DVP/docs/phase4_freeze_record.md).

