import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Kenya Census Data Dashboard", layout="wide")

st.title("🇰🇪 Kenya Census Data Science Dashboard")
st.markdown("An interactive web application exploring the 2019 Kenya population census data.")

# Load our analyzed dataset
df = pd.read_csv('kenya_population_analyzed.csv')

# Sidebar Controls
st.sidebar.header("Dashboard Filters")
min_pop = st.sidebar.slider(
    "Filter by Minimum Population", 
    min_value=0, 
    max_value=int(df['T_TL'].max()), 
    value=1000000, 
    step=100000
)

# Filter Data based on slider
filtered_df = df[df['T_TL'] >= min_pop]

# Main Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Counties Shown", len(filtered_df))
col2.metric("Total Population in View", f"{filtered_df['T_TL'].sum():,.0f}")
col3.metric("Max Population", f"{filtered_df['T_TL'].max():,.0f}")

st.markdown("---")

# Display Interactive Data Table
st.subheader("📊 Filtered County Data Table")
st.dataframe(filtered_df[['ADM1_NAME', 'T_TL', 'population_share_%']], use_container_width=True)

# Display Dynamic Bar Chart
st.subheader("📈 Population Visualization")
chart_data = filtered_df.set_index('ADM1_NAME')['T_TL'] / 1_000_000
st.bar_chart(chart_data)