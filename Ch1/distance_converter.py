# -*- coding: utf-8 -*-
# 単位変換機

def print_menu():
	print("1. Kilometers to Miles")
	print("2. Miles to Kilometers")

def km_to_miles():
	km = float(input("Enter a distance in kilometers: "))
	miles =  km / 1.609
	print("Distance in miles: {0:.2}".format(miles))

def miles_to_km():
	miles = float(input("Enter a distance in miles: "))
	km =  miles * 1.609
	print("Distance in kilometers: {0:.2}".format(km))

if __name__ == "__main__":
	print_menu()
	choice = input("Which conversion are we talking about?: ")
	if choice == 1:
		km_to_miles()
	elif choice == 2:
		miles_to_km()
	else:
		print("Do it propery!!!")
