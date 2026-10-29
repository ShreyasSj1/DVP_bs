import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLEAN_DIR = os.path.join(BASE_DIR, "clean_data")
os.makedirs(CLEAN_DIR, exist_ok=True)

print("=" * 80)
print("RELYNDIA (WEEK 5) — DATA CLEANING & RESHAPING PIPELINE")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1. CLEAN RIL FINANCIAL & SEGMENT DATA (WIDE & LONG FORMATS)
# -----------------------------------------------------------------------------
ril_path = os.path.join(DATA_DIR, "verified_ril_financial_segment_growth.csv")
df_ril = pd.read_csv(ril_path)

# Rename columns to standardized clean names
df_ril_clean = pd.DataFrame()
df_ril_clean["Financial_Year"] = df_ril["Financial Year"]
df_ril_clean["Year"] = df_ril["Financial Year"].str.replace("FY", "").astype(int)
df_ril_clean["Gross_Revenue_Cr"] = df_ril["Gross Revenue (₹ Cr)"]
df_ril_clean["EBITDA_Cr"] = df_ril["EBITDA (₹ Cr)"]
df_ril_clean["PAT_Cr"] = df_ril["PAT (₹ Cr)"]
df_ril_clean["Total_Capex_Cr"] = df_ril["Total Capex (₹ Cr)"]
df_ril_clean["O2C_Revenue_Cr"] = df_ril["O2C Revenue (₹ Cr)"]
df_ril_clean["Retail_Revenue_Cr"] = df_ril["Retail Revenue (₹ Cr)"]
df_ril_clean["Digital_Services_Revenue_Cr"] = df_ril["Digital Services Revenue (₹ Cr)"]
df_ril_clean["Financial_Others_Revenue_Cr"] = df_ril["Financial & Others Revenue (₹ Cr)"]

