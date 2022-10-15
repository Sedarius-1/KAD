from matplotlib import pyplot as plt


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
    diction = a.count_occurences(a.list, a.find_min(a.list, param, upper_bound),
                                 a.find_max(a.list, param, upper_bound), upper_bound, param, 0.1)
    draw_histogram(diction, label, 'red')
    plt.savefig("output/" + param + ".png")
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
    plt.locator_params(axis='x')
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
    colors = ['blue', 'orange', 'violet']
    for i in range(0, len(a)):
        a[i].list = sorted(a[i].list, key=lambda x: getattr(x, param))
        diction = a[i].count_occurences(a[i].list, a[i].find_min(a[i].list, param, len(a[i].list)),
                                        a[i].find_max(a[i].list, param, len(a[i].list)),
                                        len(a[i].list), param, 0.1)
        draw_histogram(diction, label, colors[i])
    plt.savefig("output/" + param + "_multi.png")
    plt.clf()


# def draw_box_plot(df, flower_args, i):
#     fig, ax = plt.subplots()
#     df.boxplot(ax=ax, column=str(i), by="5", color={'medians': 'blue'})
#     ax.set_xticklabels(["setosa", "versicolor", "virginica"])
#     ax.set_ylabel(flower_args[i] + ' [cm]')
#     plt.title('')
#     plt.suptitle('')
#     plt.savefig(f"output/{i}_boxplot.jpg", format="jpg")
#     plt.clf()


def draw_box_plot_obj(a, param, arglist):
    """
    This function takes in a list of objects, a parameter, and a string, and then creates a boxplot of the parameter for
    each object in the list

    :param a: list of objects
    :param param: the parameter to be plotted
    :param arglist: the name of the parameter being plotted
    """
    main_container = []
    for i in range(0, len(a)):
        a[i].list = sorted(a[i].list, key=lambda x: getattr(x, param))
        holder = []
        for n in range(0, len(a[i].list)):
            z = getattr(a[i].list[n], param)
            holder.append(z)
        main_container.append(holder)
    fig, ax = plt.subplots()
    plt.boxplot(main_container)
    plt.title('')
    ax.set_xticklabels(["setosa", "versicolor", "virginica"])
    ax.set_ylabel(arglist + ' [cm]')
    plt.suptitle('Species')
    plt.savefig(f"output/{param}_boxplot_obj.jpg", format="jpg")
    plt.clf()
