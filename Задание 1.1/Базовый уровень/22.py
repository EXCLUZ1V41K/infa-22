import math


u = float(input("u = "))
x = float(input("x = "))
y = float(input("y = "))
T = math.sin(2 * u) * math.log(2 * (y ** 2) + math.sqrt(x))
print("T =", T)
