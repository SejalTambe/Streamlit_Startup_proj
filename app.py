import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

# Title and description
st.title("Data Analytics Dashboard")
st.write("Upload a dataset and explore its contents!")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Data exploration and visualization
if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)

    # Show dataset summary
    st.subheader("Dataset Summary")
    st.write(df.head())  # Display first few rows
    st.write(f"Shape of the dataset: {df.shape}")  # Display number of rows and columns

    # Display descriptive statistics
    st.subheader("Descriptive Statistics")
    st.write(df.describe())  # Display basic statistics

    # Data visualization
    st.subheader("Data Visualization")

    # Scatter plot
    st.write("### Scatter Plot")
    scatter_x = st.selectbox("Select x-axis:", options=df.columns, index=0)
    scatter_y = st.selectbox("Select y-axis:", options=df.columns, index=1)
    scatter_fig = px.scatter(df, x=scatter_x, y=scatter_y)
    st.plotly_chart(scatter_fig)

    # Histogram
    st.write("### Histogram")
    hist_col = st.selectbox("Select a column for histogram:", options=df.columns, index=0)
    hist_fig = px.histogram(df, x=hist_col)
    st.plotly_chart(hist_fig)

    # Bar chart
    st.write("### Bar Chart")
    bar_col = st.selectbox("Select a column for bar chart:", options=df.columns, index=0)

    # Check if a column is selected for the bar chart
    if bar_col:
        # Count occurrences of each category in the selected column
        bar_data = df[bar_col].value_counts().reset_index()
        bar_data.columns = [bar_col, 'Count']

        # Create bar chart using Plotly Express
        bar_fig = px.bar(bar_data, x=bar_col, y='Count', title=f"Bar Chart of {bar_col}")
        st.plotly_chart(bar_fig)
    else:
        st.write("Please select a column to generate the bar chart.")

    # Pie chart
    st.write("### Pie Chart")
    pie_col = st.selectbox("Select a column for pie chart:", options=df.columns, index=0)

    # Check if a column is selected for the pie chart
    if pie_col:
        # Count occurrences of each category in the selected column
        pie_data = df[pie_col].value_counts().reset_index()
        pie_data.columns = [pie_col, 'Count']

        # Create pie chart using Plotly Express
        pie_fig = px.pie(pie_data, values='Count', names=pie_col, title=f"Pie Chart of {pie_col}")
        st.plotly_chart(pie_fig)
    else:
        st.write("Please select a column to generate the pie chart.")

    # Downloadable data
    st.sidebar.markdown("---")
    st.sidebar.subheader("Download Data")
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.sidebar.download_button("Download CSV", csv_data, "data.csv", "text/csv")
