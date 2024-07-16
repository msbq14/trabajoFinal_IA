import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the CSV file
df = pd.read_csv('dataset_2023_2024.csv', delimiter=';')

dates = df['Fecha de creacion'].unique()
months = [date.split('/')[1:3] for date in dates]
months = [f'{month}/{year}' for month, year in months]
months = sorted(list(set(months)))

# # count the number of entries for each date in the dataset and save em all in a csv with the dates and the counts
date_counts = []
for month in months:
    count = df[df['Fecha de creacion'].str.contains(month)].shape[0]
    date_counts.append([month, count])

date_counts = pd.DataFrame(date_counts, columns=['Fecha de creacion', 'Count'])
date_counts.to_csv('monthly_date_counts.csv', index=False)
