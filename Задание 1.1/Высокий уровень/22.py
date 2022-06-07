import math


x = float(input("x = "))
y = float(input("y = "))
F = math.cos(x ** 2 + 2) + (3.5 * x ** 2 + 1) / math.cos(y) ** 2
print("F =", F)
