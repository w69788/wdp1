n = int(input("Podaj n: "))

s = 1
for i in range(1, n + 1):
    s *= i

print("Silnia z", n, "to", s)