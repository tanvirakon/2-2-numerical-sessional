import numpy as np
import matplotlib.pyplot as plt


def linear_least_squares(x, y):
    x = np.array(x)
    y = np.array(y)

    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    # b = (n * sum_xy - sum_y) / (n * sum_x_squared - sum_x)
    a = (sum_y - b * sum_x) / n
    return b, a


def predict_values(x, b, a):
    x = np.array(x)
    y_pred = b * x + a
    return y_pred


def plot_linear_fit(x, y, b, a, x_predict=None, y_predict=None):
    x = np.array(x)
    y = np.array(y)
    plt.scatter(x, y, label='Data Points')
    # print(type(x))
    # print(type(y))
    plt.plot(x, b * x + a, color='black', label=f'Linear Fit: y = {b:.2f}x + {a:.2f}')

    # if x_predict is not None and y_predict is not None:
    plt.scatter(x_predict, y_predict, color='green', label='Predicted Values')

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Linear Regression Fit')
    plt.legend()

    # Show the plot
    plt.show()


# Exabple usage:
x_data = [1, 2, 3, 4, 5]
# y_data = [2, 3, 2.5, 4, 3.5]

y_data = [.6, 2.4, 3.5, 4.8, 5.7]
b, a = linear_least_squares(x_data, y_data)

print(f'Linear Equation: y = {b:.2f}x + {a:.2f}')

x_predict = [6, 7, 8]
y_predict = predict_values(x_predict, b, a)

print(f'Predicted Values for x_predict: {y_predict}')

plot_linear_fit(x_data, y_data, b, a, x_predict, y_predict)
