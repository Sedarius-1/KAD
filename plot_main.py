import pandas as pd
import scripts as scr
import classes

def draw_hist(a, param, upper_bound):
    a.list = sorted(a.list, key=lambda x: getattr(x, param))
    dict = a.count_occurences(a.list,a.find_min(a.list, param, upper_bound), a.find_max(a.list, param, upper_bound),upper_bound, param, 0.1)
    scr.draw_histogram(dict,a.find_min(a.list, param, upper_bound), a.find_max(a.list, param, upper_bound), '1', param+'.pdf')

df = pd.read_csv('data.csv',
                 names=['1', '2', "3", '4', '5'])

# print(scr.counting(df, '1'))
# print("max: ", scr.maximum(df, '1'))
# print("min: ", scr.minimum(df, '1'))
# print("sre: ", scr.mean(df, '1'))
# print("med: ", scr.median(df, '1')[0])
# print("deriv: ", scr.deriv(df, '1'))
# print("q1: ", scr.quartile(df, '1')[0])
# print("q3: ", scr.quartile(df, '1')[1])
#

# scr.draw_multiple_histogram(df, '2', "Szerokość działki kielicha [cm]", types, "2m.jpg")
# scr.draw_multiple_histogram(df, '3', "Długość płatka [cm]", types, "3m.jpg")
# scr.draw_multiple_histogram(df, '4', "Szerokość płatka [cm]", types, "4m.jpg")

a = classes.FlowerHolder()
upper_bound = len(df)
for i in range(0, upper_bound):
    flower = classes.Flower(df['1'][i], df['2'][i], df['3'][i], df['4'][i], df['5'][i])
    a.append(flower)

a.list = sorted(a.list, key=lambda x: x.s_length)
for i in range(0, upper_bound):
    a.list[i].print_info()
flower_args = {'s_length': "Sepal length", 's_width': "Sepal width", 'p_length': "Petal length",
               'p_width': "Petal width"}
for i in flower_args:
    a.list = sorted(a.list, key=lambda x: getattr(x, i))
    # for c in range(0, upper_bound):
    #     a.list[c].print_info()
    print(f"Max value of {flower_args[i]} is {a.find_max(a.list, i, upper_bound)}")
    print(f"Min value of {flower_args[i]} is {a.find_min(a.list, i, upper_bound)}")
    print(
        f"Median value of {flower_args[i]} is {a.median(a.list, i, upper_bound)[1]}, index:{a.median(a.list, i, upper_bound)[0]}")
    print(
        f"Quartile values of {flower_args[i]} are (Q1): {(a.quartile(a.list, i, upper_bound))[1]}, index: {(a.quartile(a.list, i, upper_bound))[0]} "
        f"and (Q3): {(a.quartile(a.list, i, upper_bound))[3]}, index:{(a.quartile(a.list, i, upper_bound))[2]} ")


for i in flower_args:
    draw_hist(a,i, upper_bound)