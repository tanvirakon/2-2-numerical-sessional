# iteration method


def iteration_method(func, fai, x0):
    x = x0
    tol = 1e-15
    iter_item = 1
    max_item = 50
    a = fai(x)
    b = fai(a)
    x = b
    xr = 0
    # print(a)
    # print(b)
    while iter_item < max_item and abs(a - b) > tol:
        a = xr
        xr = fai(x)
        x = xr
        iter_item += 1
        # print(abs(a - b))
    return xr, iter_item


import math

intitial_guess = 0.5


def main_func(x):
    return x - math.exp(-x)


def fai_func(x):
    return math.exp(-x)


root, iteration = iteration_method(main_func, fai_func, intitial_guess)

print(f"root x = {root} , iteration = {iteration}")