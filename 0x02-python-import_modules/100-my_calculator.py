#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    import calculator_1 as calc

    count = len(argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if op == "+":
        print("{} + {} = {}".format(a, b, (calc.add(a, b))))
    elif op == "-":
        print("{} - {} = {}".format(a, b, (calc.sub(a, b))))
    elif op == "*":
        print("{} * {} = {}".format(a, b, (calc.mul(a, b))))
    elif op == "/":
        print("{} / {} = {}".format(a, b, (calc.div(a, b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
