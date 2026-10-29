"""
RELYNDIA — Phase 4 Core Visualization Engine
Course: BISL504 Data Visualization Lab
Project: RELYNDIA — Visualizing Reliance's Business and Market Footprint in India

This script loads the analysis-ready cleaned datasets from clean_data/, runs strict
data integrity validation assertions, applies unified academic styling, descriptive
subtitles, factual macroeconomic annotations, and exports the 7 core Plotly figures.
"""

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Dynamic Base Directory Resolution
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEAN_DIR = os.path.join(BASE_DIR, "clean_data")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# Output Subdirectories
RELIANCE_OUT = os.path.join(OUTPUTS_DIR, "reliance")
TELECOM_OUT = os.path.join(OUTPUTS_DIR, "telecom")
RETAIL_OUT = os.path.join(OUTPUTS_DIR, "retail")

for d in [RELIANCE_OUT, TELECOM_OUT, RETAIL_OUT]:
    os.makedirs(d, exist_ok=True)

# Standardized Chronological Financial Year Timeline
EXPECTED_YEARS = ["FY2017", "FY2018", "FY2019", "FY2020", "FY2021", "FY2022", "FY2023", "FY2024"]

# Standardized Brand & Category Color Palettes
COLOR_MAP_RIL = {
    "Oil-to-Chemicals (O2C)": "#FD7E14",             # Industrial Amber
    "Reliance Retail": "#DC3545",                    # Retail Crimson Red
    "Digital Services (Jio)": "#0A58CA",             # Jio Tech Blue
    "Financial Services & Others": "#6C757D"         # Neutral Corporate Gray
}

COLOR_MAP_TEL = {
    "Reliance Jio": "#0A58CA",                       # Jio Blue
    "Bharti Airtel": "#E02B20",                      # Airtel Red
    "Vodafone Idea (Vi)": "#FFC107",                 # Vi Yellow/Amber
    "BSNL / MTNL": "#198754"                         # BSNL Green
}

# Unified Academic Typography & Layout Settings
LAYOUT_DEFAULTS = dict(
    template="plotly_white",
    font=dict(family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif", size=12, color="#212529"),
    title_font=dict(size=14, color="#212529"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=11)),
    margin=dict(l=65, r=65, t=85, b=55),
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF"
)

# Common Categorical X-Axis Settings
COMMON_XAXIS = dict(
    title="Financial Year",
    type="category",
    categoryorder="array",
    categoryarray=EXPECTED_YEARS,
    showgrid=True,
    gridcolor="#F1F3F5",
    linecolor="#CED4DA"
)

def save_visualization(fig, folder, basename):
    """
    Saves interactive HTML visualization with CDN Plotly engine,
    and attempts static PNG export if kaleido is installed.
    """
    html_path = os.path.join(folder, f"{basename}.html")
    fig.write_html(html_path, include_plotlyjs="cdn")
    print(f"  ▶ [Saved HTML] {html_path}")

    png_path = os.path.join(folder, f"{basename}.png")
    try:
        fig.write_image(png_path, width=1200, height=675, scale=2)
        print(f"  ▶ [Saved PNG]  {png_path}")
    except Exception:
        # Graceful fallback: Kaleido is not installed in the environment
        pass

print("=" * 80)
print("RELYNDIA (PHASE 4) — CORE VISUALIZATION ENGINE & REFINEMENT")
print("=" * 80)


# =============================================================================
# QUESTION 1: RELIANCE BUSINESS DIVERSIFICATION
# =============================================================================
print("\n[QUESTION 1] Refining Reliance Diversification Visualizations...")
df_ril_long = pd.read_csv(os.path.join(CLEAN_DIR, "clean_ril_segments_long.csv"))
df_ril_wide = pd.read_csv(os.path.join(CLEAN_DIR, "clean_ril_financial_segment_growth.csv"))

