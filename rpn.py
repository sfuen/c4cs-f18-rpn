#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(myarg, stack):
    for token in myarg.split():
        if token == "rotate":
            stack.reverse()
            continue
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    return stack[-1]

def main():
    stack = list()
    while True:
        print("rpn calculator ", stack, ">> ", end="")
        inp = input()
        result = calculate(inp, stack)
        for key in operators.keys():
            if inp.endswith(key):
                print("Result: ", result)

if __name__ == '__main__':
    main()
