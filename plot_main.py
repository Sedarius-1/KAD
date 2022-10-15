import pandas as pd

import classes
import scripts as scr

df = pd.read_csv('data.csv',
                 names=['s_length', 's_width', "p_length", 'p_width', '5'])

a = classes.FlowerHolder()
holders = []
for i in range(0, 3):
    holders.append(classes.FlowerHolder())
upper_bound = len(df)
for i in range(0, upper_bound):
    flower = classes.Flower(df.iloc[i])
    a.append(flower)
    holders[int(flower.species)].append(flower)

output = {"Value":[],"Max":[],"Min":[],"Median":[],"Q1":[],"Q3":[]}
o_formatted = pd.DataFrame(output)

flower_args = {'s_length': "Sepal length", 's_width': "Sepal width", 'p_length': "Petal length",
               'p_width': "Petal width"}
for i in flower_args:
    a.list = sorted(a.list, key=lambda x: getattr(x, i))
    print(f"Max value of {flower_args[i]} is {a.find_max(a.list, i, upper_bound)}")
    print(f"Min value of {flower_args[i]} is {a.find_min(a.list, i, upper_bound)}")
    print(
        f"Median value of {flower_args[i]} is {a.median(a.list, i, upper_bound)[1]}, "
        f"index:{a.median(a.list, i, upper_bound)[0]}")
    print(
        f"Quartile values of {flower_args[i]} are (Q1): {(a.quartile(a.list, i, upper_bound))[1]}, "
        f"index: {(a.quartile(a.list, i, upper_bound))[0]} "
        f"and (Q3): {(a.quartile(a.list, i, upper_bound))[3]}, "
        f"index:{(a.quartile(a.list, i, upper_bound))[2]} ")
    data_row = [flower_args[i], a.find_max(a.list, i, upper_bound), a.find_min(a.list, i, upper_bound),
                a.median(a.list, i, upper_bound)[1],
                (a.quartile(a.list, i, upper_bound))[1], (a.quartile(a.list, i, upper_bound))[3]]
    scr.plot_hist(a, i, upper_bound, flower_args[i])
    new_holders = scr.sort_holders_by_param(holders, i)
    scr.plot_multiple_hist(new_holders, i, flower_args[i])
    scr.draw_box_plot(df, flower_args, i)
    o_formatted.loc[len(o_formatted)] = data_row

print(o_formatted.to_string(index=False))
