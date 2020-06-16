# -*- coding: utf-8 -*-

## メソッド，パッケージの読み込み
from matplotlib import pyplot as plt
import math

##グラフの描図
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title("Projectile motion of a ball")

##不動小数点の範囲の生成（時刻 t の生成）
def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers

## 投射運動 (u は初速 (initial velocity)，theta は投射の角度)
def draw_trajectory(u, theta):
    ## 角度 theta のラジアンへの変換
    theta = math.radians(theta)
    ## 重力加速度 g
    g = 9.8
    ## 全飛行時間
    t_flight = 2*(u*math.sin(theta)/g)
    ## 0秒から全飛行時間の0.001刻みでの算出
    intervals = frange(0, t_flight, 0.01)
    ## x軸とy軸の座標を格納するための配列
    x = []
    y = []
    ## 時刻 t における座標軸の計算
    for t in intervals:
        ## Sx の計算式 [p.51]
        x.append(u*math.cos(theta)*t)
        ## Sy の計算式 [p.52]
        y.append((u*math.sin(theta)*t) - 0.5*g*t*t)
    ## 描図
    draw_graph(x, y)

if __name__ == "__main__":
    # 異なる初速の配列
    u_list = [20, 40, 60]
    # 角度
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)

    plt.legend(["20", "40", "60"])
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/plot_projectile_ext.pdf")
    plt.show()
