"""
RELYNDIA — Dynamic Plotly Visualizations Engine
Course: BISL504 Data Visualization Lab
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

def get_common_xaxis(categories):
    return dict(
        title="Financial Year",
        type="category",
        categoryorder="array",
        categoryarray=categories,
        showgrid=True,
        gridcolor="#F1F3F5",
        linecolor="#CED4DA"
    )

# -----------------------------------------------------------------------------
# QUESTION 1 CHARTS
# -----------------------------------------------------------------------------

def create_q1_revenue_trend(df_long, selected_segments, selected_years):
    filtered_df = df_long[
        df_long["Segment"].isin(selected_segments) &
        df_long["Financial_Year"].isin(selected_years)
    ]
    if filtered_df.empty:
        return None

    fig = px.line(
        filtered_df,
        x="Financial_Year",
        y="Revenue_Cr",
        color="Segment",
        color_discrete_map=COLOR_MAP_RIL,
        markers=True,
        title="<b>Reliance Industries — Segment Gross Revenue Trajectories (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Annual gross segment revenues in ₹ Crore; Source: RIL Integrated Annual Reports</span>",
        labels={"Financial_Year": "Financial Year", "Revenue_Cr": "Gross Revenue (₹ Crore)", "Segment": "Business Segment"}
    )
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8),
        hovertemplate="<b>%{x}</b><br>Segment: %{fullData.name}<br>Gross Revenue: ₹%{y:,.0f} Cr<extra></extra>"
    )
    fig.update_layout(
        **LAYOUT_DEFAULTS,
        hovermode="x unified",
        xaxis=get_common_xaxis(selected_years),
        yaxis=dict(title="Gross Revenue (₹ Crore)", tickprefix="₹", tickformat=",.0f", rangemode="tozero", showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
    )

    if "FY2021" in selected_years and "Oil-to-Chemicals (O2C)" in selected_segments:
        fig.add_annotation(
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
    return fig

def create_q1_grouped_bar(df_long, selected_segments, selected_years):
    filtered_df = df_long[
        df_long["Segment"].isin(selected_segments) &
        df_long["Financial_Year"].isin(selected_years)
    ]
    if filtered_df.empty:
        return None

    fig = px.bar(
        filtered_df,
        x="Financial_Year",
        y="Revenue_Cr",
        color="Segment",
        barmode="group",
        color_discrete_map=COLOR_MAP_RIL,
        title="<b>Reliance Industries — Annual Segment Revenue Comparison (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Side-by-side annual scale across core operating divisions (₹ Crore); Source: RIL Integrated Annual Reports</span>",
        labels={"Financial_Year": "Financial Year", "Revenue_Cr": "Gross Revenue (₹ Crore)", "Segment": "Business Segment"}
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Segment: %{fullData.name}<br>Revenue: ₹%{y:,.0f} Cr<extra></extra>"
    )
    fig.update_layout(
        **LAYOUT_DEFAULTS,
        xaxis=get_common_xaxis(selected_years),
        yaxis=dict(title="Gross Revenue (₹ Crore)", tickprefix="₹", tickformat=",.0f", rangemode="tozero", showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
    )
    return fig

def create_q1_composition_stacked(df_long, selected_segments, selected_years):
    filtered_df = df_long[
        df_long["Segment"].isin(selected_segments) &
        df_long["Financial_Year"].isin(selected_years)
    ]
    if filtered_df.empty:
        return None

    fig = px.area(
        filtered_df,
        x="Financial_Year",
        y="Share_Pct",
        color="Segment",
        color_discrete_map=COLOR_MAP_RIL,
        groupnorm="percent",
        title="<b>Reliance Industries — Business Mix Transformation & Revenue Composition (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Normalized segment share of consolidated gross revenue (%); Source: RIL Integrated Annual Reports</span>",
        labels={"Financial_Year": "Financial Year", "Share_Pct": "Share of Gross Revenue (%)", "Segment": "Business Segment"}
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Segment: %{fullData.name}<br>Revenue Contribution: %{y:.1f}%<extra></extra>"
    )
    fig.update_layout(
        **LAYOUT_DEFAULTS,
        hovermode="x unified",
        xaxis=get_common_xaxis(selected_years),
        yaxis=dict(title="Share of Gross Revenue (%)", ticksuffix="%", range=[0, 100], showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
    )
    return fig

# -----------------------------------------------------------------------------
# QUESTION 2 CHARTS
# -----------------------------------------------------------------------------

def create_q2_subscribers_trend(df_long, selected_operators, selected_years):
    filtered_df = df_long[
        df_long["Operator"].isin(selected_operators) &
        df_long["Financial_Year"].isin(selected_years)
    ]
    if filtered_df.empty:
        return None

    fig = px.line(
        filtered_df,
        x="Financial_Year",
        y="Subscribers_M",
        color="Operator",
        color_discrete_map=COLOR_MAP_TEL,
        markers=True,
        title="<b>Indian Telecom Market — Wireless Subscriber Trajectories (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Total wireless subscribers in Millions as of March 31; Source: TRAI Performance Indicator Reports</span>",
        labels={"Financial_Year": "Financial Year", "Subscribers_M": "Subscribers (Millions)", "Operator": "Telecom Operator"}
    )
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8),
        hovertemplate="<b>%{x}</b><br>Operator: %{fullData.name}<br>Subscribers: %{y:.2f} Million<extra></extra>"
    )
    fig.update_layout(
        **LAYOUT_DEFAULTS,
        hovermode="x unified",
        xaxis=get_common_xaxis(selected_years),
        yaxis=dict(title="Wireless Subscribers (Millions)", ticksuffix=" M", rangemode="tozero", showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
    )

    if "FY2018" in selected_years and "Vodafone Idea (Vi)" in selected_operators:
        fig.add_annotation(
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
    return fig

def create_q2_market_share_stacked(df_long, selected_operators, selected_years):
    filtered_df = df_long[
        df_long["Operator"].isin(selected_operators) &
        df_long["Financial_Year"].isin(selected_years)
    ]
    if filtered_df.empty:
        return None

    fig = px.area(
        filtered_df,
        x="Financial_Year",
        y="Market_Share_Pct",
        color="Operator",
        color_discrete_map=COLOR_MAP_TEL,
        groupnorm="percent",
        title="<b>Indian Telecom Industry — Operator Market Share Evolution (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Operator percentage share of total wireless subscriber base; Source: TRAI Performance Indicator Reports</span>",
        labels={"Financial_Year": "Financial Year", "Market_Share_Pct": "Market Share (%)", "Operator": "Telecom Operator"}
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Operator: %{fullData.name}<br>Market Share: %{y:.2f}%<extra></extra>"
    )
    fig.update_layout(
        **LAYOUT_DEFAULTS,
        hovermode="x unified",
        xaxis=get_common_xaxis(selected_years),
        yaxis=dict(title="Market Share (%)", ticksuffix="%", range=[0, 100], showgrid=True, gridcolor="#F1F3F5", linecolor="#CED4DA")
    )
    return fig

# -----------------------------------------------------------------------------
# QUESTION 3 CHARTS (DUAL-AXIS)
# -----------------------------------------------------------------------------

def create_q3_revenue_vs_stores_dual(df_ret, selected_years):
    filtered_df = df_ret[df_ret["Financial_Year"].isin(selected_years)]
    if filtered_df.empty:
        return None

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=filtered_df["Financial_Year"],
            y=filtered_df["Retail_Revenue_Cr"],
            name="Retail Gross Revenue (₹ Cr)",
            marker=dict(color="#DC3545", opacity=0.75, line=dict(color="#B02A37", width=1.5)),
            width=0.45,
            hovertemplate="<b>%{x}</b><br>Retail Revenue: ₹%{y:,.0f} Cr<extra></extra>"
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=filtered_df["Financial_Year"],
            y=filtered_df["Operating_Store_Count"],
            name="Operating Store Count",
            mode="lines+markers",
            line=dict(color="#0A58CA", width=3.5),
            marker=dict(size=9, symbol="diamond", color="#0A58CA", line=dict(color="#FFFFFF", width=1.5)),
            hovertemplate="<b>%{x}</b><br>Store Count: %{y:,} stores<extra></extra>"
        ),
        secondary_y=True
    )

    fig.update_layout(
        **LAYOUT_DEFAULTS,
        title_text="<b>Reliance Retail — Revenue Growth vs Physical Store Expansion (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Gross Revenue (₹ Cr, Left) vs Operating Store Count (Right); Source: Reliance Retail Filings</span>",
        hovermode="x unified",
        bargap=0.3,
        xaxis=get_common_xaxis(selected_years)
    )
    fig.update_yaxes(
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
    fig.update_yaxes(
        title_text="Operating Stores Count",
        tickformat=",.0f",
        rangemode="tozero",
        range=[0, 22000],
        secondary_y=True,
        showgrid=False,
        linecolor="#CED4DA"
    )

    if "FY2021" in selected_years:
        fig.add_annotation(
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
    return fig

def create_q3_customers_vs_area_dual(df_ret, selected_years):
    filtered_df = df_ret[df_ret["Financial_Year"].isin(selected_years)]
    if filtered_df.empty:
        return None

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=filtered_df["Financial_Year"],
            y=filtered_df["Registered_Customers_M"],
            name="Registered Customers (M)",
            mode="lines+markers",
            line=dict(color="#6F42C1", width=3.5),
            marker=dict(size=9, color="#6F42C1", line=dict(color="#FFFFFF", width=1.5)),
            hovertemplate="<b>%{x}</b><br>Registered Customers: %{y:.1f} Million<extra></extra>"
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=filtered_df["Financial_Year"],
            y=filtered_df["Retail_Floor_Area_M_SqFt"],
            name="Retail Floor Area (M Sq Ft)",
            mode="lines+markers",
            line=dict(color="#FD7E14", width=3, dash="dash"),
            marker=dict(size=8, symbol="square", color="#FD7E14", line=dict(color="#FFFFFF", width=1)),
            hovertemplate="<b>%{x}</b><br>Floor Area: %{y:.1f} Million sq ft<extra></extra>"
        ),
        secondary_y=True
    )

    fig.update_layout(
        **LAYOUT_DEFAULTS,
        title_text="<b>Reliance Retail — Customer Base Scaling & Operational Floor Area (FY2017–FY2024)</b><br><span style='font-size: 11px; color: #6C757D;'>Registered Customers (Millions, Left) vs Retail Floor Area (Million Sq Ft, Right); Source: Reliance Retail Filings</span>",
        hovermode="x unified",
        xaxis=get_common_xaxis(selected_years)
    )
    fig.update_yaxes(
        title_text="Registered Customers (Millions)",
        ticksuffix=" M",
        rangemode="tozero",
        range=[0, 350],
        showgrid=True,
        gridcolor="#F1F3F5",
        linecolor="#CED4DA",
        secondary_y=False
    )
    fig.update_yaxes(
        title_text="Floor Area (Million Sq Ft)",
        ticksuffix=" M sq ft",
        rangemode="tozero",
        range=[0, 95],
        secondary_y=True,
        showgrid=False,
        linecolor="#CED4DA"
    )
    return fig
