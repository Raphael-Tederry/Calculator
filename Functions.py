import math

#functions for the Calculator:

def multiply(str_x, str_y):
        sum = str_x * str_y
        return str(sum)


def divide(str_x, str_y):

    if str_y == 0:
        return 'Error'
    else:
        sum = str_x / str_y
    return  str(sum)



def plus(str_x, str_y):
    sum = str_x + str_y
    return  str(sum)


def minus(str_x, str_y):
    sum = str_x - str_y
    return  str(sum)


def exponent(str_x, str_y):
    sum = str_x ** str_y
    return  str(sum)

def root(str_x):
    if str_x < 0:
        return 'Error'
    return  math.sqrt(str_x)


if __name__ == "__main__":

    r = root(10)
    print(r)











