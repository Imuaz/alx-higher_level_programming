#!/usr/bin/python3
def best_score(a_dictionary):
    if my_dict is None or my_dict == {}:
        return None
    biggest = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest:
            return key
