import random
from typing import Tuple
print('''
──────────────────
──▄▄─────▄───▄▄▄▄▄
▄▀──▀▄──█─█──█───█
█────█─█───█ █───█
─▀▄▄▀─▐▄▄▄▄▄▌█▄▄▄█
──────────────────
''')

options = ['left','right']
print("Welcome to Cristal Bridge Game from the Squid Games your mission is to get to the other side of the bridge\n\n")
print("You have 2 options a solid crystal and a fragile one choose the correct one or your turn will end here\n\n")

machine = random.choice(options)

total_rounds = 5

for round in range(0,total_rounds):
    user = input("Select a Side: ").lower()
    if user != machine:
        print("You Lose..")
        exit()

print("Congratulations! You Won!")
        

        




    

    
