import os

import pandas as pd
from matplotlib import pyplot as plt

import classes


def structure(flower_args):
    if not os.path.exists("output"):
        os.makedirs("output")
    if not os.path.exists("output/assignment_1"):
        os.makedirs("output/assignment_1")
    for i in flower_args:
        if not os.path.exists(f"output/assignment_1/{i}"):
            os.makedirs(f"output/assignment_1/{i}")
        continue
    if not os.path.exists("output/assignment_2"):
        os.makedirs(f"output/assignment_2")


def assignment_1(a, flower_args, upper_bound, holders):
    print("ASSIGNMENT 1\n")
    output = {"Value": [], "Min": [], "Avarage": [], "Standard Deviation": [], "Median": [], "Q1": [], "Q3": [],
              "Max": []}
    o_formatted = pd.DataFrame(output)
    for i in flower_args:
        a.list = sorted(a.list, key=lambda x: getattr(x, i))
        print(f"Max value of {flower_args[i]} is {a.find_max(a.list, i)}")
        print(f"Min value of {flower_args[i]} is {a.find_min(a.list, i)}")
        print(f"Avg value of {flower_args[i]} is {round(a.find_average(a.list, i, upper_bound), 2)}")
        print(f"Standard Deviation value of {flower_args[i]} is {round(a.find_deviation(a.list, i, upper_bound), 2)}")
        print(
            f"Median value of {flower_args[i]} is {a.median(a.list, i, upper_bound)[1]}, "
            f"index:{a.median(a.list, i, upper_bound)[0]}")
        print(
            f"Quartile values of {flower_args[i]} are (Q1): {(a.quartile(a.list, i, upper_bound))[1]}, "
            f"index: {(a.quartile(a.list, i, upper_bound))[0]} "
            f"and (Q3): {(a.quartile(a.list, i, upper_bound))[3]}, "
            f"index:{(a.quartile(a.list, i, upper_bound))[2]} ")
        print("")
        data_row = [flower_args[i], a.find_min(a.list, i),
                    round(a.find_average(a.list, i, upper_bound), 2),
                    round(a.find_deviation(a.list, i, upper_bound), 2), a.median(a.list, i, upper_bound)[1],
                    (a.quartile(a.list, i, upper_bound))[1], (a.quartile(a.list, i, upper_bound))[3],
                    a.find_max(a.list, i)]
        plot_hist(a, i, upper_bound, flower_args[i])
        new_holders = sort_holders_by_param(holders, i)
        plot_multiple_hist(new_holders, i, flower_args[i])
        draw_box_plot_obj(new_holders, i, flower_args[i])
        o_formatted.loc[len(o_formatted)] = data_row
    print(o_formatted.to_string(index=False))


def assignment_2(flower_holder, flower_args, upper_bound):
    print("\nASSIGNMENT 2\n")
    for i in range(0, 4):
        for p in range(i + 1, 4):
            scatter_plot(flower_holder, flower_args, i, p, upper_bound)


def plot_hist(a, param, upper_bound, label):
    """
    It takes a list of objects, a parameter of those objects,
    an upper bound for the parameter, and a label for the histogram, and then it plots a histogram of the parameter
    for the objects in the list.

    :param a: the list of objects
    :param param: the parameter you want to plot
    :param upper_bound: the upper bound of the histogram
    :param label: the label of the histogram
    """
    a.list = sorted(a.list, key=lambda x: getattr(x, param))
    diction = a.count_occurences(a.list, a.find_min(a.list, param), a.find_max(a.list, param),
                                 upper_bound, param, 0.1)
    draw_histogram(diction, label, 'red')
    plt.savefig(f"output/assignment_1/{param}/{label}.png")
    plt.clf()


def scatter_plot(a, flower_args, x, y, upper_bound):
    """
    It takes in the list of flowers, the dictionary of flower arguments,
    the x and y values of the flower arguments, and the upper bound of the data set.
    It then finds the Pearson correlation coefficient of the x and y values, prints it,
    and then draws the scatter plot and linear regression plot.

    :param a: the object of the class Iris
    :param flower_args: a dictionary of the flower attributes and their corresponding column names
    :param x: the index of the first parameter
    :param y: the y-axis variable
    :param upper_bound: the upper bound of the data to be plotted
    """
    pcc = a.find_pcc(a.list, list(flower_args.keys())[x], list(flower_args.keys())[y], upper_bound)
    print(f"Pearson corelation coefficient value of {list(flower_args.values())[x]} "
          f"and {list(flower_args.values())[y]} is "
          f"{round(pcc,2)}")
    linear = a.line_regression(a.list, list(flower_args.keys())[x], list(flower_args.keys())[y], upper_bound)
    draw_scatter_plot(a.list, list(flower_args.keys())[x], list(flower_args.keys())[y], upper_bound, flower_args)
    draw_linear_regression_plot(a.list, list(flower_args.keys())[x], linear[0], linear[1], upper_bound)
    plt.title(f"r = {round(pcc, 2)}, y = {round(linear[0], 1)}x + {round(linear[1], 1)}")
    plt.savefig(f"output/assignment_2/{str(list(flower_args.keys())[x])} to {str(list(flower_args.keys())[y])}.png")
    plt.clf()


