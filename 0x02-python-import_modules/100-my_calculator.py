#!/usr/bin/python3
from sys import argv
from calculator_1 import calc


if __name__ == "__main__":

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
