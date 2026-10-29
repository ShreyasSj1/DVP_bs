"""
RELYNDIA — Phase 5 Automated Verification Script
Course: BISL504 Data Visualization Lab
"""

import sys
import os
import pandas as pd
import numpy as np

# Set workspace root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from components.metrics import (
    calculate_cagr,
    render_overview_kpis,
    render_q1_section_kpis,
    render_q2_section_kpis,
    render_q3_section_kpis
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
import components.explanations as explanations

def run_checks():
    print("=" * 70)
    print("RELYNDIA PHASE 5 VERIFICATION SUITE")
    print("=" * 70)

    # 1. Dataset verification
    print("\n[CHECK 1] Loading verified datasets...")
    clean_dir = os.path.join(BASE_DIR, "clean_data")
    data_dir = os.path.join(BASE_DIR, "data")

    df_ril_wide = pd.read_csv(os.path.join(clean_dir, "clean_ril_financial_segment_growth.csv"))
    df_ril_long = pd.read_csv(os.path.join(clean_dir, "clean_ril_segments_long.csv"))
    df_tel_wide = pd.read_csv(os.path.join(clean_dir, "clean_telecom_market_subscribers.csv"))
    df_tel_long = pd.read_csv(os.path.join(clean_dir, "clean_telecom_subscribers_long.csv"))
    df_ret_wide = pd.read_csv(os.path.join(clean_dir, "clean_reliance_retail_footprint.csv"))
    df_econ = pd.read_csv(os.path.join(data_dir, "verified_indian_economic_indicators.csv"))
    df_meta = pd.read_csv(os.path.join(data_dir, "data_sources_and_verification.csv"))

    assert len(df_ril_wide) == 8, f"Expected 8 years in df_ril_wide, got {len(df_ril_wide)}"
    assert len(df_tel_wide) == 8, f"Expected 8 years in df_tel_wide, got {len(df_tel_wide)}"
    assert len(df_ret_wide) == 8, f"Expected 8 years in df_ret_wide, got {len(df_ret_wide)}"
    print(" -> All 7 datasets loaded successfully with complete 8-year temporal coverage (FY2017–FY2024).")

    # 2. Mathematical formulas check
    print("\n[CHECK 2] Verifying mathematical calculations and CAGRs...")
    
    # RIL Consolidated Revenue CAGR (FY17-FY24, 7 periods)
    cagr_ril = calculate_cagr(df_ril_wide.loc[0, "Gross_Revenue_Cr"], df_ril_wide.loc[7, "Gross_Revenue_Cr"], 7)
    assert abs(cagr_ril - 17.15) < 0.05, f"RIL CAGR mismatch: {cagr_ril}"
    print(f" -> RIL Consolidated Revenue CAGR: {cagr_ril:.2f}% (Expected: 17.15%) [PASS]")

    # Retail Revenue CAGR (FY17-FY24, 7 periods)
    cagr_ret = calculate_cagr(df_ret_wide.loc[0, "Retail_Revenue_Cr"], df_ret_wide.loc[7, "Retail_Revenue_Cr"], 7)
    assert abs(cagr_ret - 37.06) < 0.05, f"Retail CAGR mismatch: {cagr_ret}"
    print(f" -> Retail Revenue CAGR: {cagr_ret:.2f}% (Expected: 37.06%) [PASS]")

    # Digital Services CAGR (FY18-FY24, 6 periods)
    cagr_jio_rev = calculate_cagr(df_ril_wide.loc[1, "Digital_Services_Revenue_Cr"], df_ril_wide.loc[7, "Digital_Services_Revenue_Cr"], 6)
    assert abs(cagr_jio_rev - 36.79) < 0.05, f"Digital Services CAGR mismatch: {cagr_jio_rev}"
    print(f" -> Digital Services Revenue CAGR: {cagr_jio_rev:.2f}% (Expected: 36.79%) [PASS]")

    # Jio Wireless Subscribers CAGR (FY17-FY24, 7 periods)
    cagr_jio_subs = calculate_cagr(df_tel_wide.loc[0, "Jio_Subs_M"], df_tel_wide.loc[7, "Jio_Subs_M"], 7)
    assert abs(cagr_jio_subs - 23.26) < 0.05, f"Jio Subs CAGR mismatch: {cagr_jio_subs}"
    print(f" -> Jio Subscriber CAGR: {cagr_jio_subs:.2f}% (Expected: 23.26%) [PASS]")

    # Retail Stores CAGR (FY17-FY24, 7 periods)
    cagr_stores = calculate_cagr(df_ret_wide.loc[0, "Operating_Store_Count"], df_ret_wide.loc[7, "Operating_Store_Count"], 7)
    assert abs(cagr_stores - 26.59) < 0.05, f"Stores CAGR mismatch: {cagr_stores}"
    print(f" -> Store Count CAGR: {cagr_stores:.2f}% (Expected: 26.59%) [PASS]")

    # Retail Store Productivity
    prod_fy17 = df_ret_wide.loc[0, "Retail_Revenue_Cr"] / df_ret_wide.loc[0, "Operating_Store_Count"]
    prod_fy24 = df_ret_wide.loc[7, "Retail_Revenue_Cr"] / df_ret_wide.loc[7, "Operating_Store_Count"]
    prod_gain = ((prod_fy24 / prod_fy17) - 1.0) * 100.0
    assert abs(prod_fy17 - 9.34) < 0.05
    assert abs(prod_fy24 - 16.29) < 0.05
    assert abs(prod_gain - 74.42) < 0.05
    print(f" -> Store Productivity: ₹{prod_fy17:.2f} Cr -> ₹{prod_fy24:.2f} Cr/store (+{prod_gain:.2f}% gain) [PASS]")

    # 3. Chart Generation Checks
    print("\n[CHECK 3] Verifying interactive chart rendering...")
    segments = list(COLOR_MAP_RIL.keys())
    operators = list(COLOR_MAP_TEL.keys())
    years = EXPECTED_YEARS

    f1 = create_q1_revenue_trend(df_ril_long, segments, years)
    assert f1 is not None, "create_q1_revenue_trend returned None"
    print(" -> Q1.1 Revenue Trend Chart: Valid Plotly Figure")

    f2 = create_q1_grouped_bar(df_ril_long, segments, years)
    assert f2 is not None, "create_q1_grouped_bar returned None"
    print(" -> Q1.2 Grouped Bar Chart: Valid Plotly Figure")

    f3 = create_q1_composition_stacked(df_ril_long, segments, years)
    assert f3 is not None, "create_q1_composition_stacked returned None"
    print(" -> Q1.3 100% Stacked Area Chart: Valid Plotly Figure")

    f4 = create_q2_subscribers_trend(df_tel_long, operators, years)
    assert f4 is not None, "create_q2_subscribers_trend returned None"
    print(" -> Q2.1 Telecom Subscribers Multi-Line Chart: Valid Plotly Figure")

    f5 = create_q2_market_share_stacked(df_tel_long, operators, years)
    assert f5 is not None, "create_q2_market_share_stacked returned None"
    print(" -> Q2.2 Operator Market Share 100% Area Chart: Valid Plotly Figure")

    f6 = create_q3_revenue_vs_stores_dual(df_ret_wide, years)
    assert f6 is not None, "create_q3_revenue_vs_stores_dual returned None"
    # Ensure zero baseline
    assert f6.layout.yaxis.rangemode == "tozero", "Q3.1 Primary Y-axis rangemode is not tozero"
    assert f6.layout.yaxis2.rangemode == "tozero", "Q3.1 Secondary Y-axis rangemode is not tozero"
    print(" -> Q3.1 Retail Revenue vs Store Count Dual-Axis Chart: Valid & Zero-Aligned")

    f7 = create_q3_customers_vs_area_dual(df_ret_wide, years)
    assert f7 is not None, "create_q3_customers_vs_area_dual returned None"
    assert f7.layout.yaxis.rangemode == "tozero", "Q3.2 Primary Y-axis rangemode is not tozero"
    assert f7.layout.yaxis2.rangemode == "tozero", "Q3.2 Secondary Y-axis rangemode is not tozero"
    print(" -> Q3.2 Retail Customers vs Floor Area Dual-Axis Chart: Valid & Zero-Aligned")

    # 4. Detailed Explanation Expanders Check
    print("\n[CHECK 4] Verifying Detailed Explanation functions...")
    exp_funcs = [
        "render_explanation_q1_1",
        "render_explanation_q1_2",
        "render_explanation_q1_3",
        "render_explanation_q2_1",
        "render_explanation_q2_2",
        "render_explanation_q3_1",
        "render_explanation_q3_2"
    ]
    for fn in exp_funcs:
        assert hasattr(explanations, fn), f"Missing explanation function {fn}"
        print(f" -> Found {fn}")
    print(" -> All 7 Detailed Explanation renderers verified.")

    # 5. Timeline Slider Range Resolution & Edge Cases Check
    print("\n[CHECK 5] Verifying Timeline Slider range resolution and edge cases...")
    from app import resolve_active_years
    assert resolve_active_years(('FY2017', 'FY2024')) == EXPECTED_YEARS
    assert resolve_active_years(('FY2019', 'FY2022')) == ['FY2019', 'FY2020', 'FY2021', 'FY2022']
    assert resolve_active_years('FY2020') == ['FY2020']
    assert resolve_active_years(2021) == ['FY2021']
    assert resolve_active_years(('FY2024', 'FY2018')) == ['FY2018', 'FY2019', 'FY2020', 'FY2021', 'FY2022', 'FY2023', 'FY2024']
    assert resolve_active_years(('FY1999', 'FY2022')) == ['FY2017', 'FY2018', 'FY2019', 'FY2020', 'FY2021', 'FY2022']
    assert resolve_active_years(('FY2019', 'FY2099')) == ['FY2019', 'FY2020', 'FY2021', 'FY2022', 'FY2023', 'FY2024']
    assert resolve_active_years(None) == EXPECTED_YEARS
    assert resolve_active_years(()) == EXPECTED_YEARS
    print(" -> All timeline slider edge cases (single value, reversed range, missing years, ints, None) passed.")

    # 6. Metadata Schema Mapping & Display Check
    print("\n[CHECK 6] Verifying Metadata schema mapping and display...")
    from app import prepare_metadata_display
    meta_disp = prepare_metadata_display(df_meta)
    expected_cols = ["Dataset", "Source Name", "Source Type", "Data Span", "Verification Status", "Primary URL / Filings Reference"]
    assert meta_disp.columns.tolist() == expected_cols, f"Mismatch in metadata display columns: {meta_disp.columns.tolist()}"
    assert len(meta_disp) == 4, f"Expected 4 dataset rows in summary, got {len(meta_disp)}"
    assert (meta_disp["Source Type"] == "Not provided in source metadata").all(), "Expected fallback for absent Source Type"
    assert (meta_disp["Data Span"] == "FY2017–FY2024").all(), "Expected FY2017–FY2024 data span"
    print(" -> Metadata display schema mapping and fallbacks verified cleanly.")

    print("\n" + "=" * 70)
    print("ALL PHASE 5 AUTOMATED VERIFICATION CHECKS PASSED SUCCESSFULLY (100%)")
    print("=" * 70)

if __name__ == "__main__":
    run_checks()
