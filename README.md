# Welcome to My Mobapp Studio  
***  
  
## Task  
The task of this project is to analyze Google Play Store. We need to data to analyze the Market. And we use googleplaystore.csv. You can see explanation from [_**Blog Post**_](https://medium.com/@ahmadjonovbekmurod06/my-mobapp-studio-29b859f1948a).  
  
## Description  
  
`- load_dataset()`:  
Loads a CSV file as a dataset.  
`- print_summarize_dataset(dataset)`  
Returns whole information of dataset.  
`- clean_dataset(dataset)`  
Cleans the dataset(duplicates, Nan values and so on).  
`- print_histograms(dataset)`  
Displays histograms of dataset.  
`compute_correlations_matrix(dataset, columns=None)`  
Displays correlation map.  
`- top_apps_type(dataset)`  
Plots bar charts free and paid apps in given categories.  
`- paid_apps(dataset)`  
Displays a bar chart of Top paid apps in Family category.  
`- pie_installs(dataset)`  
Displays a pie chart showing the percentage of total installs by category.  
`- pie_category_apps(dataset)`  
Displays a pie chart for the top 10 categories to show total apps number.  
`- plot_bar_expensive_apps(dataset, top_n=15, palette='viridis')`  
Displays a barchart Top-N categories with paid apps.  
`- family_apps_ratings(dataset)`  
Plots a barchart for the Top-N family apps by reviews.  
  
  
## Installation  
No specific installtions except python. Necessary libraries in _Usage section_  
  
## Usage  
We use:  
- Pandas  
- Numpy  
- Matplotlib  
- Seaborn  
- Plotly  
  
So, you should import them.