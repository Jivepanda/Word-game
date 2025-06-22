# word game for learning python
AWORD = 'brain'
is_active = True
GUESSES = 2
print(f'''Welcome to Sam's word of the day 
You have {GUESSES} guesses today's word has {len(AWORD)} letter and starts with {AWORD[0]}.''')
#creating a loop for users to guess words
UGuess = input(f'Guess the Word')
while is_active:
    if len(UGuess) != len(AWORD):
        print (f'Thats not the right length Try agin with a {len(AWORD)} Word')
        UGuess = input(f'Guess the Word Again')
    else:
        print ('''Checking ....
        Wrong Word''')
        is_active = False
guesscount = 1
while guesscount <= GUESSES:
    if UGuess != AWORD:
        print (f'''Checking ....
        Wrong Word Try again. Guess:''', guesscount)
        UGuess = input(f'Guess the Word Again')
        guesscount += 1
    else:
        print ('YOU HAVE WON')
        break
print ('GAME OVER')


