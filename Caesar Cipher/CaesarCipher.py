from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text,shift_amount,direction):
        if direction == "encode":
            cipher_text = ""
        
            for letter in plain_text:
                if letter not in alphabet:
                    cipher_text += letter
                else:
                    index = alphabet.index(letter) + shift_amount
                    cipher_text += alphabet[index]


            print(f"The encoded text is {cipher_text}")
        
        elif direction == "decode":
            decipher_text = ""
        
            for letter in plain_text:
                if letter not in alphabet:
                    decipher_text += letter
                else:
                    index = alphabet.index(letter) - shift_amount
                    decipher_text += alphabet[index]
            
            print(f"The encoded text is {decipher_text}")


print(logo)
restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26

    caesar(plain_text=text,shift_amount=shift,direction=direction)
    restartProgram = input("Do you want to restart the Encript?: ").lower()
    if restartProgram == "no":
        print("Good Bye!")
        exit()
    elif restartProgram == "yes":
        pass






