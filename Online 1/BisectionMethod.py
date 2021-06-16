import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

a3 = 8.775468*10**-8
a1 = 2.341077*10**-4
a0 = 1.129241*10**-3
k = 1/(19+273.15)


lower_bound = 12000
uppper_bound = 18000
exp_error = 0.5
max_itr = 100

def f(x):
    x = math.log(x)
    return (a3*x**3) + (a1*x) + a0 - k


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


# def bisect_table(lower_bound, upper_bound, max_itr):
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


root = bisect(lower_bound, uppper_bound, exp_error, max_itr)
print("\nThe approximate root of the equation: ", root)
