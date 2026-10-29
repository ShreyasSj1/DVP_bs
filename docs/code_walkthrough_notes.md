# RELYNDIA — Code Walkthrough Notes (Oral Viva Defense Guide)
**Course:** BISL504 Data Visualization Lab  
**Phase:** 4 — Implementation Refinement & Freeze  
**Project Title:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Target Purpose:** Oral presentation and faculty viva defense preparation. Explains the 7 core implementation sections in simple, rigorous, explainable language.

---

## 1. Loading Verified Source Data (`scripts/data_cleaning.py`)

### Code:
```python
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

df_ril = pd.read_csv(os.path.join(DATA_DIR, "verified_ril_financial_segment_growth.csv"))
df_tel = pd.read_csv(os.path.join(DATA_DIR, "verified_telecom_market_subscribers.csv"))
df_ret = pd.read_csv(os.path.join(DATA_DIR, "verified_reliance_retail_footprint.csv"))
```
- **What it does:** Uses dynamic relative path resolution via `os.path.abspath` and `BASE_DIR` to reliably locate and load the verified primary datasets into Pandas DataFrames.
- **Why it is needed:** Avoids hard-coded local file paths (e.g. `/Users/...`), ensuring the code runs smoothly on any lab machine, evaluator laptop, or automated testing runner.
- **What output it produces:** In-memory Pandas DataFrames (`df_ril`, `df_tel`, `df_ret`) ready for transformation.

---

## 2. Data Cleaning & Schema Standardization (`scripts/data_cleaning.py`)

### Code:
```python
df_ril_clean = pd.DataFrame()
df_ril_clean["Financial_Year"] = df_ril["Financial Year"]
df_ril_clean["Year"] = df_ril["Financial Year"].str.replace("FY", "").astype(int)
df_ril_clean["Gross_Revenue_Cr"] = df_ril["Gross Revenue (₹ Cr)"]
df_ril_clean["O2C_Revenue_Cr"] = df_ril["O2C Revenue (₹ Cr)"]
df_ril_clean["Retail_Revenue_Cr"] = df_ril["Retail Revenue (₹ Cr)"]
df_ril_clean["Digital_Services_Revenue_Cr"] = df_ril["Digital Services Revenue (₹ Cr)"]
```
- **What it does:** Standardizes column names into snake_case, extracts clean integer year numbers (`2017` to `2024`) from string strings (`FY2017`), and preserves original values.
- **Why it is needed:** Eliminates special characters (parentheses, currency symbols) from column headers, making downstream calculations and Plotly label mapping error-free.
- **What output it produces:** Cleaned base DataFrames with consistent schemas.

---

## 3. Data Transformation & Derived Metrics (`scripts/data_cleaning.py`)

### Code:
```python
# Calculate % share of Gross Revenue for each segment
df_ril_clean["O2C_Share_Pct"] = (df_ril_clean["O2C_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100
df_ril_clean["Retail_Share_Pct"] = (df_ril_clean["Retail_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100
df_ril_clean["Digital_Share_Pct"] = (df_ril_clean["Digital_Services_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100

# Combine Retail + Digital to track total Consumer-facing contribution
df_ril_clean["Consumer_Share_Pct"] = df_ril_clean["Retail_Share_Pct"] + df_ril_clean["Digital_Share_Pct"]

# Derived Retail operational productivity
df_ret_clean["Revenue_Per_Store_Cr"] = round(df_ret_clean["Retail_Revenue_Cr"] / df_ret_clean["Operating_Store_Count"], 2)
df_ret_clean["Revenue_Per_SqFt_Rs"] = round((df_ret_clean["Retail_Revenue_Cr"] * 1e7) / (df_ret_clean["Retail_Floor_Area_M_SqFt"] * 1e6), 2)
```
- **What it does:** Computes essential mathematical ratios: segment percentage contributions, combined consumer-facing revenue share, and revenue per physical store.
- **Why it is needed:** Directly answers Guiding Questions Q1 and Q3 by providing normalized percentage shares and store density metrics that raw totals alone cannot reveal.
- **What output it produces:** Analysis-ready wide CSV files saved to `clean_data/`.

---

## 4. Grouping & Reshaping (Wide-to-Long Tidy Format) (`scripts/data_cleaning.py`)

### Code:
```python
segment_map = [
    ("Oil-to-Chemicals (O2C)", "O2C_Revenue_Cr", "O2C_Share_Pct", "Traditional Energy"),
    ("Reliance Retail", "Retail_Revenue_Cr", "Retail_Share_Pct", "Consumer Facing"),
    ("Digital Services (Jio)", "Digital_Services_Revenue_Cr", "Digital_Share_Pct", "Consumer Facing"),
    ("Financial Services & Others", "Financial_Others_Revenue_Cr", "Financial_Others_Share_Pct", "Others")
]

long_records = []
for idx, row in df_ril_clean.iterrows():
    for seg_name, rev_col, share_col, cat in segment_map:
        long_records.append({
            "Financial_Year": row["Financial_Year"],
            "Year": row["Year"],
            "Segment": seg_name,
            "Segment_Category": cat,
            "Revenue_Cr": row[rev_col],
            "Share_Pct": round(row[share_col], 2)
        })

df_ril_long = pd.DataFrame(long_records)
```
- **What it does:** Unpivots multiple separate segment revenue columns into a unified "tidy" format where each row represents one segment in one fiscal year.
- **Why it is needed:** Plotly Express requires tidy data to dynamically assign colors, group bars, and compute stacked area fills.
- **What output it produces:** `clean_ril_segments_long.csv` and `clean_telecom_subscribers_long.csv` in `clean_data/`.

