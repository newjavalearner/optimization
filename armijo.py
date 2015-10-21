import random
import numpy as np

# the objective function
def func(x):
    return 100*np.square(np.square(x[0])-x[1])+np.square(x[0]-1)

# first order derivatives of the function
def dfunc(x):
    df1 = 400*x[0]*(np.square(x[0])-x[1])+2*(x[0]-1)
    df2 = -200*(np.square(x[0])-x[1])
    return np.array([df1, df2])

# the algorithm
def armijo(valf, grad, niters):
    beta = random.random()
    sigma = random.uniform(0, .5)
    # beta = 0.25
    # sigma = 0.25
    miter = 0
    conval = 0
    iter_conv = 0
    while miter <= niters:
        leftf = func(valf+np.power(beta, miter)*grad)
        rightf = func(valf) + sigma*np.power(beta, miter)*dfunc(valf).dot(grad)
        if leftf-rightf <= 0:
            iter_conv = miter
            conval = valf+np.power(beta, iter_conv)*grad
            break
        miter += 1
    return conval, func(conval), iter_conv

#initialization
start = np.array([-1, 1])
direction = np.array([1, -2])
maximum_iterations = 30

converge_value, minimal, no_iter = armijo(start, direction, maximum_iterations)
print "The value, minimal and number of iterations are " + str(converge_value) + ", " + str(minimal) + ", " + str(no_iter)
