from matplotlib import pyplot as plt
import math
import numpy as np
from matplotlib.pyplot import figure
from sortedcontainers import SortedDict


def mean(a, n):
    sum = 0
    for i in range(0, n):
        sum = sum + a[i]
    return float(sum / n)


def median(a):
    a.sort()
    if len(a) % 2 != 0:
        temp1 = int((len(a) + 1) / 2 - 1)
        return a[temp1]
    else:
        temp1 = int(len(a) / 2 - 1)
        temp2 = int(len(a) / 2)
        return (a[temp1] + a[temp2]) / 2


def deriv(a):
    sum = 0
    for i in range(len(a)):
        sum = sum + (a[i] - mean(a, len(a))) * (a[i] - mean(a, len(a)))
    return float(math.sqrt(sum / len(a)))


def maximum(a):
    temp = a[0]
    for x in a:
        if x > temp:
            temp = x
    return temp


def minimum(a):
    temp = a[0]
    for x in a:
        if x < temp:
            temp = x
    return temp


def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
        s = SortedDict(hist)
    return s


def draw_multiple_histogram(datafile, column, axis_label, types, output_name):
    datasets = []
    colors = ["red", "gold", "limegreen"]
    number = 0
    figure(figsize=(16, 8), dpi=80)
    els = list(count_elements(datafile[column]).items())
    for i in types:
        dl = datafile[column].loc[datafile.Gatunek == i]
        data = count_elements(dl)
        size = list(data.keys())
        amount = list(data.values())
        datasets.append(data)
        plt.bar(size, amount, color=colors[number], width=0.1, edgecolor='black', alpha=0.5)
        number += 1

    #print("Difference is: " + str(els[-1][0] - els[0][0]))
    if els[-1][0] - els[0][0] > 4:
        plt.xticks(np.arange(els[0][0], els[-1][0] + 0.2, 0.2))
    else:
        plt.xticks(np.arange(els[0][0], els[-1][0] + 0.1, 0.1))
    plt.ylabel('Liczebność')
    plt.xlabel(axis_label)

    plt.savefig(output_name)
