import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '46', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters_total = []
nr_symbols_total = []
nr_numbers_total = []
password = []

for n in range(0,nr_letters):
    nr_letters_total.append(letters[random.randint(0,len(letters)-1)])

for n in range(0,nr_symbols):
    nr_symbols_total.append(symbols[random.randint(0,len(symbols)-1)])

for n in range(0,nr_numbers):
    nr_numbers_total.append(numbers[random.randint(0,len(numbers)-1)])

password = nr_letters_total + nr_symbols_total + nr_numbers_total

random.shuffle(password)

for letter in password:
    sys.stdout.flush()
    print(letter,end='')

