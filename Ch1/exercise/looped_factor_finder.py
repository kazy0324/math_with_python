
# -*- coding: utf-8 -*-
# 整数の因数を見つける

def factors(b):
	for i in range(1, b+1):
		if b % i  == 0:
			print(i)

if __name__ == "__main__":
	while True:
		b = float(input("Your Number Please: "))

		if b > 0 and b.is_integer():
			factors(int(b))
		else:
			print("Please enter a positive integer")

		answer = input("Would you like to exit? Type 'y' for yes: \nEnter your answer: ")
		if answer == "y":
			break
