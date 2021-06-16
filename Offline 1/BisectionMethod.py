import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

k = 0.05
pt = 3
lower_bound = -0.6
uppper_bound = 0.5
exp_error = 0.5
max_itr = 20

def f(x):
    return (x / (1 - x) * (np.sqrt((2 * pt) / (2 + x)))) - k


def bisect(lower_bound, upper_bound, exp_error, max_itr):
    old_root = None
    itr = 0
    while True:
        new_root = (lower_bound + upper_bound) / 2
        if itr != 0:
            error = abs(((new_root - old_root) / new_root) * 100)
            if error <= exp_error:
                return new_root
        if f(new_root) * f(lower_bound) < 0:
            upper_bound = new_root
        elif f(new_root) * f(upper_bound) < 0:
            lower_bound = new_root
        elif f(new_root) * f(upper_bound) == 0:
            return new_root
        old_root = new_root
        itr = itr + 1
        if itr == max_itr:
            return new_root


def bisect_table(lower_bound, upper_bound, max_itr):
    old_root = None
    itr = 0
    error = None
    iterations_list = list()
    root_list = list()
    error_list = list()
    while True:
        new_root = (lower_bound + upper_bound) / 2
        if itr != 0:
            error = abs(((new_root - old_root) / new_root) * 100)
        if f(new_root) * f(lower_bound) < 0:
            upper_bound = new_root
        elif f(new_root) * f(upper_bound) < 0:
            lower_bound = new_root
        old_root = new_root
        itr = itr + 1
        iterations_list.append(itr)
        error_list.append(error)
        root_list.append(new_root)
        if itr == max_itr:
            data = {'Iterations': iterations_list, 'Approximate Root': root_list, "Errors": error_list}
            return data

plt.figure(figsize=(12, 10))
plt.title("Graph of Bisection Method")
x = np.arange(-1.99, 1, 0.1)
plt.plot(x, f(x), 'b')
x = np.arange(1.1, 10.5, 0.1)
plt.plot(x, f(x), 'b')
axis1 = np.arange(-15, 15, 0.1)
axis2 = axis1 * 0
plt.plot(axis2, axis1, 'k')
plt.plot(axis1, axis2, 'k')
plt.xticks(np.arange(-15, 15, 1))
plt.yticks(np.arange(-15, 15, 1.5))
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.show()

root = bisect(lower_bound, uppper_bound, exp_error, max_itr)
print("\nThe approximate root of the equation: ", root)

df = pd.DataFrame(bisect_table(lower_bound, uppper_bound, max_itr), index=np.arange(1, 21))
print("\n", df)
