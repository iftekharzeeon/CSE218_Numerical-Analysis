import matplotlib.pyplot as plt
import numpy as np

def lagInterpol(x, y, n, x_new):
    y_new = 0
    for i in range(0, n+1):
        l = 1
        for j in range(0, n+1):
            if (j != i):
                l = l * ((x_new - x[j]) / (x[i] - x[j]))
        term = l * y[i]
        y_new = y_new + term

    return y_new


def interpol(x, y, n, x_new):
    y_new = y[0][0]
    for i in range (1, n+1):
        for j in range (0, (n+1)-i):
            y[j][i] = (y[j+1][i-1] - y[j][i-1]) / (x[i+j] - x[j])
    for i in range (1, n+1):
        
        for j in range (1, i+1):
    print(y)


def relativeError(x, y, n, x_new):
    y1 = lagInterpol(x, y, n, x_new)
    print
    y2 = lagInterpol(x, y, n-1, x_new)

    error = abs(((y2 - y1) / y2) * 100)
    print(error)


x = [10, 15, 20, 22.5]

n = 3
y = [[0 for i in range(n+1)] 
        for j in range(n+1)]
y[0][0] = 227.04
y[1][0] = 362.78
y[2][0] = 517.35
y[3][0] = 602.97
print(y)
xnew = 16
# relativeError(x, y, n, xnew)

interpol(x, y, n, xnew)


x.sort()
y.sort()



# plt.figure(figsize=(12, 10))
# plt.title("Graph of Bisection Method")

# plt.plot(x, y, 'b')

# axis1 = np.arange(-15, 15, 0.1)
# axis2 = axis1 * 0
# plt.plot(axis2, axis1, 'k')
# plt.plot(axis1, axis2, 'k')

# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid()
# plt.show()

# from sympy import *
# x = Symbol('x')
# f = (x-4)*(x+8)
# f_prime = f.diff(x)
# print(f)
# print(f_prime)
# f_prime = lambdify(x, f_prime)
# print(f_prime(2))
