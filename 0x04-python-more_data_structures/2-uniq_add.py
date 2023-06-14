#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    n = 0
    for i in uniq_lst:
        n += i
    return (n)
