"""
Radoslaw Tomaszewski
poczta@radtomas.pl
"""
# TODO:
# add gui
# add keyboard support
# rewrite in EAFP error handling
from tkinter import *
from tkinter import ttk

# TODO add more operators
# Dictionary where key is a operator and value is list [priority]
operators = {
    '(': [0, ],
    ')': [0, ],
    '+': [1, lambda x, y: y + x],
    '-': [1, lambda x, y: y - x],
    '*': [2, lambda x, y: y * x],
    '/': [2, lambda x, y: y / x],
    '^': [3, lambda x, y: y ** x]
    }


def convert_to_rpn(in_expression):
    """
    Function converts infix algebraic expression into postfix
    :param in_expression: string with infix expression
    :return out_expression: tuple with postfix expression
    """

    # checking in_expression is string type
    if type(in_expression) != str:
        raise TypeError("Only string type argument, not {}".format(type(in_expression)))

    # remove all whitespace from string
    in_expression = in_expression.replace(" ", "")

    # list for prepared expression
    expression = []

    # checking for multi digits numbers
    i = 0
    while i < len(in_expression):
        if in_expression[i] in operators:
            expression.append(in_expression[i])
            i += 1
        else:
            char = in_expression[i]
            i += 1
            while in_expression[i].isdigit() or in_expression[i] == '.':
                char += in_expression[i]
                i += 1
            else:
                expression.append(char)

    # list contains operators
    stack = []
    # list contains output elements
    out_expression = []

    # loop work on single char in string
    for char in expression:
        if char in operators:
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    out_expression.append(stack.pop())
                stack.pop()
            elif char in operators:
                while len(stack):
                    if operators[char][0] == 3 or operators[char][0] >= operators[stack[-1]][0]:
                        break
                    out_expression.append(stack.pop())
                stack.append(char)
            else:
                raise ValueError("Weird operator type: {}".format(char))
        else:
            out_expression.append(char)

    # write the remaining stack elements in the list
    for i in reversed(stack):
        out_expression.append(i)

    return tuple(out_expression)


def eval_rpn(in_expression):
    """
    Evaluate expression in reverse polish notation
    :param in_expression: tuple with infix expression
    :return result: value of the in_expression
    """

    # checking in_expression is tuple type
    if type(in_expression) != tuple:
        raise TypeError("Only tuple tuple argument, not {}".format(type(in_expression)))

    # list temporary contains operators
    stack = []

    for char in in_expression:
        if char in operators:
            result = operators[char][1](stack.pop(), stack.pop())
            stack.append(result)
        else:
            stack.append(float(char))

    return result



def main():
    """
    Main function of calculator program
    :return: nothing
    """

    expression = "(44 + 403.4 * 5 - 3) / 3 ^ ((2 + 3) / 5)"
    # 4 4 5 * 3 - + 3 2 3 + 5 / ^ /

    # convert infix expression string into postfix expression tuple
    expression = convert_to_rpn(expression)

    print(" ".join(expression))

    # evaluate a reverse polish notation
    print(eval_rpn(expression))


if __name__ == "__main__":
    main()
