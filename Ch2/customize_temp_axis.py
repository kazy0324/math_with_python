# -*- coding: utf-8 -*-

## プロットの作成とパッケージのインストール
from pylab import plot, show, axis
## データの有力
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0,
56.7, 56.4, 57.3]
years = range(2000, 2013)
## プロット
plot(nyc_temp, marker='o')
## y 軸の最小値の設定
axis(ymin=0)
## x 軸の最小，最大，y 軸の最小，最大をそれぞれ設定する
#axis(0, 10, 0, 20)

## 表示 （消さないと処理が終わらないので注意）
show()

print("end")
