from matplotlib import pyplot as plt


def draw_histogram(diction, minimal, maximal, axis_label, output_name):
    fig, ax = plt.subplots()
    fig.set_figwidth(15)
    fig.set_figheight(15)
    size = list(diction.keys())
    amount = list(diction.values())
    plt.bar(size, amount, color='red', width=1.0, edgecolor='black', alpha=0.5)
    print(minimal, maximal)
    if maximal - minimal > 5:
        every_nth = 2
        for n, label in enumerate(ax.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
    plt.ylabel('Liczebność')
    plt.xlabel(axis_label)

    plt.savefig(output_name)

def draw_multiple_histogram(arg_list, diction, minimal, maximal, axis_label, output_name):
    colors=['blue', 'orange', 'violet']
    fig, ax = plt.subplots()
    fig.set_figwidth(15)
    fig.set_figheight(15)
    number=0

    for i in arg_list:
        size = list(diction.keys())
        amount = list(diction.values())
        plt.bar(size, amount, color=colors[number], width=1.0, edgecolor='black', alpha=0.5)
        print(minimal, maximal)
        if maximal - minimal > 5:
            every_nth = 2
            for n, label in enumerate(ax.xaxis.get_ticklabels()):
                if n % every_nth != 0:
                    label.set_visible(False)
        number+=1
    plt.ylabel('Liczebność')
    plt.xlabel(axis_label)

    plt.savefig(output_name)
# def counting(datafile, column):
#     els = list(count_elements(datafile[column]).items())
#     return els


# def count_all(datafile, column):
#     els = counting(datafile, column)
#     amount = 0
#     for i in els:
#         amount += i[1]
#     return amount


# def mean(datafile, column):
#     els = counting(datafile, column)
#     value = 0
#     for i in els:
#         value += i[0] * i[1]
#     # print(amount)
#     # print(value)
#     return value / count_all(datafile, column)
#
#
# def median(datafile, column):
#     els = counting(datafile, column)
#     arr = []
#     amount = count_all(datafile, column)
#     for i in els:
#         for p in range(0, i[1]):
#             arr.append(i[0])
#     lasting = amount % 2
#     amount = math.floor(amount / 2)
#     if lasting == 0:
#         return arr[amount], amount
#     else:
#         return arr[amount] + arr[amount + 1], amount
#
#
# def quartile(datafile, column):
#     els = counting(datafile, column)
#     arr = []
#     for i in els:
#         for p in range(0, i[1]):
#             arr.append(i[0])
#     middle = median(datafile, column)[1]
#     parity = middle % 2
#     amount = math.floor(middle / 2)
#     if parity:
#         return arr[amount], arr[amount * 3], amount
#     else:
#         return arr[amount] + arr[amount + 1], arr[3 * amount] + arr[3 * amount + 1], amount
#
#
# def deriv(datafile, column):
#     els = counting(datafile, column)
#     amount = 0
#     value = 0
#     for i in els:
#         value_temp = i[0]
#         amount += i[1]
#         for p in range(0, i[1]):
#             value = value + ((value_temp - mean(datafile, column)) * (value_temp - mean(datafile, column)))
#             # print(value)
#             # print(amount)
#     return float(math.sqrt(value / amount))
#
#
# def maximum(datafile, column):
#     els = counting(datafile, column)
#     return els[-1][0]
#
#
# def minimum(datafile, column):
#     els = counting(datafile, column)
#     return els[0][0]
#
#
# def count_elements(seq) -> dict:
#     hist = {}
#     for i in seq:
#         hist[i] = hist.get(i, 0) + 1
#         s = SortedDict(hist)
#     return s
#
#
