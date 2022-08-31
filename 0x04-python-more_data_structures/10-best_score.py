#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        m = list(a_dictionary.values())
        n = list(a_dictionary.keys())
        return (n[m.index(max(m))])
