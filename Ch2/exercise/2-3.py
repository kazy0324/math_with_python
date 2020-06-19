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
    print("全飛行時間: {t_flight}".format(t_flight = t_flight))
    print("最大水平距離: {max_height}".format(max_height = max(y)))
    print("最大垂直距離: {max_length}".format(max_length = max(x)))
    draw_graph(x, y)


if __name__ == "__main__":
    # 初速の配列
    u_list = []
    # 角度の配列
    theta_list = []
    # index
    index = 1
    # ユーザーからの入力
    n = int(input("How many trajectories?: "))
    while n > len(u_list):
        u_list.append(float(input("Enter the initial velocity for trajectory {index} (m/s):".format(index = index))))
        theta_list.append(float(input("Enter the angle of projection for trajectory {index} (degrees):".format(index = index))))
        index += 1

    for j in list(range(3)):
        draw_trajectory(u_list[j], theta_list[j])

    #plt.legend(["20", "40", "60"])
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/2-4.pdf")
    plt.show()
