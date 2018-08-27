m = [[0, 2, 7, 0]]

#  We name the current list : x
#  The "new" list that we work on : y

def new_position(width, position):
    if position + 1 > width - 1:
        return 0
    else:
        return position + 1

counter = 0


x = m[0]
width = len(x)
max_value = max(x)
position = x.index(max_value)
print(position)

y = x.copy()
y[position] = 0

while max_value > 0:
    position = new_position(width, position)
    y[position] += 1
    max_value -= 1  # keep add 1 to new position, until all max_value is splitted
m.append(y)
print(m)
