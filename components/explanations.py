"""
RELYNDIA — 7-Point Detailed Explanation Panels
Course: BISL504 Data Visualization Lab
"""

import streamlit as st

def render_explanation_q1_1():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        An interactive multi-line time series tracking annual gross revenue (in ₹ Crore) across Reliance's four primary reporting business segments:
        - **Oil-to-Chemicals (O2C)**
        - **Reliance Retail**
        - **Digital Services (Jio Platforms)**
        - **Financial Services & Others**
        between FY2017 and FY2024.

        #### 2. Overall Trend
        All core operating segments demonstrated substantial top-line expansion over the 8-year period. However, the trajectory slopes of consumer-facing businesses (Retail and Jio) were significantly steeper than the traditional energy business, leading to an increasingly balanced conglomerate revenue structure.

        #### 3. Important Changes & Periods
        - **FY2017–FY2020 (Consumer Takeoff):** Rapid scaling phase where Retail grew 4.8x and Jio scaled from commercial rollout to ₹68,462 Cr.
        - **FY2021 (COVID-19 Pandemic Divergence):** O2C revenue dropped by **-₹96,476 Cr (-25.7%)** due to global fuel demand destruction during lockdowns. Retail saw a mild dip of **-3.3%**, while Digital Services revenue grew by **+₹18,031 Cr (+26.3%)** driven by surging stay-at-home data demand.
        - **FY2022–FY2024 (Post-Pandemic Rebound):** Strong recovery across all verticals as consolidated gross revenue crossed ₹10 Lakh Crore.

        #### 4. Relevant Quantitative Metrics
        - **Reliance Retail 7-Year CAGR (FY17–FY24):** `37.06%` (Scaled from ₹33,765 Cr to ₹3,06,786 Cr; +808.58%).
        - **Digital Services 6-Year CAGR (FY18 full year to FY24):** `36.79%` (Expanded from ₹20,154 Cr to ₹1,32,045 Cr; +555.18%).
        - **O2C 7-Year CAGR (FY17–FY24):** `12.89%` (Moved from ₹2,41,674 Cr to ₹5,64,748 Cr; +133.68%).
        - **Largest Single-Year Increase:** O2C in FY2022 (+₹1,88,173 Cr post-lockdown rebound).
        - **Deepest Single-Year Decrease:** O2C in FY2021 (-₹96,476 Cr pandemic crude oil drop).

        #### 5. Documented Business Factors
        - *Data observation:* Retail and Digital Services grew at persistent double-digit rates year-over-year.
        - *Documented context:* RIL Integrated Annual Reports attribute Retail growth to rapid physical store additions (3,616 to 18,837 stores), expanding grocery/electronics formats, and omni-channel digital commerce. Digital Services growth is documented in annual filings as resulting from pan-India 4G/5G mobile subscriber adoption (108M to 470M users) and high data consumption. O2C revenue trends were driven by global crude refining margins (GRMs) and product crack spreads.

        #### 6. Limitations & Cautions
        Pre-FY2020 O2C figures combine previously separated Refining and Petrochemicals reporting lines to maintain consistency with RIL's unified segment reporting format introduced in FY2020.

        #### 7. Key Takeaway
        While Oil-to-Chemicals remains Reliance's largest single revenue stream, the primary engine of top-line expansion between FY2017 and FY2024 shifted decisively toward consumer-facing Retail and Digital verticals.
        """)

def render_explanation_q1_2():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        A grouped bar chart comparing the absolute revenue scale (₹ Crore) of all 4 reporting segments side-by-side across each fiscal year from FY2017 to FY2024.

        #### 2. Overall Trend
        Visualizes the narrowing gap in absolute scale between industrial energy businesses and consumer-facing retail and telecom businesses.

        #### 3. Important Changes & Periods
        - In FY2017, O2C (₹2,41,674 Cr) dwarfed all other segments combined. Retail was ₹33,765 Cr and Digital Services was ₹1,207 Cr.
        - By FY2024, Retail reached ₹3,06,786 Cr and Digital Services reached ₹1,32,045 Cr, establishing multi-pillar corporate scale.

        #### 4. Relevant Quantitative Metrics
        - **Scale Ratio (O2C : Retail):** Contracted from `7.16x` in FY2017 to `1.84x` in FY2024.
        - **Non-O2C Combined Revenue:** Expanded from `₹88,506 Cr (FY17)` to `₹4,35,374 Cr (FY24)` (+391.9%).

        #### 5. Documented Business Factors
        - *Data observation:* Retail and Jio bars showed progressive year-on-year height increases while O2C bar heights moved in cyclical steps.
        - *Documented context:* RIL Board Reports identify this as the planned outcome of strategic capital expenditure redeployed from mature refining operations into high-growth domestic consumer markets.

        #### 6. Limitations & Cautions
        Annual grouped bars do not show intra-year seasonality such as festive quarter retail sales spikes.

        #### 7. Key Takeaway
        Direct yearly comparison confirms that Reliance has evolved into a balanced multi-segment conglomerate where consumer verticals command scale comparable to traditional industrial operations.
        """)

