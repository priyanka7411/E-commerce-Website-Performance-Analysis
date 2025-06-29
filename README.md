# 🛍️ E-commerce Website Performance Analysis

This project analyzes an e-commerce website's user behavior using GA4-based event-level data. It includes data exploration, funnel analysis, A/B testing, cohort analysis, and an interactive Streamlit dashboard to visualize and interpret user behavior patterns.

---

## 📁 Project Structure

```
Ecommerce_Performance_Analysis/
│
├── data/
│   ├── raw_data.csv
│   ├── cleaned_ecommerce_data.csv
│   └── cohort.csv
│
├── notebooks/
│   ├── 1_data_exploration.ipynb
│   ├── 2_funnel_ab_testing.ipynb
│   ├── 3_cohort_analysis.ipynb
│   └── 4_optional_streamlit_code.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- 📊 **Exploratory Data Analysis**
  - Dataset structure, missing value treatment
  - Event type and session-based breakdown
  - Key metrics (bounce rate, session duration)

- 🔄 **Funnel & A/B Testing**
  - Simulated A/B groups from GA data
  - Conversion funnel analysis
  - Statistical test to compare versions

- 👥 **Cohort Analysis**
  - Monthly cohort segmentation by `user_first_touch_timestamp`
  - User retention matrix and visualization
  - Revenue per cohort insights

- 🌐 **Interactive Streamlit Dashboard**
  - Filters for date, device, region, visitor type
  - KPIs: Sessions, Unique Visitors, Bounce Rate, Avg. Session Duration
  - Funnel drop-off chart, daily session trends
  - A/B comparison plots and pie charts

---

## 📦 Requirements

Install the required libraries using:

```bash
pip install -r requirements.txt
```

Main dependencies include:
- `pandas`
- `numpy`
- `matplotlib`, `seaborn`
- `plotly`
- `streamlit`
- `scipy`

---

## ▶️ Running the Dashboard

To run the Streamlit dashboard locally:

```bash
streamlit run app.py
```

---

## 📌 Key Insights

- Returning visitors drive higher session durations and conversions.
- Significant drop-off occurs between product view and cart stage.
- A/B test indicates Variant B improves conversion by 25%.
- Cohorts show a gradual retention drop over 4 weeks.

---

## 📚 Data Source

- Google Analytics 4 event-based dataset (obfuscated GA4 public data)
- Pre-cleaned and aggregated for session-level insights

---

## 👩‍💻 Author

**Priyanka Malavade**  
*Data Analyst | Python & Streamlit Developer | Dashboard Enthusiast*

---

## 📜 License

Licensed under the [MIT License](LICENSE).
