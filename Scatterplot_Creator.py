import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_streamlit_scatter_plot(csv_filepath):
    """
    Creates an interactive scatter plot using Streamlit.

    Args:
        csv_filepath (str): The path to the CSV file.
    """
    try:
        df = pd.read_csv(csv_filepath)
    except FileNotFoundError:
        st.error(f"Error: CSV file not found at '{csv_filepath}'")
        return
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        return

    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

    if not numerical_columns or len(numerical_columns) < 2:
        st.error("Error: The CSV file must contain at least two numerical columns.")
        return

    st.title("Interactive Scatter Plot")

    x_axis = st.selectbox("Select X-axis:", numerical_columns)
    y_axis = st.selectbox("Select Y-axis:", numerical_columns)

    if x_axis and y_axis and x_axis != y_axis:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df[x_axis], y=df[y_axis])
        sns.regplot(x=df[x_axis], y=df[y_axis], scatter=False, color='red')
        plt.title(f'Scatter Plot of {y_axis} vs {x_axis}')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.grid(True)
        st.pyplot()
    elif x_axis == y_axis and x_axis is not None:
        st.warning("Please select different columns for X and Y axes.")
    elif not x_axis or not y_axis:
        st.info("Select columns for both X and Y axes to generate the plot.")

if __name__ == '__main__':
    # Replace 'your_file.csv' with the actual path to your CSV file
    csv_file = 'your_file.csv'
    create_streamlit_scatter_plot(csv_file)
