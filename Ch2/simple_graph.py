# -*- coding: utf-8 -*-

x = [1, 2, 3]
y = [2, 4, 6]

## プロットの作成とパッケージのインストール
from pylab import plot, show
## 直線
# plot(x,y)
## 点を含む直線
# plot(x, y, marker="o")
## 点のみを含む場合
plot(x, y, "o")

## 表示 （消さないと処理が終わらないので注意）
show()
