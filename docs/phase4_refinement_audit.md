# RELYNDIA — Phase 4 Refinement Audit & Initial State Analysis

**Course:** BISL504 Data Visualization Lab  
**Phase:** 4 — Implementation Refinement and Freeze  
**Project:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Date:** October 2026  
**Auditor:** RELYNDIA Project Team  

---

## 1. Initial Project Inventory & State Assessment

Before implementing any modifications, a complete audit of the repository assets, scripts, data pipelines, and documentation was conducted.

### 1.1 Verified Primary Datasets (`data/`)
All primary datasets are verified against official regulatory filings (TRAI, RBI) and corporate annual reports (RIL, Reliance Retail):

| Dataset File | Dimensions | Time Horizon | Non-Null Rate | Duplicates | Primary Verification Source |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `verified_ril_financial_segment_growth.csv` | 8 rows × 9 cols | FY2017–FY2024 | 100% | 0 | RIL Integrated Annual Reports (FY17–FY24) |
| `verified_telecom_market_subscribers.csv` | 8 rows × 7 cols | FY2017–FY2024 | 100% | 0 | TRAI Yearly Performance Indicator Reports |
| `verified_reliance_retail_footprint.csv` | 8 rows × 7 cols | FY2017–FY2024 | 100% | 0 | Reliance Retail Media Releases & RIL Filings |
| `verified_indian_economic_indicators.csv` | 8 rows × 6 cols | FY2017–FY2024 | 100% | 0 | RBI Handbook of Statistics & MoSPI GVA |
| `data_sources_and_verification.csv` | Metadata Audit | FY2017–FY2024 | 100% | 0 | Full citation & page index tracking |

*Audit Finding:* Primary source datasets are 100% intact, clean, and contain zero missing or fabricated values. They will remain completely untouched.

### 1.2 Cleaned & Reshaped Datasets (`clean_data/`)
The automated cleaning pipeline (`scripts/data_cleaning.py`) produces both wide and tidy-long formats:
- `clean_ril_financial_segment_growth.csv` (Wide format with derived percentage contributions and margins)
- `clean_ril_segments_long.csv` (Tidy long format for Plotly Express color grouping)
- `clean_telecom_market_subscribers.csv` (Wide format with calculated market shares)
- `clean_telecom_subscribers_long.csv` (Tidy long format for multi-operator plotting)
- `clean_reliance_retail_footprint.csv` (Wide format with derived store density and productivity metrics)

### 1.3 Python Automation Scripts (`scripts/`)
- `scripts/data_profile.py`: Automatically inspects all raw datasets and outputs markdown summary tables to `docs/data_profile.md`.
- `scripts/data_cleaning.py`: Performs schema standardization, feature engineering, wide-to-long reshaping, and exports clean CSVs.
- `scripts/visualizations.py`: Generates the 7 core Plotly visualizations.

### 1.4 Visualizations & Generated Outputs (`outputs/`)
All 7 retained visualizations are generated as standalone interactive HTML files:
- `outputs/reliance/q1_segment_revenue_trend.html` (Multi-line)
- `outputs/reliance/q1_segment_comparison_grouped_bar.html` (Grouped bar)
- `outputs/reliance/q1_business_composition_100pct_stacked.html` (100% stacked area)
- `outputs/telecom/q2_telecom_subscribers_multiline.html` (Multi-line)
- `outputs/telecom/q2_telecom_market_share_stacked_area.html` (100% stacked area)
- `outputs/retail/q3_retail_revenue_vs_stores_dual_axis.html` (Dual-axis bar + line)
- `outputs/retail/q3_retail_customers_and_area_trend.html` (Dual-axis multi-line)

### 1.5 Presentation Interfaces & Documentation (`index.html`, `docs/`)
- `index.html`: Unified local visual explorer embedding the 7 HTML charts via iframes, featuring interactive `[ Detailed Explanation ]` panels.
- `docs/visualization_insights.md`: 6-point structured academic commentary for each chart.
- `docs/code_walkthrough_notes.md`: Oral viva examination preparation notes.
- `docs/AI_usage_log.md`: Transparent record of AI assistance and team decisions.
- `docs/implementation_freeze_status.md`: Week 7 freeze register.

---

## 2. Gap Analysis: What is Correct vs What Needs Correction

