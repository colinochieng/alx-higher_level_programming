#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc


    a = 10
    b = 5

    tot = calc.add(a, b)
    pro = calc.mul(a, b)
    quotient = calc.div(a, b)
    diff = calc.sub(a, b)

    print('{0} + {1} = {2}\n{0} -\
    {1} = {3}'.format(a, b, tot, diff))
    print('{0} * {1} = {2}\n{0} /\
    {1} = {3}'.format(a, b, pro, quotient))
