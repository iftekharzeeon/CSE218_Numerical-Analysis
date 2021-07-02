import matplotlib.pyplot as plt
import numpy as np
import math


def gaussianElimination(A, B):
    length = (len(A)) - 1
    for i in range(length):
        j = i
        while j < length:
            factor = A[j + 1][i] / A[i][i]
            temp_a = np.array(A[i] * factor)
            temp_b = np.array(B[i] * factor)
            temp_a = A[j + 1] - temp_a
            temp_b = B[j + 1] - temp_b
            A[j + 1] = temp_a
            B[j + 1] = temp_b
            j += 1

    x = np.zeros((len(A), 1), dtype=np.double)

    for k in range(length, -1, -1):
        coefficient_b = B[k][0]
        coefficient_a = A[k][k]
        l = k + 1
        sum = 0
        while l <= length:
            sum = sum + (x[l][0] * A[k][l])
            l = l + 1
        x[k][0] = (coefficient_b - sum) / coefficient_a
    return x


input_file = open("data.txt", "r")

x_values = list()
y_values = list()

sum_of_x = 0
sum_of_y = 0
sum_of_z = 0
sum_of_x_squared = 0
sum_of_x_cubed = 0
sum_of_x_power4 = 0
sum_of_x_power5 = 0
sum_of_x_power6 = 0
sum_of_xy = 0
sum_of_xSquared_y = 0
sum_of_xCubed_y = 0
sum_of_xz = 0

lines = input_file.readlines()

for line in lines:
    x_values.append(float(line.split(" ")[0]))
    y_values.append(float(line.split(" ")[1]))

n = len(x_values)

plt.figure(figsize=(12, 15))

for i in range(0, len(x_values)):
    sum_of_x += x_values[i]
    sum_of_y += y_values[i]
    sum_of_z += math.log(y_values[i])
    sum_of_x_squared += (x_values[i] ** 2)
    sum_of_x_cubed += (x_values[i] ** 3)
    sum_of_x_power4 += (x_values[i] ** 4)
    sum_of_x_power5 += (x_values[i] ** 5)
    sum_of_x_power6 += (x_values[i] ** 6)
    sum_of_xy += (x_values[i] * y_values[i])
    sum_of_xSquared_y += (x_values[i] * x_values[i] * y_values[i])
    sum_of_xCubed_y += (x_values[i] * x_values[i] * x_values[i] * y_values[i])
    sum_of_xz += (x_values[i] * (math.log(y_values[i])))


# First Order
a0_firstOrder = ((sum_of_x_squared * sum_of_y) - (sum_of_x * sum_of_xy)) / (
            (n * sum_of_x_squared) - (sum_of_x * sum_of_x))
a1_firstOrder = ((n * sum_of_xy) - sum_of_x * sum_of_y) / ((n * sum_of_x_squared) - (sum_of_x * sum_of_x))

print('\nConstants for First Order')
print('a0 = ', a0_firstOrder)
print('a1 = ', a1_firstOrder)


# Second Order
A = np.array([[n, sum_of_x, sum_of_x_squared],
              [sum_of_x, sum_of_x_squared, sum_of_x_cubed],
              [sum_of_x_squared, sum_of_x_cubed, sum_of_x_power4]])

B = np.array([[sum_of_y],
              [sum_of_xy],
              [sum_of_xSquared_y]])

constants_of_secondOrder = gaussianElimination(A, B)
a0_secondOrder = constants_of_secondOrder[0][0]
a1_secondOrder = constants_of_secondOrder[1][0]
a2_secondOrder = constants_of_secondOrder[2][0]

print('\nConstants for Second Order')
print('a0 = ', a0_secondOrder)
print('a1 = ', a1_secondOrder)
print('a2 = ', a2_secondOrder)


# Third Order
C = np.array([[n, sum_of_x, sum_of_x_squared, sum_of_x_cubed],
              [sum_of_x, sum_of_x_squared, sum_of_x_cubed, sum_of_x_power4],
              [sum_of_x_squared, sum_of_x_cubed, sum_of_x_power4, sum_of_x_power5],
              [sum_of_x_cubed, sum_of_x_power4, sum_of_x_power5, sum_of_x_power6]
              ])

D = np.array([[sum_of_y],
              [sum_of_xy],
              [sum_of_xSquared_y],
              [sum_of_xCubed_y]])

constants_of_thirdOrder = gaussianElimination(C, D)
a0_thirdOrder = constants_of_thirdOrder[0][0]
a1_thirdOrder = constants_of_thirdOrder[1][0]
a2_thirdOrder = constants_of_thirdOrder[2][0]
a3_thirdOrder = constants_of_thirdOrder[3][0]

print('\nConstants of Third Order')
print('a0 = ', a0_thirdOrder)
print('a1 = ', a1_thirdOrder)
print('a2 = ', a2_thirdOrder)
print('a3 = ', a3_thirdOrder)


# Exponential Model-> y = ae^bx
a0_exp = ((sum_of_x_squared * sum_of_z) - (sum_of_x * sum_of_xz)) / (
            (n * sum_of_x_squared) - (sum_of_x * sum_of_x))

a1_exp = ((n * sum_of_xz) - sum_of_x * sum_of_z) / ((n * sum_of_x_squared) - (sum_of_x * sum_of_x))
a = math.exp(a0_exp)
b = a1_exp

print('\nConstants of Exponential Model')
print('a = ', a)
print('b = ', b)


# Plotting Graph
x = np.array(x_values)
y = np.array(y_values)

plt.xticks(np.arange(0, math.ceil(max(x_values)), 1))
plt.yticks(np.arange(0, math.ceil(max(y_values)), 1))

# Scattered Data Points
plt.scatter(x, y, marker='.', s=5)


def lf(x):
    return a0_firstOrder + a1_firstOrder * x


# Linear Function
plt.plot(x, lf(x), linewidth=0.5, color='g', label='First Order')


def sf(x):
    return a0_secondOrder + (a1_secondOrder * x) + (a2_secondOrder * (np.power(x, 2)))


# Second Order Function
plt.plot(x, sf(x), linewidth=0.2, color='r', label='Second Order')


def tf(x):
    return a0_thirdOrder + (a1_thirdOrder * x) + (a2_thirdOrder * (np.power(x, 2))) + (a3_thirdOrder * (np.power(x, 3)))


# Third Order Function
plt.plot(x, tf(x), linewidth=0.2, color='y', label='Third Order')


def expf(x):
    return a * (np.exp(b * x))


# Exponential Function
plt.plot(x, expf(x), linewidth=0.2, color='b', label='Exponential')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid()
plt.show()
