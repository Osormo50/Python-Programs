
# TODO 1: Agregar Volver a Jugar o Salir Opcion
# TODO 2: Agregar la Funcion de Limpiar Pantalla 

from random import choice
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
word = choice(word_list)
word_length = len(word)

lives = 6

print(logo)

display = []
for n in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
    elif guess in display:
        print(f"You've already guessed {guess}")
  
    print(stages[lives])
    print(f"{' '.join(display)}")
   
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print("You Lose")

    
    