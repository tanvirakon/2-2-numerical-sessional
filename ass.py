import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

data = pd.read_csv('populaton_data.csv')  # reading the csv file
print(data)


# curve fitting
def linear_least_squares(x, y):
    x = np.array(x)  # this will make tha array from array x
    y = np.array(y)  # this will make tha array from array y
    n = len(x)  # size of input
    sum_x = np.sum(x)  # sum of all years
    sum_y = np.sum(y)  # sum of all population
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)  # find value of b
    a = (sum_y - b * sum_x) / n  # find value of a
    return b, a  # return b and a


def predict_values(x, b, a):
    x = np.array(x)
    y_pred = b * x + a  # formula for determine value of y
    return y_pred


def plot_linear_fit(x, y, b, a, x_predict=None, y_predict=None):  # this function will plot the graph
    x = np.array(x)  # this will make tha array from array x
    y = np.array(y)  # this will make tha array from array y
    plt.scatter(x, y, label='Data Points')  # it can be used to create scatter plots
    plt.plot(x, b * x + a, color='black', label=f'Linear Fit: y = {b:.2f}x + {a:.2f}')  # plots y vs x graph
    plt.scatter(x_predict, y_predict, color='green', label='Predicted Values')
    plt.xlabel('X-Axis')  # label x axis
    plt.ylabel('Y-Axis')  # label y axis
    plt.title('curve fitting')  # title for graph
    plt.legend()  # labels data by color
    plt.show()  # shows the graph


year = data['year'].tolist()  # taking year from the csv file
population = data['population'].tolist()  # taking population from the csv file

year_predict = [2023, 2024, 2025, 2026,2027,2028,2029,2030,2031,2032]  # this year has to predict
b, a = linear_least_squares(year, population)

population_predict = predict_values(year_predict, b, a)  # we will get the population for the year after putting the values in formula
print(f'Linear Equation: y = {b:.2f}x + {a:.2f}')
z=zip(year_predict,population_predict)
print(f'Predicted populaton:')
for i,j in z:
  print(i,math.floor(j))

plot_linear_fit(year, population, b, a, year_predict, population_predict)  # draw the graph






# newton interpolation
def print_fd(forward_diff):
    for index in forward_diff:
        for element in index:
            print(element, end='')
        print('\n')


def newton_backward_difference(x, y, xi):
    n = len(x)
    h = x[1] - x[0]
    backward_diff = [y]

    for i in range(1, n):  # element 7ta , del^7 y prjnto jabe
        next_diff = []
        for j in range(n - i):  # i ta element thakle, next e i-1 ta elemnt hbe
            # print(f"n - i: {n - i}, j: {j}, i: {i}")
            next_diff.append(backward_diff[i - 1][j + 1] - backward_diff[i - 1][j])
        backward_diff.append(next_diff)
    # print(f"{forward_diff}")

    # calculate population of next year by newton raphson
    result = y[-1]
    u = (x[-1] - xi) / h

    # drawing the dataframe
    df = pd.DataFrame(backward_diff).transpose()
    df.index = x
    df.columns = [f'D{n}' for n in range(n)]


    for i in range(1, n):
        term = backward_diff[i][-1]
        # print(term)
        for j in range(i):
            term *= (u + j)
            term /= (j + 1)
        result += term

    return result, df


xi=2019
interpolated_value, difference_table = newton_backward_difference(year, population, xi)
print('population at', xi, 'will be: ', interpolated_value)
# print(difference_table)




# newton raphson
import math


def newton_rafson(func, func_derivative, x0, tol=1e-15, max_iter=100):
    x = x0
    iter_count = 0

    while iter_count < max_iter:
        f_x = func(x)
        f_prime_x = func_derivative(x)

        if abs(f_x) < tol:
            return x

        x = x - f_x / f_prime_x
        iter_count += 1


# year have to dind for population y
y = 2000000


# equation found in desmos after plotting all the points
def cubic_function(x):
    return 8346.47 * x - 15418581.79 - y


# derivative of the main equation
def cubic_function_derivative(x):
    return 8346.47


initial_guess = 2025  # lets say our population will touch at number y in 2025
root = newton_rafson(cubic_function, cubic_function_derivative, initial_guess)

print(f'population will be {y} in year {math.ceil(root)}')
