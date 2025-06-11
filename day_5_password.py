# Password Generator
# Author: Lucas Faria
# Date: 06/11/25
# Description: A Python script that generates secure random passwords with customizable length and character sets.
# Day 5/100




import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

## easy password - there is no randomization of characters / symbols / numbers

# random_pass = ''
# for num in range(0, nr_letters):
#     random_pass += random.choice(letters)
# 
# for num in range(0, nr_symbols):
#     random_pass += random.choice(symbols)
# 
# for num in range(0, nr_numbers):
#     random_pass += random.choice(numbers)
# 
# print(random_pass)


random_pass_hard = []
final_pass_hard = ''
for num in range(nr_letters):
    random_pass_hard += random.choice(letters)

for num in range(nr_symbols):
    random_pass_hard += random.choice(symbols)

for num in range(nr_numbers):
    random_pass_hard += random.choice(numbers)

for chars in random_pass_hard:
    final_pass_hard += random.choice(random_pass_hard)

print(f"Your final password is: {final_pass_hard}")



