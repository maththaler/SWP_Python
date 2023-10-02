import random
import matplotlib.pyplot as plt


def swap_positions(pos1, pos2, list):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def create_list(max):
    return [a for a in range(1, max + 1)]


def create_dic(max):
    dic = {}
    for i in range(1, max + 1):
        dic[i] = 0
    return dic


def lotto_ziehen(list, numbers_to_draw):
    for i in range(numbers_to_draw):
        draw = random.randint(0, len(list) - 1 - i)
        swap_positions(draw, len(list) - 1 - i, list)
    return list[len(list) - numbers_to_draw:]


def add_to_dic(dictionary, list):
    for element in list:
        dictionary[element] += 1
    return dictionary


max = 90
dic = create_dic(max)
for i in range(100000):
    add_to_dic(dic, lotto_ziehen(create_list(max), 6))

plt.bar(list(dic.keys()), list(dic.values()))
plt.ylabel("Häufigkeit")
plt.xlabel("Zahlen")
plt.show()
