"""
title:$(NAME)
author: Michael
date:$(date)$(title)
"""


def food_order(choice, menu):
    """Tells user if choice is in menu"""
    choices = 'pizza, salad, sushi, fajitas, omlets'
    if choice in menu:
        return "Your choice " + choice + " is on the menu it will be out soon!"
    else:
        return choice + "is not on the menu. Please choose a different option!"

def guess_number(low, high):
    """Tell user if guess is out of range"""
    guess = input(f"Give a number between {low} and {high}")
    guess = int(guess)
    if guess < low:
        return f"No, {guess} is less than {low}"
    elif guess > high:
        return f"no {guess} is greater"
    else:
        return guess


if __name__ == '__main__':
    # menu = ['pizza', 'salad', 'sushi', 'fajitas', 'omlets']
    # choice = raw_input("Enter your choice of entree: ")
    # print(food_order(choice, menu))
    print(guess_number(1, 80))