def render_explanation_q1_3():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        A 100% normalized stacked area chart displaying the proportionate contribution (%) of each business segment to consolidated gross revenue from FY2017 to FY2024.

        #### 2. Overall Trend
        A clear structural transition where the red (Retail) and blue (Jio) consumer bands steadily widen, displacing the dominant amber (O2C) energy band over the 8-year timeline.

        #### 3. Important Changes & Periods
        - **FY2017 Baseline:** O2C accounted for `73.20%` of revenue, while Retail was `10.23%` and Digital was `0.37%`.
        - **FY2021 Peak Consumer Share:** Consumer share reached `45.28%` when global oil refining was suppressed during pandemic lockdowns.
        - **FY2024 Current Position:** Retail and Digital Services together constitute `43.88%` of gross revenue.

        #### 4. Relevant Quantitative Metrics
        - **Total Consumer Share (Retail + Digital):** Expanded from `10.59%` (FY17) to `43.88%` (FY24) (+3,329 basis points shift).
        - **O2C Contribution:** Contracted from `73.20%` (FY17) to `56.47%` (FY24) (-1,673 basis points).
        - **Retail Share:** Tripled from `10.23%` (FY17) to `30.67%` (FY24) (+2,044 basis points).

        #### 5. Documented Business Factors
        - *Data observation:* The composition mix changed permanently, not temporarily reverting back after the FY2021 pandemic period.
        - *Documented context:* RIL investor presentations explicitly cite the strategic goal of establishing consumer businesses as equal co-drivers of profitability alongside energy.

        #### 6. Limitations & Cautions
        Proportional share is influenced by denominator swings; a spike in crude oil prices raises O2C revenue, which mechanically lowers the percentage share of consumer verticals even if retail sales grow.

        #### 7. Key Takeaway
        The 100% stacked area chart provides definitive visual and mathematical proof of Reliance's portfolio diversification, transitioning from a single-industry firm into a consumer-tech and industrial conglomerate.
        """)

def render_explanation_q2_1():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        A multi-line time series tracking total wireless subscriber counts (in Millions) for Reliance Jio, Bharti Airtel, Vodafone Idea (Vi), and BSNL/MTNL as reported by TRAI at the end of each fiscal year (March 31) from FY2017 to FY2024.

        #### 2. Overall Trend
        Rapid initial subscriber expansion for Jio, steady growth for Bharti Airtel, and sustained contraction for Vodafone Idea and BSNL, while total industry subscribers remained stable around 1.14B to 1.18B.

        #### 3. Important Changes & Periods
        - **FY2017–FY2020 (4G Mass Adoption):** Jio added +278.84M subscribers in 3 years.
        - **FY2018–FY2019 (Vodafone Idea Merger):** Vodafone and Idea Cellular completed their merger in August 2018, consolidating their base at a peak of 408.06M subscribers, after which the merged entity saw persistent declines.
        - **FY2022 (Inactive SIM Cleanup):** Jio subscriber count temporarily contracted from 422.92M to 410.19M (-12.73M) due to systematic deactivation of low-ARPU inactive SIMs.
        - **FY2023–FY2024 (5G Rollout Phase):** Jio resumed growth, crossing 469M subscribers.

        #### 4. Relevant Quantitative Metrics
        - **Jio Subscriber CAGR (FY17–FY24):** `23.26%` (108.68M to 469.73M; +332.21% net expansion).
        - **Airtel Subscriber CAGR (FY17–FY24):** `5.03%` (273.65M to 385.83M; +41.00% net expansion).
        - **Vi Subscriber CAGR (FY18 peak to FY24):** `-10.30%` (408.06M to 212.64M; -47.89% net contraction).
        - **Total Industry Wireless Base:** Moved from 1,170.17M (FY17) to 1,165.17M (FY24) (-0.06% CAGR).

        #### 5. Documented Business Factors
        - *Data observation:* Jio subscriber growth occurred concurrently with subscriber contractions at Vi and BSNL, while total industry subscribers remained flat.
        - *Documented context:* TRAI reports document that subscriber migrations coincided with pan-India 4G coverage rollout, VoLTE adoption, bundled data tariffs, and Mobile Number Portability (MNP) shifts.

        #### 6. Limitations & Cautions
        Subscriber counts represent Total Wireless Subscribers (VLR active + HLR registered SIMs) as recorded by TRAI at fiscal year-end (March 31).

        #### 7. Key Takeaway
        Jio's expansion from 108M to 470M subscribers coincided with a major consolidation of India's wireless subscriber base into two primary private operators (Jio and Airtel).
        """)

