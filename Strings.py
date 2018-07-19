"""
title:$(NAME)
author: Michael
date:$(date)$(title)
"""


def how_eligible(essay):
    "Returns how many categories are in a string"
    count = 0
    if '!' in essay:
        count += 1
    elif '"' in essay:
        count += 1
    else '?' in essay:
        return count


if __name__ == '__main__':
        print(how_eligible('This? "Yes." No, not really!'))
        print(how_eligible('Really, not a compound sentence.'))