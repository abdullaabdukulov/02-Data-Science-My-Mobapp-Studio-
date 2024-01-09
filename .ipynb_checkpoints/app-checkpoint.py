import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
    """Ma'lumotlar to'plamini yuklash"""
    df = pd.read_csv('googleplaystore.csv')
    return df

def print_summarize_dataset(dataset):
    """Ma'lumotlar to'plamining tavsifi"""
    print(dataset.describe(include='all'))

def clean_dataset(dataset):
    """Ma'lumotlar to'plamini tozalash"""
    dataset.drop_duplicates(inplace=True)
    dataset.dropna(inplace=True)

def print_histograms(dataset):
    """Ma'lumotlar to'plamining istoriyalarini chizish"""
    dataset.hist(figsize=(15, 10), bins=20)
    plt.show()

def compute_correlations_matrix(dataset):
    """Ma'lumotlar to'plamining ta'riflar matritsasi"""
    corr = dataset.corr()
    print(corr)

def print_scatter_matrix(dataset):
    """Ma'lumotlar to'plamining scatter matritsasi"""
    pd.plotting.scatter_matrix(dataset, figsize=(15,15))
    plt.show()

# Ma'lumotlar to'plamini yuklab olish
df = pd.read_csv('googleplaystore.csv')

# Family kategoriyasidagi eng mashhur to'lovli ilovalar
top_family_paid_apps = df[(df['Category'] == 'FAMILY') & (df['Type'] == 'Paid')].sort_values('Installs', ascending=False).head(10)
plt.figure(figsize=(15, 10))
plt.bar(top_family_paid_apps['App'], top_family_paid_apps['Installs'])
plt.xticks(rotation=90)
plt.xlabel('App name')
plt.ylabel('Installs')
plt.title('Family Category')
plt.show()


# To'lovli oila kategoriyasiga o'rnatilgan o'yin janrlari bo'yicha yuklamalar son

# Data Setni o'qish
df = pd.read_csv('googleplaystore.csv')

# to'lovli ilovalarning soni bo'yicha bo'limlash
df_paid = df[df['Type'] == 'Paid']
downloads_per_genre = df_paid.groupby(['Category'])['Installs'].sum().sort_values(ascending=False)

downloads_per_genre = df[df['Category'] == 'FAMILY']['Installs'].value_counts()

downloads_per_genre = downloads_per_genre.apply(lambda x: int(x.replace('+', '').replace(',', '')) if isinstance(x, str) else x)


# Pie diagrammani yaratish
plt.pie(downloads_per_genre, labels=downloads_per_genre.index, autopct='%1.1f%%')
plt.title('Family kategoriyasiga tegishli to\'lovli o\'yinlar bo\'yicha yuklamalar soni')
plt.show()

# import pandas as pd

# Load the dataset
dataset = pd.read_csv('googleplaystore.csv')

# Define the function to get installs by category
def get_installs_by_category(dataset):
    installs_by_category = {}
    for row in dataset[1:]:
        category = row[1]
        try:
            installs = int(row[5].replace('+', '').replace(',', ''))
        except ValueError:
            continue
        if category in installs_by_category:
            installs_by_category[category] += installs
        else:
            installs_by_category[category] = installs
    return installs_by_category
# import pandas as pd
# import matplotlib.pyplot as plt

dataset = pd.read_csv("googleplaystore.csv")

categories = dataset['Category'].unique()

installations_by_category = [sum(int(installs.replace('+', '').replace(',', '')) for installs in dataset[(dataset['Category']==category) & (~dataset['Installs'].str.contains("00000000000000000000000000000000000000000000000000000"))]['Installs'] if installs != 'Free') for category in categories]
plt.pie(installations_by_category, labels=categories, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

categories = dataset['Category'].unique()





mean_price_by_category = [pd.to_numeric(dataset[dataset['Category']==category]['Price'], errors='coerce').mean() for category in categories]

dataset = dataset[pd.to_numeric(dataset['Price'], errors='coerce').notnull()]

plt.bar(categories, mean_price_by_category)

plt.xticks(rotation=90)
plt.xlabel('Kategoriyalar')
plt.ylabel("O'rtacha narx")
plt.title("Kategoriya bo'yicha o'rtacha narxlar")

plt.title("Rating")
plt.hist(dataset["Rating"])
plt.text(2.7, 4150, 'The highest indicator')
plt.grid(True)
plt.show()
