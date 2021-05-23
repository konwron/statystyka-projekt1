# importuję bibliotekę potrzebną do stworzenia wektora losowych liczb
from random import uniform
from math import sqrt

x_min = -100000
x_max = 100000
x_length = 10
x = []

# tworzę wektor 10 losowych liczb z zakresu (-100000, 100000)
for i in range(0, x_length):
    x.append(uniform(x_min, x_max))


# Liczę średnią arytmetyczną
def mean(data):
    data_sum = 0
    for i in data:
        data_sum += i
    data_mean = data_sum / len(data)

    return data_mean


def standard_deviation(data):
    m = mean(data)
    dev_sum = 0
    for i in x:
        dev_sum += (i - m) ** 2
    std_dev = sqrt(dev_sum / (len(x) - 1))

    return std_dev


print('Dla wektora {}:\nŚrednia wynosi: {}\nOdchylenie standardowe wynosi: {}'.format(x, mean(x), standard_deviation(x)))
