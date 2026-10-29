"""
RELYNDIA — KPI Metrics & Financial Ratios Engine
Course: BISL504 Data Visualization Lab
"""

import streamlit as st
import pandas as pd
import numpy as np

def calculate_cagr(start_val, end_val, periods):
    """
    Computes Compound Annual Growth Rate (CAGR) strictly for valid, positive values.
    CAGR = (Ending Value / Beginning Value) ** (1 / Number of Periods) - 1
    """
    if start_val <= 0 or end_val <= 0 or periods <= 0:
        return 0.0
    return ((end_val / start_val) ** (1.0 / periods) - 1.0) * 100.0

def render_overview_kpis(df_ril, df_tel, df_ret):
    """
    Renders high-level KPI cards with clear reporting periods, units, and baseline deltas.
    """
    st.markdown("### 📌 Executive KPI Snapshot (FY2017 Baseline vs FY2024 Current)")

    # Data row extraction (FY17 index 0, FY24 index 7)
    fy17_ril_rev = df_ril.loc[0, "Gross_Revenue_Cr"]
    fy24_ril_rev = df_ril.loc[7, "Gross_Revenue_Cr"]
    cagr_ril_rev = calculate_cagr(fy17_ril_rev, fy24_ril_rev, 7)

    fy17_ret_rev = df_ret.loc[0, "Retail_Revenue_Cr"]
    fy24_ret_rev = df_ret.loc[7, "Retail_Revenue_Cr"]
    cagr_ret_rev = calculate_cagr(fy17_ret_rev, fy24_ret_rev, 7)

    fy17_jio_subs = df_tel.loc[0, "Jio_Subs_M"]
    fy24_jio_subs = df_tel.loc[7, "Jio_Subs_M"]
    cagr_jio_subs = calculate_cagr(fy17_jio_subs, fy24_jio_subs, 7)

    fy17_stores = df_ret.loc[0, "Operating_Store_Count"]
    fy24_stores = df_ret.loc[7, "Operating_Store_Count"]
    cagr_stores = calculate_cagr(fy17_stores, fy24_stores, 7)

    fy17_consumer_share = df_ril.loc[0, "Consumer_Share_Pct"]
    fy24_consumer_share = df_ril.loc[7, "Consumer_Share_Pct"]
    delta_share = fy24_consumer_share - fy17_consumer_share

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="Consolidated Revenue",
            value=f"₹{fy24_ril_rev:,.0f} Cr",
            delta=f"{cagr_ril_rev:.2f}% 7-Yr CAGR (3.03x)",
            help="Consolidated Gross Turnover as reported in RIL Integrated Annual Report (FY2024 vs FY2017 baseline of ₹3,30,180 Cr)."
        )
        st.caption("Period: FY2024 | Source: RIL")

    with col2:
        st.metric(
            label="Reliance Retail Revenue",
            value=f"₹{fy24_ret_rev:,.0f} Cr",
            delta=f"{cagr_ret_rev:.2f}% 7-Yr CAGR (9.09x)",
            help="Reliance Retail Gross Revenue (FY2024 vs FY2017 baseline of ₹33,765 Cr)."
        )
        st.caption("Period: FY2024 | Source: Reliance Retail")

    with col3:
        st.metric(
            label="Jio Wireless Subscribers",
            value=f"{fy24_jio_subs:.2f} M",
            delta=f"{cagr_jio_subs:.2f}% 7-Yr CAGR (4.32x)",
            help="Total Wireless Subscribers as reported by TRAI at fiscal year-end March 31, 2024 (vs FY2017 baseline of 108.68M)."
        )
        st.caption("Period: FY2024 | Source: TRAI")

    with col4:
        st.metric(
            label="Retail Store Network",
            value=f"{fy24_stores:,} Stores",
            delta=f"{cagr_stores:.2f}% 7-Yr CAGR (5.21x)",
            help="Physical operating retail store count across all formats (FY2024 vs FY2017 baseline of 3,616 stores)."
        )
        st.caption("Period: FY2024 | Source: Reliance Retail")

    with col5:
        st.metric(
            label="Consumer Share of Mix",
            value=f"{fy24_consumer_share:.1f}%",
            delta=f"+{delta_share:.1f}% (+{delta_share*100:.0f} bps)",
            help="Combined contribution of Retail and Digital Services to consolidated gross turnover (FY2024 vs 10.59% in FY2017)."
        )
        st.caption("Period: FY2024 | Sourced: Calculated")

def render_q1_section_kpis(df_ril_wide, active_segments, active_years):
    """
    Renders filter-responsive KPIs for Business Diversification (Q1).
    """
    if not active_years:
        return

    start_year = active_years[0]
    end_year = active_years[-1]
    n_periods = len(active_years) - 1

    df_filtered = df_ril_wide[df_ril_wide["Financial_Year"].isin(active_years)].reset_index(drop=True)
    if df_filtered.empty:
        return

    start_row = df_filtered.iloc[0]
    end_row = df_filtered.iloc[-1]

    start_turnover = start_row["Gross_Revenue_Cr"]
    end_turnover = end_row["Gross_Revenue_Cr"]
    cagr_turnover = calculate_cagr(start_turnover, end_turnover, n_periods) if n_periods > 0 else 0.0

    start_consumer = start_row["Retail_Revenue_Cr"] + start_row["Digital_Services_Revenue_Cr"]
    end_consumer = end_row["Retail_Revenue_Cr"] + end_row["Digital_Services_Revenue_Cr"]
    cagr_consumer = calculate_cagr(start_consumer, end_consumer, n_periods) if n_periods > 0 else 0.0

    start_share = (start_consumer / start_turnover) * 100.0 if start_turnover > 0 else 0.0
    end_share = (end_consumer / end_turnover) * 100.0 if end_turnover > 0 else 0.0
    delta_share = end_share - start_share

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label=f"Selected Timeline Window",
            value=f"{start_year} → {end_year}",
            delta=f"{n_periods} Annual Periods"
        )
    with col2:
        st.metric(
            label=f"Gross Turnover ({end_year})",
            value=f"₹{end_turnover:,.0f} Cr",
            delta=f"{cagr_turnover:.2f}% Period CAGR" if n_periods > 0 else "Baseline"
        )
    with col3:
        st.metric(
            label=f"Consumer Revenue ({end_year})",
            value=f"₹{end_consumer:,.0f} Cr",
            delta=f"{cagr_consumer:.2f}% Period CAGR" if n_periods > 0 else "Baseline"
        )
    with col4:
        st.metric(
            label=f"Consumer Share ({end_year})",
            value=f"{end_share:.2f}%",
            delta=f"{'+' if delta_share >= 0 else ''}{delta_share:.2f}% shift" if n_periods > 0 else "Baseline"
        )