# Validation Assertions
assert df_ril_wide["Financial_Year"].tolist() == EXPECTED_YEARS, "RIL Financial Year sequence mismatch"
assert df_ril_wide["Financial_Year"].is_unique, "Duplicate financial years in RIL dataset"
assert not df_ril_wide["Gross_Revenue_Cr"].isna().any(), "NaN found in RIL Gross Revenue"
assert not df_ril_wide["Retail_Revenue_Cr"].isna().any(), "NaN found in RIL Retail Revenue"
assert not df_ril_wide["O2C_Revenue_Cr"].isna().any(), "NaN found in RIL O2C Revenue"

# Q1-A: Line Chart — Segment Revenue Growth Trajectory
fig_q1_line = px.line(
    df_ril_long,
    x="Financial_Year",
    y="Revenue_Cr",
    color="Segment",
    color_discrete_map=COLOR_MAP_RIL,
    markers=True,
    title="<b>Reliance Industries — Segment Gross Revenue Trajectories (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Annual gross segment revenues in ₹ Crore; Source: RIL Integrated Annual Reports</span>",
    labels={"Financial_Year": "Financial Year", "Revenue_Cr": "Gross Revenue (₹ Crore)", "Segment": "Business Segment"}
)
fig_q1_line.update_traces(
    line=dict(width=3),
    marker=dict(size=8),
    hovertemplate="<b>%{x}</b><br>Segment: %{fullData.name}<br>Gross Revenue: ₹%{y:,.0f} Cr<extra></extra>"
)
fig_q1_line.update_layout(
    **LAYOUT_DEFAULTS,
    hovermode="x unified",
    xaxis=COMMON_XAXIS,
    yaxis=dict(title="Gross Revenue (₹ Crore)", tickprefix="₹", tickformat=",.0f", rangemode="tozero", showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
)
# Factual Macroeconomic Annotation: FY21 Pandemic Impact
fig_q1_line.add_annotation(
    x="FY2021",
    y=278940,
    text="<b>FY21 COVID-19 Slump</b><br>O2C crude/fuel demand drop (-25.7%)<br>offset by Digital Services resilience",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=1.5,
    arrowcolor="#FD7E14",
    ax=-65,
    ay=-50,
    font=dict(size=10, color="#495057"),
    bgcolor="#FFFFFF",
    bordercolor="#FD7E14",
    borderwidth=1,
    borderpad=4,
    opacity=0.95
)
save_visualization(fig_q1_line, RELIANCE_OUT, "q1_segment_revenue_trend")

# Q1-B: Grouped Bar Chart — Annual Segment Comparison
fig_q1_bar = px.bar(
    df_ril_long,
    x="Financial_Year",
    y="Revenue_Cr",
    color="Segment",
    barmode="group",
    color_discrete_map=COLOR_MAP_RIL,
    title="<b>Reliance Industries — Annual Segment Revenue Comparison (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Side-by-side annual scale across core operating divisions (₹ Crore); Source: RIL Integrated Annual Reports</span>",
    labels={"Financial_Year": "Financial Year", "Revenue_Cr": "Gross Revenue (₹ Crore)", "Segment": "Business Segment"}
)
fig_q1_bar.update_traces(
    hovertemplate="<b>%{x}</b><br>Segment: %{fullData.name}<br>Revenue: ₹%{y:,.0f} Cr<extra></extra>"
)
fig_q1_bar.update_layout(
    **LAYOUT_DEFAULTS,
    xaxis=COMMON_XAXIS,
    yaxis=dict(title="Gross Revenue (₹ Crore)", tickprefix="₹", tickformat=",.0f", rangemode="tozero", showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
)
save_visualization(fig_q1_bar, RELIANCE_OUT, "q1_segment_comparison_grouped_bar")

# Q1-C: 100% Stacked Area Chart — Business Mix Transformation & Revenue Composition
fig_q1_stack = px.area(
    df_ril_long,
    x="Financial_Year",
    y="Share_Pct",
    color="Segment",
    color_discrete_map=COLOR_MAP_RIL,
    groupnorm="percent",
    title="<b>Reliance Industries — Business Mix Transformation & Revenue Composition (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Normalized segment share of consolidated gross revenue (%); Source: RIL Integrated Annual Reports</span>",
    labels={"Financial_Year": "Financial Year", "Share_Pct": "Share of Gross Revenue (%)", "Segment": "Business Segment"}
)
fig_q1_stack.update_traces(
    hovertemplate="<b>%{x}</b><br>Segment: %{fullData.name}<br>Revenue Contribution: %{y:.1f}%<extra></extra>"
)
fig_q1_stack.update_layout(
    **LAYOUT_DEFAULTS,
    hovermode="x unified",
    xaxis=COMMON_XAXIS,
    yaxis=dict(title="Share of Gross Revenue (%)", ticksuffix="%", range=[0, 100], showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
)
save_visualization(fig_q1_stack, RELIANCE_OUT, "q1_business_composition_100pct_stacked")


# =============================================================================
# QUESTION 2: JIO & TELECOM MARKET DYNAMICS
# =============================================================================
print("\n[QUESTION 2] Refining Telecom Market Visualizations...")
df_tel_long = pd.read_csv(os.path.join(CLEAN_DIR, "clean_telecom_subscribers_long.csv"))
df_tel_clean = pd.read_csv(os.path.join(CLEAN_DIR, "clean_telecom_market_subscribers.csv"))

# Validation Assertions
assert df_tel_clean["Financial_Year"].tolist() == EXPECTED_YEARS, "Telecom Financial Year sequence mismatch"
assert df_tel_clean["Financial_Year"].is_unique, "Duplicate financial years in Telecom dataset"
assert not df_tel_clean["Total_Wireless_Subs_M"].isna().any(), "NaN found in Total Wireless Subscribers"
assert not df_tel_clean["Jio_Subs_M"].isna().any(), "NaN found in Jio Subscribers"

# Q2-A: Multi-Line Chart — Wireless Subscriber Base Trends (Strict Non-Causal Framing)
fig_q2_line = px.line(
    df_tel_long,
    x="Financial_Year",
    y="Subscribers_M",
    color="Operator",
    color_discrete_map=COLOR_MAP_TEL,
    markers=True,
    title="<b>Indian Telecom Market — Wireless Subscriber Trajectories (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Total wireless subscribers in Millions as of March 31; Source: TRAI Performance Indicator Reports</span>",
    labels={"Financial_Year": "Financial Year", "Subscribers_M": "Subscribers (Millions)", "Operator": "Telecom Operator"}
)
fig_q2_line.update_traces(
    line=dict(width=3),
    marker=dict(size=8),
    hovertemplate="<b>%{x}</b><br>Operator: %{fullData.name}<br>Subscribers: %{y:.2f} Million<extra></extra>"
)
fig_q2_line.update_layout(
    **LAYOUT_DEFAULTS,
    hovermode="x unified",
    xaxis=COMMON_XAXIS,
    yaxis=dict(title="Wireless Subscribers (Millions)", ticksuffix=" M", rangemode="tozero", showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
)
# Factual Structural Annotation: Vodafone Idea Merger Peak
fig_q2_line.add_annotation(
    x="FY2018",
    y=408.06,
    text="<b>Vodafone-Idea Merger Peak</b><br>Consolidated 408.1M subscriber base;<br>subsequent multi-year contraction",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=1.5,
    arrowcolor="#D39E00",
    ax=65,
    ay=-45,
    font=dict(size=10, color="#495057"),
    bgcolor="#FFFFFF",
    bordercolor="#D39E00",
    borderwidth=1,
    borderpad=4,
    opacity=0.95
)
save_visualization(fig_q2_line, TELECOM_OUT, "q2_telecom_subscribers_multiline")

# Q2-B: 100% Stacked Area Chart — Market Share Evolution
fig_q2_share = px.area(
    df_tel_long,
    x="Financial_Year",
    y="Market_Share_Pct",
    color="Operator",
    color_discrete_map=COLOR_MAP_TEL,
    groupnorm="percent",
    title="<b>Indian Telecom Industry — Operator Market Share Evolution (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Operator percentage share of total wireless subscriber base; Source: TRAI Performance Indicator Reports</span>",
    labels={"Financial_Year": "Financial Year", "Market_Share_Pct": "Market Share (%)", "Operator": "Telecom Operator"}
)
fig_q2_share.update_traces(
    hovertemplate="<b>%{x}</b><br>Operator: %{fullData.name}<br>Market Share: %{y:.2f}%<extra></extra>"
)
fig_q2_share.update_layout(
    **LAYOUT_DEFAULTS,
    hovermode="x unified",
    xaxis=COMMON_XAXIS,
    yaxis=dict(title="Market Share (%)", ticksuffix="%", range=[0, 100], showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
)
save_visualization(fig_q2_share, TELECOM_OUT, "q2_telecom_market_share_stacked_area")


# =============================================================================
# QUESTION 3: RELIANCE RETAIL EXPANSION & CONSUMER REACH
# =============================================================================
print("\n[QUESTION 3] Refining Reliance Retail Visualizations...")
df_ret_clean = pd.read_csv(os.path.join(CLEAN_DIR, "clean_reliance_retail_footprint.csv"))

# Strict Pre-Plotting Assertions: Retail Alignment & Data Integrity
assert df_ret_clean["Financial_Year"].tolist() == EXPECTED_YEARS, f"Financial Year sequence mismatch: {df_ret_clean['Financial_Year'].tolist()}"
assert df_ret_clean["Financial_Year"].is_unique, "Duplicate financial years found in retail dataset"
assert len(df_ret_clean["Retail_Revenue_Cr"]) == len(df_ret_clean["Operating_Store_Count"]) == 8, "Length mismatch across retail series"
assert not df_ret_clean["Retail_Revenue_Cr"].isna().any(), "NaN found in Retail Revenue"
assert not df_ret_clean["Operating_Store_Count"].isna().any(), "NaN found in Operating Store Count"

# Q3-A: Dual-Axis Chart — Revenue (Bars) vs Operating Store Count (Line)
# Proper zero-aligned baselines, distinct bar width, clear legend & non-clashing line styling
fig_q3_dual = make_subplots(specs=[[{"secondary_y": True}]])

# Primary Y-axis: Retail Gross Revenue Bar (Sleek width with soft opacity)
fig_q3_dual.add_trace(
    go.Bar(
        x=df_ret_clean["Financial_Year"],
        y=df_ret_clean["Retail_Revenue_Cr"],
        name="Retail Gross Revenue (₹ Cr)",
        marker=dict(
            color="#DC3545",
            opacity=0.75,
            line=dict(color="#B02A37", width=1.5)
        ),
        width=0.45,
        hovertemplate="<b>%{x}</b><br>Retail Revenue: ₹%{y:,.0f} Cr<extra></extra>"
    ),
    secondary_y=False
)

# Secondary Y-axis: Operating Store Count Line (Zero-aligned baseline, high-contrast diamond markers)
fig_q3_dual.add_trace(
    go.Scatter(
        x=df_ret_clean["Financial_Year"],
        y=df_ret_clean["Operating_Store_Count"],
        name="Operating Store Count",
        mode="lines+markers",
        line=dict(color="#0A58CA", width=3.5),
        marker=dict(size=9, symbol="diamond", color="#0A58CA", line=dict(color="#FFFFFF", width=1.5)),
        hovertemplate="<b>%{x}</b><br>Store Count: %{y:,} stores<extra></extra>"
    ),
    secondary_y=True
)

fig_q3_dual.update_layout(
    **LAYOUT_DEFAULTS,
    title_text="<b>Reliance Retail — Revenue Growth vs Physical Store Expansion (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Gross Revenue (₹ Cr, Left) vs Operating Store Count (Right); Source: Reliance Retail Filings</span>",
    hovermode="x unified",
    bargap=0.3,
    xaxis=COMMON_XAXIS
)
fig_q3_dual.update_yaxes(
    title_text="Gross Revenue (₹ Crore)",
    tickprefix="₹",
    tickformat=",.0f",
    rangemode="tozero",
    range=[0, 360000],
    showgrid=True,
    gridcolor="#F1F3F5",
    linecolor="#CED4DA",
    secondary_y=False
)
fig_q3_dual.update_yaxes(
    title_text="Operating Stores Count",
    tickformat=",.0f",
    rangemode="tozero",
    range=[0, 22000],
    secondary_y=True,
    showgrid=False,
    linecolor="#CED4DA"
)
# Factual Macroeconomic Annotation: COVID-19 Retail Disruption
fig_q3_dual.add_annotation(
    x="FY2021",
    y=157629,
    text="<b>FY21 Pandemic Lockdowns</b><br>Temporary retail store closures<br>paused revenue growth (-3.3%)",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=1.5,
    arrowcolor="#DC3545",
    ax=55,
    ay=-55,
    font=dict(size=10, color="#495057"),
    bgcolor="#FFFFFF",
    bordercolor="#DC3545",
    borderwidth=1,
    borderpad=4,
    opacity=0.95,
    secondary_y=False
)
save_visualization(fig_q3_dual, RETAIL_OUT, "q3_retail_revenue_vs_stores_dual_axis")

# Q3-B: Dual-Axis Line Chart — Registered Customer Base & Floor Area Scaling
fig_q3_cust = make_subplots(specs=[[{"secondary_y": True}]])

fig_q3_cust.add_trace(
    go.Scatter(
        x=df_ret_clean["Financial_Year"],
        y=df_ret_clean["Registered_Customers_M"],
        name="Registered Customers (M)",
        mode="lines+markers",
        line=dict(color="#6F42C1", width=3.5),
        marker=dict(size=9, color="#6F42C1", line=dict(color="#FFFFFF", width=1.5)),
        hovertemplate="<b>%{x}</b><br>Registered Customers: %{y:.1f} Million<extra></extra>"
    ),
    secondary_y=False
)

fig_q3_cust.add_trace(
    go.Scatter(
        x=df_ret_clean["Financial_Year"],
        y=df_ret_clean["Retail_Floor_Area_M_SqFt"],
        name="Retail Floor Area (M Sq Ft)",
        mode="lines+markers",
        line=dict(color="#FD7E14", width=3, dash="dash"),
        marker=dict(size=8, symbol="square", color="#FD7E14", line=dict(color="#FFFFFF", width=1)),
        hovertemplate="<b>%{x}</b><br>Floor Area: %{y:.1f} Million sq ft<extra></extra>"
    ),
    secondary_y=True
)

fig_q3_cust.update_layout(
    **LAYOUT_DEFAULTS,
    title_text="<b>Reliance Retail — Customer Base Scaling & Operational Floor Area (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Registered Customers (Millions, Left) vs Retail Floor Area (Million Sq Ft, Right); Source: Reliance Retail Filings</span>",
    hovermode="x unified",
    xaxis=COMMON_XAXIS
)
fig_q3_cust.update_yaxes(
    title_text="Registered Customers (Millions)",
    ticksuffix=" M",
    rangemode="tozero",
    range=[0, 350],
    showgrid=True,
    gridcolor="#F1F3F5",
    linecolor="#CED4DA",
    secondary_y=False
)
fig_q3_cust.update_yaxes(
    title_text="Floor Area (Million Sq Ft)",
    ticksuffix=" M sq ft",
    rangemode="tozero",
    range=[0, 95],
    secondary_y=True,
    showgrid=False,
    linecolor="#CED4DA"
)
save_visualization(fig_q3_cust, RETAIL_OUT, "q3_retail_customers_and_area_trend")

print("\n" + "=" * 80)
print("PHASE 4 COMPLETE: REFINED VISUALIZATIONS & ANNOTATIONS EXPORTED")
print("=" * 80)
