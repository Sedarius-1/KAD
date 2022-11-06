import pandas as pd

import classes
import scripts as scr

df = pd.read_csv('data.csv', names=['s_length', 's_width', "p_length", 'p_width', '5'])

flower_holder = classes.FlowerHolder()
holders = []
for i in range(0, 3):
    holders.append(classes.FlowerHolder())
upper_bound = len(df)
# This is creating a list of flowers and appending them to a list of flower holders.
for i in range(0, upper_bound):
    flower = classes.Flower(df.iloc[i])
    flower_holder.append(flower)
    holders[int(flower.species)].append(flower)

flower_args = {'s_length': "Sepal length", 's_width': "Sepal width", 'p_length': "Petal length",
               'p_width': "Petal width"}
scr.structure(flower_args)
scr.assignment_1(flower_holder, flower_args, upper_bound, holders)
#scr.assignment_2(flower_holder, flower_args, upper_bound)
