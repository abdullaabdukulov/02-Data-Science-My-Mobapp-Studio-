def detect_duplicate(dataset, column = 'App'):
    magazine = []
    disclosed = []
    n = 0
    for app in dataset[column]:
        if app in magazine:
            n+=1
            disclosed.append(app)
        magazine.append(app)
    print(f"Detected {n} element")
    return disclosed


def replace_column(dataset, column = None, match = None):
    for key, value in match.items():
        dataset.loc[:, column] = dataset[column].str.replace(key, value)
    return dataset

def calculate_installs(columns = None):
    outcome = []
    for column in columns:
        amounts = dataset['Installs'][dataset['Category'] == column].sum()
        outcome.append(amounts)
    return outcome

def calculate_free(column):
    count = column.value_counts()
    free = count[1]
    paied = count[0]
    return free, paied