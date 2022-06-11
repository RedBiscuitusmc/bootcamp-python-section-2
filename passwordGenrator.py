#########################################################
########################################################
#Coding BootCamp Challenge Udemy
#Section 5
#Password Generator TEST
#Jacob A. Merlin
########################################################
#########################################################
#Password Generator Project
#########################################################
#import Section
import random
#########################################################
#List Section
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#########################################################
#########################################################

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

#########################################################
#########################################################

length_of_string = nr_letters
length_of_numbers = nr_numbers
length_of_symbols = nr_symbols
total_length = nr_letters + nr_numbers + nr_symbols

#########################################################

letters_and_digits = letters + letters
numbers_and_digits = numbers + numbers
symbols_and_digits = symbols + symbols

#########################################################

result_string = ""
result_number = ""
result_symbols = ""

#########################################################

for number in range(length_of_string):
    result_string += random.choice(letters_and_digits)

for number in range(length_of_numbers):
    result_number += random.choice(numbers_and_digits)

for number in range(length_of_symbols):
    result_symbols += random.choice(symbols_and_digits)

#########################################################

#########################################################

total_result = result_string+result_number+result_symbols

#########################################################

#########################################################

random_result = ""

for number in range(total_length):
    random_result += random.choice(total_result)

#########################################################

#########################################################

print(random_result)