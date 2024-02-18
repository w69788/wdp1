n = int(input("Podaj liczbę elementów: "))
x = int(input("Podaj długość ciągu: "))
l = [input(f"Podaj ciąg znaków o długości {x}: ") for _ in range(n)]

k = tuple(l)

# a)
z = sum(len(c) for c in l)
print("a) Ilość znaków w liście:", z)

# b)
kk = sum(c.count('k') for c in l)
print("b) Ilość wystąpień litery 'k' w liście:", kk)

# c)
kt = sum(c.count('kt') for c in l)
print("c) Ilość wystąpień ciągu 'kt' w liście:", kt)

# d)
s = int(input("Podaj długość ciągu s: "))
d = sum(1 for c in l if len(c) > s)
print("d) Ilość ciągów dłuższych niż", s, "w liście:", d)