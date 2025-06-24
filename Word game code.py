# word game for learning python
import random
class Fruit:
    def __init__(self):
        self.words = ["apple", "banana", "cherry"]
        self.name = "Fruit"
class Animal:
    def __init__(self):
        self.words = ["dog", "cat", "mouse"]
        self.name = "Animal"
class Colour:
    def __init__(self):
        self.words = ["red", "blue", "green"]
        self.name = "Colour"
class Vehicle:
    def __init__(self):
        self.words = ["car", "bike", "bus"]
        self.name = "Vehicle"

# Create instances of each category
categories = [Fruit(), Animal(), Colour(), Vehicle()]
# Randomly select a category
random_category = random.choice(categories)
# Randomly select a word from the selected category
AWORD = random.choice(random_category.words)

is_active = True
GUESSES = 2
print(f'''Welcome to Sam's word of the day 
You have {GUESSES} guesses today's word has {len(AWORD)} letter and starts with {AWORD[0]} and is from the category {random_category.name}.''')
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


