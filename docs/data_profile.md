# RELYNDIA — Week 5 Verified Data Profiling Report

**Course:** BISL504 Data Visualization Lab | Week 5

**Status:** Automated Quality Check over Verified Datasets

---

## RIL Financial & Segment Growth (`verified_ril_financial_segment_growth.csv`)

- **Dimensions:** 8 rows × 9 columns
- **Missing Values:** 0 (0.0%)
- **Duplicate Records:** 0
- **Time Horizon:** FY2017 to FY2024

### Column Schema & Data Types

| Column Name | Pandas Data Type | Non-Null Count | Unique Values |
| :--- | :--- | :---: | :---: |
| `Financial Year` | `object` | 8 | 8 |
| `Gross Revenue (₹ Cr)` | `int64` | 8 | 8 |
| `EBITDA (₹ Cr)` | `int64` | 8 | 8 |
| `PAT (₹ Cr)` | `int64` | 8 | 8 |
| `Total Capex (₹ Cr)` | `int64` | 8 | 8 |
| `O2C Revenue (₹ Cr)` | `int64` | 8 | 8 |
| `Retail Revenue (₹ Cr)` | `int64` | 8 | 8 |
| `Digital Services Revenue (₹ Cr)` | `int64` | 8 | 8 |
| `Financial & Others Revenue (₹ Cr)` | `int64` | 8 | 8 |

### Numerical Descriptive Statistics

| Metric Column | Count | Mean | Min | Median (50%) | Max | Std Dev |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Gross Revenue (₹ Cr) | 8.00 | 668,945.62 | 330,180.00 | 641,007.00 | 1,000,122.00 | 242,064.68 |
| EBITDA (₹ Cr) | 8.00 | 109,919.50 | 55,529.00 | 99,930.00 | 178,677.00 | 40,668.49 |
| PAT (₹ Cr) | 8.00 | 49,529.75 | 29,901.00 | 46,809.50 | 69,648.00 | 15,120.98 |
| Total Capex (₹ Cr) | 8.00 | 96,536.88 | 66,684.00 | 80,609.50 | 141,809.00 | 28,566.28 |
| O2C Revenue (₹ Cr) | 8.00 | 399,300.88 | 241,674.00 | 385,131.00 | 564,748.00 | 124,065.06 |
| Retail Revenue (₹ Cr) | 8.00 | 165,118.50 | 33,765.00 | 160,282.50 | 306,786.00 | 91,062.58 |
| Digital Services Revenue (₹ Cr) | 8.00 | 71,340.62 | 1,207.00 | 77,477.50 | 132,045.00 | 46,788.41 |
| Financial & Others Revenue (₹ Cr) | 8.00 | 38,049.88 | 16,176.00 | 34,902.50 | 53,987.00 | 14,026.81 |

---

## Indian Telecom Market Subscribers (`verified_telecom_market_subscribers.csv`)

- **Dimensions:** 8 rows × 7 columns
- **Missing Values:** 0 (0.0%)
- **Duplicate Records:** 0
- **Time Horizon:** FY2017 to FY2024

### Column Schema & Data Types

| Column Name | Pandas Data Type | Non-Null Count | Unique Values |
| :--- | :--- | :---: | :---: |
| `Financial Year` | `object` | 8 | 8 |
| `Jio Subscribers (M)` | `float64` | 8 | 8 |
| `Airtel Subscribers (M)` | `float64` | 8 | 8 |
| `Vi Subscribers (M)` | `float64` | 8 | 8 |
| `BSNL MTNL Subscribers (M)` | `float64` | 8 | 8 |
| `Total Wireless Subscribers (M)` | `float64` | 8 | 8 |
| `Jio Market Share (%)` | `float64` | 8 | 8 |

### Numerical Descriptive Statistics

