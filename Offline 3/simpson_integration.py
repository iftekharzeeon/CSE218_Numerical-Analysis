import math
import pandas as pd

u = 2000
q = 2100
m0 = 140000
a = 8
b = 30
g = 9.8
exact_value = 11061


def f(t):
    y = u*math.log(m0 / (m0 - q*t)) - g*t
    return y

def simpson_integration(n):
    sum = 0
    h = (b-a) / n
    sum += f(a) + f(b)
    for i in range(1, n, 2):
        sum += 4*f(a + i*h)
    
    for i in range(2, n, 2):
        sum += 2*f(a + i*h)
    
    y = ((b-a) / (3*n)) * sum
    return y

def true_error_simpson(n):
    approximate_value = simpson_integration(n)
    et_value = exact_value - approximate_value
    absolute_relative_et = abs((et_value / exact_value) * 100)
    return et_value, absolute_relative_et

interval_size = list()
value = list()
true_errors = list()
rel_true_errors = list()
approximate_errors = list()
approximate_errors.append(None)

for i in range(1, 6):
    i = 2*i
    interval_size.append(i)
    value.append((simpson_integration(i)))
    et , rel_et = true_error_simpson(i)
    true_errors.append(et)
    rel_true_errors.append(rel_et)
    if i != 2:
        ea = abs((simpson_integration(i-2) - simpson_integration(i)) / simpson_integration(i-2)) * 100
        approximate_errors.append(ea)

data = {'N' : interval_size, 'Value': value, 'Et': true_errors, '|Et|%': rel_true_errors, '|Ea|%': approximate_errors}
df = pd.DataFrame(data, index=range(1,6))
print('\n', df, '\n')

n = int(input('Enter the number of sub-intervals: '))

print('Approximate Result of the Integration: ', simpson_integration(2*n))
