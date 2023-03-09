#!/usr/bin/python3
def magic_calculation(a, b):
   import magic_calculation_102 as calc

    if a < b:
        c = calc.add(a, b)
        for i in range(4, 7):
            c = calc.add(c, i)
        return (c)
    else:
        return(calc.sub(a, b))
