from matplotlib import pyplot as plt
import math

def multiple_histogram(datafile, column, axis_label,output_name):
    dl = datafile[column].loc[datafile.Gatunek == "setosa"]
    print(dl.dtypes)
    dl.hist(label='setosa')
    dl = datafile[column].loc[datafile.Gatunek == "versicolor"]
    print(dl)
    dl.hist(label='versicolor')
    dl = datafile[column].loc[datafile.Gatunek == "virginica"]
    print(dl.dtypes)
    dl.hist(label='virginica')
    plt.ylabel('Liczebność')
    plt.xlabel(axis_label)

    plt.legend()
    plt.savefig(output_name)
    plt.clf()

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
