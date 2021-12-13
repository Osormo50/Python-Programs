print('''
──────────────────
──▄▄─────▄───▄▄▄▄▄
▄▀──▀▄──█─█──█───█
█────█─█───█ █───█
─▀▄▄▀─▐▄▄▄▄▄▌█▄▄▄█
──────────────────
''')

print("Welcome to Cristal Bridge Game from the Squid Games your mission is to get to the other side of the bridge\n\n")
print("You have 2 options a solid crystal and a fragile one choose the correct one or your turn will end here\n\n")

phaseI = input('left or right? ').lower()
if phaseI == 'left':
    print('Game Over...')
elif phaseI == 'right':
    phaseII = input('left or right? ').lower()
    if phaseII == 'left':
        print('Game Over...')
    elif phaseII == 'right':
        phaseIII = input('left or right? ').lower()
        if phaseIII == 'right':
            print('Game Over...')
        elif phaseIII == 'left':
            phaseIV = input('left or right? ').lower()
            if phaseIV == 'right':
                print('Game Over...')
            elif phaseIV == 'left':
                phaseV = input('left or right? ').lower()
                if phaseV == 'left':
                    print('Game Over...')
                elif phaseV == 'right':
                    print('Congrats You Won!')

    