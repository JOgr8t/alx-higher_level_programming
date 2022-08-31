#!/usr/bin/python3
def search_replace(my_list, search, replace):
    Newlist = my_list.copy()
    i = 0
    for a in my_list:
        if a is search:
            Newlist[i] = replace
        i += 1
    return (Newlist)
