def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("--- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("--- Lovely plumage, the", type)
    print("--- It's", state, "!")
    print("***")


# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=1000000, action='VOOOOOM')
# parrot(action='VOOOOOM', voltage=1000000)
# parrot('a million', 'bereft of life', 'jump')
# parrot('a thousand', state='pushing up the daisies')


# def make_incrementor(n):
#     return lambda x: x + n
#
#
# f = make_incrementor(88)
# print(f(22))


def my_function():
    """
    do nothing, but document it.

    No, really, it doesn't do anything
    :return:
    """
    pass

print(my_function.__doc__)

