import pandas as pd
import numpy as np

csvfile = pd.read_csv("day5_input.csv", header=None)
m = np.array(csvfile)

index = 0
counter = 0
while index <= len(m)-1:
    current_number = m[index, 0]
    m[index, 0] = current_number + 1  # Update number at current position
    index += current_number  # Get the new index
    counter += 1

print(counter)

