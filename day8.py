import read_csv

# Read in the instructions into m
# Create a empty matrix result_m to store the "outcome"
# Pick out the elements from m : eg. x = 'o', operation = 'inc' , amount = '394', a = 'tcy', sympol = '>=', b = '-3'
# Use functions compare(sympol, a, b), calc(operation, x_value, amount) to calculate
# Store the outcome into result_m

def compare(sympol, a, b):
    if sympol == '==':
        if a == b:
            return True
        else:
            return False
    elif sympol == '<=':
        if a <= b:
            return True
        else:
            return False
    elif sympol == '<':
        if a < b:
            return True
        else:
            return False
    elif sympol == '>=':
        if a >= b:
            return True
        else:
            return False
    elif sympol == '>':
        if a > b:
            return True
        else:
            return False
    elif sympol == '!=':
        if a != b:
            return True
        else:
            return False


def get_value(x, m_result):
    x_value = 0
    found = False
    i = 0
    while not found and i < len(m_result):
        if x == m_result[i][0]:
            x_value = int(m_result[i][1])
            found = True
        i += 1
    return x_value


def calc(operation, x_value, amount):
    if operation == 'inc':
        return x_value + amount
    elif operation == 'dec':
        return x_value - amount


def set_value(x, m_result, operation, amount):
    found = False
    i = 0
    x_value = calc(operation, get_value(x, m_result), amount)

    while not found and i < len(m_result):
        if x == m_result[i][0]:
            m_result[i][1] = x_value
            found = True
        i += 1

    if not found:
        m_result.append([x, x_value])

# read input into m
m = read_csv.read_csv_function("day8_input.csv", " ")
print(m)
m_result = []

# run through instructions
m_result = []
for i in range(len(m)):
    x = m[i][0]
    operation = m[i][1]
    amount = int(m[i][2])
    a = get_value(m[i][4], m_result)
    sympol = m[i][5]
    b = int(m[i][6])
    if compare(sympol, a, b):
        set_value(x, m_result, operation, amount)


# print result and max
print(m_result)
max = 0
for i in range(len(m_result)):
    if m_result[i][1] > max:
        max = m_result[i][1]
print(max)