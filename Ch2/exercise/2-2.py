# -*- coding: utf-8 -*-
## 描画用のメソッド
from matplotlib import pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker="o")
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/2-2.pdf")
    plt.show()

x_values = range(-500, 500)
y_values = []

for x in x_values:
    y_values.append(x**2 + 2*x +1)

draw_graph(x_values, y_values)
