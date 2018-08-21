import math


def cal_n(number):
    root_number = math.ceil(number**0.5)

    if root_number % 2 == 0:
        return root_number + 1
    else:
        return root_number


number = 28

n = cal_n(number)

coor_1_1 = int((n-1)/2+1)

location = math.floor((n**2 - number)/(n-1))






print(n)
print(coor_1_1)
print(location)