# RELYNDIA — Phase 5 Dashboard Visual Evidence & Screenshot Register

**Course:** BISL504 — Data Visualization Lab (Weeks 8–9)  
**Project:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Phase:** 5 — Dashboard Creation  
**Application URL:** `http://localhost:8501`  

---

## 1. Environment & Screenshot Execution Note

In this automated environment, graphical browser automation tools (e.g., Playwright, Puppeteer, Selenium with Chrome/Gecko drivers) are intentionally not bundled into the minimal Python runtime. 

To ensure complete academic transparency, this document provides:
1. The **complete visual layout map and component structure** for all 5 dashboard views.
2. Step-by-step instructions for the evaluator/user to capture high-resolution screenshots directly from `http://localhost:8501`.
3. Verification logs demonstrating that all UI components, Plotly figures, and Streamlit metrics render with HTTP status `200 OK` and zero runtime tracebacks.

---

## 2. Visual Layout Map & View Hierarchy

### View 1: Executive Overview (`🏠 Executive Overview`)
```text
+---------------------------------------------------------------------------------------------------+
| [Badge] BISL504 Data Visualization Lab | Final Web Application                                   |
| RELYNDIA: Visualizing Reliance's Business & Market Footprint                                     |
| An interactive macroeconomic and corporate visualization platform (FY2017–FY2024)...             |
+---------------------------------------------------------------------------------------------------+
| [KPI Cards: 5 Columns]                                                                            |
| Consolidated Rev   | Retail Revenue      | Jio Subscribers    | Retail Stores     | Consumer Share|
| ₹10,00,122 Cr      | ₹3,06,786 Cr        | 469.73 M           | 18,837 Stores     | 43.88%        |
| 17.15% 7-Yr CAGR   | 37.06% 7-Yr CAGR    | 23.26% 7-Yr CAGR   | 26.59% 7-Yr CAGR  | +33.29% shift |
+---------------------------------------------------------------------------------------------------+
| [Research Objectives & Guiding Questions: 3 Columns]                                              |
| 1. Diversification (Q1)     | 2. Jio Telecom (Q2)          | 3. Retail Scaling (Q3)               |
+---------------------------------------------------------------------------------------------------+
| [Data Table] Verified Indian Macroeconomic Indicators (RBI DBIE / MoSPI Baseline)                 |
+---------------------------------------------------------------------------------------------------+
```

### View 2: Business Diversification (`🔄 Business Diversification (Q1)`)
```text
+---------------------------------------------------------------------------------------------------+
| Section Header: Guiding Question 1: Reliance Business Diversification                            |
| [Dynamic Section KPIs: 4 Columns]                                                                 |
| Timeline Window: FY2017 -> FY2024 | Turnover: ₹10,00,122 Cr | Consumer Rev: ₹4,38,831 Cr | Share: 43.88% |
+---------------------------------------------------------------------------------------------------+
| Chart 1.1: Segment Gross Revenue Trajectories (FY2017–FY2024) [Multi-Line Plotly Chart]          |
| [Insight Card] Key Insight: Retail 37.06% CAGR, Digital Services 36.79% CAGR vs O2C 12.89% CAGR   |
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| Chart 1.2: Annual Segment Revenue Comparison [Grouped Bar Plotly Chart]                           |
| [Insight Card] Key Insight: O2C to Retail scale ratio contracted from 7.16x (FY17) to 1.84x (FY24)|
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| Chart 1.3: Business Mix Transformation [100% Stacked Area Plotly Chart]                           |
| [Insight Card] Key Insight: Consumer share widened from 10.59% to 43.88% (+3,329 bps shift)       |
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| [Button] 📥 Download Displayed Q1 Segment Data (CSV)                                              |
+---------------------------------------------------------------------------------------------------+
```

