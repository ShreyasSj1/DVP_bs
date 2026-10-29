# RELYNDIA — Phase 5 Dashboard Testing & Verification Report

**Course:** BISL504 — Data Visualization Lab (Weeks 8–9)  
**Project:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Phase:** 5 — Dashboard Creation  
**Date of Testing:** October 2026  
**Test Suite Script:** `scripts/verify_phase5.py`  
**Overall Status:** **PASSED (100% Test Pass Rate)**  

---

## 1. Environment & Test Architecture

Testing was executed in the project workspace on macOS Darwin with Python 3.12, Streamlit 1.56.0, Plotly 6.7.0, and Pandas 2.3.3.

| Component / Layer | Implementation File | Verification Method | Result |
| :--- | :--- | :--- | :--- |
| **Pipeline Batch Script** | `scripts/data_profile.py` | Standalone script execution (`exit code 0`) | **PASS** |
| **Data Cleaning Pipeline** | `scripts/data_cleaning.py` | Generates 5 cleaned CSVs in `clean_data/` | **PASS** |
| **Batch Chart Engine** | `scripts/visualizations.py` | Generates 7 HTML Plotly visualizations in `outputs/` | **PASS** |
| **Core Web Application** | `app.py` | `py_compile` & component integration check | **PASS** |
| **Modular Chart Library** | `components/charts.py` | Automated Plotly figure object generation | **PASS** |
| **Dynamic Metric Engine** | `components/metrics.py` | Exact mathematical and CAGR validation | **PASS** |
| **Detailed Explanations** | `components/explanations.py`| Function introspection and structure audit | **PASS** |
| **Automated Test Suite** | `scripts/verify_phase5.py` | Full programmatic regression testing | **PASS** |

---

## 2. Mathematical & Financial Metric Verification

All quantitative indicators were mathematically audited against primary annual reports (FY2017 to FY2024, representing 7 annual compounding periods; and FY2018 to FY2024, representing 6 compounding periods):

$$\text{CAGR} = \left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{n}} - 1$$

| Metric / Indicator | Formula Baseline ($V_{\text{start}}$) | Formula End ($V_{\text{end}}$) | Periods ($n$) | Expected Value | Calculated Value | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **RIL Consolidated Turnover** | ₹3,30,180 Cr (FY17) | ₹10,00,122 Cr (FY24) | 7 | `17.15%` | `17.15%` | **PASS** |
| **Reliance Retail Gross Revenue** | ₹33,765 Cr (FY17) | ₹3,06,786 Cr (FY24) | 7 | `37.06%` | `37.06%` | **PASS** |
| **Digital Services Revenue** | ₹20,154 Cr (FY18) | ₹1,32,045 Cr (FY24) | 6 | `36.79%` | `36.79%` | **PASS** |
| **Jio Wireless Subscribers** | 108.68 M (FY17) | 469.73 M (FY24) | 7 | `23.26%` | `23.26%` | **PASS** |
| **Reliance Retail Store Count** | 3,616 Stores (FY17) | 18,837 Stores (FY24) | 7 | `26.59%` | `26.59%` | **PASS** |
| **Retail Store Productivity** | ₹9.34 Cr / Store (FY17) | ₹16.29 Cr / Store (FY24) | 7 | `+74.42%` | `+74.42%` | **PASS** |
| **Consumer Share of Revenue** | 10.59% (FY17) | 43.88% (FY24) | 7 | `+3,329 bps` | `+3,329 bps` | **PASS** |
| **Top 2 Telecom Share (CR2)** | 32.68% (FY17) | 73.42% (FY24) | 7 | `+4,074 bps` | `+4,074 bps` | **PASS** |

---

## 3. Interactive Component & User Flow Verification

### 3.1 Navigation & Section Routing
- **Test:** Verify seamless switching across the 5 primary views via the sidebar radio selector (`🏠 Executive Overview`, `🔄 Business Diversification (Q1)`, `📶 Jio & Telecom Dynamics (Q2)`, `🛍️ Reliance Retail Reach (Q3)`, `📚 Data Sources & Methodology`).
- **Result:** **PASS**. All 5 views route cleanly without state collision or unhandled exceptions.

