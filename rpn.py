#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def rotate_stack(stack):
    stack.reverse()

def copy_stack(stack):
    stack.insert(0, stack[0])

stack_ops = {
    'rotate': rotate_stack,
    'copy': copy_stack
}

def calculate(myarg, stack):
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            for command in stack_ops:
                if token == command:
                    function = stack_ops[token]
                    function(stack)
                    break
            else:
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
