import math


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
ma = 0.5 * math.sqrt(2 * b ** 2 + 2 * c ** 2 - a ** 2)
mb = 0.5 * math.sqrt(2 * a ** 2 + 2 * c ** 2 - b ** 2)
mc = 0.5 * math.sqrt(2 * a ** 2 + 2 * b ** 2 - c ** 2)
print("медиана a = ", ma, "медиана b = ", mb, "медиана c = ", mc)
