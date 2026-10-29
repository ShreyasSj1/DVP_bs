# RELYNDIA — Interactive Web Application Run Guide

**Course:** BISL504 Data Visualization Lab  
**Project:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Application Framework:** Streamlit (v1.56.0) + Plotly Express & Graph Objects  
**Primary Entry Point:** `app.py`  

---

## 1. Quick Start

To launch the RELYNDIA interactive web application on your local machine, open your terminal, navigate to the project root directory, and execute:

```bash
# Recommended Launch Command
python3 -m streamlit run app.py
```

Or alternatively, if `streamlit` is directly available in your shell PATH:

```bash
streamlit run app.py
```

### Local Browser Access:
Once launched, Streamlit will automatically open the application in your default web browser at:
- **Local URL:** `http://localhost:8501`
- **Network URL:** `http://127.0.0.1:8501`

---

## 2. Environment & Dependencies Installation

If running on a fresh machine or virtual environment, install the verified dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Verified Dependency Versions:
- **Python:** `>= 3.9` (Tested on 3.12 / 3.13 / 3.14)
- **streamlit:** `>= 1.30.0` (Installed: `1.56.0`)
- **plotly:** `>= 5.10.0` (Installed: `6.7.0`)
- **pandas:** `>= 2.0.0` (Installed: `2.3.3`)
- **numpy:** `>= 1.20.0` (Installed: `1.26.4`)

---

## 3. Application Structure & Key Modules

The web application is organized into 5 cohesive analytical views accessible via the sidebar navigation:

### 1. 🏠 Executive Overview (Reliance at a Glance)
- **High-Level Headline KPIs:** Compares FY2017 baselines against FY2024 current performance:
  - *Consolidated Gross Revenue:* ₹10,00,122 Cr (17.15% 7-Yr CAGR, 3.03x)
  - *Reliance Retail Revenue:* ₹3,06,786 Cr (37.06% 7-Yr CAGR, 9.09x)
  - *Jio Wireless Subscribers:* 469.73 Million (23.26% 7-Yr CAGR, 4.32x)
  - *Physical Store Network:* 18,837 Stores (26.59% 7-Yr CAGR, 5.21x)
  - *Consumer Revenue Share:* 43.88% (vs 10.59% in FY17; +3,329 bps shift)
- **Verified Macroeconomic Indicators Table:** India Nominal GDP, Real GDP Growth (%), Private Capex, and Telecom GVA from RBI DBIE and MoSPI.

### 2. 🔄 Business Diversification (Guiding Question 1)
- *“How has Reliance diversified across its major business segments over time?”*
- **Interactive Controls:** Filter by any combination of operating segments (O2C, Retail, Digital Services, Financials/Others) and adjust the financial year range slider (FY2017–FY2024).
- **Visualizations:**
  - *Chart 1.1:* Multi-line segment revenue trajectories with FY21 pandemic divergence annotation.
  - *Chart 1.2:* Grouped bar side-by-side annual comparison.
  - *Chart 1.3:* 100% normalized stacked area showing portfolio transition.
- **Detailed Explanation:** 7-point expandable panels and one-click filtered CSV data downloads.

### 3. 📶 Jio & Telecom Dynamics (Guiding Question 2)
- *“How did the growth of Jio coincide with changes in India's telecom market?”*
- **Interactive Controls:** Toggle operator visibility (Reliance Jio, Bharti Airtel, Vodafone Idea, BSNL/MTNL) and timeline range.
- **Visualizations:**
  - *Chart 2.1:* Multi-line wireless subscriber base trajectories with Vodafone-Idea merger consolidation peak annotation.
  - *Chart 2.2:* 100% stacked area tracking market share shifts and 2-firm industry concentration.
- **Academic Guardrail:** Strict non-causal language adhering to observational time-series standards.

### 4. 🛍️ Reliance Retail Expansion (Guiding Question 3)
- *“How has Reliance expanded its retail footprint and consumer reach over time?”*
- **Visualizations:**
  - *Chart 3.1:* Dual-axis chart with Retail Revenue (₹ Cr, Bars on left) vs Operating Store Count (Line on right), calibrated with zero-aligned baselines (`rangemode="tozero"`).
  - *Chart 3.2:* Dual-axis line chart tracking Registered Customer Base (Millions, left) alongside Retail Operational Floor Space (M sq ft, right).
- **Data Integrity:** Strict 1-to-1 year alignment keyed by financial year, not assumed row position.

### 5. 📚 Data Sources & Methodology
- Complete audit trail of primary filings (RIL Integrated Annual Reports, TRAI Performance Indicator Reports, RBI DBIE).
- Exact mathematical definitions for CAGR, consumer revenue share, market share, and store throughput.
- Documentation of limitations, annual reporting cutoff (March 31), and segment reclassifications.

---

## 4. Detailed Explanation Feature

Every major visualization in the application features an expandable button labelled:

`📋 [ Detailed Explanation ]`

When clicked, it renders the 7 required analytical sections:
1. **What the Chart Shows:** Exact axes, metrics, categories, and periods.
2. **Overall Trend:** Macro-level trajectory over the timeline.
3. **Important Changes & Periods:** Key historical inflection points (e.g., FY21 COVID-19 crude slump vs data demand surge, FY18 Vodafone-Idea merger).
4. **Relevant Quantitative Metrics:** Precise CAGRs, multiples, and absolute gains calculated directly from the data.
5. **Documented Business Factors:** Context cited strictly from official corporate filings and regulatory releases.
6. **Limitations & Cautions:** Reporting definition nuances and interpretation boundaries.
7. **Key Takeaway:** Concise academic conclusion directly answering the guiding question.

---

## 5. Troubleshooting & FAQ

### Issue: Port 8501 is already in use
If another application or Streamlit process is occupying port 8501, specify an alternative port:
```bash
python3 -m streamlit run app.py --server.port 8502
```

### Issue: Streamlit prompts for email onboarding on first run
The project includes a pre-configured `.streamlit/config.toml` and `.streamlit/credentials.toml` that disables onboarding prompts and telemetry. If running in a restricted sandbox, you can also pass:
```bash
python3 -m streamlit run app.py --browser.gatherUsageStats false --server.headless true
```

### How to Regenerate the Underlying Batch Analysis Pipeline:
If you modify source datasets or want to regenerate all standalone HTML outputs from scratch:
```bash
# Step 1: Run automated profiling
python3 scripts/data_profile.py

# Step 2: Clean and reshape datasets
python3 scripts/data_cleaning.py

# Step 3: Regenerate static & standalone Plotly charts
python3 scripts/visualizations.py
```
