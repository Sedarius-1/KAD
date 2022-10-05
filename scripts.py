from matplotlib import pyplot as plt
import math
import numpy as np
from matplotlib.pyplot import figure
from sortedcontainers import SortedDict


def counting(datafile, column):
    els = list(count_elements(datafile[column]).items())
    return els


def count_all(datafile, column):
    els = counting(datafile, column)
    amount = 0
    for i in els:
        amount += i[1]
    return amount


def mean(datafile, column):
    els = counting(datafile, column)
    value = 0
    for i in els:
        value += i[0] * i[1]
    # print(amount)
    # print(value)
    return value / count_all(datafile, column)


def median(datafile, column):
    els = counting(datafile, column)
    arr = []
    amount = count_all(datafile, column)
    for i in els:
        for p in range(0, i[1]):
            arr.append(i[0])
    lasting = amount % 2
    amount = math.floor(amount / 2)
    if lasting == 0:
        return arr[amount], amount
    else:
        return arr[amount] + arr[amount + 1], amount


def quartile(datafile, column):
    els = counting(datafile, column)
    arr = []
    for i in els:
        for p in range(0, i[1]):
            arr.append(i[0])
    middle = median(datafile, column)[1]
    parity = middle % 2
    amount = math.floor(middle / 2)
    if parity:
        return arr[amount], arr[amount * 3], amount
    else:
        return arr[amount] + arr[amount + 1], arr[3 * amount] + arr[3 * amount + 1], amount


def deriv(datafile, column):
    els = counting(datafile, column)
    amount = 0
    value = 0
    for i in els:
        value_temp = i[0]
        amount += i[1]
        for p in range(0, i[1]):
            value = value + ((value_temp - mean(datafile, column)) * (value_temp - mean(datafile, column)))
            # print(value)
            # print(amount)
    return float(math.sqrt(value / amount))


def maximum(datafile, column):
    els = counting(datafile, column)
    return els[-1][0]


def minimum(datafile, column):
    els = counting(datafile, column)
    return els[0][0]


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
    els = counting(datafile, column)
    figure(figsize=(16, 8), dpi=80)
    for i in types:
        dl = datafile[column].loc[datafile.Gatunek == i]
        data = count_elements(dl)
        size = list(data.keys())
        amount = list(data.values())
        datasets.append(data)
        plt.bar(size, amount, color=colors[number], width=0.1, edgecolor='black', alpha=0.5)
        number += 1

    # print("Difference is: " + str(els[-1][0] - els[0][0]))
    if els[-1][0] - els[0][0] > 4:
        plt.xticks(np.arange(els[0][0], els[-1][0] + 0.2, 0.2))
    else:
        plt.xticks(np.arange(els[0][0], els[-1][0] + 0.1, 0.1))
    plt.ylabel('Liczebność')
    plt.xlabel(axis_label)

    plt.savefig(output_name)
