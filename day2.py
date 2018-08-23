import numpy as np
import pandas as pd

def checksum(m):
    rows = len(m)
    cols = len(m[0])

    diff_sum = 0
    for i in range(rows):
        min = 1000000
        max = 0
        for j in range(cols):
            if m[i, j] <= min:
                min = m[i, j]
            if m[i, j] >= max:
                max = m[i, j]
        diff_sum += abs(max - min)

    return diff_sum


csvfile = pd.read_csv("day2_input.csv", sep="\t", header=None)
m = np.array(csvfile)

print("The matrix is: ")
print(m)
answer = checksum(m)
print("The checksum is: " + str(answer))






