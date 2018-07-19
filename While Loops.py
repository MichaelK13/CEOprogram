"""
title:$(NAME)
author: Michael
date:$(date)$(title)
"""
import random



def goguess():
    guess = input("guess a number between 1 and 20")
    guess = int(guess)
    answer = random.randint(1, 20)
    while guess <= answer:()
