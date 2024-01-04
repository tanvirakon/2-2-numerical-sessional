#bisection

def bisection_method(func, a, b, tol=1e-15, max_iter=100):       #tollerance -> jto kom, toto accurate chai
#1e-6 = 1 * 10 ^ -6
  if(func(a)*func(b)>=0):
    raise ValueError(f"function has the same sign at both endpoints.")

  iter_count=0
  while (b-a) / 2.0>tol and iter_count<max_iter: #sutro
    c=(a+b)/2.0
    if func(c)==0.0:
      return c,iter_count
    elif func(c) * func(a) < 0:
      b=c
    else:
      a=c
    iter_count+=1

  root = (a+b)/2.0
  return root, iter_count

def quadratic_function(x):
  return x**3 - 2*x -5

initial_interval= (2,3) #err mdde root ache
root,iterations= bisection_method(quadratic_function, *initial_interval) #2ta value return krbe

if root is not None:
  print('root found at x= ', root , 'after ',iterations, 'iterations.')
else:
  print(f"bisection method did not converge within the specified tolerance.")