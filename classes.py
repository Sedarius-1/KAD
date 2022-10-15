import math

import numpy as np


def index_to_name(arg):
    """
    It takes an integer as an argument and returns the name of the iris species that corresponds to that integer

    :param arg: the index of the predicted class
    :return: The name of the flower.
    """
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
    """
    It takes a string as an argument and returns an integer

    :param arg: the name of the flower
    :return: The index of the flower name.
    """
    if arg == "setosa":
        arg = 0
        return arg
    elif arg == "versicolor":
        arg = 0
        return arg
    elif arg == "virginica":
        arg = 2
        return arg


# The Flower class takes in a list of 5 elements, and assigns the first 4 elements to the attributes s_length, s_width,
# p_length, and p_width. The last element is assigned to the attribute species
class Flower:
    def __init__(self, df):
        self.s_length = df[0]
        self.s_width = df[1]
        self.p_length = df[2]
        self.p_width = df[3]
        self.species = df[4]

    def print_info(self):
        """
        This function takes in an instance of the Iris class and prints out the sepal length, sepal width, petal length,
        petal width, and species of the instance
        """
        self.species = index_to_name(self.species)
        print(f"Sepal length: {self.s_length}, Sepal width: {self.s_width}, "
              f"Petal length: {self.p_length}, Petal width: {self.p_width}, , Species: {self.species}")
        self.species = name_to_index(self.species)


# It's a class that holds a list of flowers, and has methods that
# can be used to find the median, quartile, and count the occurences of a certain attribute of the flowers in the list.
def count_occurences(arr, minimal, maximal, upper_bound, arg, step):
    """
    It takes an array of objects, a minimal value, a maximal value, an upper bound, an argument, and a step, and returns
    a dictionary of the number of occurences of each value in the array of objects

    :param arr: the array of objects
    :param minimal: the minimal value of the attribute you want to count
    :param maximal: the maximum value of the parameter you want to count
    :param upper_bound: the number of elements in the array
    :param arg: the attribute of the object you want to count
    :param step: the step size of the histogram
    :return: A dictionary with the keys being the values of the attribute and the values being the number of times that
    value appears in the array.
    """
    holder = {}
    for i in np.arange(minimal, maximal+0.2, step):
        index = round(i, 1)
        holder.update([(str(index), 0)])
    for p in range(0, upper_bound):
        if str(round(getattr(arr[p], arg), 1)) in holder:
            holder[str(round(getattr(arr[p], arg), 1))] += 1
    return holder


class FlowerHolder:
    def __init__(self):
        self.list = []

    def append(self, item):
        """
        Append the item to the list.

        :param item: The item to be appended to the list
        """
        self.list.append(item)

    def get_list(self):
        """
        It returns the list attribute of the object
        :return: The list is being returned.
        """
        return self.list

    @staticmethod
    def find_max(arr, arg, upper_bound):
        """
                It takes an array of objects, an attribute of those objects, and an upper bound, and returns the maximum
                value of that attribute in the array

                :param arr: the array of objects
                :param arg: the attribute of the object you want to find the max of
                :param upper_bound: the number of elements in the array
                :return: The maximum value of the attribute arg in the array arr.
                """
        temp = 0
        for i in range(0, upper_bound):
            if getattr(arr[i], arg) > temp:
                temp = getattr(arr[i], arg)
        return temp

    def find_min(self, arr, arg, upper_bound):
        """
        It finds the minimum value of a given attribute in a given array.

        :param arr: the array of objects
        :param arg: the attribute of the object you want to find the max/min of
        :param upper_bound: the number of elements in the array
        :return: The minimum value of the attribute arg in the array arr.
        """
        temp = self.find_max(arr, arg, upper_bound)
        for i in range(0, upper_bound):
            if getattr(arr[i], arg) < temp:
                temp = getattr(arr[i], arg)
        return temp

    @staticmethod
    def median(arr, arg, upper_bound):
        """
        The function takes in an array, an argument, and an upper bound. It then calculates the median index and median
        value of the array

        :param arr: the array of objects
        :param arg: the attribute of the object that we want to sort by
        :param upper_bound: the upper bound of the array
        :return: The median index and the median value.
        """
        median_index = math.ceil(upper_bound / 2)
        if median_index % 2 != 0:
            median_value = getattr(arr[median_index - 1], arg)
            return median_index, median_value
        else:
            median_value = ((getattr(arr[median_index], arg)) + getattr(arr[median_index + 1], arg)) / 2
            return median_index, median_value

    def quartile(self, arr, arg, upper_bound):
        """
        The function takes in an array, an argument, and an upper bound. It then finds the median of the array, and then
        finds the median of the array up to the upper bound. It then returns the index of the median, the value of the
        median, the index of the third quartile, and the value of the third quartile

        :param arr: the array of objects
        :param arg: the attribute of the object you want to sort by
        :param upper_bound: the upper bound of the array
        :return: The median, the median value, the index of the median, and the value of the third quartile.
        """
        middle = self.median(arr, arg, upper_bound)
        mid_index = middle[0]
        upper_bound = mid_index
        quart = self.median(arr, arg, upper_bound)
        if quart[0] % 2 == 0:
            quart_3_value = getattr(arr[(quart[0] * 3) - 2], arg)
            return quart[0], quart[1], ((quart[0] * 3) - 1), quart_3_value
        else:
            quart_3_value = (getattr(arr[(quart[0] * 3) - 2], arg) + getattr(arr[quart[0] * 3 - 1], arg)) / 2
            return quart[0], quart[1], quart[0] * 3, quart_3_value
