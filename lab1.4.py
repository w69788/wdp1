import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("x1=", x1, "   x2=", x2)
elif d == 0:
    x = -b / (2*a)
    print("x=", x)
else:
    print("Równanie nie ma rozwiązań w dziedzinie liczb rzeczywistych.")