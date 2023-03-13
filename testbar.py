import Functions as f

d = {"/": f.divide, "*": f.multiply, "-": f.minus, "+": f.plus}


def reform_paragraph(sentence):
    """
    this function will receive a sentence(how will contain a full paragraph) and will add the missing lines
     everywhere there is a dot.
    :param sentence: a string of one sentence
    :return: the full paragraph as a string
    """

    pass


def my_eval(str1):
    for operator, func in d.items():
        if operator in str1:
            a, b = str1.split(operator)
            print(func(a, b))
    return eval(str1)


if __name__ == '__main__':
    # math_stuff('09+88')
    sentence = "Mitzee was in prison for a crime he did not commit.Well, OK, he probably had committed it once or " \
               "twice.Who knew? Who kept count? But he was very sure that he had been incarcerated now because of " \
               "something he didn’t do. He glared through the prison bars, plotting. He was Houdini, Al Capone, " \
               "and Einstein rolled into one. There was nothing he couldn’t do… except break out of this prison, " \
               "apparently. "

    reform_paragraph(sentence)

    ss = '3.7'
    s = float(ss)


    print(s)

"""
    s = ''
    for c in sentence:
        s += c if c != '.' else c + '\n'
    print(s == sentence.replace('.', '.\n'))
    print(s == sentence.replace('.', '.\n'))
    print(s == sentence.replace('.', '.\n'))
"""