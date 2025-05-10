import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

def create_interactive_scatter_plots(csv_filepath):
    """
    Creates interactive scatter plots from a given CSV file, allowing users
    to select the x and y axes features. Includes a regression line.

    Args:
        csv_filepath (str): The path to the CSV file.
    """
    try:
        df = pd.read_csv(csv_filepath)
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_filepath}'")
        return
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

    if not numerical_columns or len(numerical_columns) < 2:
        print("Error: The CSV file must contain at least two numerical columns to create scatter plots.")
        return

    x_dropdown = widgets.Dropdown(
        options=numerical_columns,
        description='X-axis:',
        disabled=False,
        style={'description_width': 'initial'}
    )

    y_dropdown = widgets.Dropdown(
        options=numerical_columns,
        description='Y-axis:',
        disabled=False,
        style={'description_width': 'initial'}
    )

    plot_button = widgets.Button(description="Generate Scatter Plot")
    output = widgets.Output()

    def plot_scatter(b):
        with output:
            output.clear_output()
            x_col = x_dropdown.value
            y_col = y_dropdown.value

            if x_col and y_col and x_col != y_col:
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x=df[x_col], y=df[y_col])
                sns.regplot(x=df[x_col], y=df[y_col], scatter=False, color='red')
                plt.title(f'Scatter Plot of {y_col} vs {x_col}')
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.grid(True)
                plt.show()
            elif x_col == y_col:
                print("Error: Please select different columns for X and Y axes.")
            else:
                print("Error: Please select columns for both X and Y axes.")

    plot_button.on_click(plot_scatter)

    display(x_dropdown, y_dropdown, plot_button, output)

if __name__ == '__main__':
    # Replace 'your_file.csv' with the actual path to your CSV file
    csv_file = 'your_file.csv'
    create_interactive_scatter_plots(csv_file)
