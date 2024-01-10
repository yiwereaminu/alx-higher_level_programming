#!/usr/bin/python3

def element_at(my_list, idx, element):
    for i in my_list:
        if idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list
        else:
            my_list[iidx] = element
