def ckeck_match(number1, number2):
    if number1 == number2:
        return True
    return False


def pick_single_digit(digit_sequence, i):
    single_digit = int(digit_sequence[i])
    return single_digit

digit_sequence = input("Please input a sequence of digits")


# Save the digits into a list
digit_sequence_length = len(digit_sequence)
digit_list = []

for i in range(digit_sequence_length):
    single_digit = pick_single_digit(digit_sequence, i)
    digit_list.append(single_digit)

digit_list.append(pick_single_digit(digit_sequence, 0))  # Add the first digit to the end to firm a "circle"

# Calculate the sum
sum = 0
for i in range(digit_sequence_length):
    number1 = digit_list[i]
    number2 = digit_list[i+1]
    digits_equal = ckeck_match(number1, number2)

    if digits_equal:
        sum += number1

print("The sum is: " + str(sum))


