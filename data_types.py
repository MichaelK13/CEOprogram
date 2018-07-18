"""
title:$(NAME)
author: Michael
date:$(date)$(title)
"""

def add_tip(total, tip_percent):
    # return total amt including tip
    tip = tip_percent * total
    return total + tip


def age_calculator(current_year, birth_year):
    """Returns user's age"""
    age = current_year - birth_year
    return age


def mean(a, b, c):
    """finding average of three numbers"""
    return (a + b + c) / 3


if __name__ == "__main__":
    print(age calculator(2018,2003))
    print(4, 7, 8)