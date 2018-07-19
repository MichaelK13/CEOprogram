"""
title:$(NAME)
author: Michael
date:$(date)$(title)
"""

def fill_ticket():
    guess_list = []
    for snickers in range(5):
        num = input('Enter a number: ')
        guess_list.append(num)
    return guess_list


def create_word(list_input):
    output = ''
    for i in name:
        output += i
    return output


if __name__ == "__main__":
    guesses = fill_ticket()
    print(guesses)
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
    create_word(letters)


def find_matches(secret, guesses):
    num_matches = 0
    for i in range(5):
        if int(secret[i]) == int(guesses[i]):
            num_matches += 1
    return num_matches


def short_hand(phrase):
    phrase = phrase.replacing("for", "4")
    phrase = phrase.replacing("too", "2")
    phrase = phrase.replacing("and", "&")
    phrase = phrase.replacing("you", "123456789")
    phrase = phrase.replacing("You", "123456789")

    removing = "aeiouAEIOU"



if __name__ == "__main__":
    name = "elizabeth"
    name = name. replace("e", "")
    print(name)
    guesses = fill_ticket()


def matches(ticket, winners):
    "takes two lists and returns an integer that says how many numbers the two lists are in the exact same position"
    guesses = fill_ticket()
    winners = [1, 2, 3, 4, 5]
    print(matches(guesses, winners))


