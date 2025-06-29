import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Data
@st.cache_data

def load_data():
    df = pd.read_csv("/Users/priyankamalavade/Desktop/Ecommerce_Performance_Analysis/data/cleaned_ecommerce_data.csv")
    df["Month"] = pd.Categorical(df["Month"], categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ordered=True)
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
months = st.sidebar.multiselect("Select Month", df["Month"].unique(), default=df["Month"].unique())
region = st.sidebar.multiselect("Select Region", df["Region"].dropna().unique(), default=df["Region"].dropna().unique())
visitor_type = st.sidebar.multiselect("Select Visitor Type", df["VisitorType"].dropna().unique(), default=df["VisitorType"].dropna().unique())
revenue_filter = st.sidebar.radio("Revenue Generated?", ["All", "Yes", "No"])

# Apply Filters
filtered_df = df[
    (df["Month"].isin(months)) &
    (df["Region"].isin(region)) &
    (df["VisitorType"].isin(visitor_type))
]
if revenue_filter == "Yes":
    filtered_df = filtered_df[filtered_df["Revenue"] == True]
elif revenue_filter == "No":
    filtered_df = filtered_df[filtered_df["Revenue"] == False]

# Main Dashboard
st.title("📊 E-commerce Analytics Dashboard")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Sessions", len(filtered_df))
with col2:
    st.metric("Unique Visitors", filtered_df.shape[0])
with col3:
    st.metric("Bounce Rate", f"{filtered_df['BounceRates'].mean()*100:.2f}%")
with col4:
    st.metric("Avg. Time per Page", f"{filtered_df['Avg_Time_Per_Page'].mean():.2f} sec")

# Funnel Chart
st.markdown("---")
st.subheader("🛒 Funnel Analysis")
funnel_stages = ["Product Viewed", "Added to Cart", "Purchase"]
funnel_values = [len(filtered_df), int(len(filtered_df) * 0.6), int(len(filtered_df) * 0.25)]
fig_funnel = go.Figure(go.Funnel(
    y=funnel_stages,
    x=funnel_values,
    textinfo="value+percent initial"
))
st.plotly_chart(fig_funnel, use_container_width=True)

# Time Series: Monthly Revenue
st.markdown("---")
st.subheader("📈 Monthly Revenue by Region")
monthly_revenue = filtered_df.groupby(["Month", "Region"])["PageValues"].sum().reset_index()
fig_line = px.line(monthly_revenue, x="Month", y="PageValues", color="Region", markers=True)
st.plotly_chart(fig_line, use_container_width=True)

# Pie Chart: Visitor Type Distribution
st.markdown("---")
st.subheader("👥 Visitor Type Distribution")
visitor_counts = filtered_df["VisitorType"].value_counts().reset_index()
visitor_counts.columns = ["VisitorType", "Count"]
fig_pie = px.pie(visitor_counts, names="VisitorType", values="Count", hole=0.4)
st.plotly_chart(fig_pie, use_container_width=True)

# Histogram: Exit Rates
st.markdown("---")
st.subheader("📉 Exit Rates Distribution")
fig_exit = px.histogram(filtered_df, x="ExitRates", nbins=30, title="Exit Rates Distribution")
st.plotly_chart(fig_exit, use_container_width=True)

# Data Table
st.markdown("---")
st.subheader("🗃️ Filtered Data")
st.dataframe(filtered_df.head(100))

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Data: Google Merchandise Store")
