# -*- coding: utf-8 -*-
# 乗算表生成機

def multi_table(a):
	for i in range(1,11):
		## 全桁表示
		#print("{0} x {1} = {2}".format(a, i, a*i))
		## 小数点3桁まで
		print("{0:.3f} x {1:.3f} = {2:.3f}".format(a, i, a*i))

if __name__ == "__main__":
	while True:
		a = input("Enter a number: ")
		multi_table(float(a))

		answer = input("Would you like to exit? Type 'y' for yes: \nEnter your answer: ")
		if answer == "y":
			break
