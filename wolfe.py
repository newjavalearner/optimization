#bisection search of wolfe condition

import random
import numpy as np


def func(x):
    return 100*np.square(np.square(x[0])-x[1]) + np.square(x[0]-1)


def dfunc(x):
    df1 = 400*x[0]*(np.square(x[0])-x[1])+2*(x[0]-1)
    df2 = -200*(np.square(x[0])-x[1])
    return np.array([df1, df2])


def wolfe(valf, direction, max_iter):

    alpha = 0
    beta = 1000
    i = 0
    step = 5.0
    c1 = 0.15
    c2 = 0.3

    stop_iter = 0
    stop_val = valf
    minima = 0
    while i <= max_iter:
        # first confition
        leftf = func(valf + step*direction)
        rightf = func(valf) + c1*dfunc(valf).dot(direction)
        print leftf, rightf
        if leftf > rightf:
            beta = step
            step = .5*(alpha + beta)
        elif dfunc(valf + step*direction).dot(direction) < c2*dfunc(valf).dot(direction):
            alpha = step
            if beta > 100:
                step = 2*alpha
            else:
                step = .5*(alpha + beta)
        else:
            break
        i += 1
        stop_val = valf+step*direction
        stop_iter = i
        minima = func(stop_val)
    return stop_val, minima, stop_iter, step

start = np.array([.6, .5])
direction = np.array([-.3, -.4])
converge_value, minimal, no_iter, size = wolfe(start, direction, 30)
print "The value, minimal and iterations needed are " + str(converge_value) + ", " + str(minimal) + ", " + str(no_iter) + ', ' + str(size)
