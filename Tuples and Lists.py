"""
title:$(NAME)
author: Michael
date:$(date)$(title)
"""
import random


def name_generator(first_list, last_list):
    """Generates random name
    :param first_list: The list of strings of first names
    :param last_list: The list of strings of last names"""
    firstname = random.choice(first_list)
    last_name = random.choice(last_list)



if __name__=='__main__':
    first_list = ["Joe", "Moe", "Bo", "LoLo", "Zo"]
    last_list = ["Smith", "Rodriguez", "Hernandez", "Doe", "Phillips"]
    print(name_generator(first_list, last_list))
