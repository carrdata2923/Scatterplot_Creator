import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_interactive_scatter_plot():
    """
    Creates an interactive scatter plot using Streamlit, allowing users
    to upload their own CSV file.
    """
    st.title("Interactive Scatter Plot")

    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("CSV file uploaded successfully!")

            numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

            if not numerical_columns or len(numerical_columns) < 2:
                st.error("Error: The CSV file must contain at least two numerical columns.")
                return

            x_axis = st.selectbox("Select X-axis:", numerical_columns)
            y_axis = st.selectbox("Select Y-axis:", numerical_columns)

            if st.button("Generate Scatter Plot"):
                if x_axis and y_axis and x_axis != y_axis:
                    plt.figure(figsize=(20, 12))
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

        except pd.errors.EmptyDataError:
            st.error("Error: The uploaded CSV file is empty.")
        except pd.errors.ParserError:
            st.error("Error: Could not parse the CSV file. Please ensure it's a valid CSV format.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    create_interactive_scatter_plot()
