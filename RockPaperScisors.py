rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game = [rock,paper,scissors]

print("Welcome to Rock, Paper or Scissors.\n")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
machine = random.randint(0,2)

print(game[user])
print(game[machine])

if user == 0 and machine == 1:
    print("You Won!")
elif user == 0 and machine == 2:
    print("You Won!")
elif user == 1 and machine == 0:
    print("You Won!")
elif user == 1 and machine == 2:
    print("You Lose!")
elif user == 2 and machine == 0:
    print("You Lose!")
elif user == 2 and machine == 1:
    print("You Won!")
else:
    print("Tie!")