def draw_histogram(diction, axis_label, colour):
    """
    It takes a dictionary, an axis label, and a colour, and plots a histogram of the dictionary's values

    :param diction: a dictionary with the keys being the x-axis values and the values being the y-axis values
    :param axis_label: the label of the x-axis
    :param colour: the colour of the bars
    """
    size = list(diction.keys())
    amount = list(diction.values())
    plt.bar(size, amount, color=colour, width=1.0, edgecolor='black', alpha=0.4)
    # plt.locator_params(axis='x')
    plt.ylabel('Quantity')
    plt.xlabel(axis_label + " [cm]")
    xticks = plt.gca().xaxis.get_major_ticks()
    for i in range(len(xticks)):
        if i % 3 != 0:
            xticks[i].set_visible(False)
    plt.xticks(rotation=90)


def sort_holders_by_param(a, param):
    """
    It sorts a list of holders by the parameter of the first element in each holder's list

    :param a: the list of holders
    :param param: the parameter to sort by
    :return: A list of lists of objects, sorted by the parameter.
    """
    ordered = []
    for i in range(0, len(a)):
        a[i].list = sorted(a[i].list, key=lambda x: getattr(x, param))
        ordered.append(a[i])
    ordered = sorted(ordered, key=lambda x: getattr(x.list[0], param))
    return ordered


def plot_multiple_hist(a, param, label):
    """
    It takes a list of objects, a parameter, and a label, and plots a histogram for each object in the list

    :param a: list of objects of class Data
    :param param: the parameter we want to plot the histogram for
    :param label: the label of the x-axis
    """
    colors = ['blue', 'green', 'violet']
    for i in range(0, len(a)):
        color = int(getattr(a[i].list[0], 'species'))
        diction = a[i].count_occurences(a[i].list, a[i].find_min(a[i].list, param),
                                        a[i].find_max(a[i].list, param),
                                        len(a[i].list), param, 0.1)
        draw_histogram(diction, label, colors[color])
    plt.savefig(f"output/assignment_1/{param}/{label}_multi.png")
    plt.clf()


def draw_box_plot_obj(a, param, arglist):
    """
    This function takes in a list of objects, a parameter, and a string, and then creates a boxplot of the parameter for
    each object in the list

    :param a: list of objects
    :param param: the parameter to be plotted
    :param arglist: the name of the parameter being plotted
    """
    main_container = []
    name_container = []
    for i in range(0, len(a)):
        holder = []
        for n in range(0, len(a[i].list)):
            z = getattr(a[i].list[n], param)
            holder.append(z)
        main_container.append(holder)
        name_container.append(classes.index_to_name(getattr(a[i].list[0], 'species')))
    fig, ax = plt.subplots()
    plt.boxplot(main_container)
    plt.title('')
    ax.set_xticklabels(name_container)
    ax.set_ylabel(arglist + ' [cm]')
    plt.suptitle('Species')
    plt.savefig(f"output/assignment_1/{param}/{param}_boxplot_obj.jpg", format="jpg")
    plt.clf()


def draw_scatter_plot(arr, arg1, arg2, upper_bound, arglist):
    """
    It takes in an array of objects, two arguments from the object, an upper bound, and a list of arguments,
    and then plots the two arguments against each other

    :param arr: the array of objects
    :param arg1: the index of the first argument to be plotted
    :param arg2: the attribute of the object to be plotted on the y-axis
    :param upper_bound: the number of data points to be plotted
    :param arglist: a list of the arguments in the class
    """
    x = []
    y = []
    for i in range(0, upper_bound):
        x.append(getattr(arr[i], arg1))
        y.append(getattr(arr[i], arg2))
    fig, ax = plt.subplots()
    ax.set_ylabel(arglist[arg2])
    ax.set_xlabel(arglist[arg1])
    plt.scatter(x, y)


def draw_linear_regression_plot(arr, arg, a, b, upper_bound):
    """
    It takes an array of objects, an argument of those objects, and two numbers, and plots
    a line of best fit for the given argument

    :param arr: the array of objects
    :param arg: the argument to be used for the linear regression
    :param a: slope of the line
    :param b: the y-intercept of the line
    :param upper_bound: the number of data points to use for the regression
    """
    x = []
    y = []
    for i in range(0, upper_bound):
        x.append(getattr(arr[i], arg))
        y.append(a * getattr(arr[i], arg) + b)
    plt.plot(x, y, color="red")
