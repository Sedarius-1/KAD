
import pandas as pd
import scripts as scr

df = pd.read_csv('data.csv',
                 names=['1', '2', "3", '4', 'Gatunek'])

print(df)
df['Gatunek'].replace([0, 1, 2], ["setosa", "versicolor", "virginica"], inplace=True)
print(df)

types = ["setosa", "versicolor", "virginica"]

print(scr.counting(df, '1'))
print("max: ", scr.maximum(df, '1'))
print("min: ", scr.minimum(df, '1'))
print("sre: ", scr.mean(df, '1'))
print("med: ", scr.median(df, '1')[0])
print("deriv: ", scr.deriv(df, '1'))
print("q1: ", scr.quartile(df, '1')[0])
print("q3: ", scr.quartile(df, '1')[1])

scr.draw_multiple_histogram(df, '1', "Długość działki kielicha [cm]", types, "1m.jpg")
scr.draw_multiple_histogram(df, '2', "Szerokość działki kielicha [cm]", types, "2m.jpg")
scr.draw_multiple_histogram(df, '3', "Długość płatka [cm]", types, "3m.jpg")
scr.draw_multiple_histogram(df, '4', "Szerokość płatka [cm]", types, "4m.jpg")
