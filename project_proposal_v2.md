# RELYNDIA — PROJECT PROPOSAL — VERSION 2 (REVISED)
**Sub-title:** Visualizing Reliance's Business and Market Footprint in India  
**Status:** Approved Final Version (Week 4 / Proposal V2)  
**Course:** BISL504 Data Visualization Lab | Department of IS&E, NIE Mysuru  

---

## 1. Project Title
**RELYNDIA — Visualizing Reliance's Business and Market Footprint in India**

---

## 2. Revised Problem Statement
Reliance Industries has evolved from its traditional energy and petrochemical businesses into a diversified business group with operations across energy and materials, digital services, telecommunications, retail, media and emerging businesses.

The scale of this transformation is difficult to understand from individual financial reports and isolated statistics. Different Reliance businesses have developed at different rates, while some have also expanded into rapidly changing Indian markets.

**RELYNDIA** aims to visualize this transformation as a connected story — from Reliance's traditional businesses and diversification to the expansion of Digital/Jio and Retail, supported by relevant market and economic context.

The project will focus on measurable historical trends and comparisons and will **avoid unsupported claims of direct causation**.

---

## 3. Objectives
- **Visualize Reliance's evolution and diversification** across its major business segments.
- **Compare the growth and contribution** of major segments such as O2C, Oil & Gas, Digital Services/Jio, Retail and other segments where consistent data is available.
- **Examine Jio's growth** alongside changes in India's telecom market.
- **Analyse Reliance Retail's expansion** through revenue, stores and consumer reach.
- **Use appropriate visualizations** to reveal trends, comparisons and relationships.
- **Develop an interactive dashboard** that presents the overall Reliance story in a clear sequence.

---

## 4. Scope of the Project

### Core Analysis
- Reliance's overall evolution and diversification across major business segments.
- Financial and operational growth of O2C, Oil & Gas, Digital Services/Jio, Retail and other major segments where reliable and comparable data is available.
- Jio subscriber growth and comparison with major Indian telecom operators.
- Reliance Retail revenue, store expansion and registered consumer reach.
- Cross-segment comparison to understand how Reliance's business mix has changed over time.

### Supporting Context
- Indian economic indicators where they add meaningful context and have reliable, consistent definitions.
- External market indicators, particularly telecom market share, to place Jio's growth in context.

### Boundaries (Academic Guardrails)
- **No prediction** of future performance.
- **No claim** that Reliance or Jio directly caused observed economic or competitor changes.
- **No attempt** to analyse every subsidiary when comparable quantitative data is unavailable.
- **No unsupported claim** that Reliance controls the Indian economy or individual markets.

---

## 5. Guiding Questions

* **Q1. How has Reliance diversified across its major business segments over time?**  
  *Data:* Reliance segment data (`verified_ril_financial_segment_growth.csv`)  
  *Visualizations:* Line charts, grouped/stacked bars, and business-composition charts.
* **Q2. How did the growth of Jio coincide with changes in India's telecom market?**  
  *Data:* Telecom subscriber/market-share data (`verified_telecom_market_subscribers.csv`)  
  *Visualizations:* Multi-line and market-share charts.
* **Q3. How has Reliance expanded its retail footprint and consumer reach over time?**  
  *Data:* Retail revenue, stores and customers (`verified_reliance_retail_footprint.csv`)  
  *Visualizations:* Line/bar charts and KPI cards.

---

## 6. Dataset Strategy

| Dataset / Data Group | Purpose | Priority |
| :--- | :--- | :---: |
| **`verified_ril_financial_segment_growth.csv`** | Track diversification and financial/segment growth across major businesses. | **Core** |
| **`verified_telecom_market_subscribers.csv`** | Analyse Jio growth and changes in the Indian telecom market. | **Core** |
| **`verified_reliance_retail_footprint.csv`** | Analyse retail revenue, stores and consumer reach. | **Core** |
| **`verified_indian_economic_indicators.csv`** | Provide broader context where useful and sufficiently verified. | **Supporting / Optional** |

