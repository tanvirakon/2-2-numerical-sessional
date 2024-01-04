import numpy as np
import matplotlib.pyplot as plt

def func(x):
    # Define the function to be integrated
    return x**2  # You can replace this with your own function

def trapezoidal_rule(func, a, b, n):
    # Trapezoidal Rule for numerical integration
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    integral = h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)
    return integral

def simpsons_one_third_rule(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals must be even for Simpson's 1/3 Rule.")

    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)

    integral = h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])
    return integral

def plot_function_and_integral(func, a, b, n):
    x = np.linspace(a, b, 1000)
    y = func(x)

    plt.plot(x, y, label='Function to be Integrated')
    plt.fill_between(x, y, alpha=0.1, color='blue', label='Area under the curve')

    # Trapezoidal Rule
    integral_trapezoidal = trapezoidal_rule(func, a, b, n)
    plt.title(f'Trapezoidal Rule\nIntegral: {integral_trapezoidal:.4f}')

    #Simson's Rule
    integral_simpson = simpsons_one_third_rule(func, a, b, n)
    plt.title(f'Simpson\'s 1/3 Rule\nIntegral: {integral_simpson:.4f}')

    plt.legend()
    plt.show()

# Define the interval [a, b] and the number of subintervals n
a = 0
b = 2
n = 4  # You can adjust the number of subintervals

plot_function_and_integral(func, a, b, n)