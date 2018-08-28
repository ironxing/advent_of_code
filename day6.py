# m = [[0, 2, 7, 0]]
m = [[10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]]

#  We name the current list : x
#  The "new" list that we work on : y

def new_position(width, position):
    if position + 1 > width - 1:
        return 0
    else:
        return position + 1

def list_exist(matrix, list):
    found = False
    i = 0
    while not found and i < len(matrix):
        if matrix[i] == list:
            found = True
        i += 1
        continue
    return found

#  The current list x
counter = 0
found = False
i = 0
while not found:
    x = m[i]
    width = len(x)
    max_value = max(x)
    position = x.index(max_value)

    #  The new list y
    y = x.copy()
    y[position] = 0

    while max_value > 0:
        position = new_position(width, position)
        y[position] += 1
        max_value -= 1  # keep add 1 to new position, until all max_value is split

    found = list_exist(m, y)
    m.append(y)
    counter += 1
    i += 1

print("Blocks-in-banks configuration is produced that has been seen before")
print(counter)