### 2.1 What is Already Correct:
1. **Source Data Integrity:** 100% verified against primary sources, zero nulls, zero duplicates.
2. **Chart Selection:** Appropriate visual forms selected for all 3 guiding questions (trends over time, side-by-side annual comparisons, and 100% compositional shares).
3. **Dual-Axis Baselines:** Both axes of dual-axis charts have `rangemode="tozero"`, ensuring no distorted baseline perceptions.
4. **Interactive Features:** Standalone HTML export with CDN-linked Plotly engine; toggleable `[ Detailed Explanation ]` panels in `index.html`.
5. **Non-Causal Academic Framing:** Neutral vocabulary used throughout titles and notes.

### 2.2 What Needs Refinement & Correction in Phase 4:
1. **Subtitles & Informative Context:** Charts currently have descriptive main titles, but lack explicit subtitles detailing metric definitions, units, and source citations directly on the canvas.
2. **Targeted Factual Annotations:** Key verified macroeconomic/historical events (such as the FY21 COVID-19 pandemic divergence and the FY18–FY19 Vodafone-Idea merger) should be annotated directly on the relevant time-series to enhance interpretability without crowding.
3. **Categorical Axis Ordering:** While data is chronologically sorted, Plotly categorical X-axes should explicitly define `categoryorder="array"` and `categoryarray` to prevent any browser-level ordering discrepancies.
4. **PNG Image Export Graceful Fallback:** Plotly 6.7.0 is installed, but the static image engine (`kaleido`) is not present in the lab environment. The export function must catch this gracefully and document it in the reproducibility report.
5. **Mathematical Verification:** Standardize all CAGR calculations to 2 decimal places using exact elapsed periods ($n=7$ for FY17–FY24; $n=6$ for FY18–FY24).
6. **Documentation Synchronization:** Create Phase 4 audit, reproducibility report, freeze record, and update code walkthrough and AI usage logs.

---

## 3. Data Integrity & Mathematical Recalculations

All metrics were re-computed directly from verified source data using the standard CAGR formula:
$$\text{CAGR} = \left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{n}} - 1$$

### 3.1 Reliance Segment & Corporate Growth (FY2017–FY2024, $n=7$)
- **Consolidated Gross Revenue:** ₹3,30,180 Cr $\rightarrow$ ₹10,00,122 Cr | **3.03x** | **17.15% CAGR**
- **O2C Gross Revenue:** ₹2,41,674 Cr $\rightarrow$ ₹5,64,748 Cr | **2.34x** | **12.89% CAGR**
- **Retail Gross Revenue:** ₹33,765 Cr $\rightarrow$ ₹3,06,786 Cr | **9.09x** | **37.06% CAGR**
- **Digital Services Revenue (FY18–FY24, $n=6$):** ₹20,154 Cr $\rightarrow$ ₹1,32,045 Cr | **6.55x** | **36.79% CAGR**
  *(Note: FY17 was commercial launch year with partial ₹1,207 Cr revenue; using FY18 full year gives the standard 6-year operational CAGR)*
- **Consumer Share of Revenue:** 10.59% (FY17) $\rightarrow$ 43.88% (FY24) (**+3,329 basis points**)
- **O2C Share of Revenue:** 73.20% (FY17) $\rightarrow$ 56.47% (FY24) (**-1,673 basis points**)

### 3.2 Telecom Market & Operator Trajectories (FY2017–FY2024, $n=7$)
- **Reliance Jio Subscribers:** 108.68M $\rightarrow$ 469.73M | **4.32x** | **23.26% CAGR**
- **Bharti Airtel Subscribers:** 273.65M $\rightarrow$ 385.83M | **1.41x** | **5.03% CAGR**
- **Vodafone Idea Subscribers (FY18 peak to FY24, $n=6$):** 408.06M $\rightarrow$ 212.64M | **0.52x** | **-10.30% CAGR**
  *(FY17 to FY24, $n=7$: 387.06M $\rightarrow$ 212.64M, -8.20% CAGR)*
- **Jio Subscriber Market Share:** 9.29% (FY17) $\rightarrow$ 40.31% (FY24) (**+3,102 basis points**)
- **Top 2 Private Concentration (CR2 = Jio + Airtel):** 32.68% (FY17) $\rightarrow$ 73.42% (FY24)

### 3.3 Reliance Retail Operational Footprint (FY2017–FY2024, $n=7$)
- **Operating Store Count:** 3,616 $\rightarrow$ 18,837 stores | **5.21x** | **26.59% CAGR** (+15,221 stores)
- **Registered Customers:** 35.0M $\rightarrow$ 304.0M | **8.69x** | **36.18% CAGR**
- **Retail Floor Area:** 13.5M $\rightarrow$ 79.1M sq ft | **5.86x** | **28.73% CAGR**
- **Revenue per Store:** ₹9.34 Cr/store $\rightarrow$ ₹16.29 Cr/store | **+74.42% productivity gain**

