import math

# Definition used:
#   number: the input number
#   n: the square root of the number that sits on the right lower corner of the layer the number is on
#         example for these numbers on right lower corner: 9, 25, 49
#         square root n: 3, 5, 7
#         for example, 48 sits on the third layer, the "right lower corner number" is 49, n = 7
#      n is used to calculate the "base coordinates" i.e. the coordinates of "right lower corner number"
#   interval_location: on the layer, which side the number sits on.
#      bottom side 0, left side 1, top side 2, right side 3

# Calculation idea:
#   see the numbers as a n*n matrix
#   calculate coordinates of the number 1 coor_1:[a, b]
#   calculate the input number's coordinates coor_num: [i, j]
#   steps = abs(i-a) + abs(j-b)



def cal_n(number): # calculate n
    root_number = math.ceil(number**0.5)

    if root_number % 2 == 0:
        return root_number + 1
    else:
        return root_number

def cal_indices(number, n, interval_location):
    x = (n**2 - number) % (n-1)
    if interval_location == 0:
        i = n
        j = n - x
    elif interval_location == 1:
        i = n - x
        j = 1
    elif interval_location == 2:
        i = 1
        j = 1 + x
    else:
        i = 1 + x
        j = n

    coor_number = [i, j]
    return coor_number


number = int(input("Please input an integer number: "))

if number <= 0:
    print("Pleaes enter an integer that is larger than 0")
elif number == 1:
    steps = 0
    print(steps)
else:
    n = cal_n(number)

    coor_1_1 = int((n-1)/2+1)  # coordinates for number 1 is: [coor_1_1, coor_1_1]

    interval_location = math.floor((n**2 - number)/(n-1))

    coor_number = cal_indices(number, n, interval_location)

    steps = abs(coor_number[0] - coor_1_1) + abs(coor_number[1] - coor_1_1)

    print("The square root of the right lower corner number is: "+ str(n))
    print("The coordinates for number 1 is: [" + str(coor_1_1) + ", " + str(coor_1_1) + "]")
    print("The coordinates for the number is: [" + str(coor_number[0]) + ", " + str(coor_number[1])+ "]")
    print("Steps from the number to 1 is: " + str(steps))

