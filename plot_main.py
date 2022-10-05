import csv
import pandas as pd
import scripts as scr

df = pd.read_csv('data.csv',
                 names=['1', '2', "3", '4', 'Gatunek'])

print(df)
df['Gatunek'].replace([0, 1, 2], ["setosa", "versicolor", "virginica"], inplace=True)
print(df)

types = ["setosa", "versicolor", "virginica"]
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

scr.draw_multiple_histogram(df, '1', "Długość działki kielicha [cm]", types, "1m.jpg")
scr.draw_multiple_histogram(df, '2', "Szerokość działki kielicha [cm]", types, "2m.jpg")
scr.draw_multiple_histogram(df, '3', "Długość płatka [cm]", types, "3m.jpg")
scr.draw_multiple_histogram(df, '4', "Szerokość płatka [cm]", types, "4m.jpg")
