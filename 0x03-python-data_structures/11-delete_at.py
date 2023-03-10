#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    values = len(my_list) - 1
    if idx < 0 or values < idx:
        return (my_list)
    new = my_list[:idx] + my_list[idx+1:]
    i = my_list[idx]
    my_list.remove(i)
    return (new)
