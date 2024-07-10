#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_scores = list(sorted(a_dictionary.values()))
    best_score = best_scores[-1]

    for key, value in a_dictionary.items():
        if value == best_score:
            return key
