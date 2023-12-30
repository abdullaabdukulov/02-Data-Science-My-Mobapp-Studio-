# My MobApp Studio

## Task
The program aims to retrieve and analyze information about mobile applications from the Google Play Store. It provides various functionalities for data cleaning, summarization, and visualization.

## Description
The code includes a set of functions to perform tasks such as loading the dataset, cleaning the data, and generating visualizations. It utilizes popular Python libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn` for effective data manipulation and visualization.

## Installation
No specific installation is required for this program. Ensure that you have Python installed, along with the necessary libraries mentioned in the code.

## Usage
1. **`load_dataset()`**: Loads a CSV file containing Google Play Store data and returns a `pandas` DataFrame.
2. **`print_summarize_dataset(dataset)`**: Prints general information and the first 10 rows of the dataset.
3. **`clean_dataset(dataset)`**: Cleans and preprocesses the dataset, handling duplicates, incorrect categories, and missing values.
4. **`print_histograms(dataset)`**: Displays histograms for key numerical columns in the dataset.
5. **`compute_correlations_matrix(dataset, columns=None)`**: Plots a heatmap of the correlation matrix for selected columns.
6. **`top_apps_type(dataset)`**: Plots bar charts illustrating the count of free and paid apps in specific categories.
7. **`paid_apps(dataset)`**: Displays a horizontal bar chart of the top 20 paid apps in the "Family" category.
8. **`pie_installs(dataset)`**: Displays a pie chart showing the percentage of total installs by category.
9. **`pie_category_apps(dataset)`**: Displays a pie chart showing the number of apps in the top 10 categories.
10. **`plot_bar_expensive_apps(dataset, top_n=15, palette='viridis')`**: Plots a bar chart of the average prices for the top N categories with expensive (paid) apps.
11. **`family_apps_ratings(dataset)`**: Displays a bar chart of the top N family apps by reviews.

For more details, check out my blog post https://medium.com/@muhammadaminsidiko6/my-mobapp-studio-b28620455faf.

