#!/usr/bin/env python3
# Using a list comprehension, write a function return_evens() that returns a list of all of the even elements of a sequence of integers.
def return_evens(num_list):
    even_nums = [n for n in num_list if (n/2).is_integer() == True]
    return even_nums

# takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end.
def make_exclamation(sentence_list):
    new_string = [n + '!' for n in sentence_list]
    return new_string