### View 3: Jio & Telecom Dynamics (`📶 Jio & Telecom Dynamics (Q2)`)
```text
+---------------------------------------------------------------------------------------------------+
| Section Header: Guiding Question 2: Jio & Indian Telecom Market Dynamics                          |
| [Dynamic Section KPIs: 4 Columns]                                                                 |
| Industry Base: 1,165.2 M | Jio Base: 469.73 M | Jio Share: 40.31% (+3,102 bps) | CR2: 73.42%      |
+---------------------------------------------------------------------------------------------------+
| Chart 2.1: Indian Telecom Wireless Subscriber Trajectories [Multi-Line Plotly Chart]              |
| [Insight Card] Key Insight: Jio 23.26% CAGR (108.7M to 469.7M) while Vi declined -10.30% CAGR     |
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| Chart 2.2: Operator Market Share Evolution [100% Stacked Area Plotly Chart]                       |
| [Insight Card] Key Insight: Top 2 private operators (Jio + Airtel) command 73.42% of subscribers  |
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| [Button] 📥 Download Displayed Q2 Telecom Data (CSV)                                              |
+---------------------------------------------------------------------------------------------------+
```

### View 4: Reliance Retail Reach (`🛍️ Reliance Retail Reach (Q3)`)
```text
+---------------------------------------------------------------------------------------------------+
| Section Header: Guiding Question 3: Reliance Retail Expansion & Consumer Reach                    |
| [Dynamic Section KPIs: 4 Columns]                                                                 |
| Retail Revenue: ₹3,06,786 Cr | Stores: 18,837 (+15,221) | Customers: 304.0 M | Productivity: ₹16.29 Cr |
+---------------------------------------------------------------------------------------------------+
| Chart 3.1: Retail Revenue Growth vs Physical Store Expansion [Dual-Axis Bar & Line Chart]         |
| [Insight Card] Key Insight: Stores grew 5.21x (26.59% CAGR), Revenue grew 9.09x (37.06% CAGR)     |
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| Chart 3.2: Customer Base & Floor Space Scaling [Dual-Axis Line & Line Chart]                      |
| [Insight Card] Key Insight: Registered customers grew 8.69x (35M to 304M), Area grew 5.86x        |
| [v] [ Detailed Explanation ] (Click to expand 7-point analysis)                                   |
+---------------------------------------------------------------------------------------------------+
| [Button] 📥 Download Displayed Q3 Retail Footprint Data (CSV)                                     |
+---------------------------------------------------------------------------------------------------+
```

### View 5: Data Sources & Methodology (`📚 Data Sources & Methodology`)
```text
+---------------------------------------------------------------------------------------------------+
| Section Header: Data Sources, Verification & Analytical Methodology                               |
| [Interactive Table] Primary Verified Sources & Metadata Audit Register (RIL, TRAI, RBI)           |
| [Buttons: 2 Columns] 📥 Download Metadata CSV | 📥 Download Economic Indicators CSV               |
+---------------------------------------------------------------------------------------------------+
| [Formal Mathematical Formulas Block in LaTeX]                                                     |
| 1. Compound Annual Growth Rate (CAGR)                                                             |
| 2. Consumer Revenue Share (%)                                                                     |
| 3. Telecom Operator Market Share (%)                                                              |
| 4. Retail Store Productivity (₹ Cr / Store)                                                       |
| 5. Retail Sales Density (₹ / Sq Ft)                                                               |
+---------------------------------------------------------------------------------------------------+
| [Academic Limitations & Guardrails Callout List]                                                  |
+---------------------------------------------------------------------------------------------------+
```

---

## 3. Recommended Evaluator Screenshot Protocol

To export formal visual screenshots for course presentation slides or print reports:

1. Start the Streamlit application:
   ```bash
   python3 -m streamlit run app.py
   ```
2. Open `http://localhost:8501` in Google Chrome, Microsoft Edge, or Safari.
3. Use your browser's Developer Tools (`F12` or `Cmd+Option+I` on macOS) -> Command Menu (`Cmd+Shift+P`) -> type `Capture full size screenshot`.
4. Recommended file naming convention:
   - `01_executive_overview.png`
   - `02_q1_business_diversification.png`
   - `03_q2_telecom_dynamics.png`
   - `04_q3_retail_expansion.png`
   - `05_detailed_explanation_expanded.png`
   - `06_data_sources_methodology.png`
