def detect_duplicate(dataset, column = 'App'):
    store = []
    detected = []
    n = 0
    for app in dataset[column]:
        if app in store:
            n+=1
            detected.append(app)
        store.append(app)
    print(f"Detected {n} element")
    return detected


def replace_column(dataset, column = None, match = None):
    for key, value in match.items():
        dataset.loc[:, column] = dataset[column].str.replace(key, value)
    
    #display(dataset[column].unique())
    return dataset

def calculate_installs(columns = None):
    result = []
    for column in columns:
        summ = dataset['Installs'][dataset['Category'] == column].sum()
        result.append(summ)
    return result

def calculate_free(column):
    count = column.value_counts()
    free = count[1]
    paied = count[0]
    return free, paied