def render_explanation_q2_2():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        A 100% stacked area chart tracking the relative percentage market share of wireless subscribers across all major Indian telecom operators from FY2017 to FY2024.

        #### 2. Overall Trend
        The Indian telecom industry consolidated from a multi-operator competitive landscape into a market structure where the top two private operators command nearly three-quarters of all subscribers.

        #### 3. Important Changes & Periods
        - **FY2017:** Highly fragmented market where Vi (combined) had 33.1%, Airtel had 23.4%, BSNL had 8.9%, and Jio had 9.3%.
        - **FY2020:** Jio crossed 33% share, becoming the market leader by subscriber volume.
        - **FY2024:** Top 2 private operators command 73.4% of total wireless subscribers.

        #### 4. Relevant Quantitative Metrics
        - **Reliance Jio Share:** Rose from `9.29%` (FY17) to `40.31%` (FY24) (+3,102 basis points).
        - **Bharti Airtel Share:** Rose from `23.39%` (FY17) to `33.11%` (FY24) (+972 basis points).
        - **Vodafone Idea Share:** Contracted from `33.08%` (FY17) to `18.25%` (FY24) (-1,483 basis points).
        - **Top 2 Concentration Ratio (CR2 = Jio + Airtel):** Rose from `32.68%` (FY17) to `73.42%` (FY24).
        - **Private Sector Total Share (Jio + Airtel + Vi):** Rose from `65.76%` (FY17) to `91.67%` (FY24).

        #### 5. Documented Business Factors
        - *Data observation:* Market share gains were concentrated in Jio and Airtel.
        - *Documented context:* TRAI Performance Indicator Reports document that smaller operators (Aircel, RCom, Tata Tele) exited the market between FY18–FY20, transferring subscriber shares to capitalized 4G network operators.

        #### 6. Limitations & Cautions
        Market share is based on subscriber volume rather than Adjusted Gross Revenue (AGR) revenue market share.

        #### 7. Key Takeaway
        The telecom market share evolution illustrates industry consolidation, with Jio emerging as the market leader with over 40% subscriber market share by FY2024.
        """)

def render_explanation_q3_1():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        A dual-axis chart comparing Reliance Retail Gross Revenue (₹ Crore, Bars on left axis) alongside Total Operating Store Count (Line on right axis) from FY2017 to FY2024, with both axes zero-aligned.

        #### 2. Overall Trend
        Strong simultaneous expansion of physical footprint and revenue, with revenue growth accelerating faster than physical store additions.

        #### 3. Important Changes & Periods
        - **FY2017–FY2020:** Rapid initial nationwide rollout across grocery, electronics, and fashion apparel formats.
        - **FY2021 (COVID-19 Impact):** Temporary store closures and footfall restrictions paused revenue growth (-3.3% to ₹1,57,629 Cr) despite net physical store additions (+927 stores).
        - **FY2022–FY2024:** Post-lockdown acceleration; revenue surged past ₹3 Lakh Crore while stores approached 19,000.

        #### 4. Relevant Quantitative Metrics
        - **Store Count 7-Year CAGR (FY17–FY24):** `26.59%` (3,616 stores to 18,837 stores; 5.21x expansion, +15,221 stores).
        - **Retail Revenue 7-Year CAGR (FY17–FY24):** `37.06%` (₹33,765 Cr to ₹3,06,786 Cr; 9.09x expansion, +₹2,73,021 Cr).
        - **Average Revenue Throughput per Store:** Increased from `₹9.34 Cr/store (FY17)` to `₹16.29 Cr/store (FY24)` (+74.42% productivity gain).

        #### 5. Documented Business Factors
        - *Data observation:* Revenue expanded 9.1x while store count expanded 5.2x.
        - *Documented context:* Reliance Retail Annual Reports document that growth was driven by nationwide expansion across grocery, consumer electronics, and fashion apparel formats, paired with higher sales density in mature stores and digital commerce (JioMart) order fulfillment.

        #### 6. Limitations & Cautions
        Store counts aggregate different store formats (ranging from small neighborhood stores to large hypermarkets) with varying floor spaces and unit revenues.

        #### 7. Key Takeaway
        Reliance Retail's scaling over FY2017–FY2024 was achieved through a dual strategy: aggressive physical store network rollout across India alongside a 74.4% increase in revenue productivity per store.
        """)

