from os import SCHED_OTHER
from typing import Counter, NewType
from game_data import data
from art import logo, vs
import random

def randomNumber():
    number = random.randint(0,len(data)-1)
    return number

num1 = randomNumber()
num2 = randomNumber()
game_over = False
score = 0

def dataComparation(number):
    name = {data[number]['name']}
    description = {data[number]['description']}
    country = {data[number]['country']}
    return f"{data[number]['name']}, a {data[number]['description']}, from {data[number]['country']}"

def inputComparation(num1,num2,selection):
    if data[num1]['follower_count'] > data[num2]['follower_count'] and selection == 'A':
        return True
    elif data[num1]['follower_count'] < data[num2]['follower_count'] and selection == 'B':
        return True
    else:
        return False

firtst_comparation = dataComparation(num1)
second_comparation = dataComparation(num2)

print(logo)
while not game_over:
    print(f"Compare A: {firtst_comparation}")
    print(vs)
    print(f"Compare B: {second_comparation}")

    selectionII = inputComparation(num1,num2,input("Who has more followers? Type 'A' or 'B': ").capitalize())

    if selectionII == True:
        firtst_comparation = second_comparation
        num1 = num2
        num2 = randomNumber()
        second_comparation = dataComparation(num2)
        score += 1
    elif selectionII == False:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_over = True






  