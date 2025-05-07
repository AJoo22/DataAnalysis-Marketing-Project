import streamlit as st
import time
import pandas as pd
import numpy as np

# App Configuration
st.set_page_config(page_title="Marketing Insights Dashboard", page_icon="📊", layout="centered")

# Header
st.title("📊 Welcome to the Marketing Insights Dashboard")
st.subheader("Powered by Data. Driven by Insights.")

# Description
st.markdown("""
Please wait while we prepare your data analysis report.
This may take a few moments depending on the data size and complexity.
""")

# Simulated Loading
with st.spinner('Crunching the numbers...'):
    time.sleep(4)  # simulate data loading

# Success message
st.success("✅ Your report is ready! Scroll down to explore insights.")

# Example KPIs
st.header("🔍 Key Marketing Metrics")
st.metric("Conversion Rate", "4.2%", "+0.6% from last month")
st.metric("Ad Spend ROI", "3.8x", "+15% YoY")
st.metric("Customer Retention", "82%", "↑ steady")

# Example DataFrame
st.header("📈 Sample Data Overview")
data = pd.DataFrame({
    'Channel': ['Email', 'Social Media', 'Paid Ads', 'Organic Search'],
    'Leads': [120, 300, 250, 180],
    'Conversions': [24, 45, 37, 28],
    'Conversion Rate': [20, 15, 14.8, 15.6]
})
st.dataframe(data)

# Optional: Refresh or Upload Buttons
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()
