# false position

# if i increase max_itr, program runs till (count <= max_itr) but ans doesnt become anymore precise........nande?!
def solve(func, a, b):
    tol = 1e-4
    max_itr = 50
    count = 0
    if func(a) * func(b) >= 0:
        print(f"initial value error")
    while (b - a) > tol and count <= max_itr:
        xr = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(xr) == 0:
            return xr, count
        elif func(a) * func(xr) < 0:
            b = xr
        else:
            a = xr
        count += 1
    xr = (a * func(b) - b * func(a)) / (func(b) - func(a))
    return xr, count


initial_guess = (2, 3)


def eq(x):
    return x**3 - 2 * x - 5


root, req_iter = solve(eq, *initial_guess)
print(f"root is = {root}")
print(f"iteration requried is = {req_iter}")