---

## 4. Retail Revenue vs Store Count Data Mapping Audit

### 4.1 Verification Table: Raw vs Clean Alignment
To address the suspected mapping error in Chart 3.1 (*"Reliance Retail — Revenue Growth vs Physical Store Expansion"*), the data rows from `data/verified_reliance_retail_footprint.csv` and `clean_data/clean_reliance_retail_footprint.csv` were compared row-for-row:

| Financial Year | Raw Revenue (₹ Cr) | Clean Revenue (₹ Cr) | Raw Stores | Clean Stores | Revenue Match | Store Match |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FY2017** | ₹33,765 | ₹33,765 | 3,616 | 3,616 | ✅ True | ✅ True |
| **FY2018** | ₹69,198 | ₹69,198 | 7,573 | 7,573 | ✅ True | ✅ True |
| **FY2019** | ₹1,30,566 | ₹1,30,566 | 10,415 | 10,415 | ✅ True | ✅ True |
| **FY2020** | ₹1,62,936 | ₹1,62,936 | 11,784 | 11,784 | ✅ True | ✅ True |
| **FY2021** | ₹1,57,629 | ₹1,57,629 | 12,711 | 12,711 | ✅ True | ✅ True |
| **FY2022** | ₹1,99,704 | ₹1,99,704 | 15,196 | 15,196 | ✅ True | ✅ True |
| **FY2023** | ₹260,364 | ₹260,364 | 18,040 | 18,040 | ✅ True | ✅ True |
| **FY2024** | ₹306,786 | ₹306,786 | 18,837 | 18,837 | ✅ True | ✅ True |

### 4.2 Root Cause Analysis of the Suspected Mapping Error
1. **Data Rows & Indexes:** Both series are derived from the identical DataFrame (`df_ret_clean`), sorted chronologically by financial year. There is zero index misalignment, zero missing years, and zero row swapping.
2. **Root Cause Identified:** The visual perception of a "mapping error" in early project iterations stemmed from **unaligned dual Y-axis zero baselines**. When secondary Y-axes default to automatic range clamping (e.g., starting at 3,000 stores instead of 0), the store line begins elevated, visually obscuring the proportional relationship with the revenue bars starting at 0.
3. **Resolution Implemented:** Explicitly setting `rangemode="tozero"` with calibrated ranges (`[0, 360000]` for revenue, `[0, 22000]` for stores) and adding strict pre-plotting assertion checks permanently guarantees visual and mathematical fidelity.

---

## 5. Chart Selection Audit

| Chart ID | File Name | Guiding Question | Chart Type | Suitability Assessment | Recommendation |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Q1.1** | `q1_segment_revenue_trend.html` | Q1: Diversification | Multi-Line Chart | **Optimal:** Ideal for tracking continuous multi-year financial trends across 4 segments. | **RETAIN** |
| **Q1.2** | `q1_segment_comparison_grouped_bar.html` | Q1: Diversification | Grouped Bar Chart | **Optimal:** Best for direct side-by-side magnitude comparisons across segments in each fiscal year. | **RETAIN** |
| **Q1.3** | `q1_business_composition_100pct_stacked.html` | Q1: Diversification | 100% Stacked Area | **Optimal:** Mathematically normalizes consolidated revenue to 100%, proving portfolio transformation. | **RETAIN** |
| **Q2.1** | `q2_telecom_subscribers_multiline.html` | Q2: Telecom Dynamics | Multi-Line Chart | **Optimal:** Accurately depicts subscriber trajectories across 4 competing operators without clutter. | **RETAIN** |
| **Q2.2** | `q2_telecom_market_share_stacked_area.html` | Q2: Telecom Dynamics | 100% Stacked Area | **Optimal:** Perfectly suited for continuous market share distribution summing to 100%. | **RETAIN** |
| **Q3.1** | `q3_retail_revenue_vs_stores_dual_axis.html` | Q3: Retail Expansion | Dual-Axis Bar + Line | **Optimal:** Clearly differentiates financial flow (bars) from physical assets (line) on a unified timeline. | **RETAIN** |
| **Q3.2** | `q3_retail_customers_and_area_trend.html` | Q3: Retail Expansion | Dual-Axis Line Chart | **Optimal:** Effective for comparing two non-additive scaling metrics (customers vs floor space). | **RETAIN** |

All 7 visualizations are appropriate for their respective analytical goals. No new charts are needed, and no charts should be removed.
