import csv
import pandas as pd
import scripts as scr
df = pd.read_csv('data.csv',
                 names=['1', '2', "3", '4', 'Gatunek'])

print(df)
df['Gatunek'].replace([0, 1, 2], ["setosa", "versicolor", "virginica"], inplace=True)
print(df)

#df_species_counts = df.Gatunek.value_counts().reset_index()
#df_species_counts.columns = ["Gatunek", "Liczebność"]

#scr.multiple_histogram(df, '1', "Długość działki kielicha [cm]", "multi_histogram1.pdf")
#scr.multiple_histogram(df, '2', "Szerokość działki kielicha [cm]", "multi_histogram2.pdf")
#scr.multiple_histogram(df, '3', "Długość płatka [cm]", "multi_histogram3.pdf")
#scr.multiple_histogram(df, '4', "Szerokość płatka [cm]", "multi_histogram4.pdf")

list = []
with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        list.append(row[0])
final = [float(i) for i in list]

print("max: ", scr.maximum(final))
print("min: ", scr.minimum(final))
print("sre: ", scr.mean(final, len(final)))
print("med: ", scr.median(final))
print("deriv: ", scr.deriv(final))