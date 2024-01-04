#newton rapshon

def newton_rafson(func, func_derivative, x0 , tol=1e-15, max_iter=100):
  x=x0
  iter_count= 0

  while iter_count < max_iter:
    f_x = func(x)
    f_prime_x = func_derivative(x)

    if abs(f_x) <tol:
      return x,iter_count

    if f_prime_x ==0:
      return None, iter_count

    x=x-f_x /f_prime_x
    iter_count +=1


def cubic_function(x):
  return x ** 3- 4 *x**2 - x+4

def cubic_function_derivative(x):
  return 3*x**2-8*x-1

initial_guess = 3.0
root , iterations = newton_rafson(cubic_function, cubic_function_derivative,initial_guess)

if root is not None:
  print(f"root found at x= {root}, iteration ={iterations}")
else:
  print(f"did not coverage within the specified tolerance")