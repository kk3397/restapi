import math

import equations


def area_tri(length, width):
    return (length * width) / 2.0


def perm_tri(side1, side2, side3):
    return (side1 + side2 + side3)


def area_rec(length, width):
    return length * width


def perim_rec(width, length):
    return (width * 2) + (length * 2)
# ###if __name__ =='__main__':
#     while True:
#         side1 = int(input("side 1: "))
#         side2 = int(input("side 2: "))
#         side3 = int(input("side 3: "))
#         result = equations.perm_tri(side1, side2, side3)
#    ###     print(result)