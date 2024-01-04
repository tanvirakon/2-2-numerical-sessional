#ramanujan method

import sympy as sp


def ramanujan(func):
    poly = sp.Poly(func, x)
    coeffs = poly.coeffs()  # a1,a2,a3...coefficients
    last_number = -coeffs[-1]  # a3 / coefficient without x / last x
    As = []  # store all a
    for i in reversed(coeffs):
        if i is not coeffs[-1]:
            As.append((i / last_number))
    Bs = [1, As[0]]  # found b1,b2
    x0 = Bs[0]  # b1
    x1 = Bs[1]  # b2
    k = 2  # need to find from b3(index 0 based) by loop
    iteras = 0
    max_iteras = 7
    y = x0 / x1  # 1st root
    newy = -1  # 2nd root..suppose its any number just to enter the loop
    while abs(y - newy) < 1e8 and iteras < max_iteras:
        y = x0 / x1
        sum = 0  # to find new b through loop
        a = 0  # to iterasate over a1,a2...
        b = k - 1  # iterasate over b2,b1...
        while a < k and b >= 0:
            # bk = a1*bk-1 + a2*bk-2 ...+ak-1*b1
            if a >= len(As) or b < 0:  # if not present -> means As[i]=0
                sum += 0
            else:
                sum += (As[a] * Bs[b])
            a += 1
            b -= 1
        Bs.append(sum)  # new bk found
        x0 = x1
        x1 = Bs[k]
        newy = x0 / x1  # next root
        k += 1  # next bk
        iteras += 1
    return newy, iteras


x = sp.Symbol("x")
main_eq = x ** 3 - 9 * x ** 2 + 26 * x - 24

root, iteras = ramanujan(main_eq)
print(f"root = {float(root)}")
print(f"iterasation = {iteras}")