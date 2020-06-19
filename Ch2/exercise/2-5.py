# -*- coding: utf-8 -*-
# フィボナッチ数の比と黄金比の関係
import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # a > 2
    a = 1
    b = 1
    # first two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

def plot_list(list):
    plt.plot(result)
    plt.xlabel("No")
    plt.ylabel("Ratio")
    plt.axis(ymin=1.0, ymax=2.2, xmin=0, xmax=100)
    plt.title("Ratio between cosecutive Fibonacci numbers")
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/2-5.pdf")
    plt.show()


#print(fibo(100))
x_list = list(range(100))
fibo_x_list = fibo(100)
result = []

for i in x_list:
    result.append(fibo_x_list[i+1]/fibo_x_list[i])

plot_list(result)
