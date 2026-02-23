from functools import reduce

def sum_nums(*args):
    return sum(args)

def subtract_nums(*args):
    return reduce(lambda x, y: x - y, args)

def multiply_nums(*args):
    return reduce(lambda x, y: x * y, args)

def divide_nums(*args):
    return reduce(lambda x, y: x / y, args)

mapper = {
    '+': sum_nums,
    '-': subtract_nums,
    '*': multiply_nums,
    '/': divide_nums
}

def operate(op, *args):
    func = mapper[op]
    return func(*args)

print(operate('+', 1, 2, 3))