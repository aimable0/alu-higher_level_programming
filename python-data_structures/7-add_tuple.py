#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) > 1 and len(tuple_b) > 1:
        add_1 = tuple_a[0] + tuple_b[0]
        add_2 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        add_1 = tuple_a[0] + tuple_b[0]
        add_2 = 0
    elif len(tuple_a) > 1 and len(tuple_b) <= 1:
        if len(tuple_b) == 1:
            add_1 = tuple_a[0] + tuple_b[0]
        else:
            add_1 = tuple_a[0]
        add_2 = tuple_a[1]
    elif len(tuple_a) <= 1 and len(tuple_b) > 1:
        if len(tuple_a) == 1:
            add_1 = tuple_a[0] + tuple_b[0]
        else:
            add_1 = tuple_b[0]
        add_2 = tuple_b[1]
    else:
        add_1 = 0
        add_2 = 0

    added_tuple = (add_1, add_2)

    return added_tuple
