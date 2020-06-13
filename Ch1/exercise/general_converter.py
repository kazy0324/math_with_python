# -*- coding: utf-8 -*-
# 単位変換機
## エラー処理が冗長．

## 選択肢表示用
def print_menu():
	print("1. Kilometers to Miles")
	print("2. Miles to Kilometers")

## 距離
def convert_distance():
	choice = input("Which conversion are we talking about?: \n 1: km => miles, 2: miles => km \nEnter your number: ")
	try:
		if int(choice) == 1:
			km_to_miles()
		elif int(choice) == 2:
			miles_to_km()
		else:
			print("Please do it propery!!!")
	except ValueError:
		print("Invalid INPUT!!!!")

def km_to_miles():
	km = float(input("Enter a distance in kilometers: "))
	miles =  km / 1.609
	print("Distance in miles: {0:.2}".format(miles))

def miles_to_km():
	miles = float(input("Enter a distance in miles: "))
	km =  miles * 1.609
	print("Distance in kilometers: {0:.2}".format(km))

## 重さ
def convert_weight():
	choice = input("Which conversion are we talking about?: \n 1: kg => pounds, 2: pounds => kg \nEnter your number: ")

	if choice == 1:
		kg_to_pounds()
	elif choice == 2:
		pounds_to_kg()
	else:
		print("Please do it propery!!!")

def kg_to_pounds():
	kg = float(input("Enter a weight in kilogram: "))
	pounds =  kg*2.205
	print("Weight in pounds: {0:.2}".format(pounds))

def pounds_to_kg():
	pounds = float(input("Enter a weight in pounds: "))
	kg =  pounds/2.205
	print("Distance in kilograms: {0:.2}".format(kg))

## 気温
def convert_temperature():
	choice = input("Which conversion are we talking about?: \n 1: cel => fah, 2: fah => cel")
	try:
		if int(choice) == 1:
			cel_to_fah()
		elif int(choice) == 2:
			fah_to_cel()
		else:
			print("Please do it propery!!!")
	except ValueError:
		print("Invalid INPUT!!!!")

def cel_to_fah():
	cel = float(input("Enter a temperature in celsius: "))
	fah = (cel*9/5) + 32
	print("Temperature in fahrenheit: {fah:.2}".format(fah))

def fah_to_cel():
	fah = float(input("Enter a temperature in fahrenheit: "))
	cel = (fah-32)*5/9
	print("Temperature in celsius: {0:.2}".format(cel))

if __name__ == "__main__":
	print_menu()
	choice = input("Which conversion are we talking about?: \n 1 => distance, 2 => weight, 3 => temperature \nEnter your number: ")
	try:
		if int(choice) == 1:
			convert_distance()
		elif int(choice) == 2:
			convert_weight()
		elif int(choice) == 3:
			convert_temperature()
		else:
			print("Please do it propery")
	except ValueError:
		print("Invalid INPUT!!!!")
