#!/usr/bin/env python3
import operator


op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def calculate(arg):
    #stack for calculator
    stack = arg.split()

    #process tokens
    while len(stack) > 1:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            #Look up function in table
            func = op[token]
            result = func(val1, val2)

            stack.append(result)
            
    return int(stack[0])

def main():
    while True:
        calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
