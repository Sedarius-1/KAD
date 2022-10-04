# import numpy as np
# import matplotlib as mat
import pandas as pd

df = pd.read_csv('data.csv',
                 names=['sepal length[cm]', 'sepal width[cm]', 'petal length[cm]', 'petal width[cm]', 'species'])

print(df)
df.replace([0,1,2],["setosa", "versicolor","virginica"], inplace=True)
print(df)
df_species_counts = df.species.value_counts().reset_index()
df_species_counts.columns = ["Gatunek", "Liczebność"]
print(df_species_counts.to_string(index=False))