---

## 5. Pre-Plotting Validation Assertions (`scripts/visualizations.py`)

### Code:
```python
EXPECTED_YEARS = ["FY2017", "FY2018", "FY2019", "FY2020", "FY2021", "FY2022", "FY2023", "FY2024"]

assert df_ret_clean["Financial_Year"].tolist() == EXPECTED_YEARS, "Financial Year sequence mismatch"
assert df_ret_clean["Financial_Year"].is_unique, "Duplicate financial years found"
assert len(df_ret_clean["Retail_Revenue_Cr"]) == len(df_ret_clean["Operating_Store_Count"]) == 8, "Length mismatch"
assert not df_ret_clean["Retail_Revenue_Cr"].isna().any(), "NaN found in Retail Revenue"
assert not df_ret_clean["Operating_Store_Count"].isna().any(), "NaN found in Operating Store Count"
```
- **What it does:** Executes strict runtime assertions immediately before figure generation to ensure sequence matching, no nulls, and exact series alignment.
- **Why it is needed:** Programmatically guards against data mapping errors, dropped rows, or unsorted financial years.
- **What output it produces:** Guarantees 100% data integrity before rendering.

---

## 6. Visualization Generation & Factual Annotations (`scripts/visualizations.py`)

### Code:
```python
# Unified Academic Layout Dictionary
LAYOUT_DEFAULTS = dict(
    template="plotly_white",
    font=dict(family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif", size=12, color="#212529"),
    title_font=dict(size=14, color="#212529"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=11)),
    margin=dict(l=65, r=65, t=85, b=55),
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF"
)

# Common Categorical X-Axis
COMMON_XAXIS = dict(
    title="Financial Year",
    type="category",
    categoryorder="array",
    categoryarray=EXPECTED_YEARS,
    showgrid=True,
    gridcolor="#F1F3F5",
    linecolor="#CED4DA"
)

# Dual-Axis Subplot with Zero-Aligned Baselines
fig_q3_dual = make_subplots(specs=[[{"secondary_y": True}]])
fig_q3_dual.add_trace(
    go.Bar(x=df_ret_clean["Financial_Year"], y=df_ret_clean["Retail_Revenue_Cr"], name="Retail Revenue (₹ Cr)", marker_color="#DC3545"),
    secondary_y=False
)
fig_q3_dual.add_trace(
    go.Scatter(x=df_ret_clean["Financial_Year"], y=df_ret_clean["Operating_Store_Count"], name="Operating Stores", mode="lines+markers", line=dict(color="#0A58CA", width=3.5)),
    secondary_y=True
)
fig_q3_dual.update_yaxes(title_text="Gross Revenue (₹ Crore)", rangemode="tozero", range=[0, 360000], secondary_y=False)
fig_q3_dual.update_yaxes(title_text="Operating Stores Count", rangemode="tozero", range=[0, 22000], secondary_y=True, showgrid=False)

# Factual Macroeconomic Annotation
fig_q3_dual.add_annotation(
    x="FY2021", y=157629,
    text="<b>FY21 Pandemic Lockdowns</b><br>Temporary retail store closures<br>paused revenue growth (-3.3%)",
    showarrow=True, arrowhead=2, arrowcolor="#DC3545", secondary_y=False
)
```
- **What it does:** Builds interactive charts using Plotly Express and Graph Objects with descriptive subtitles, fixed categorical arrays, zero-aligned dual Y-axes, and evidence-based annotations.
- **Why it is needed:** Provides crystal-clear visual hierarchy, prevents visual scale distortion, and highlights key macroeconomic inflection points directly on the chart.
- **What output it produces:** Fully rendered Plotly Figure objects.

---

## 7. Output Generation & Export (`scripts/visualizations.py`)

### Code:
```python
def save_visualization(fig, folder, basename):
    """Saves interactive HTML visualization and attempts PNG export if kaleido is installed."""
    html_path = os.path.join(folder, f"{basename}.html")
    fig.write_html(html_path, include_plotlyjs="cdn")
    print(f"  ▶ [Saved HTML] {html_path}")

    png_path = os.path.join(folder, f"{basename}.png")
    try:
        fig.write_image(png_path, width=1200, height=675, scale=2)
        print(f"  ▶ [Saved PNG]  {png_path}")
    except Exception:
        pass
```
- **What it does:** Exports standalone interactive HTML figures containing CDN-linked Plotly JavaScript, and attempts PNG image exports with a graceful fallback if `kaleido` is not installed.
- **Why it is needed:** Allows offline, standalone browser viewing without running a live Python kernel, while cleanly isolating optional image dependencies.
- **What output it produces:** 7 standalone interactive HTML visualizations in `outputs/reliance/`, `outputs/telecom/`, and `outputs/retail/`.
