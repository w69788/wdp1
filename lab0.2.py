import random

a = float(input("Podaj przebytą drogę w km "))
s = float(input("Podaj średnie spalanie  w l/100km "))
d = a * s/100
f = 6.5 * d
print(f"Zużycie paliwa wynosi {d}l\nKoszt podróży:{f}zł")

aa = random.randint(1, 100000)
ss = aa *s/100
dd = 6.5 * ss
print(f"Przewidywane zużycie paliwa na losowej trasie {aa}km wynosi {ss}l\nKoszt podróży:{dd}zł")