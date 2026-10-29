"""
RELYNDIA — Visualizing Reliance's Business and Market Footprint in India
Course: BISL504 Data Visualization Lab
Interactive Streamlit Web Application
"""

import os
import streamlit as st
import pandas as pd
import numpy as np

# Import Modular Application Components
from components.metrics import (
    render_overview_kpis,
    render_q1_section_kpis,
    render_q2_section_kpis,
    render_q3_section_kpis,
    calculate_cagr
)
from components.charts import (
    EXPECTED_YEARS,
    COLOR_MAP_RIL,
    COLOR_MAP_TEL,
    create_q1_revenue_trend,
    create_q1_grouped_bar,
    create_q1_composition_stacked,
    create_q2_subscribers_trend,
    create_q2_market_share_stacked,
    create_q3_revenue_vs_stores_dual,
    create_q3_customers_vs_area_dual
)
from components.explanations import (
    render_explanation_q1_1,
    render_explanation_q1_2,
    render_explanation_q1_3,
    render_explanation_q2_1,
    render_explanation_q2_2,
    render_explanation_q3_1,
    render_explanation_q3_2
)

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="RELYNDIA — Reliance Business & Market Footprint",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Corporate CSS Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0A58CA;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #495057;
        margin-bottom: 1.5rem;
    }
    .badge-course {
        background-color: #E7F1FF;
        color: #0A58CA;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
    .insight-card {
        background-color: #F8F9FA;
        border-left: 4px solid #0A58CA;
        padding: 14px 18px;
        border-radius: 4px;
        margin: 12px 0 16px 0;
        font-size: 0.95rem;
        color: #212529;
    }
    .footer-text {
        text-align: center;
        color: #6C757D;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #DEE2E6;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA LOADING & CACHING
# -----------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLEAN_DIR = os.path.join(BASE_DIR, "clean_data")

@st.cache_data
def load_all_datasets():
    df_ril_wide = pd.read_csv(os.path.join(CLEAN_DIR, "clean_ril_financial_segment_growth.csv"))
    df_ril_long = pd.read_csv(os.path.join(CLEAN_DIR, "clean_ril_segments_long.csv"))
    df_tel_wide = pd.read_csv(os.path.join(CLEAN_DIR, "clean_telecom_market_subscribers.csv"))
    df_tel_long = pd.read_csv(os.path.join(CLEAN_DIR, "clean_telecom_subscribers_long.csv"))
    df_ret_wide = pd.read_csv(os.path.join(CLEAN_DIR, "clean_reliance_retail_footprint.csv"))
    df_econ = pd.read_csv(os.path.join(DATA_DIR, "verified_indian_economic_indicators.csv"))
    df_meta = pd.read_csv(os.path.join(DATA_DIR, "data_sources_and_verification.csv"))
    return df_ril_wide, df_ril_long, df_tel_wide, df_tel_long, df_ret_wide, df_econ, df_meta

try:
    df_ril_wide, df_ril_long, df_tel_wide, df_tel_long, df_ret_wide, df_econ, df_meta = load_all_datasets()
except Exception as e:
    st.error(f"Error loading verified datasets: {e}")
    st.stop()

# -----------------------------------------------------------------------------
# 3. SIDEBAR NAVIGATION & INTERACTIVE FILTERS
# -----------------------------------------------------------------------------
st.sidebar.markdown("## 🧭 RELYNDIA Navigation")
section = st.sidebar.radio(
    "Select Section:",
    [
        "🏠 Executive Overview",
        "🔄 Business Diversification (Q1)",
        "📶 Jio & Telecom Dynamics (Q2)",
        "🛍️ Reliance Retail Reach (Q3)",
        "📚 Data Sources & Methodology"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Global Interactive Controls")

# Helper: Safe Timeline Range Resolution
def resolve_active_years(selected_years, expected_years=EXPECTED_YEARS):
    """
    Safely resolves, validates, and normalizes selected timeline years from the slider.
    Guarantees a valid, non-empty, chronologically ordered sublist of expected_years.
    Handles single values, tuples, strings, ints, reversed ranges, and missing years.
    """
    if not expected_years:
        return []

    def _normalize(val):
        if val is None:
            return None
        if isinstance(val, (int, float)):
            return f"FY{int(val)}"
        s = str(val).strip()
        if s.startswith("FY") and len(s) == 6 and s[2:].isdigit():
            return s
        if s.isdigit() and len(s) == 4:
            return f"FY{s}"
        if s.upper().startswith("FY"):
            rest = s[2:].strip()
            if rest.isdigit():
                if len(rest) == 2:
                    return f"FY20{rest}"
                elif len(rest) == 4:
                    return f"FY{rest}"
        return s

    if selected_years is None:
        raw_start, raw_end = expected_years[0], expected_years[-1]
    elif isinstance(selected_years, (str, int, float)):
        raw_start = raw_end = selected_years
    elif isinstance(selected_years, (list, tuple)):
        if len(selected_years) == 0:
            raw_start, raw_end = expected_years[0], expected_years[-1]
        elif len(selected_years) == 1:
            raw_start = raw_end = selected_years[0]
        else:
            raw_start, raw_end = selected_years[0], selected_years[1]
    else:
        raw_start, raw_end = expected_years[0], expected_years[-1]

    norm_start = _normalize(raw_start)
    norm_end = _normalize(raw_end)

    start_val = norm_start if norm_start in expected_years else expected_years[0]
    end_val = norm_end if norm_end in expected_years else expected_years[-1]

    start_idx = expected_years.index(start_val)
    end_idx = expected_years.index(end_val)

    if start_idx > end_idx:
        start_idx, end_idx = end_idx, start_idx

    active = expected_years[start_idx : end_idx + 1]
    return active if active else list(expected_years)

def prepare_metadata_display(df):
    """
    Normalizes metadata schema and constructs a display-ready DataFrame.
    Maps semantically equivalent columns from data_sources_and_verification.csv:
      - 'Source Organization' -> 'Source Name'
      - 'Source URL' / 'Source Document' -> 'Primary URL / Filings Reference'
      - 'Year' -> 'Data Span'
    Gracefully supplies a clear fallback for absent fields (e.g., 'Source Type').
    """
    if df is None or df.empty:
        return pd.DataFrame(columns=[
            "Dataset", "Source Name", "Source Type", "Data Span", "Verification Status", "Primary URL / Filings Reference"
        ])

    df_clean = df.copy()
    # Normalize accidental leading/trailing whitespace in column headers
    df_clean.columns = [str(col).strip() for col in df_clean.columns]

    expected_cols = ["Dataset", "Source Name", "Source Type", "Data Span", "Verification Status", "Primary URL / Filings Reference"]
    if all(col in df_clean.columns for col in expected_cols):
        return df_clean[expected_cols]

    records = []
    if "Dataset" in df_clean.columns:
        for dataset_name, group in df_clean.groupby("Dataset", sort=False):
            # 1. Source Name (mapped from 'Source Organization')
            if "Source Name" in group.columns and not group["Source Name"].dropna().empty:
                source_name = str(group["Source Name"].dropna().iloc[0])
            elif "Source Organization" in group.columns and not group["Source Organization"].dropna().empty:
                source_name = str(group["Source Organization"].dropna().iloc[0])
            else:
                source_name = "Not provided in source metadata"

            # 2. Source Type (absent in source schema, provide clear fallback)
            if "Source Type" in group.columns and not group["Source Type"].dropna().empty:
                source_type = str(group["Source Type"].dropna().iloc[0])
            else:
                source_type = "Not provided in source metadata"

            # 3. Data Span (derived from 'Year' range or column)
            if "Data Span" in group.columns and not group["Data Span"].dropna().empty:
                data_span = str(group["Data Span"].dropna().iloc[0])
            elif "Year" in group.columns:
                years = sorted([str(y).strip() for y in group["Year"].dropna().unique() if str(y).strip()])
                data_span = f"{years[0]}–{years[-1]}" if len(years) > 1 else (years[0] if years else "Not provided in source metadata")
            else:
                data_span = "Not provided in source metadata"

            # 4. Verification Status (direct mapping)
            if "Verification Status" in group.columns and not group["Verification Status"].dropna().empty:
                statuses = [str(s).strip() for s in group["Verification Status"].dropna().unique() if str(s).strip()]
                verif_status = ", ".join(statuses)
            else:
                verif_status = "Not provided in source metadata"

            # 5. Primary URL / Filings Reference (mapped from 'Source URL' or 'Source Document')
            if "Primary URL / Filings Reference" in group.columns and not group["Primary URL / Filings Reference"].dropna().empty:
                primary_url = str(group["Primary URL / Filings Reference"].dropna().iloc[0])
            elif "Source URL" in group.columns and not group["Source URL"].dropna().empty:
                primary_url = str(group["Source URL"].dropna().iloc[0])
            elif "Source Document" in group.columns and not group["Source Document"].dropna().empty:
                primary_url = str(group["Source Document"].dropna().iloc[0])
            else:
                primary_url = "Not provided in source metadata"

            records.append({
                "Dataset": dataset_name,
                "Source Name": source_name,
                "Source Type": source_type,
                "Data Span": data_span,
                "Verification Status": verif_status,
                "Primary URL / Filings Reference": primary_url
            })
        return pd.DataFrame(records)

    return pd.DataFrame(records)

# Session State Initialization
default_range = (EXPECTED_YEARS[0], EXPECTED_YEARS[-1])
if "saved_segments" not in st.session_state:
    st.session_state["saved_segments"] = list(COLOR_MAP_RIL.keys())
if "saved_operators" not in st.session_state:
    st.session_state["saved_operators"] = list(COLOR_MAP_TEL.keys())

# Sanitize timeline_range if already in session_state to guarantee valid 2-element range
if "timeline_range" in st.session_state:
    val = st.session_state["timeline_range"]
    if not (isinstance(val, (tuple, list)) and len(val) == 2 and val[0] in EXPECTED_YEARS and val[1] in EXPECTED_YEARS):
        st.session_state.pop("timeline_range", None)

def reset_all_filters():
    st.session_state.pop("timeline_range", None)
    st.session_state["saved_segments"] = list(COLOR_MAP_RIL.keys())
    st.session_state["saved_operators"] = list(COLOR_MAP_TEL.keys())
    st.session_state.pop("selected_segments", None)
    st.session_state.pop("selected_operators", None)

# Reset Button
if st.sidebar.button("🔄 Reset All Filters", use_container_width=True, on_click=reset_all_filters):
    st.sidebar.success("All filters reset to defaults.")

# Financial Year Range Selector
# Always supply value=default_range to ensure Streamlit configures a two-handled range slider
selected_years_tuple = st.sidebar.select_slider(
    "Timeline Range:",
    options=EXPECTED_YEARS,
    value=default_range,
    key="timeline_range"
)
active_years = resolve_active_years(selected_years_tuple, EXPECTED_YEARS)
start_idx = EXPECTED_YEARS.index(active_years[0])
end_idx = EXPECTED_YEARS.index(active_years[-1])

# Dynamic Section-Specific Filters with Cross-Section State Persistence
def _sync_segments():
    st.session_state["saved_segments"] = st.session_state["selected_segments"]

def _sync_operators():
    st.session_state["saved_operators"] = st.session_state["selected_operators"]

active_segments = st.session_state["saved_segments"]
active_operators = st.session_state["saved_operators"]

if section == "🔄 Business Diversification (Q1)":
    st.sidebar.markdown("#### 🎯 Filter Business Segments:")
    active_segments = st.sidebar.multiselect(
        "Operating Segments:",
        options=list(COLOR_MAP_RIL.keys()),
        default=st.session_state["saved_segments"],
        key="selected_segments",
        on_change=_sync_segments
    )

elif section == "📶 Jio & Telecom Dynamics (Q2)":
    st.sidebar.markdown("#### 🎯 Filter Telecom Operators:")
    active_operators = st.sidebar.multiselect(
        "Operators:",
        options=list(COLOR_MAP_TEL.keys()),
        default=st.session_state["saved_operators"],
        key="selected_operators",
        on_change=_sync_operators
    )

st.sidebar.markdown("---")
st.sidebar.info("""
**Academic Compliance Notice:**  
All metrics are verified from official corporate filings (RIL, Reliance Retail) and regulatory releases (TRAI, RBI DBIE). Observational time-series proves coexistence, not causal determination.
""")

# -----------------------------------------------------------------------------
# 4. SECTION ROUTING & PRESENTATION
# -----------------------------------------------------------------------------

# =============================================================================
# SECTION A: EXECUTIVE OVERVIEW
# =============================================================================
if section == "🏠 Executive Overview":
    st.markdown("<span class='badge-course'>BISL504 Data Visualization Lab | Final Web Application</span>", unsafe_allow_html=True)
    st.markdown("<div class='main-title'>RELYNDIA: Visualizing Reliance's Business & Market Footprint</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>An interactive macroeconomic and corporate visualization platform examining Reliance Industries Limited's (RIL) structural transformation across Energy, Telecom, and Retail (FY2017–FY2024).</div>", unsafe_allow_html=True)

    # Headline KPI Cards
    render_overview_kpis(df_ril_wide, df_tel_wide, df_ret_wide)
    st.markdown("<br>", unsafe_allow_html=True)

    # Narrative Introduction
    st.markdown("### 🎯 Research Objectives & Guiding Questions")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        #### 1. Business Diversification
        **Guiding Question 1:**  
        *How has Reliance diversified across its major business segments over time?*  
        Tracks the strategic rebalancing from traditional refining and petrochemicals (**O2C**) to consumer-facing **Retail** and **Digital Services (Jio)**.
        """)

    with col2:
        st.markdown("""
        #### 2. Jio & Telecom Market
        **Guiding Question 2:**  
        *How did the growth of Jio coincide with changes in India's telecom market?*  
        Analyzes wireless subscriber migration and industry market share consolidation across **Jio**, **Airtel**, **Vodafone Idea**, and **BSNL**.
        """)

    with col3:
        st.markdown("""
        #### 3. Reliance Retail Scaling
        **Guiding Question 3:**  
        *How has Reliance expanded its retail footprint and consumer reach over time?*  
        Explores physical store rollout, operational floor space expansion, customer base acquisition, and sales productivity.
        """)

    st.markdown("---")
    st.markdown("### 🇮🇳 Verified Indian Macroeconomic Indicators (Contextual Baseline)")
    st.dataframe(
        df_econ.rename(columns={
            "India Nominal GDP (₹ Lakh Cr)": "Nominal GDP (₹ Lakh Cr)",
            "India Real GDP Growth (%)": "Real GDP Growth (%)",
            "Private Sector Capex (₹ Lakh Cr)": "Private Capex (₹ Lakh Cr)",
            "Telecom Sector GVA (₹ Cr)": "Telecom GVA (₹ Cr)"
        }),
        use_container_width=True
    )
    st.caption("Source: Reserve Bank of India (RBI DBIE) & Ministry of Statistics and Programme Implementation (MoSPI)")


# =============================================================================
# SECTION B: BUSINESS DIVERSIFICATION (Q1)
# =============================================================================
elif section == "🔄 Business Diversification (Q1)":
    st.markdown("## 🔄 Guiding Question 1: Reliance Business Diversification")
    st.markdown("*How has Reliance diversified across its major business segments over time?*")
    st.markdown("This section analyzes how RIL transformed from an energy-heavy refining conglomerate into a multi-pillar consumer-tech conglomerate between FY2017 and FY2024.")

    # Dynamic Section KPIs
    render_q1_section_kpis(df_ril_wide, active_segments, active_years)
    st.markdown("<br>", unsafe_allow_html=True)

    if not active_segments:
        st.warning("⚠️ Please select at least one business segment in the sidebar.")
    else:
        # Chart 1.1: Multi-Line Trajectory
        st.markdown("### 1.1 Segment Gross Revenue Trajectories (FY2017–FY2024)")
        fig_q1_line = create_q1_revenue_trend(df_ril_long, active_segments, active_years)
        if fig_q1_line:
            st.plotly_chart(fig_q1_line, use_container_width=True, key="plotly_q1_revenue_trend")
            st.markdown("""
            <div class='insight-card'>
                <strong>Key Insight:</strong> Retail expanded at a 7-year CAGR of <strong>37.06%</strong> (₹33,765 Cr to ₹306,786 Cr) while Digital Services grew at a 6-year CAGR of <strong>36.79%</strong> from its first full operating year FY2018 (₹20,154 Cr to ₹132,045 Cr), significantly outpacing traditional O2C growth (12.89% CAGR).
            </div>
            """, unsafe_allow_html=True)
            render_explanation_q1_1()

        st.markdown("---")

        # Chart 1.2: Grouped Bar Comparison
        st.markdown("### 1.2 Annual Segment Revenue Comparison (Grouped Bar)")
        fig_q1_bar = create_q1_grouped_bar(df_ril_long, active_segments, active_years)
        if fig_q1_bar:
            st.plotly_chart(fig_q1_bar, use_container_width=True, key="plotly_q1_grouped_bar")
            st.markdown("""
            <div class='insight-card'>
                <strong>Key Insight:</strong> Side-by-side scale comparison shows the ratio between O2C and Retail revenue narrowing from <strong>7.16x</strong> in FY2017 to <strong>1.84x</strong> in FY2024, demonstrating structural corporate rebalancing.
            </div>
            """, unsafe_allow_html=True)
            render_explanation_q1_2()

        st.markdown("---")

        # Chart 1.3: 100% Stacked Area Composition
        st.markdown("### 1.3 Business Mix Transformation & Revenue Composition (100% Stacked Area)")
        fig_q1_stack = create_q1_composition_stacked(df_ril_long, active_segments, active_years)
        if fig_q1_stack:
            st.plotly_chart(fig_q1_stack, use_container_width=True, key="plotly_q1_composition_stacked")
            st.markdown("""
            <div class='insight-card'>
                <strong>Key Insight:</strong> Consumer-facing businesses (Retail + Jio) expanded from <strong>10.59%</strong> of gross revenue in FY2017 to <strong>43.88%</strong> in FY2024 (+3,329 basis points), while O2C contribution contracted from <strong>73.20%</strong> to <strong>56.47%</strong>.
            </div>
            """, unsafe_allow_html=True)
            render_explanation_q1_3()

        # Data Download Option
        q1_filtered = df_ril_long[df_ril_long["Segment"].isin(active_segments) & df_ril_long["Financial_Year"].isin(active_years)]
        st.download_button(
            label="📥 Download Displayed Q1 Segment Data (CSV)",
            data=q1_filtered.to_csv(index=False),
            file_name="relyndia_q1_segment_data.csv",
            mime="text/csv"
        )


# =============================================================================
# SECTION C: JIO & TELECOM MARKET (Q2)
# =============================================================================
elif section == "📶 Jio & Telecom Dynamics (Q2)":
    st.markdown("## 📶 Guiding Question 2: Jio & Indian Telecom Market Dynamics")
    st.markdown("*How did the growth of Jio coincide with changes in India's telecom market?*")
    st.markdown("This section examines multi-operator subscriber trajectories and market share dynamics based on official TRAI filings (FY2017–FY2024).")

    # Dynamic Section KPIs
    render_q2_section_kpis(df_tel_wide, active_operators, active_years)
    st.markdown("<br>", unsafe_allow_html=True)

    if not active_operators:
        st.warning("⚠️ Please select at least one telecom operator in the sidebar.")
    else:
        # Chart 2.1: Multi-Line Subscriber Trends
        st.markdown("### 2.1 Indian Telecom Wireless Subscriber Trajectories (FY2017–FY2024)")
        fig_q2_line = create_q2_subscribers_trend(df_tel_long, active_operators, active_years)
        if fig_q2_line:
            st.plotly_chart(fig_q2_line, use_container_width=True, key="plotly_q2_subscribers_trend")
            st.markdown("""
            <div class='insight-card'>
                <strong>Key Insight:</strong> Jio's wireless subscriber base expanded at a 7-year CAGR of <strong>23.26%</strong> (108.68M to 469.73M), while Airtel maintained steady growth (5.03% CAGR) and Vodafone Idea declined (-10.30% CAGR post-FY18 merger peak).
            </div>
            """, unsafe_allow_html=True)
            render_explanation_q2_1()

        st.markdown("---")

        # Chart 2.2: 100% Stacked Area Market Share
        st.markdown("### 2.2 Operator Market Share Evolution (100% Stacked Area)")
        fig_q2_share = create_q2_market_share_stacked(df_tel_long, active_operators, active_years)
        if fig_q2_share:
            st.plotly_chart(fig_q2_share, use_container_width=True, key="plotly_q2_market_share_stacked")
            st.markdown("""
            <div class='insight-card'>
                <strong>Key Insight:</strong> Jio's wireless market share increased from <strong>9.29%</strong> in FY2017 to <strong>40.31%</strong> in FY2024 (+3,102 bps), while combined 2-firm concentration (Jio + Airtel) reached <strong>73.42%</strong>.
            </div>
            """, unsafe_allow_html=True)
            render_explanation_q2_2()

        # Data Download Option
        q2_filtered = df_tel_long[df_tel_long["Operator"].isin(active_operators) & df_tel_long["Financial_Year"].isin(active_years)]
        st.download_button(
            label="📥 Download Displayed Q2 Telecom Data (CSV)",
            data=q2_filtered.to_csv(index=False),
            file_name="relyndia_q2_telecom_data.csv",
            mime="text/csv"
        )


# =============================================================================
# SECTION D: RELIANCE RETAIL EXPANSION (Q3)
# =============================================================================
elif section == "🛍️ Reliance Retail Reach (Q3)":
    st.markdown("## 🛍️ Guiding Question 3: Reliance Retail Expansion & Consumer Reach")
    st.markdown("*How has Reliance expanded its retail footprint and consumer reach over time?*")
    st.markdown("This section analyzes store network expansion, operational floor area, registered customer base, and top-line revenue growth (FY2017–FY2024).")

    # Dynamic Section KPIs
    render_q3_section_kpis(df_ret_wide, active_years)
    st.markdown("<br>", unsafe_allow_html=True)

    # Chart 3.1: Dual-Axis Revenue vs Store Expansion
    st.markdown("### 3.1 Retail Revenue Growth vs Physical Store Expansion (Dual-Axis)")
    fig_q3_dual = create_q3_revenue_vs_stores_dual(df_ret_wide, active_years)
    if fig_q3_dual:
        st.plotly_chart(fig_q3_dual, use_container_width=True, key="plotly_q3_revenue_vs_stores")
        st.markdown("""
        <div class='insight-card'>
            <strong>Key Insight:</strong> Store count grew <strong>5.21x</strong> (3,616 to 18,837 stores, 26.59% CAGR) while Revenue grew <strong>9.09x</strong> (₹33,765 Cr to ₹306,786 Cr, 37.06% CAGR), with revenue per store rising from <strong>₹9.34 Cr to ₹16.29 Cr/store</strong> (+74.42% productivity gain).
        </div>
        """, unsafe_allow_html=True)
        render_explanation_q3_1()

    st.markdown("---")

    # Chart 3.2: Dual-Axis Customer Base vs Floor Area
    st.markdown("### 3.2 Registered Customer Base & Operational Floor Space Scaling (Dual-Axis)")
    fig_q3_cust = create_q3_customers_vs_area_dual(df_ret_wide, active_years)
    if fig_q3_cust:
        st.plotly_chart(fig_q3_cust, use_container_width=True, key="plotly_q3_customers_vs_area")
        st.markdown("""
        <div class='insight-card'>
            <strong>Key Insight:</strong> Registered customer base grew <strong>8.69x</strong> (35.0M to 304.0M, 36.18% CAGR) while operational retail floor area expanded <strong>5.86x</strong> (13.5M to 79.1M sq ft, 28.73% CAGR).
        </div>
        """, unsafe_allow_html=True)
        render_explanation_q3_2()

    # Data Download Option
    q3_filtered = df_ret_wide[df_ret_wide["Financial_Year"].isin(active_years)]
    st.download_button(
        label="📥 Download Displayed Q3 Retail Footprint Data (CSV)",
        data=q3_filtered.to_csv(index=False),
        file_name="relyndia_q3_retail_data.csv",
        mime="text/csv"
    )


# =============================================================================
# SECTION E: DATA SOURCES & METHODOLOGY
# =============================================================================
elif section == "📚 Data Sources & Methodology":
    st.markdown("## 📚 Data Sources, Verification & Analytical Methodology")
    st.markdown("Complete technical audit trail and mathematical formulas supporting the RELYNDIA project.")

    st.markdown("### 1. Primary Verified Sources")
    df_meta_display = prepare_metadata_display(df_meta)
    st.dataframe(
        df_meta_display,
        column_config={
            "Primary URL / Filings Reference": st.column_config.LinkColumn(
                "Primary URL / Filings Reference",
                help="Click to open the verified official source repository"
            )
        },
        use_container_width=True
    )

    with st.expander("🔍 View Complete Itemized Audit Register (200 Data Points)"):
        st.markdown("Granular itemized verification records for every financial, operational, and macroeconomic data point:")
        st.dataframe(
            df_meta,
            column_config={
                "Source URL": st.column_config.LinkColumn("Source URL")
            },
            use_container_width=True
        )

    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.download_button(
            label="📥 Download Data Sources Metadata (CSV)",
            data=df_meta.to_csv(index=False),
            file_name="relyndia_data_sources_metadata.csv",
            mime="text/csv"
        )
    with col_d2:
        st.download_button(
            label="📥 Download Economic Indicators (CSV)",
            data=df_econ.to_csv(index=False),
            file_name="relyndia_indian_economic_indicators.csv",
            mime="text/csv"
        )

    st.markdown("---")
    st.markdown("### 2. Mathematical Formulas & Derived Metrics")
    st.markdown(r"""
    1. **Compound Annual Growth Rate (CAGR):**
       $$\text{CAGR} = \left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{n}} - 1$$
       Where $n$ is the number of elapsed annual periods ($n=7$ for FY2017–FY2024; $n=6$ for FY2018–FY2024).

    2. **Consumer Revenue Share (%):**
       $$\text{Consumer Share (\%)} = \frac{\text{Retail Revenue} + \text{Digital Services Revenue}}{\text{Consolidated Gross Turnover}} \times 100$$

    3. **Telecom Operator Market Share (%):**
       $$\text{Market Share (\%)} = \frac{\text{Operator Wireless Subscribers (M)}}{\text{Total Wireless Subscribers (M)}} \times 100$$

    4. **Retail Store Productivity (₹ Cr / Store):**
       $$\text{Revenue Throughput} = \frac{\text{Retail Gross Revenue (₹ Cr)}}{\text{Total Operating Store Count}}$$

    5. **Retail Sales Density (₹ / Sq Ft):**
       $$\text{Revenue Density} = \frac{\text{Retail Gross Revenue (₹ Cr)} \times 10^7}{\text{Retail Operational Floor Area (M sq ft)} \times 10^6}$$
    """)

    st.markdown("---")
    st.markdown("### 3. Data Integrity & Academic Limitations")
    st.markdown("""
    - **Single Source of Truth:** All data originates from verified primary filings (`data/*.csv`) and is cleaned into standardized schemas (`clean_data/*.csv`).
    - **Dual-Axis Zero Baseline Guarantee:** All dual-axis visualizations enforce `rangemode="tozero"` to eliminate visual scale distortion.
    - **Non-Causal Guardrail:** Observational time-series data proves concurrent growth and structural consolidation, not mathematical causation.
    - **Annual Fiscal Year-End Reporting:** Figures represent positions as of March 31 of each fiscal year. Intra-year or festive seasonality is not captured in annual totals.
    - **Historical Segment Harmonization:** Pre-FY2020 O2C figures combine previously separate refining and petrochemical lines to maintain comparability with RIL's unified reporting format introduced in FY2020.
    """)

# -----------------------------------------------------------------------------
# 5. FOOTER
# -----------------------------------------------------------------------------
st.markdown("<div class='footer-text'>RELYNDIA Web Application | BISL504 Data Visualization Lab | Developed with Streamlit & Plotly</div>", unsafe_allow_html=True)
