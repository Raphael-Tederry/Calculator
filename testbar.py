import math
def eval(equation):
    return equation.split()


def math_stuff(snum1, snum2):
    print(snum2.isnumeric())
    int(snum2)

    if snum1 > 1:
        pass
    if snum1 < 0:
        pass
    else:pass

if __name__ == '__main__':
    # math_stuff('09+88')
    s = '01234X+7X89'
    b = '99'
    while True:
        if "X" in s:
            s = s.replace('X', b)
            break

    print(s)