def render_q2_section_kpis(df_tel_clean, active_operators, active_years):
    """
    Renders filter-responsive KPIs for Jio & Telecom Market (Q2).
    """
    if not active_years:
        return

    start_year = active_years[0]
    end_year = active_years[-1]
    n_periods = len(active_years) - 1

    df_filtered = df_tel_clean[df_tel_clean["Financial_Year"].isin(active_years)].reset_index(drop=True)
    if df_filtered.empty:
        return

    start_row = df_filtered.iloc[0]
    end_row = df_filtered.iloc[-1]

    total_subs_end = end_row["Total_Wireless_Subs_M"]
    jio_subs_end = end_row["Jio_Subs_M"]
    jio_subs_start = start_row["Jio_Subs_M"]
    cagr_jio = calculate_cagr(jio_subs_start, jio_subs_end, n_periods) if n_periods > 0 else 0.0

    jio_share_end = end_row["Jio_Share_Pct"]
    jio_share_start = start_row["Jio_Share_Pct"]
    delta_share_bps = (jio_share_end - jio_share_start) * 100.0

    airtel_subs_end = end_row["Airtel_Subs_M"]
    cr2_end = ((jio_subs_end + airtel_subs_end) / total_subs_end) * 100.0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label="Total Industry Base",
            value=f"{total_subs_end:,.1f} M",
            delta=f"As of March 31, {end_year[-4:]}"
        )
    with col2:
        st.metric(
            label=f"Jio Subscriber Base ({end_year})",
            value=f"{jio_subs_end:,.2f} M",
            delta=f"{cagr_jio:.2f}% Period CAGR" if n_periods > 0 else "Baseline"
        )
    with col3:
        st.metric(
            label=f"Jio Market Share ({end_year})",
            value=f"{jio_share_end:.2f}%",
            delta=f"{'+' if delta_share_bps >= 0 else ''}{delta_share_bps:.0f} bps" if n_periods > 0 else "Baseline"
        )
    with col4:
        st.metric(
            label=f"Top 2 Private Share (CR2)",
            value=f"{cr2_end:.2f}%",
            delta="Jio + Bharti Airtel"
        )

def render_q3_section_kpis(df_ret_clean, active_years):
    """
    Renders filter-responsive KPIs for Reliance Retail Expansion (Q3).
    """
    if not active_years:
        return

    start_year = active_years[0]
    end_year = active_years[-1]
    n_periods = len(active_years) - 1

    df_filtered = df_ret_clean[df_ret_clean["Financial_Year"].isin(active_years)].reset_index(drop=True)
    if df_filtered.empty:
        return

    start_row = df_filtered.iloc[0]
    end_row = df_filtered.iloc[-1]

    rev_start = start_row["Retail_Revenue_Cr"]
    rev_end = end_row["Retail_Revenue_Cr"]
    cagr_rev = calculate_cagr(rev_start, rev_end, n_periods) if n_periods > 0 else 0.0

    stores_start = start_row["Operating_Store_Count"]
    stores_end = end_row["Operating_Store_Count"]
    delta_stores = stores_end - stores_start
    cagr_stores = calculate_cagr(stores_start, stores_end, n_periods) if n_periods > 0 else 0.0

    cust_end = end_row["Registered_Customers_M"]
    floor_end = end_row["Retail_Floor_Area_M_SqFt"]

    rev_per_store_start = rev_start / stores_start if stores_start > 0 else 0.0
    rev_per_store_end = rev_end / stores_end if stores_end > 0 else 0.0
    gain_per_store = ((rev_per_store_end / rev_per_store_start) - 1.0) * 100.0 if rev_per_store_start > 0 else 0.0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label=f"Retail Revenue ({end_year})",
            value=f"₹{rev_end:,.0f} Cr",
            delta=f"{cagr_rev:.2f}% Period CAGR" if n_periods > 0 else "Baseline"
        )
    with col2:
        st.metric(
            label=f"Store Network ({end_year})",
            value=f"{stores_end:,} Stores",
            delta=f"{'+' if delta_stores >= 0 else ''}{delta_stores:,} stores ({cagr_stores:.2f}% CAGR)" if n_periods > 0 else "Baseline"
        )
    with col3:
        st.metric(
            label=f"Registered Customers ({end_year})",
            value=f"{cust_end:.1f} M",
            delta=f"Area: {floor_end:.1f} M sq ft"
        )
    with col4:
        st.metric(
            label=f"Store Productivity ({end_year})",
            value=f"₹{rev_per_store_end:.2f} Cr/Store",
            delta=f"{'+' if gain_per_store >= 0 else ''}{gain_per_store:.2f}% gain" if n_periods > 0 else "Baseline"
        )
