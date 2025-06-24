# word game for learning python
import random

from jinja2.nodes import Continue


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
guess_count = 1
print(f'''Welcome to Sam's word of the day 
You have {GUESSES} guesses today's word has {len(AWORD)} letter and starts with {AWORD[0]} and is from the category {random_category.name}.''')
#creating a loop for users to guess words

while is_active and guess_count <= GUESSES:
    UGuess = input(f"Guess the {len(AWORD)}-letter word: ")
    if len(UGuess) != len(AWORD):
        print (f'That\'s not the right length Try agin with a {len(AWORD)} Word')
       #UGuess = input(f'Guess the Word Again: ')
        continue
        guess_count += 1

    if UGuess == AWORD:
        print (f'''Checking .... 
        Correct! YOU HAVE WON''')
        is_active = False
    else:
        print(f'''Checking ....
        Wrong word. Guess attempt {guess_count} of {GUESSES}.''')

print ('GAME OVER')
