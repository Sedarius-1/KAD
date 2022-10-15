import pandas as pd
from matplotlib import pyplot as plt


def plot_hist(a, param, upper_bound, label):
    a.list = sorted(a.list, key=lambda x: getattr(x, param))
    dict = a.count_occurences(a.list, a.find_min(a.list, param, upper_bound), a.find_max(a.list, param, upper_bound),
                              upper_bound, param, 0.1)
    draw_histogram(dict, label, 'red')
    plt.savefig("output/" + param + ".png")
    plt.clf()


def draw_histogram(diction, axis_label, colour):
    size = list(diction.keys())
    amount = list(diction.values())
    plt.bar(size, amount, color=colour, width=1.0, edgecolor='black', alpha=0.4)
    plt.locator_params(axis='x')
    plt.ylabel('Quantity')
    plt.xlabel(axis_label+" [cm]")
    xticks = plt.gca().xaxis.get_major_ticks()
    for i in range(len(xticks)):
        if i % 3 != 0:
            xticks[i].set_visible(False)
    plt.xticks(rotation=90)


def sort_holders_by_param(a, param):
    ordered = []
    for i in range(0, len(a)):
        a[i].list = sorted(a[i].list, key=lambda x: getattr(x, param))
        ordered.append(a[i])
    ordered = sorted(ordered, key=lambda x: getattr(x.list[0], param))
    return ordered


def plot_multiple_hist(a, param, label):
    colors = ['blue', 'orange', 'violet']
    for i in range(0, len(a)):
        a[i].list = sorted(a[i].list, key=lambda x: getattr(x, param))
        dict = a[i].count_occurences(a[i].list, a[i].find_min(a[i].list, param, len(a[i].list)),
                                     a[i].find_max(a[i].list, param, len(a[i].list)),
                                     len(a[i].list), param, 0.1)
        draw_histogram(dict, label, colors[i])
    plt.savefig("output/" + param + "_multi.png")
    plt.clf()


def draw_box_plot(df,flower_args,i):
    fig,ax=plt.subplots()
    df.boxplot(ax=ax,column=str(i), by="5",color={'medians':'blue'})
    ax.set_xticklabels(["setosa","versicolor","virginica"])
    ax.set_ylabel(flower_args[i]+' [cm]')
    plt.title('')
    plt.suptitle('')
    plt.savefig(f"output/{i}_boxplot.jpg", format="jpg")
    plt.clf()