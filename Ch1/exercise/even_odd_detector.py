# -*- coding: utf-8 -*-
# 単位変換機

## いらない
def is_even(n):
	n % 2 == 0

def get_numbers(n):
	for i in range(1, 9):
		print(n + (i*2))

if __name__ == "__main__":
	n = float(input("Enter a number: "))
	if n.is_integer():
		get_numbers(int(n))
	else:
		"You need a positive integer!!!"
