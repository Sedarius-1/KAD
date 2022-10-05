import math

import numpy as np


def index_to_name(arg):
    if arg == 0:
        arg = "setosa"
        return arg
    elif arg == 1:
        arg = "versicolor"
        return arg
    elif arg == 2:
        arg = "virginica"
        return arg

def name_to_index(arg):
    if arg == "setosa":
        arg = 0
        return arg
    elif arg == "versicolor":
        arg = 0
        return arg
    elif arg == "virginica":
        arg = 2
        return arg
class Flower:
    def __init__(self, s_length, s_width, p_length, p_width, species):
        self.s_length = s_length
        self.s_width = s_width
        self.p_length = p_length
        self.p_width = p_width
        self.species = species

    def print_info(self):
        self.species = index_to_name(self.species)
        print(f"Sepal length: {self.s_length}, Sepal width: {self.s_width}, "
              f"Petal length: {self.p_length}, Petal width: {self.p_width}, , Species: {self.species}")
        self.species = name_to_index(self.species)


class FlowerHolder:
    def __init__(self):
        self.list = []

    def append(self, item):
        self.list.append(item)

    def get_list(self):
        return self.list

    def count_occurences(self, arr,min, max, upper_bound, arg, step):
        holder= {}
        for i in np.arange(min,max,step):
            index=round(i,1)
            holder.update([(str(index),0)])
        for p in range(0, upper_bound):
            if str(round(getattr(arr[p],arg),1)) in holder:
                holder[str(round(getattr(arr[p],arg),1))] += 1
        return holder

    @staticmethod
    def find_max(arr, arg, upper_bound):
        temp = 0
        for i in range(0, upper_bound):
            if getattr(arr[i], arg) > temp:
                temp= getattr(arr[i], arg)
        return temp

    def find_min(self, arr, arg, upper_bound):
        temp = self.find_max(arr, arg, upper_bound)
        for i in range(0, upper_bound):
            if getattr(arr[i], arg) < temp:
                temp = getattr(arr[i], arg)
        return temp

    @staticmethod
    def median(arr, arg,upper_bound):
        median_index = math.ceil(upper_bound / 2)
        if median_index % 2 != 0:
            median_value = getattr(arr[median_index-1], arg)
            return median_index, median_value
        else:
            median_value = ((getattr(arr[median_index], arg)) + getattr(arr[median_index+1],arg)) / 2
            return median_index, median_value

    def quartile(self, arr, arg, upper_bound):
        middle = self.median(arr, arg, upper_bound)
        mid_index = middle[0]
        upper_bound = mid_index
        quart = self.median(arr, arg, upper_bound)
        if quart[0] % 2 == 0:
            quart_3_value = getattr(arr[(quart[0]*3)-2], arg)
            return quart[0], quart[1], ((quart[0] * 3)-1), quart_3_value
        else:
            quart_3_value = (getattr(arr[(quart[0]*3)-2],arg) + getattr(arr[quart[0]*3-1],arg)) / 2
            return quart[0], quart[1], quart[0] * 3, quart_3_value
