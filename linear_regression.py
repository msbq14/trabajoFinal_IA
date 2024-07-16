import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# Load the CSV file
df = pd.read_csv('monthly_date_counts.csv')

# Encode the months
le = LabelEncoder()
df['Fecha de creacion'] = le.fit_transform(df['Fecha de creacion'])

# Split the data
X = df['Fecha de creacion'].values.reshape(-1, 1)
x = df['Fecha de creacion'].values
y = df['Count'].values



model = np.poly1d(np.polyfit(x, y, 7))

line = np.linspace(0, 17, 30)

plt.scatter(x, y)
plt.plot(line, model(line), color='red')
plt.show()

