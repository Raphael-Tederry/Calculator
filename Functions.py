import math

#functions for the Calculator:

def multiply(str_x, str_y):
    if str_x.isdigit() and str_y.isdigit():
        result = int(str_x) * int(str_y)
        return str(result) if isinstance(result, int) else str(round(result, 6))
    else:
        try:
            result = float(str_x) * float(str_y)
            return str(int(result)) if isinstance(result, int) else str(round(result, 6))
        except ValueError:
            return 'Math Error'


def divide(str_x, str_y):

    if str_x.isnumeric() and str_y.isnumeric() and int(str_y) != 0 :
        result = int(str_x) / int(str_y)
        return str(result) if isinstance(result, int) else str(round(result, 6))
    else:
        try:
            if float(str_y) != 0:
                result = float(str_x) / float(str_y)
                return str(int(result)) if isinstance(result, int) else str(round(result, 6))
        except ValueError:
            return 'Math Error'


def plus(str_x, str_y):
    try:
        result = float(str_x) + float(str_y)
        # 2.2  or  2.0   2        0.0  or 0.2
        return str(int(result)) if result - int(result) == 0 else str(round(result, 6))
    except ValueError:
        return "Math Error"


def minus(str_x, str_y):
    if str_x.isdigit() and str_y.isdigit():
        result = int(str_x) - int(str_y)
        return str(result) if isinstance(result, int) else str(round(result, 6))
    else:
        try:
            result = float(str_x) - float(str_y)
            return str(int(result)) if isinstance(result, int) else str(round(result, 6))
        except ValueError:
            return "Math Error"



def exponent(str_x, str_y):
    if str_x.isdigit() and str_y.isdigit():
        sum = math.pow(int(str_x), int(str_y))
        return str(int(sum)) if sum.is_integer() else str(sum)
    else:
        try:
            sum1 = math.pow(float(str_x), int(str_y))
            return str(int(sum1)) if sum1.is_integer() else str(sum1)
        except ValueError:
            return "Math Error"

def root(str_x):
    if str_x.isdigit() and int(str_x) >= 0:
        sum = math.sqrt(int(str_x))
        return str(int(sum)) if sum.is_integer() else str(sum)
    else:
        try:
           sum1 = math.sqrt(float(str_x))
           return str(int(sum1)) if sum1.is_integer() else str(sum1)
        except ValueError:
            return "Math Error"






def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == "__main__":

    r = plus('5a2', '2')
    print(r)












