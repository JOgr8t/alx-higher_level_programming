#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_int_list = []
    for a in my_list:
        if a not in unique_list:
            unique_int_list.append(a)
    for a in unique_int_list:
        sum += a
    return (sum)