### 3.2 Timeline Range Slider
- **Test:** Adjust timeline range slider between arbitrary bounds (e.g., `FY2017`–`FY2020`, `FY2020`–`FY2024`, `FY2017`–`FY2024`).
- **Result:** **PASS**. All Plotly charts dynamically filter X-axis categories, and section-level KPI summary cards recompute periods ($n$), ending values, and period CAGRs in real time.

### 3.3 Dynamic Multiselect Filters
- **Test:** Filter operating segments in Q1 (e.g., isolate `Reliance Retail` and `Digital Services (Jio)`). Filter operators in Q2 (e.g., isolate `Reliance Jio` and `Bharti Airtel`).
- **Result:** **PASS**. Charts update instantly with corresponding series. Invariant brand color mapping is strictly preserved.

### 3.4 "🔄 Reset All Filters" Action
- **Test:** Modify timeline slider to a sub-window (`FY2019`–`FY2022`), deselect segments, then trigger the sidebar "🔄 Reset All Filters" button.
- **Result:** **PASS**. `st.session_state` restores `timeline_range` to `("FY2017", "FY2024")`, re-enables all business segments and all operators, and triggers a clean rerun.

### 3.5 CSV Data Downloads
- **Test:** Verify CSV download triggers in Sections Q1, Q2, Q3, and Methodology.
- **Result:** **PASS**. Buttons emit RFC-4180 compliant CSV strings matching the active filtered subset:
  - `relyndia_q1_segment_data.csv`
  - `relyndia_q2_telecom_data.csv`
  - `relyndia_q3_retail_data.csv`
  - `relyndia_data_sources_metadata.csv`
  - `relyndia_indian_economic_indicators.csv`

---

## 4. Detailed Explanation Panels Verification

All 7 major analytical visualizations were verified to feature an interactive collapsible expander titled exactly:

```text
[ Detailed Explanation ]
```

Each explanation was verified to contain all 7 mandatory numbered sections in strict sequence:
1. **What the Chart Shows:** Visual encodings, coordinate systems, and data series definition.
2. **Overall Trend:** Macro trajectory over the 8-year span.
3. **Important Changes & Periods:** Phase-by-phase inflection points (e.g., FY21 COVID dip, 5G rollout, store network expansion).
4. **Relevant Quantitative Metrics:** Precise CAGRs, volume additions, and percentage shifts.
5. **Documented Business Factors:** Context cited from RIL Integrated Annual Reports, Reliance Retail filings, and TRAI reports.
6. **Limitations & Cautions:** Segment harmonization caveats, seasonality notes, and metric boundaries.
7. **Key Takeaway:** High-level strategic conclusion.

---

## 5. Visual Integrity & Academic Guardrails

1. **Zero-Baseline Verification:**
   - Both dual-axis visualizations (`create_q3_revenue_vs_stores_dual` and `create_q3_customers_vs_area_dual`) were programmatically inspected. Both primary Y-axis (`yaxis`) and secondary Y-axis (`yaxis2`) enforce `rangemode="tozero"`, guaranteeing zero optical distortion.
2. **Color Palette Invariance:**
   - RIL O2C (`#FD7E14`), Retail (`#DC3545`), Jio (`#0A58CA`), and Others (`#6C757D`) remain invariant across lines, bars, and stacked area charts.
   - Jio (`#0A58CA`), Airtel (`#E02B20`), Vi (`#FFC107`), and BSNL (`#198754`) remain invariant across telecom subscriber and market share views.
3. **Empty-State Resilience:**
   - If a user clears all multiselect options, the application renders informative warning banners (`⚠️ Please select at least one business segment in the sidebar.`) rather than crashing.
4. **Non-Causal Framing:**
   - Observational language is consistently applied across all text: "coincided with", "accompanied by", "concurrent growth", avoiding causal claims.

---

## 6. Final Test Result

**ALL 24 VERIFICATION CHECKS PASSED.** The RELYNDIA dashboard meets all Phase 5 functional, mathematical, and design requirements.
