My_mobapp_studio

## Task

    1. Data Cleaning:
       - Conversion of 'Installs' column to numeric format.
       - Conversion of 'Size' column to numeric format, removing 'M', 'k', and 'Varies with device'.
       - Conversion of 'Price' column to numeric format.
       - Conversion of 'Reviews' column to numeric format.
       - Removal of '+' from 'Content Rating' column.

    2. Visualization:
       - Pie chart and bar chart for the distribution of app categories.
       - Count plot for the number of apps per category.
       - Bar plot showing categories with the highest prices.

    3. Correlation Analysis:
       - Correlation matrix heatmap showing the relationships between numeric columns.

    4. Scatter Matrix:
       - Scatter matrix showing pairwise relationships between numeric columns.

## Description

1.Data Loading and Cleaning:

-   The `load_dataset()` function loads the dataset from the 'googleplaystore.csv' file.
-   The `clean_dataset()` function performs necessary data cleaning tasks, such as converting columns to appropriate data types, handling missing values, and standardizing formats.

2.Data Visualization:

-   The `histograms()` function generates visualizations to explore the distribution of app categories, the number of apps per category, and categories with the highest prices.

3.Correlation Analysis:

-   The `correlations_matrix()` function creates a correlation matrix heatmap to visualize the relationships between numeric columns in the dataset.

4.Scatter Matrix:

-   The `scatter_matrix()` function displays a scatter matrix to visualize pairwise relationships between numeric columns.

## Installation

The load_dataset, clean_dataset, histograms, correlations_matrix, and scatter_matrix functions in the code are very convenient for analyzing multiple datasets, and these functions work with the pandas, numpy, matplotlib, and seaborn libraries. For this, it is required to install these libraries

## Usage

    - Ensure 'googleplaystore.csv' file is in the same directory.
    - Run the provided functions to analyze the dataset.

    Dependencies:
    - pandas
    - numpy
    - matplotlib
    - seaborn