*Strategy Note:* The project will use complementary datasets rather than a single dataset. Reliance data will cover the broader business portfolio, while telecom and retail datasets will support deeper analysis of selected areas. Only segments with sufficiently reliable and comparable quantitative data will be used for detailed year-on-year comparisons.

---

## 7. Question-to-Visualization Mapping

| Guiding Question | Primary Visualization | Supporting Visualizations |
| :--- | :--- | :--- |
| **Reliance Diversification (Q1)** | Segmented / stacked bar chart | Line chart; KPI cards |
| **Jio & Telecom Market (Q2)** | Multi-line chart | Market-share stacked area/bar chart |
| **Retail Expansion (Q3)** | Line chart | Bar chart; KPI cards |

*Note:* Additional visualizations may be introduced during implementation when they answer a specific analytical question. Chart variety alone will not determine selection.

---

## 8. Dashboard Design (5 Progressive Story Sections)

The interactive dashboard will present the project as a progressive visual story:

| Section | Purpose | Key Elements |
| :--- | :--- | :--- |
| **1. Reliance at a Glance** | Introduce scale and portfolio. | Revenue, EBITDA and selected segment KPIs |
| **2. The Diversification Story** | Show how major Reliance businesses evolved. | O2C, Oil & Gas, Digital/Jio, Retail and other available segments |
| **3. The Jio / Telecom Shift** | Place Jio's growth within India's telecom market. | Subscriber trends and operator market share |
| **4. The Retail / Consumer Expansion** | Show physical and consumer reach. | Revenue, stores and registered customers |
| **5. Economic / Market Context** | Add context where data is relevant and verified. | Selected economic indicators |

*Potential Interactions:* Year selection, segment selection, telecom-operator filters, hover tooltips, and cross-filtering.

---

## 9. Tools & Technologies
- **Python and Pandas** for data cleaning, transformation and analysis.
- **Plotly (Express / Dash)** for interactive analytical charts and standalone web dashboard.
- **AI tools** for research, data profiling, critique and coding assistance, with human verification.

---

## 10. Project Timeline

| Phase | Work / Output |
| :--- | :--- |
| **Weeks 1–2** | Tool comparison, hands-on trials and selection (**Completed & Verified**) |
| **Week 3** | Dataset selection, verification, profiling and guiding questions (**Completed & Verified**) |
| **Week 4** | Proposal V1 → AI critique → decisions log → **Proposal V2 (Approved Final)** |
| **Weeks 5–6** | Data preparation, segment analysis and core visualizations |
| **Week 7** | Visualization refinement, validation and implementation freeze |
| **Weeks 8–9** | Interactive dashboard, usability/accessibility review and iteration |
| **Week 10** | Final presentation, report and viva preparation |

---

## 11. Expected Outcomes
- A verified, analysis-ready data foundation covering Reliance's broader business portfolio.
- A visual account of Reliance's diversification and changing business mix.
- A market-based analysis of Jio's growth alongside telecom changes.
- A visual account of Reliance Retail's expansion and consumer reach.
- An interactive dashboard connecting the major findings into one coherent story.

---

## 12. Limitations & Academic Guardrails
- The project depends primarily on publicly available historical data (FY2017–FY2024).
- Reporting periods, segment definitions and measurement methods may vary across years. Some metrics may be derived from official data.
- **Observed trends and temporal coincidence will NOT be interpreted as proof of causation.** Source definitions and data limitations will be documented in the final report.

---

## 13. Revision Summary from Version 1
Following the AI critique and team decisions, Version 2 retains the broader Reliance diversification concept while structuring it into an overall portfolio view and focused deep dives. The scope was refined rather than reduced: major Reliance segments remain part of the core story, while Jio/telecom and Retail receive deeper analysis because stronger supporting datasets are available.
