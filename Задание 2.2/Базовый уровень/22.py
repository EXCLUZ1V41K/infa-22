v1 = float(input("V1 = "))
m1 = float(input("m1 = "))
v2 = float(input("V2 = "))
m2 = float(input("m2 = "))
p1 = v1 * m1
p2 = v2 * m2
if p1 > p2:
    print("Плотность первого материала больше")
elif p1 < p2:
    print("Плотность второго материала больше")
else:
    print("Они равны")
