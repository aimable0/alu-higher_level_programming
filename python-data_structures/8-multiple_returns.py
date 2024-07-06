#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    for letter in sentence:
        length = length + 1
    char_1 = sentence[0]
    len_and_char1 = (length, char_1)
    return len_and_char1
