a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if b - a < c - a:
    print("Точка с координатами (0, b) ближе к а")
elif b - a > c - a:
    print("Точка с координатами (0, c) ближе к а")
else:
    print("Все они рядом")
