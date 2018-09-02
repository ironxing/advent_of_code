
test = [3, 4, 10, 11, 17, 18, 24, 25]


def check_double_cancel_sign(cancel_sing_indices):



    for i in range(len(cancel_sing_indices)-1):
        if cancel_sing_indices[i] + 1 == cancel_sing_indices[i+1]:
            del cancel_sing_indices[i+1]
    return cancel_sing_indices

print(check_double_cancel_sign(test))
