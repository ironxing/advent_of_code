import numpy as np


def checksum(m):
    rows = len(m)
    cols = len(m[0])

    diff_sum = 0
    for i in range(rows):
        min = 9
        max = 0
        for j in range(cols):
            if m[i, j] <= min:
                min = m[i, j]
            if m[i, j] >= max:
                max = m[i, j]
        diff_sum += (max - min)

    return diff_sum


m = np.random.randint(10, size=(4, 4))

print("The matrix is: ")
print(m)
answer = checksum(m)
print("The checksum is: " + str(answer))






