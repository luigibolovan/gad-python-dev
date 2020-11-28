# Assignment 2

# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă numere întregi sau reale
def get_sum_of_params(*args, **kwargs):
    param_sum = 0

    for arg in args:
        param_sum += arg if (type(arg) == int) or (type(arg) == float) else 0

    return param_sum


print('Suma parametrilor:', get_sum_of_params(1, 2, -4, 'ab', 7, param=1), '\n')


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează
# - suma tuturor numerelor de la [0, n]
# - suma numerelor pare de la [0, n]
# - suma numerelor impare de la [0, n]
def recursive_sum(int_num):
    if int_num == 0:
        return 0

    return recursive_sum(int_num - 1) + int_num


def recursive_even_sum(int_num):
    if int_num == 0:
        return 0

    return recursive_even_sum(int_num - 1) + int_num if int_num % 2 == 0 else recursive_even_sum(int_num - 1)


def recursive_odd_sum(int_num):
    if int_num == 0:
        return 0

    return recursive_odd_sum(int_num - 1) + int_num if int_num % 2 != 0 else recursive_odd_sum(int_num - 1)


# [sum(0,n), sum_even(0,n), sum_odd(0,n)]
def recursive_sums(int_num):
    if int_num == 0:
        return 0, 0, 0

    return (recursive_sums(int_num - 1)[0] + int_num,
            recursive_sums(int_num - 1)[1] + (int_num if int_num % 2 == 0 else 0),
            recursive_sums(int_num - 1)[2] + (int_num if int_num % 2 != 0 else 0))


sums = recursive_sums(5)
print(f'Suma [0,n]: {sums[0]}; Suma pare [0,n]: {sums[1]}; Suma impare [0,n]: {sums[2]};\n')


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0
def get_int_from_keyboard():
    keyboard_int = input("Int: ")
    try:
        return int(keyboard_int)
    except ValueError as error:
        print(f'An error occurred: {error}')
        return 0


print('Input:', get_int_from_keyboard())
