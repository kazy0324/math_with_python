# -*- coding: utf-8 -*-


def roots(a,b,c):
	D = ((b*b) - (4*a*c))**0.5
	x1 = (-b + D)/(2*a)
	x2 = (-b - D)/(2*a)
	print("x1: {0}".format(x1))
	print("x2: {0}".format(x2))

if __name__ == "__main__":
	while True:
		a = input("Enter a: ")
		b = input("Enter b: ")
		c = input("Enter c: ")
		roots(float(a), float(b), float(c))

		answer = input("Would you like to exit? Type 'y' for yes: \nEnter your answer: ")
		if answer == "y":
			break
