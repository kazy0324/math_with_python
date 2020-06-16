# -*- coding: utf-8 -*-
## 描画用のメソッド
from matplotlib import pyplot as plt
import numpy as np


def draw_graph(x, y):
    plt.plot(x, y, marker="o")
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title("Weather in Kyoto [2020/06/17]")
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/2-1.pdf")

## 2020年6月17日の京都市の気温を plot する
kyoto_weather = [20.5, 20.0, 19.9, 19.4, 19.1, 19.5, 20.7, 21.8, 23.7, 25.6, 27.4, 28.6, 29.9, 30.8, 31.5, 31.3, 30.3, 28.4, 27.1, 25.8, 24.8, 24.1, 23.2, 22.1]
## 時間の範囲
time = range(0, 24)

draw_graph(time, kyoto_weather)
