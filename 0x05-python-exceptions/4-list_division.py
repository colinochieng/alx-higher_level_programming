#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = 0
    new_list = []
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
        i += 1
    return new_list
