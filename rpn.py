#!/usr/bin/env python3

def calculate(arg):
    #stack for calculator
    stack = []

    #tokenize input
    tokens = arg.split()

    #process tokens
    try:
        value = int(token)
        stack.append(value)
    except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
           elif token == '-':
                result = val1 - val2

           stack.append(result)
           return stack[0]

def main():
    while True:
        calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
