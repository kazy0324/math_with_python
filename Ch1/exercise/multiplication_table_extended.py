# -*- coding: utf-8 -*-
# 乗算表生成機（改良版）

def multi_table(a, row_number):
	for i in range(1, row_number):
		## 全桁表示
		#print("{0} x {1} = {2}".format(a, i, a*i))
		## 小数点3桁まで
		print("{0}: {1:.3f} x {2:.3f} = {3:.3f}".format(i+1, a, i, a*i))

if __name__ == "__main__":
	a = input("Enter a number: ")
	b = input("Enter the row number you want (only integer allowed): ")

	multi_table(float(a), int(b))
