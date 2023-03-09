import math

#functions for the Calculator:

def multiply(str_x, str_y):
    if str_x.isnumeric() and str_y.isnumeric():
        sum = int(str_x) * int(str_y)
        return str(sum)
    else:
        return "Invalid input"


def divide(str_x, str_y):

    if str_x.isnumeric() and str_y.isnumeric() and int(str_y) != 0 :
         sum = int(str_x) / int(str_y)
         return str(sum)
    else:
       return 'Math Error'




def plus(str_x, str_y):
    if str_x.isnumeric() and str_y.isnumeric():
        sum = int(str_x) + int(str_y)
        return str(sum)
    else:
        return "Math Error"


def minus(str_x, str_y):
    if str_x.isnumeric() and str_y.isnumeric():
        sum = int(str_x) - int(str_y)
        return str(sum)
    else:
        return "Math Error"


def exponent(str_x, str_y):
    if str_x.isnumeric() and str_y.isnumeric():
        sum = int(str_x) ** int(str_y)
        return str(sum)
    else:
        return "Math Error"

def root(str_x):
    if str_x.isnumeric() and int(str_x) >= 0:
        return str(math.sqrt(int(str_x)))
    else:
        return 'Math Error'


if __name__ == "__main__":

    r = root('10')
    print(r)











