
test = [3, 4, 10, 11, 17, 18, 24, 25]
test2 = [3, 4, 5, 17, 18, 24, 25, 26, 27]


def check_double_cancel_sign(cancel_sign_indices):
    to_delete=[]
    for i in range(len(cancel_sign_indices)-1):
        if cancel_sign_indices[i] + 1 == cancel_sign_indices[i+1]:
            to_delete.append(i+1)
    return to_delete

print(check_double_cancel_sign(test))
print(check_double_cancel_sign(test2))
