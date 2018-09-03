import read_csv

m = read_csv.read_csv_function("day9_input.csv", "\n")

def check_double_cancel_sign(cancel_sing_indices):
    for i in range(len(cancel_sing_indices)):
        if cancel_sing_indices[i] == cancel_sing_indices[i+1]:
            del cancel_sing_indices[i+1]

def cancel(string_input):
    while string_input[:]

def cancel_sign(string_input):
    string_output = string_input[:]
    cancel_sing_indices = []
    for i in range(len(string_input)):
        if string_input[i] == "!":
            cancel_sing_indices.append(i)
    return cancel_sing_indices


print(cancel_sign(m[7][0]))