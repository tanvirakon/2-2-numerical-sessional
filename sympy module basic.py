# Import sympy library
import sympy as sp

# Define the variable x
x = sp.Symbol('x')

# Define the equation
eq = x**3 - 9 * x**2 + 26 * x - 24

# Convert the equation to a polynomial object
poly = sp.Poly(eq, x)

# Get the coefficients and powers of x as lists
coeffs = poly.coeffs()
powers = poly.monoms()

# Print the results
print("Coefficients:", coeffs)
print("Powers:", powers)
