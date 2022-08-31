#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_list = []
    for a in my_list:
        if a not in unique_list:
            unique_list.append(a)
    for a in unique_list:
        sum += a
    return (sum)
