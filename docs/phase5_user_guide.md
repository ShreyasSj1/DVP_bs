# RELYNDIA — Phase 5 Dashboard User & Operational Guide

**Course:** BISL504 — Data Visualization Lab  
**Project:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Target Audience:** Academic evaluators, peer researchers, and data visualization students  

---

## 1. Introduction

**RELYNDIA** is an interactive macroeconomic and corporate data-visualization web application built with **Streamlit** and **Plotly**. It visualizes the structural transformation of Reliance Industries Limited (RIL) across Energy (Oil-to-Chemicals), Telecom (Jio Platforms), and Physical Retail from FY2017 to FY2024.

All visualizations are driven by verified primary filings (RIL Integrated Annual Reports, Reliance Retail annual accounts, Telecom Regulatory Authority of India (TRAI) reports, and Reserve Bank of India (RBI DBIE) statistics).

---

## 2. Installation & Quick Start

### 2.1 System Requirements
- **Python:** Version 3.10, 3.11, or 3.12
- **Operating System:** macOS, Linux, or Windows 10/11
- **Browser:** Google Chrome, Safari, Mozilla Firefox, or Microsoft Edge

### 2.2 Setup Instructions

1. **Clone or Navigate to the Project Directory:**
   ```bash
   cd /path/to/DVP
   ```

2. **(Optional but Recommended) Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit Application:**
   ```bash
   python3 -m streamlit run app.py
   ```
   *Alternative command:*
   ```bash
   streamlit run app.py
   ```

5. **Access the Dashboard:**
   Open your browser to:
   ```text
   http://localhost:8501
   ```

---

## 3. Navigating the Dashboard

The application features a persistent **Left Sidebar** containing navigation controls, global interactive filters, and academic compliance disclosures.

### 3.1 Section Selector (Sidebar Radio)
Switch between 5 analytical views:
- **`🏠 Executive Overview`**: Top-level executive summary, 5 headline portfolio KPI cards, guiding research question summaries, and verified Indian macroeconomic indicator context (RBI/MoSPI).
- **`🔄 Business Diversification (Q1)`**: Deep dive into RIL's segment revenue trajectories, grouped scale comparison, and 100% normalized stacked area composition shift.
- **`📶 Jio & Telecom Dynamics (Q2)`**: Telecom wireless subscriber trajectories and 100% subscriber market share evolution across Jio, Airtel, Vi, and BSNL (TRAI).
- **`🛍️ Reliance Retail Reach (Q3)`**: Retail scaling analysis through dual-axis charts: Gross Revenue vs Physical Store Count, and Registered Customers vs Operational Floor Area.
- **`📚 Data Sources & Methodology`**: Primary source audit register, LaTeX mathematical formulas (CAGR, shares, productivity), academic limitations, and metadata CSV downloads.

---

## 4. Interactive Controls & Features

### 4.1 Timeline Range Slider
Located in the sidebar under **Global Interactive Controls**:
- Drag the left and right slider handles to focus on any custom historical window (e.g., `FY2017` to `FY2020` for consumer takeoff, or `FY2021` to `FY2024` for post-COVID recovery).
- **Dynamic Effect:** All charts, tables, and section-level KPI summary cards instantly update their calculations to reflect the selected temporal window.

### 4.2 Dynamic Segment & Operator Filters
- When viewing **Business Diversification (Q1)**, a multiselect box appears in the sidebar allowing you to isolate specific business segments (e.g., compare `Reliance Retail` against `Digital Services (Jio)`).
- When viewing **Jio & Telecom Dynamics (Q2)**, an operator multiselect box appears, allowing pairwise or multi-operator comparisons (e.g., `Reliance Jio` vs `Bharti Airtel`).

### 4.3 "🔄 Reset All Filters" Button
Located directly in the sidebar above the slider:
- One click instantly restores the timeline slider to the full 8-year span (`FY2017`–`FY2024`) and re-enables all business segments and telecom operators.

### 4.4 Data Download Buttons (CSV)
At the bottom of each analytical section and on the methodology page, click:
- `📥 Download Displayed Q1 Segment Data (CSV)`
- `📥 Download Displayed Q2 Telecom Data (CSV)`
- `📥 Download Displayed Q3 Retail Footprint Data (CSV)`
- `📥 Download Data Sources Metadata (CSV)`
- `📥 Download Economic Indicators (CSV)`
This provides direct, transparent access to the exact data currently rendered on screen for external validation.

### 4.5 Chart Hover & Tooltips
- Hover your mouse over any data point, bar, or line to view rich contextual tooltips displaying the exact fiscal year, metric name, monetary/volume value, and formatted units.
- **Plotly Toolbar (Top-Right of Each Chart):**
  - **Zoom / Pan:** Click and drag on the chart to zoom into specific years or ranges.
  - **Reset Axes:** Double-click anywhere on the chart, or click the home icon in the Plotly toolbar, to reset the view.
  - **Legend Toggle:** Single-click a legend item to hide/show its trace; double-click a legend item to isolate it exclusively.

---

## 5. Using the "[ Detailed Explanation ]" Feature

Directly beneath every major analytical visualization, you will find an expandable panel clearly labeled:

```text
[ Detailed Explanation ]
```

### How to Use:
1. Click the expander to open the panel.
2. Review the structured, academic commentary organized into 7 standard numbered sections:
   - **1. What the Chart Shows:** Clarifies visual encodings, coordinate systems, and data series.
   - **2. Overall Trend:** Synthesizes the macro trajectory over the 8-year period.
   - **3. Important Changes & Periods:** Highlights key economic inflection points (e.g., FY2021 pandemic divergence, 4G adoption, store expansion).
   - **4. Relevant Quantitative Metrics:** Details verified CAGRs, volume net additions, and basis-point shifts.
   - **5. Documented Business Factors:** Contextualizes trends using primary corporate annual reports and regulatory filings.
   - **6. Limitations & Cautions:** Discloses segment harmonization, seasonality, or reporting boundaries.
   - **7. Key Takeaway:** Concludes with the primary empirical takeaway.
3. Click again to collapse the panel and maintain a clean visual reading flow.

---

## 6. Troubleshooting & FAQs

### Q1: The terminal says "Port 8501 is not available".
- **Cause:** Another process (e.g., an earlier Streamlit session) is occupying port 8501.
- **Fix:** Specify a different port when launching:
  ```bash
  python3 -m streamlit run app.py --server.port 8502
  ```

### Q2: Streamlit prompts for an email address on first run.
- **Cause:** Streamlit displays a one-time onboarding prompt on newly installed machines.
- **Fix:** Press `Enter` to leave it blank, or configure `.streamlit/credentials.toml`:
  ```toml
  [general]
  email = ""
  ```

### Q3: Deselecting all segments or operators causes a warning.
- **Behavior:** The dashboard displays an informative notice: `⚠️ Please select at least one business segment in the sidebar.`
- **Fix:** Re-select at least one segment/operator, or click the **"🔄 Reset All Filters"** button in the sidebar.

### Q4: Are the dual-axis charts zero-aligned?
- **Yes:** Both dual-axis charts in Section Q3 enforce `rangemode="tozero"` on both the left and right Y-axes, ensuring visual proportion accurately reflects empirical values without distorting growth rates.
