import streamlit as st
import pandas as pd
import numpy as np

# Set page title and favicon
st.set_page_config(page_title="Disease Surveillance System", page_icon=":microbe:")

# Set color palette
primary_color = "#472731"
secondary_color = "#282130"
accent_color = "#F18A85"
background_color = "#849DAB"
text_color = "#24788F"

# Set page layout
st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {background_color};
            color: {text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {primary_color};
        }}
        .btn-primary {{
            background-color: {accent_color};
            color: {text_color};
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

# Create header section
st.markdown(f"<h1 style='text-align: center; color: {accent_color};'>Disease Surveillance System</h1>", unsafe_allow_html=True)
st.write("This system monitors disease outbreaks and provides early warning to public health officials to help prevent the spread of infectious diseases.")

# Create data input section
st.subheader("Data Input")
data_file = st.file_uploader("Upload data file", type=["csv", "xlsx"])

if data_file is not None:
    data = pd.read_csv(data_file)

    # Create data summary section
    st.subheader("Data Summary")
    st.write("Here is a summary of the data:")
    st.write(data.describe())

    # Create data visualization section
    st.subheader("Data Visualization")
    chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart"])
    x_column = st.selectbox("Select x-axis column", data.columns)
    y_column = st.selectbox("Select y-axis column", data.columns)

    if chart_type == "Line Chart":
        st.line_chart(data[[x_column, y_column]])
    else:
        st.bar_chart(data[[x_column, y_column]])

    # Create analysis section
    st.subheader("Analysis")
    threshold = st.number_input("Enter outbreak threshold", value=10)
    outbreak_data = data[data[y_column] >= threshold]

    if len(outbreak_data) > 0:
        st.write("Outbreak detected!")
        st.write(outbreak_data)
    else:
        st.write("No outbreak detected.")
