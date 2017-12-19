import requests
from random import randint


def word_list_sum(word_list):

    sum = 0
    for word, value in word_list.items():
        sum += value

    return sum


def retrieve_random_word(word_list):

    rand_index = randint(1, word_list_sum(word_list))
    for word, value in word_list.items():
        rand_index -= value
        if rand_index <= 0:
            return word


def build_word_dict(text):

    # Remove newlines and quotes
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')

    # Make sure punctuation marks are treated as their own "words,"
    # so that they will be included in the Markov chain
    