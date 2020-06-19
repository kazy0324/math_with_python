# -*- coding: utf-8 -*-
## 棒グラフを描く
import matplotlib.pyplot as plt
def create_bar_chart(data, labels):
    # 棒の数
    num_bars = len(data)
    # 各リストが描かれた際の中央の値
    positions = range(1, num_bars + 1)
    # 棒グラフの描図
    plt.barh(positions, data, align="center")
    # 棒のラベル設定
    plt.yticks(positions, labels)
    plt.xlabel("Steps")
    plt.ylabel("Day")
    plt.title("Number of steps walked")
    # グリッドの設定
    plt.grid()
    plt.show()

if __name__ == "__main__":
    steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
    labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    create_bar_chart(steps, labels)
