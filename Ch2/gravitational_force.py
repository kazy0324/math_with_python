# -*- coding: utf-8 -*-
# 二物体間の万有引力と距離の関係
## F = (G*m_1*m_2)/r^2

import matplotlib.pyplot as plt

# グラフの描図
def draw_graph(x, y):
    plt.plot(x, y, marker="o")
    plt.xlabel("Distance in meters")
    plt.ylabel("Gravitational force in newtons")
    plt.title("Gravitational force and disstance")
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/f_plot.pdf")
    plt.show()

# F の生成
def generate_F_r():
    # 50刻みで 100 から 1001 km の値の範囲を生成する
    r = range(100, 1001, 50)
    # Fの計算結果を格納するリスト
    F = []
    # 定数 G
    G = 6.674*(10**-11)
    # 二つの物体 (kg)
    m1 = 0.5
    m2 = 1.5
    # 引力の計算とその結果の格納
    for dist in r:
        F.append(G*(m1*m2)/dist**2)
    # 可視化
    draw_graph(r, F)

# 関数の実行
if __name__ == "__main__":
    generate_F_r()
