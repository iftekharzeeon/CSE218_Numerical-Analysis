import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *

def lagInterpol(x, y, n, x_new):
    y_new = 0
    for i in range(0, n + 1):
        l = y[i]
        for j in range(0, n + 1):
            if j != i:
                l = l * ((x_new - x[j]) / (x[i] - x[j]))

        y_new = y_new + l

    return y_new


def lagInterpol_integ(x, y, n):
    x_new = Symbol('x')
    y_new = 0
    for i in range(0, n + 1):
        l = y[i]
        for j in range(0, n + 1):
            if j != i:
                l = l * ((x_new - x[j]) / (x[i] - x[j]))

        y_new = y_new + l
    return y_new

def relativeError(x, x_rel, y, y_rel, n, x_new):
    y1 = lagInterpol(x, y, n, x_new)
    y2 = lagInterpol(x_rel, y_rel, n-1, x_new)
    error = abs((y1 - y2)/y1) * 100
    return error


n = 3
v1 = [22, 25, 27, 30]
v1_new = 28
p1 = [44, 43, 42, 40]

v1_rel = [25, 27, 30]
p1_rel = [43, 42, 40]

v2 = [30, 31, 35, 37]
p2 = [40, 35, 30, 25]
v2_new = 32

v2_rel = [30, 31, 35]
p2_rel = [40, 35, 30]

p1_new = lagInterpol(v1, p1, n, v1_new)
print("The pressure at Volume ", v1_new , "cubic m is ", p1_new, " Pa\n")

p2_new = lagInterpol(v2, p2, n, v2_new)
print("The pressure at Volume ", v2_new, " cubic m is ", p2_new, " Pa\n")

error1 = relativeError(v1, v1_rel, p1, p1_rel, n, v1_new)
error2 = relativeError(v2, v2_rel, p2, p2_rel, n, v2_new)

print("The relative error for case 1: ", error1)
print("The relative error for case 2: ", error2)

v1_sorted = v1
v1_sorted.append(v1_new)
p1_sorted = p1
p1_sorted.append(p1_new)

v2_sorted = v2
v2_sorted.append(v2_new)
p2_sorted = p2
p2_sorted.append(p2_new)


# Plotting the graphs
lower = 10
upper = 70
plt.ylim([lower, upper])  # limiting y axis value
# plt.plot([-3, 10], [0, 0], color='blue')  # x-axis
# plt.plot([0, 0], [-15, 15], color='blue')  # y-axis
plt.plot(v1_sorted, p1_sorted, color='green', linestyle='dashed', linewidth=2)  # main graph
plt.plot(v1_new, p1_new, color='blue', linestyle='-')

plt.plot(v2_sorted, p2_sorted, color='red', linestyle='dashed', linewidth=2)  # main graph

# Creating axis
plt.grid(True, which='both')
plt.axhline(y=0, color='blue')
plt.axvline(x=0, color='blue')

# Labeling axis
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()

p1_integ = lagInterpol_integ(v1, p1, n)
p1_integ_prime = integrate(p1_integ)
p1_integ_prime = lambdify(Symbol('x'), p1_integ_prime)
work1 = p1_integ_prime(30) - p1_integ_prime(25)

p2_integ = lagInterpol_integ(v2, p2, n)
p2_integ_prime = integrate(p2_integ)
p2_integ_prime = lambdify(Symbol('x'), p2_integ_prime)
work2 = p2_integ_prime(35) - p2_integ_prime(30)

work = work1 + work2


print("\nWork done ", work)

