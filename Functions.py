import math

#functions for the Calculator:

def multiply(x, y):
    sum = x * y
    return str(x) + ' x ' + str(y) + ' = ' + str(sum)

sum = multiply(10, 2)

print(sum)


def divide(x, y):
    sum = x / y
    return str(x) + ' / ' + str(y) + ' = ' + str(sum)


def plus(x, y):
    sum = x + y
    return str(x) + ' + ' + str(y) + ' = ' + str(sum)


def minus(x, y):
    sum = x - y
    return str(x) + ' - ' + str(y) + ' = ' + str(sum)


def exponent(x, y):
    sum = x ** y
    return str(x) + ' ** ' + str(y) +  ' = ' + str(sum)

def root(x):
    return  math.sqrt(x)











