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
        arg = 1
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
    def count_occurences(arr, minimal, maximal, upper_bound, arg, step):
        """
        It takes an array of objects, a minimal value, a maximal value, an upper bound,
        an argument, and a step, and returns a dictionary of the number of occurences
        of each value in the array of objects

        :param arr: the array of objects
        :param minimal: the minimal value of the attribute you want to count
        :param maximal: the maximum value of the parameter you want to count
        :param upper_bound: the number of elements in the array
        :param arg: the attribute of the object you want to count
        :param step: the step size of the histogram
        :return: A dictionary with the keys being the values of
        the attribute and the values being the
        number of times that value appears in the array.
        """
        holder = {}
        for i in np.arange(minimal, maximal + 0.2, step):
            index = round(i, 1)
            holder.update([(str(index), 0)])
        for p in range(0, upper_bound):
            if str(round(getattr(arr[p], arg), 1)) in holder:
                holder[str(round(getattr(arr[p], arg), 1))] += 1
        return holder

    @staticmethod
    def find_max(arr, arg):
        """
        It takes an array of objects and an attribute name, and returns the value of the attribute of the last
        object in the sorted array

        :param arr: the array of objects
        :param arg: The name of the attribute to find the max of
        :return: The last element of the array.
        """
        return getattr(arr[-1], arg)

    @staticmethod
    def find_min(arr, arg):
        """
        It takes an array of objects and an attribute name, and returns the
        minimum value of that attribute in the sorted array

        :param arr: the array of objects
        :param arg: The name of the attribute you want to find the minimum of
        :return: The first element of the array.
        """
        return getattr(arr[0], arg)

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
        if upper_bound % 2 != 0:
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

    @staticmethod
    def find_average(arr, arg, upper_bound):
        """
        It takes an array of objects, an attribute of those objects, and an upper bound, and returns the average of that
        attribute for the first upper_bound objects in the array

        :param arr: the array of objects
        :param arg: the attribute of the object you want to find the average of
        :param upper_bound: the number of elements in the array to be averaged
        :return: The average of the attribute arg of the first upper_bound elements of the array arr.
        """
        avg = 0
        for i in range(0, upper_bound):
            avg += getattr(arr[i], arg)
        return avg / upper_bound

    def find_deviation(self, arr, arg, upper_bound):
        """
        It takes an array of objects, an attribute of those objects, and an upper bound,
        and returns the standard deviation of that attribute

        :param arr: the array of objects
        :param arg: the name of the attribute you want to find the average of
        :param upper_bound: the number of elements in the array to be considered
        :return: The standard deviation of the given attribute of the given array.
        """
        sum_dev = 0
        avg = self.find_average(arr, arg, upper_bound)
        for i in range(0, upper_bound):
            sum_dev = sum_dev + (getattr(arr[i], arg) - avg) * (getattr(arr[i], arg) - avg)
        return math.sqrt(sum_dev / upper_bound)

    def find_pcc(self, arr, arg1, arg2, upper_bound):
        """
        The function takes in an array of objects, the name of two attributes of those objects, and an upper bound.
        It then calculates the Pearson correlation coefficient between the two attributes

        :param arr: the array of objects
        :param arg1: The first argument to be compared
        :param arg2: The name of the second attribute to be compared
        :param upper_bound: the number of rows to be considered for the calculation of the PCC
        :return: The Pearson Correlation Coefficient (PCC) is being returned.
        """
        sum_upper = 0
        sum_lower_1 = 0
        sum_lower_2 = 0
        avg_x = self.find_average(arr, arg1, upper_bound)
        avg_y = self.find_average(arr, arg2, upper_bound)
        for i in range(0, upper_bound):
            sum_upper += ((getattr(arr[i], arg1) - avg_x) * (getattr(arr[i], arg2) - avg_y))
            sum_lower_1 += (getattr(arr[i], arg1) - avg_x) ** 2
            sum_lower_2 += (getattr(arr[i], arg2) - avg_y) ** 2
        pcc = sum_upper / (np.sqrt(sum_lower_1) * np.sqrt(sum_lower_2))
        return pcc

    def line_regression(self, arr, arg1, arg2, upper_bound):
        """
        It takes an array of objects, two arguments of those objects, and an upper bound, and returns the slope and
        y-intercept of the line of best fit

        :param arr: the array of objects
        :param arg1: the name of the first argument (e.g. "x")
        :param arg2: the name of the column that you want to predict
        :param upper_bound: the number of elements in the array to be used for the regression
        :return: The slope and the intercept of the regression line
        """
        sum_upper = 0
        sum_lower = 0
        avg_x = self.find_average(arr, arg1, upper_bound)
        avg_y = self.find_average(arr, arg2, upper_bound)
        for i in range(0, upper_bound):
            sum_upper += ((getattr(arr[i], arg1) - avg_x) * (getattr(arr[i], arg2) - avg_y))
            sum_lower += (getattr(arr[i], arg1) - avg_x) ** 2
        a = sum_upper / sum_lower
        b = avg_y - a * avg_x
        return a, b
