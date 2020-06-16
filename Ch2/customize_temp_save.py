# -*- coding: utf-8 -*-

## プロットの作成とパッケージのインストール
from pylab import plot, show, savefig
## データの有力
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0,
56.7, 56.4, 57.3]
years = range(2000, 2013)
## プロット
plot(nyc_temp, marker='o')

## 保存
savefig("/Users/kazy/Dropbox/Script/_Python/python_math_book/Ch2/image/pyfig.pdf")

print("end")
