import pandas as pd
import plotly.express as px
import streamlit as st
from colorthief import ColorThief

# Load data (ensure correct path)
df = pd.read_csv("alcohol_consumption_data.csv")

# Create interactive bar chart with select box
st.header("Bar Chart with Select Box")
country_options = df["Entity"].unique()
selected_country = st.selectbox("Select Country:", country_options)
filtered_df = df[df["Entity"] == selected_country]
bar_chart = px.bar(filtered_df, x="Year", y="Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)", color="Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)", barmode="group")
st.plotly_chart(bar_chart)

# Create line chart with interactive color picker
st.header("Line Chart with Color Picker")
entity_options = df["Entity"].unique()
selected_entity = st.selectbox("Select Entity:", entity_options)
filtered_df_1 = df[df["Entity"] == selected_entity]

# Define color picker and get selected color
selected_color = st.color_picker("Select Line Color:", "#00f900")

# Create line chart with color
line_chart = px.line(
    filtered_df_1,
    x="Year",
    y="Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)",
)
line_chart.update_traces(line_color=selected_color)

line_chart.update_layout(
    title="Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)",
    xaxis_title="Year",
    yaxis_title="Consumption (Liters)",
)
st.plotly_chart(line_chart)


# Add download functionality
st.header("Download Files")
st.download_button("Download Bar Chart Data", data=filtered_df.to_csv(), file_name="bar_chart_data.csv")
st.download_button("Download Heatmap Data", data=heatmap_data.to_csv(), file_name="heatmap_data.csv")



