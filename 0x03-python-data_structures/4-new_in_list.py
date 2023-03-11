#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    value = len(my_list) - 1
    if idx < 0 or value < idx:
        return (my_list)
    else:  
        new = []
        i = 0
        while i <= value:
            new.append(my_list[i])
            i += 1
        new[idx] = element
        return (new)
