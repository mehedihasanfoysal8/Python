import math

def return_multiple_value(a):
    area = math.pi * a ** 2
    circumference = 2 * math.pi * a
    return area, circumference

a, b = return_multiple_value(3)

print("A : ", round(a, 2))
print("B : ", round(b, 2))