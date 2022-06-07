import math


t = float(input("t = "))
y = float(input("y = "))
S = ((4.351 * (y ** 3)) + (2 * t * math.log(t))) / math.sqrt(math.cos(2 * y) + 4.351)
print("S = ", S)
