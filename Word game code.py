# word game for learning python
AWORD = 'brain'
is_active = True
GUESSES = 2
print(f'''Welcome to Sam's word of the day 
You have {GUESSES} guesses today's word has {len(AWORD)} letter and starts with {AWORD[0]}.''')
#creating a loop for users to guess words
UGuess = input(f'Guess the Word: ')
while is_active:
    if len(UGuess) != len(AWORD):
        print (f'That\'s not the right length Try agin with a {len(AWORD)} Word')
        UGuess = input(f'Guess the Word Again: ')
    else:
        is_active = False
guess_count = 1
while guess_count <= GUESSES:
    if UGuess != AWORD:
        print (f'''Checking ....
        Wrong Word Try again. 
        Guess: ''', guess_count)
        UGuess = input(f'Guess the Word Again: ')
    else:
        print('''Checking ....
        Correct!''')
        print ('YOU HAVE WON')
        break
    guess_count += 1
print ('GAME OVER')