| Metric Column | Count | Mean | Min | Median (50%) | Max | Std Dev |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Jio Subscribers (M) | 8.00 | 340.32 | 108.68 | 398.86 | 469.73 | 129.39 |
| Airtel Subscribers (M) | 8.00 | 331.99 | 273.65 | 338.81 | 385.83 | 41.70 |
| Vi Subscribers (M) | 8.00 | 303.90 | 212.64 | 279.46 | 408.06 | 80.67 |
| BSNL MTNL Subscribers (M) | 8.00 | 112.41 | 90.11 | 117.34 | 122.95 | 11.17 |
| Total Wireless Subscribers (M) | 8.00 | 1,163.16 | 1,142.09 | 1,163.49 | 1,183.41 | 15.24 |
| Jio Market Share (%) | 8.00 | 29.32 | 9.29 | 34.64 | 40.31 | 11.25 |

---

## Reliance Retail Footprint (`verified_reliance_retail_footprint.csv`)

- **Dimensions:** 8 rows × 7 columns
- **Missing Values:** 0 (0.0%)
- **Duplicate Records:** 0
- **Time Horizon:** FY2017 to FY2024

### Column Schema & Data Types

| Column Name | Pandas Data Type | Non-Null Count | Unique Values |
| :--- | :--- | :---: | :---: |
| `Financial Year` | `object` | 8 | 8 |
| `Retail Revenue (₹ Cr)` | `int64` | 8 | 8 |
| `Retail EBITDA (₹ Cr)` | `int64` | 8 | 8 |
| `Operating Store Count` | `int64` | 8 | 8 |
| `Registered Customers (M)` | `float64` | 8 | 8 |
| `Retail Floor Area (M sq ft)` | `float64` | 8 | 8 |
| `Digital Commerce Share (%)` | `float64` | 8 | 8 |

### Numerical Descriptive Statistics

| Metric Column | Count | Mean | Min | Median (50%) | Max | Std Dev |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Retail Revenue (₹ Cr) | 8.00 | 165,118.50 | 33,765.00 | 160,282.50 | 306,786.00 | 91,062.58 |
| Retail EBITDA (₹ Cr) | 8.00 | 10,345.88 | 1,203.00 | 9,721.50 | 23,082.00 | 7,430.67 |
| Operating Store Count | 8.00 | 12,271.50 | 3,616.00 | 12,247.50 | 18,837.00 | 5,152.05 |
| Registered Customers (M) | 8.00 | 149.00 | 35.00 | 140.50 | 304.00 | 95.73 |
| Retail Floor Area (M sq ft) | 8.00 | 37.75 | 13.50 | 31.25 | 79.10 | 23.41 |
| Digital Commerce Share (%) | 8.00 | 10.32 | 2.10 | 8.85 | 20.00 | 7.04 |

---

## Indian Economic Indicators (`verified_indian_economic_indicators.csv`)

- **Dimensions:** 8 rows × 6 columns
- **Missing Values:** 0 (0.0%)
- **Duplicate Records:** 0
- **Time Horizon:** FY2017 to FY2024

### Column Schema & Data Types

| Column Name | Pandas Data Type | Non-Null Count | Unique Values |
| :--- | :--- | :---: | :---: |
| `Financial Year` | `object` | 8 | 8 |
| `India Nominal GDP (₹ Lakh Cr)` | `float64` | 8 | 8 |
| `India Real GDP Growth (%)` | `float64` | 8 | 8 |
| `Private Sector Capex (₹ Lakh Cr)` | `float64` | 8 | 8 |
| `Telecom Sector GVA (₹ Cr)` | `int64` | 8 | 8 |
| `CPI Inflation (%)` | `float64` | 8 | 8 |

### Numerical Descriptive Statistics

| Metric Column | Count | Mean | Min | Median (50%) | Max | Std Dev |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| India Nominal GDP (₹ Lakh Cr) | 8.00 | 214.00 | 153.92 | 199.38 | 295.36 | 48.78 |
| India Real GDP Growth (%) | 8.00 | 5.50 | -5.83 | 7.02 | 9.05 | 4.84 |
| Private Sector Capex (₹ Lakh Cr) | 8.00 | 62.93 | 48.15 | 59.00 | 86.50 | 13.47 |
| Telecom Sector GVA (₹ Cr) | 8.00 | 236,143.75 | 182,450.00 | 232,170.00 | 302,500.00 | 41,347.33 |
| CPI Inflation (%) | 8.00 | 5.01 | 3.40 | 5.10 | 6.70 | 1.17 |

---

