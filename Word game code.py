# word game for learning python
import random
word_choice = ['cherry','grape', 'peach', 'plum', 'pineapple''apple', 'house', 'water', 'light', 'green', 'happy', 'child', 'music', 'river', 'stone',
'heart', 'world', 'plant', 'table', 'night', 'laugh', 'dream', 'cloud', 'grass', 'smile',
'phone', 'chair', 'bread', 'glass', 'floor', 'river', 'shirt', 'clock', 'bread', 'field',
'park', 'bird', 'tree', 'road', 'shoe', 'star', 'wind', 'fish', 'ball', 'door',
'game', 'milk', 'fire', 'king', 'queen', 'book', 'pen', 'cat', 'dog', 'car',
'box', 'cup', 'hat', 'key', 'map', 'net', 'owl', 'pig', 'rat', 'sun',
'top', 'van', 'web', 'yak', 'zip', 'ant', 'bee', 'cow', 'fox', 'hen',
'jar', 'kid', 'leg', 'man', 'nut', 'owl', 'pop', 'run', 'sit', 'toy''elephant', 'mountain', 'computer', 'dinosaur', 'pineapple', 'butterfly', 'chocolate', 'adventure', 'beautiful', 'happiness',
'pineapple', 'telephone', 'discovery', 'education', 'important', 'generation', 'knowledge', 'literature', 'mysterious', 'wonderful''sanguine', 'tenacious', 'unctuous', 'vicarious', 'whimsical',]
AWORD = random.choice (word_choice)
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
    else:
        print('''Checking ....
        Correct!''')
        print ('YOU HAVE WON')
        break
    UGuess = input(f'Guess the Word Again: ')
    guess_count += 1
print ('GAME OVER')


