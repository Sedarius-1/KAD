# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv',
                 names=['1', '2', "3", '4', 'Gatunek'])

print(df)
df['Gatunek'].replace([0, 1, 2], ["setosa", "versicolor", "virginica"], inplace=True)
print(df)
df_species_counts = df.Gatunek.value_counts().reset_index()
df_species_counts.columns = ["Gatunek", "Liczebność"]
print(df_species_counts.to_string(index=False))
dl = df['1'].loc[df.Gatunek=="setosa"].astype(float)
print(dl.dtypes)
dl.hist(label='setosa')
dl = df['1'].loc[df.Gatunek=="versicolor"].astype(float)
print(dl)
dl.hist(label='versicolor')
dl = df['1'].loc[df.Gatunek=="virginica"].astype(float)
print(dl.dtypes)
dl.hist(label='virginica')
plt.ylabel('Liczebność')
plt.xlabel('Szerokość [cm]')

plt.legend()
plt.savefig('hist1.pdf')