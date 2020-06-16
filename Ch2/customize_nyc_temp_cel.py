# -*- coding: utf-8 -*-

## プロットの作成とパッケージのインストール
from pylab import plot, show, title, xlabel, ylabel, legend

## 気温の変換
def fah_to_cel(fah):
	return((fah-32)*5/9)

## 2000年，2006年，2012年の月ごとの推移を年ごとに比較したプロット
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0,
57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6,
56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8,
58.0, 43.9, 41.5]

nyc_temp_2000_cel = list(map(lambda x: fah_to_cel(x), nyc_temp_2000))
nyc_temp_2006_cel = list(map(lambda x: fah_to_cel(x), nyc_temp_2006))
nyc_temp_2012_cel = list(map(lambda x: fah_to_cel(x), nyc_temp_2012))

months = range(1, 13)

## 一気に表示
plot(months, nyc_temp_2000_cel, months, nyc_temp_2006_cel, months, nyc_temp_2012_cel)
## タイトル
title("Average monthly temperature in NYC")
## x軸のタイトル
xlabel("Month")
## y軸のタイトル
ylabel("Temperature")
## 凡例
legend([2000, 2006, 2012])

## 表示 （消さないと処理が終わらないので注意）
show()

print("end")
