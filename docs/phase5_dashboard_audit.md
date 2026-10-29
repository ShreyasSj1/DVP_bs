# RELYNDIA — Phase 5 Dashboard Creation Audit

**Course:** BISL504 Data Visualization Lab (Weeks 8–9)  
**Phase:** 5 — Dashboard Creation  
**Project:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Date of Audit:** October 2026  
**Auditor:** RELYNDIA Project Team  

---

## 1. Project Inventory & Baseline Readiness

A comprehensive inspection of the repository was conducted before initiating Phase 5 dashboard refinement.

### 1.1 Existing Assets & Pipeline Status:
- **Verified Source Datasets (`data/`):** 4 primary CSV datasets (`verified_ril_financial_segment_growth.csv`, `verified_telecom_market_subscribers.csv`, `verified_reliance_retail_footprint.csv`, `verified_indian_economic_indicators.csv`) and 1 metadata audit register (`data_sources_and_verification.csv`). All 100% verified against RIL Annual Reports, TRAI, and RBI DBIE with zero missing values.
- **Cleaned Datasets (`clean_data/`):** 5 analysis-ready CSVs (wide and tidy-long formats) generated programmatically by `scripts/data_cleaning.py`.
- **Batch Visualization Engine (`scripts/visualizations.py`):** Produces 7 standalone Plotly HTML charts in `outputs/` with calibrated zero-aligned baselines and factual annotations.
- **Web Application Foundation (`app.py`, `components/`):** Basic Streamlit application structured with modular `components/charts.py`, `components/metrics.py`, and `components/explanations.py`.

---

## 2. Gap Analysis: What Works vs What is Incomplete for Phase 5

| Dashboard Component | Existing Status | Phase 5 Requirement & Gap Identified | Action Plan |
| :--- | :---: | :--- | :--- |
| **Executive Overview Page** | Basic Layout | Needs portfolio-level research narrative, headline KPI cards with explicit baseline deltas, and macroeconomic context table. | **ENHANCE:** Add comprehensive intro, methodology summary, and verified macro table. |
| **Business Diversification (Q1)** | Functional Charts | Visualizations display well, but lacks dynamic section-level KPI cards that adapt when segments or years are filtered. | **ADD:** Dynamic KPI summary (Selected Turnover, Consumer Revenue, Consumer Share) above charts. |
| **Jio & Telecom Dynamics (Q2)** | Functional Charts | Static layout; lacks operator-level net growth summaries and dynamic concentration metrics based on user selection. | **ADD:** Dynamic telecom KPIs (Total Selected Base, Jio Share of Selected, Net Growth). |
| **Reliance Retail Reach (Q3)** | Functional Dual-Axes | Dual-axis charts are zero-aligned, but lacks dynamic store addition and productivity throughput KPI cards for selected timeline. | **ADD:** Dynamic retail KPIs (Period Revenue, Net Stores Added, Store Productivity). |
| **Interactivity & Controls** | Sliders Present | Has year slider and multiselects, but **lacks a "Reset Filters" button** to quickly return to the default state. | **IMPLEMENT:** Add session-state backed "🔄 Reset All Filters" button in sidebar. |
| **Detailed Explanation Feature** | Present | Expanders currently use custom titles; course specification requires exact label: **`Detailed Explanation`**. | **STANDARDIZE:** Enforce exact label `st.expander("Detailed Explanation")` for all 7 charts. |
| **Design & Typography Hierarchy** | Clean Styling | Needs refined spacing, high-contrast KPI cards, consistent brand color swatches, and clean empty states. | **POLISH:** Refine CSS styles and layout spacing. |
| **Documentation & User Guide** | Partial | Needs Phase 5 audit, AI design critique log, testing report, user guide, and updated README. | **CREATE:** Compile complete Phase 5 documentation suite. |

---

## 3. Preserved Phase 4 Artifacts & Constraints

To maintain academic rigor and project integrity:
1. **Zero Raw Data Modification:** `data/*.csv` remains completely untouched.
2. **Zero Fabrication of Calculations:** All CAGRs, multiples, and ratios are dynamically derived using standard formulas:
   $$\text{CAGR} = \left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{n}} - 1$$
3. **Retail Revenue / Store Mapping:** Strict 1-to-1 year keying is preserved; zero manual visual point shifting is permitted.
4. **Academic Guardrails:** Observational language is strictly maintained across all titles, captions, and explanations (coexistence, concurrent growth, and market transition—avoiding causal determinism).
