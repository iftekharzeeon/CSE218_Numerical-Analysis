import numpy as np


def gaussianElimination(A, B, d):
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
            if d:
                print('Step ', i + 1, '.', j - i + 1)
                print('Matrix A: ')
                print(A)
                print('Matrix B:')
                print(B)
                print('\n')
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


d = True
size = int(input('Enter the size of the array:\n'))
temp_list = []
a = np.zeros((size, size), np.double)
b = np.zeros((size, 1), np.double)

for i in range(size):
    row = list(map(int, input().split(' ')[:size]))
    temp_list.append(row)

print('\n')
for j in range(size):
    b[j] = float(input())

print('\n')
a = np.array(temp_list, np.double)
x = gaussianElimination(a, b, d)
print('\n')
print('Solution:')
for i in range(size):
    print('%.4f' % x[i][0])
