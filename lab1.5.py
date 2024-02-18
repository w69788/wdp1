x = float(input("Podaj x "))
y = float(input("Podaj y "))
z = float(input("Podaj z"))

if x > y:
    x, y = y, x

if y > z:
    y, z = z, y

if x > y:
    x, y = y, x

print(x, y, z)