d = float(input("День недели 1-7: "))
t = float(input("Время разговора: "))
dt = float(input("Продолжительность разговора в минутах: "))
s = float(input("Стоимость минуты: "))
if t >= 22 or t <= 8:
    if d == 6 or d == 7:
        st = (dt * s) - ((dt * s) * 0.15)
        print(st)
    if d < 6 and d > 0:
        st = (dt * s) - ((dt * s) * 0.1)
        print(st)
print()
