# RELYNDIA — Course AI Usage Log
**Course:** BISL504 Data Visualization Lab  
**Project Title:** RELYNDIA — Visualizing Reliance's Business and Market Footprint in India  
**Institution:** Department of Information Science & Engineering, NIE Mysuru  
**Compliance Statement:** This log transparently records all AI assistance utilized during the project lifecycle, clearly distinguishing AI-generated code/suggestions from student/team modifications and decisions.

---

## 📅 Week 5 Log Entries: Data Preparation & Core Visualizations

### Entry 5.1: Automated Profiling Script Development
* **Prompt Summary:** Generate a Python script using Pandas to inspect verified CSV datasets for missing values, duplicates, and summary statistics.
* **AI Output Summary:** Provided boilerplate `df.info()`, `df.describe()`, and `df.to_markdown()` calls.
* **What the Team Modified:** Replaced `df.to_markdown()` with a custom string formatter function `df_to_markdown_table()` to build clean Markdown tables without external dependencies.
* **Why Modified:** Prevented runtime failures in the local environment due to the absence of the `tabulate` library.

### Entry 5.2: Wide-to-Long Tidy Data Reshaping
* **Prompt Summary:** Assist in reshaping wide segment revenue columns into long format for Plotly Express color mapping.
* **AI Output Summary:** Generated basic `pd.melt()` transformation.
* **What the Team Modified:** Replaced with explicit iterative mapping to assign standardized category tags (`Traditional Energy & Petrochemicals`, `Consumer Facing`, `Financial & Others`) and calculate verified percentage share metrics.
* **Why Modified:** Allowed precise control over segment definitions and enabled direct plotting of 100% normalized area charts.

### Entry 5.3: Dual-Axis Chart Construction for Retail
* **Prompt Summary:** Suggest visualization approaches for comparing Retail Revenue (₹ Cr) and Operating Store Count.
* **AI Output Summary:** Suggested separate bar and line charts.
* **What the Team Modified:** Implemented a single dual-axis chart using `plotly.subplots.make_subplots(specs=[[{"secondary_y": True}]])` with revenue as bars on the left axis and store count as a diamond-marker line on the right axis.
* **Why Modified:** Allowed direct visual comparison of revenue growth against physical network expansion on a unified timeline.

---

## 📅 Week 6 Log Entries: Core Analysis Completion & Validation

### Entry 6.1: Telecom Title & Interpretation Non-Causality Check
* **Prompt Summary:** Review visualization titles and draft observations for Question 2 (Telecom Market).
* **AI Output Summary:** Initial draft included phrases like *"Jio's aggressive pricing disrupted incumbents and forced market share loss."*
* **What the Team Modified:** Explicitly rejected causal wording. Rewrote all titles and insights to neutral, academically defensible terms: *"Jio wireless subscriber growth alongside changes in the Indian telecom market (FY2017–FY2024)."*
* **Why Modified:** Adhered strictly to BISL504 academic guardrails; observational time-series data proves correlation and coexistence, not mathematical causality.

### Entry 6.2: Analytical Insight Structuring
* **Prompt Summary:** Create a structured framework to record factual observations for each of the 7 core charts.
* **AI Output Summary:** Provided generic chart summaries.
* **What the Team Modified:** Enforced a rigorous 3-point analytical format for every visualization in `docs/visualization_insights.md`:
  1. *What does the chart show?* (Axes, measures, categories).
  2. *What trend or pattern is visible?* (Exact numerical evidence, start vs end values).
  3. *Why is that pattern relevant to the guiding question?* (Direct tie to Q1, Q2, or Q3).
* **Why Modified:** Ensured each visualization directly substantiates the project's core research questions for oral lab evaluation.

---

## 📅 Week 7 Log Entries: Visual Refinement & Implementation Freeze

### Entry 7.1: Unified Academic Visual Styling & Layout Dictionary
* **Prompt Summary:** Refactor Plotly script to enforce consistent font hierarchy, margins, and legend positioning across all charts.
* **AI Output Summary:** Suggested individual layout calls inside each figure definition.
* **What the Team Modified:** Created a centralized `LAYOUT_DEFAULTS` dictionary in `scripts/visualizations.py` and unpacked it across all figures (`**LAYOUT_DEFAULTS`).
* **Why Modified:** Enforced DRY (Don't Repeat Yourself) principles and guaranteed visual consistency across typography, font size, margins, and legend coordinates.

### Entry 7.2: Number Formatting & Currency Prefix Standards
* **Prompt Summary:** Standardize currency and unit formats on axes and hover templates.
* **AI Output Summary:** Suggested general integer formatting.
* **What the Team Modified:** Implemented explicit tick formatting (`tickprefix="₹"`, `tickformat=",.0f"`, `ticksuffix=" M"`, `ticksuffix="%"`) and customized `hovertemplate` strings across all 7 charts.
* **Why Modified:** Prevented ambiguity in metric scales during presentation (clarifying ₹ Crore vs Millions vs Percentages).

### Entry 7.3: Implementation Freeze Verification
* **Prompt Summary:** Prepare checklist to freeze Weeks 5–7 deliverables before starting dashboard phase.
* **AI Output Summary:** Outlined a generic project completion checklist.
* **What the Team Modified:** Created `docs/implementation_freeze_status.md` with explicit classification of all 7 retained charts as **KEEP (FROZEN)** and confirmed that dashboard layout/design is deferred to Weeks 8–9.
* **Why Modified:** Maintained strict lab syllabus discipline and avoided premature dashboard construction.

---

## 📅 Phase 4 Log Entries: Implementation Refinement & Freeze

### Entry 4.1: Retail Revenue vs Store Count Data Mapping Audit
* **Prompt Summary:** Investigate potential year-to-value mapping misalignment in Chart 3.1 dual-axis visualization.
* **AI Output Summary:** Suggested adjusting visual offsets or rebuilding series independently.
* **What the Team Modified:** Rejected manual offsets. Built a row-for-row verification script comparing raw CSV against clean DataFrame, identified that data was 100% aligned, and traced the visual artifact to unaligned secondary Y-axis zero baselines. Implemented `rangemode="tozero"` with calibrated bounds and added strict pre-plotting validation assertions.
* **Why Modified:** Enforced data integrity from authoritative sources and eliminated visual distortion without altering verified data.

### Entry 4.2: Factual Macroeconomic Annotations & Canvas Subtitles
* **Prompt Summary:** Add contextual annotations and informative subtitles across all 7 visualizations.
* **AI Output Summary:** Proposed generic text boxes explaining market changes with causal language.
* **What the Team Modified:** Authored concise, non-causal annotations pointing to verified historical inflection points (FY21 COVID-19 pandemic crude slump vs Jio resilience, Vodafone-Idea merger consolidation peak, and FY21 retail lockdown impact). Added standardized canvas subtitles with units and source citations (`Source: RIL Annual Reports`, `Source: TRAI`).
* **Why Modified:** Enhanced oral presentation interpretability and visual hierarchy while adhering strictly to academic non-causality guidelines.

### Entry 4.3: Full Pipeline Reproducibility & Image Export Isolation
* **Prompt Summary:** Update chart export workflow to handle both interactive HTML and static image exports.
* **AI Output Summary:** Proposed adding hard dependency on `kaleido` via unconditional `fig.write_image()`.
* **What the Team Modified:** Wrapped static image generation in a graceful try-except block in `save_visualization()` to prevent runtime failure in environments where `kaleido` is absent, while guaranteeing 100% reliable HTML generation.
* **Why Modified:** Guaranteed end-to-end reproducibility across standard student lab environments without environment breakage.