def render_explanation_q3_2():
    with st.expander("[ Detailed Explanation ]"):
        st.markdown("""
        #### 1. What the Chart Shows
        A dual-axis line chart comparing Registered Retail Customer Base (Millions, left axis) against Total Retail Operational Floor Space (Million Square Feet, right axis) from FY2017 to FY2024.

        #### 2. Overall Trend
        Consistent, compounding growth across both consumer reach (customer accounts) and physical real estate footprint across Indian urban and rural markets.

        #### 3. Important Changes & Periods
        - **FY2017–FY2020:** Early customer base expansion from 35M to 125M as store area doubled from 13.5M to 28.7M sq ft.
        - **FY2021–FY2024:** Broadened footprint reaching 304M registered customers and 79.1M sq ft across Tier 1 through Tier 4 cities.

        #### 4. Relevant Quantitative Metrics
        - **Customer Base 7-Year CAGR:** `36.18%` (35.0M to 304.0M accounts; 8.69x expansion, +269.0M customers).
        - **Floor Area 7-Year CAGR:** `28.73%` (13.5M to 79.1M sq ft; 5.86x expansion, +65.6M sq ft).
        - **Average Store Floor Size:** Grew from `3,733 sq ft/store (FY17)` to `4,199 sq ft/store (FY24)`.

        #### 5. Documented Business Factors
        - *Data observation:* Customer base growth (36.18% CAGR) outpaced physical space expansion (28.73% CAGR).
        - *Documented context:* Reliance Retail filings attribute customer acquisition to integrated retail loyalty programs, aggressive geographical expansion into Tier 2–4 towns, and omni-channel digital onboarding.

        #### 6. Limitations & Cautions
        Registered customer figures reflect cumulative loyalty accounts and active customer IDs, which may include multi-card holders or duplicate consumer profiles.

        #### 7. Key Takeaway
        The expansion of Reliance Retail's registered customer base to over 300 million and operational area to 79 million sq ft captures its widespread consumer presence across India.
        """)
