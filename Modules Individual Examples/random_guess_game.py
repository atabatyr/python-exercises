# -*- coding: utf-8 -*-
"""
@author: A
"""
import sys
from random import randint

first = sys.argv[1]
last = sys.argv[2]

random_num = randint(int(first), int(last))

while True:
    user_guess = int(input("Guess the random no.: "))
    if user_guess == random_num:
        print("Congratulations, You WON!!")
        break
    else:
        print("You Lose! Guess again....")
