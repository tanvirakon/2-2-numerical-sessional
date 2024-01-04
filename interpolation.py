import pandas as pd


def print_fd(forward_diff):
    for index in forward_diff:
        for element in index:
            print(element, end='')
        print('\n')


def gauss_forward_difference(x, y, xi):
    n = len(x)
    h = x[1] - x[0]
    forward_diff = [y]

    for i in range(1, n):  # element 7ta , del^7 y prjnto jabe
        next_diff = []
        for j in range(n - i):  # i ta element thakle, next e i-1 ta elemnt hbe
            # print(f"n - i: {n - i}, j: {j}, i: {i}")
            next_diff.append(forward_diff[i - 1][j + 1] - forward_diff[i - 1][j])
        forward_diff.append(next_diff)
    # print(f"{forward_diff}")

    df = pd.DataFrame(forward_diff).transpose()
    df.index = x
    df.columns = [f'D{n}' for n in range(n)]

    # calculate the interpolation
    result = y[0]
    u = (xi - x[0]) / h
    for i in range(1, n):
        term = forward_diff[i][0]
        for j in range(i):
            term *= (u - j)
            term /= (j + 1)
        result += term

    return result, df


# Example data points
x = [1, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
y = [2.7183, 2.8577, 3.0042, 3.1582, 3.3201, 3.4903, 3.6693]
# value of interpole
xi = 1.17

interpolated_value, difference_table = gauss_forward_difference(x, y, xi)

print('Forward Diffenence Table:')
print(difference_table)

print('\nInterpolated value at', xi, 'is: ', interpolated_value)
