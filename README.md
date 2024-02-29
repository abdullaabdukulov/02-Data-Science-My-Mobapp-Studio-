   # 02-Data-Science-My-Mobapp-Studio

## Task

Welcome to the Mobile App Market Analysis project! In this project, we aim to provide insights into the Google Play Store's mobile app market, focusing on the Family category and Paid apps. The analysis covers various aspects such as market size, popular genres, installation statistics, and pricing.

## Description

As part of this project, we have implemented a Jupyter Notebook containing Python code for data loading, cleaning, analysis, and visualization. The project focuses on providing valuable insights into the mobile app market, aiding decision-making for the development of a new mobile app by My MobApp Studio.

## Installation

To run this project, you need to have Python installed on your system. Additionally, the following libraries are required and can be installed using the following commands:

```bash
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly
```

## Usage

1. **Load and Clean Data:**
   - Run the `load_dataset()` function to load the dataset.
   - Utilize the `clean_dataset(dataset)` function to clean the data, removing duplicates and transforming columns.

2. **Explore and Summarize Data:**
   - Gain an overview of the dataset using `print_summarize_dataset(dataset)`.
   - Visualize histograms with `print_histograms(dataset)` for key features like Rating, Reviews, Size, Installs, and Price.
   - Examine correlations between numeric features using `compute_correlations_matrix(dataset)`.

3. **Visualize Family Genre Popularity:**
   - Explore the popularity of paid apps in the Family category with `family_genre_popularity(dataset)`.

4. **Explore Additional Visualizations:**
   - Generate a scatter matrix of numeric variables using `print_scatter_matrix(dataset)`.

5. **Generate Blog Report:**
   - Use the insights gained to generate a scientific experiment-style blog report.
   - Create visualizations such as bar charts, pie diagrams, and arrays as outlined in the technical specification.