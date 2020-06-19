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
    plt.xlabel("Amount")
    plt.ylabel("Categories")
    plt.title("Weekly expenditure")
    plt.savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/2-4.pdf")
    # グリッドの設定
    plt.grid()

    plt.show()

if __name__ == "__main__":
    n = int(input("How many categories?: "))
    # カテゴリーと支出のリスト
    cat_list = []
    exp_list = []

    while n > len(exp_list):
        cat_list.append(str(input("Enter the name of a category: ")))
        exp_list.append(int(input("Enter the expenditure (yen): ")))

    create_bar_chart(exp_list, cat_list)
