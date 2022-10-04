from matplotlib import pyplot as plt


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