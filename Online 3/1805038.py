import matplotlib.pyplot as plt
import numpy as np
import math

input_file = open("data.txt", "r")

c_values = list()
k_values = list()

lines = input_file.readlines()

for line in lines:
    c_values.append(float(line.split(" ")[0]))
    k_values.append(float(line.split(" ")[1]))

n = len(c_values)
c = np.array(c_values)
k = np.array(k_values)

# Transforming the equation into linear model
x = np.power((1/c), 2)
y = (1/k)

sum_of_x = np.sum(x)
sum_of_y = np.sum(y)
sum_of_x_squared = np.sum(x ** 2)
sum_of_xy = np.sum(x * y)

a0_firstOrder = ((sum_of_x_squared * sum_of_y) - (sum_of_x * sum_of_xy)) / ((n * sum_of_x_squared) - (sum_of_x * sum_of_x))
a1_firstOrder = ((n * sum_of_xy) - sum_of_x * sum_of_y) / ((n * sum_of_x_squared) - (sum_of_x * sum_of_x))

# Getting the original equation constants
k_max = (1/a0_firstOrder)
cs = (a1_firstOrder * k_max)

print('\nConstants for the equation')
print('k_max = ', k_max)
print('cs = ', cs)


# Graph Plot
plt.figure(figsize=(12, 15))

plt.xticks(np.arange(math.floor(min(c_values)), math.ceil(max(c_values))+1, 1))
plt.yticks(np.arange(math.floor(min(k_values)), math.ceil(max(k_values))+1, 1))


plt.scatter(c, k, marker='.', s=40)


def f(c):
    return (k_max * (c ** 2)) / (cs + (c ** 2))


c_values_for_graph = np.arange(math.floor(min(c_values)), math.ceil(max(c_values)) + 0.5, 0.1)

plt.plot(c_values_for_graph, f(c_values_for_graph), linewidth=1, color='r')

plt.xlabel("C")
plt.ylabel("K")
plt.grid()
plt.show()
