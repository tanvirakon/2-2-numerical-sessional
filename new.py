import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def linear_least_squares(x, y):
    x = np.array(x)
    y = np.array(y)

    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(np.power(x,2))


    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - m * sum_x) / n

    return m, b

def predict_values(x, m, b):
    x = np.array(x ,dtype=int)
    y_predicted = m * x + b
    y1_predicted=np.array(y_predicted,dtype=int)
    return y1_predicted

def plot_linear_fit(x, y, m, b, x_predict, y_predict):
    x = np.array(x,dtype=int)
    plt.figure(figsize=(13,6))
    plt.scatter(x, y, label='Data Points')
    plt.plot(x, m * x + b, color='r', label=f'Linear Fit: y = {m:.2f}x + {b:.2f}')
    plt.scatter(x_predict, y_predict, color='green', label='Predicted Values')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(np.arange(2014,2035,1))
    plt.legend()
    plt.show()

d=pd.read_csv('populaton_data.csv')
year = d['year'].tolist()
population = d['population'].tolist()
m, b = linear_least_squares(year,population)
print(f'Linear Equation: y = {m:.2f}x + {b:.2f}')


# year_predict = [2025, 2026, 2027, 2028,2029, 2030,2031,2032,2033,2034]
year_predict = [2023]
population_predict = predict_values(year_predict, m, b)
print(f'Predicted Values for year_predict: {population_predict}')

plot_linear_fit(year, population, m, b, year_predict, population_predict)