# Derived Percentage Contributions
df_ril_clean["O2C_Share_Pct"] = (df_ril_clean["O2C_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100
df_ril_clean["Retail_Share_Pct"] = (df_ril_clean["Retail_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100
df_ril_clean["Digital_Share_Pct"] = (df_ril_clean["Digital_Services_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100
df_ril_clean["Financial_Others_Share_Pct"] = (df_ril_clean["Financial_Others_Revenue_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100

# Consumer Facing Share (Retail + Digital)
df_ril_clean["Consumer_Share_Pct"] = df_ril_clean["Retail_Share_Pct"] + df_ril_clean["Digital_Share_Pct"]
df_ril_clean["EBITDA_Margin_Pct"] = (df_ril_clean["EBITDA_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100
df_ril_clean["PAT_Margin_Pct"] = (df_ril_clean["PAT_Cr"] / df_ril_clean["Gross_Revenue_Cr"]) * 100

# Save wide format
ril_clean_path = os.path.join(CLEAN_DIR, "clean_ril_financial_segment_growth.csv")
df_ril_clean.to_csv(ril_clean_path, index=False)
print(f"✅ Generated: {ril_clean_path}")

# Create Long / Tidy Format for Plotly
segment_map = [
    ("Oil-to-Chemicals (O2C)", "O2C_Revenue_Cr", "O2C_Share_Pct", "Traditional Energy & Petrochemicals"),
    ("Reliance Retail", "Retail_Revenue_Cr", "Retail_Share_Pct", "Consumer Facing"),
    ("Digital Services (Jio)", "Digital_Services_Revenue_Cr", "Digital_Share_Pct", "Consumer Facing"),
    ("Financial Services & Others", "Financial_Others_Revenue_Cr", "Financial_Others_Share_Pct", "Financial & Others")
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
ril_long_path = os.path.join(CLEAN_DIR, "clean_ril_segments_long.csv")
df_ril_long.to_csv(ril_long_path, index=False)
print(f"✅ Generated: {ril_long_path}")

# -----------------------------------------------------------------------------
# 2. CLEAN TELECOM MARKET DATA (WIDE & LONG FORMATS)
# -----------------------------------------------------------------------------
telecom_path = os.path.join(DATA_DIR, "verified_telecom_market_subscribers.csv")
df_tel = pd.read_csv(telecom_path)

df_tel_clean = pd.DataFrame()
df_tel_clean["Financial_Year"] = df_tel["Financial Year"]
df_tel_clean["Year"] = df_tel["Financial Year"].str.replace("FY", "").astype(int)
df_tel_clean["Jio_Subs_M"] = df_tel["Jio Subscribers (M)"]
df_tel_clean["Airtel_Subs_M"] = df_tel["Airtel Subscribers (M)"]
df_tel_clean["Vi_Subs_M"] = df_tel["Vi Subscribers (M)"]
df_tel_clean["BSNL_MTNL_Subs_M"] = df_tel["BSNL MTNL Subscribers (M)"]
df_tel_clean["Total_Wireless_Subs_M"] = df_tel["Total Wireless Subscribers (M)"]

# Derived Exact Operator Market Shares
df_tel_clean["Jio_Share_Pct"] = (df_tel_clean["Jio_Subs_M"] / df_tel_clean["Total_Wireless_Subs_M"]) * 100
df_tel_clean["Airtel_Share_Pct"] = (df_tel_clean["Airtel_Subs_M"] / df_tel_clean["Total_Wireless_Subs_M"]) * 100
df_tel_clean["Vi_Share_Pct"] = (df_tel_clean["Vi_Subs_M"] / df_tel_clean["Total_Wireless_Subs_M"]) * 100
df_tel_clean["BSNL_MTNL_Share_Pct"] = (df_tel_clean["BSNL_MTNL_Subs_M"] / df_tel_clean["Total_Wireless_Subs_M"]) * 100

tel_clean_path = os.path.join(CLEAN_DIR, "clean_telecom_market_subscribers.csv")
df_tel_clean.to_csv(tel_clean_path, index=False)
print(f"✅ Generated: {tel_clean_path}")

# Long / Tidy format for Telecom
op_map = [
    ("Reliance Jio", "Jio_Subs_M", "Jio_Share_Pct", "Private Disruptor (4G/5G)"),
    ("Bharti Airtel", "Airtel_Subs_M", "Airtel_Share_Pct", "Private Incumbent"),
    ("Vodafone Idea (Vi)", "Vi_Subs_M", "Vi_Share_Pct", "Merged Entity"),
    ("BSNL / MTNL", "BSNL_MTNL_Subs_M", "BSNL_MTNL_Share_Pct", "Public Sector")
]

tel_long_records = []
for idx, row in df_tel_clean.iterrows():
    for op_name, sub_col, share_col, cat in op_map:
        tel_long_records.append({
            "Financial_Year": row["Financial_Year"],
            "Year": row["Year"],
            "Operator": op_name,
            "Operator_Category": cat,
            "Subscribers_M": row[sub_col],
            "Market_Share_Pct": round(row[share_col], 2)
        })

df_tel_long = pd.DataFrame(tel_long_records)
tel_long_path = os.path.join(CLEAN_DIR, "clean_telecom_subscribers_long.csv")
df_tel_long.to_csv(tel_long_path, index=False)
print(f"✅ Generated: {tel_long_path}")

# -----------------------------------------------------------------------------
# 3. CLEAN RELIANCE RETAIL FOOTPRINT DATA
# -----------------------------------------------------------------------------
retail_path = os.path.join(DATA_DIR, "verified_reliance_retail_footprint.csv")
df_ret = pd.read_csv(retail_path)

df_ret_clean = pd.DataFrame()
df_ret_clean["Financial_Year"] = df_ret["Financial Year"]
df_ret_clean["Year"] = df_ret["Financial Year"].str.replace("FY", "").astype(int)
df_ret_clean["Retail_Revenue_Cr"] = df_ret["Retail Revenue (₹ Cr)"]
df_ret_clean["Retail_EBITDA_Cr"] = df_ret["Retail EBITDA (₹ Cr)"]
df_ret_clean["Operating_Store_Count"] = df_ret["Operating Store Count"]
df_ret_clean["Registered_Customers_M"] = df_ret["Registered Customers (M)"]
df_ret_clean["Retail_Floor_Area_M_SqFt"] = df_ret["Retail Floor Area (M sq ft)"]
df_ret_clean["Digital_Commerce_Share_Pct"] = df_ret["Digital Commerce Share (%)"]

# Derived Productivity & Density Metrics
df_ret_clean["Revenue_Per_Store_Cr"] = round(df_ret_clean["Retail_Revenue_Cr"] / df_ret_clean["Operating_Store_Count"], 2)
df_ret_clean["Revenue_Per_SqFt_Rs"] = round((df_ret_clean["Retail_Revenue_Cr"] * 1e7) / (df_ret_clean["Retail_Floor_Area_M_SqFt"] * 1e6), 2)
df_ret_clean["Avg_Store_Size_SqFt"] = round((df_ret_clean["Retail_Floor_Area_M_SqFt"] * 1e6) / df_ret_clean["Operating_Store_Count"], 1)
df_ret_clean["Retail_EBITDA_Margin_Pct"] = round((df_ret_clean["Retail_EBITDA_Cr"] / df_ret_clean["Retail_Revenue_Cr"]) * 100, 2)

ret_clean_path = os.path.join(CLEAN_DIR, "clean_reliance_retail_footprint.csv")
df_ret_clean.to_csv(ret_clean_path, index=False)
print(f"✅ Generated: {ret_clean_path}")

print("\n" + "=" * 80)
print("ALL CLEANED & RESHAPED DATASETS SUCCESSFULLY PREPARED IN clean_data/")
print("=" * 80)
