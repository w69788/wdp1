import random

# a) 
a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

# b)
if 5 in X:
    print("a) Zbiór X zawiera liczbę 5.")
else:
    print("a) Zbiór X nie zawiera liczby 5.")

# c)
if X.issubset(Y):
    print("b) Zbiór X jest podzbiorem zbioru Y.")
else:
    print("b) Zbiór X nie jest podzbiorem zbioru Y.")

# d)
if X.issuperset(Y):
    print("d) Zbiór X jest nadzbiorem zbioru Y.")
else:
    print("d) Zbiór X nie jest nadzbiorem zbioru Y.")

# e)
if Y.issuperset(X):
    print("e) Zbiór Y jest nadzbiorem zbioru X.")
else:
    print("e) Zbiór Y nie jest nadzbiorem zbioru X.")

# f)
s = X.union(Y)
print("f) Suma zbiorów X i Y:", s)

# g)
r_XY = X.difference(Y)
print("g) Różnica zbiorów X i Y:", r_XY)

# h)
r_YX = Y.difference(X)
print("h) Różnica zbiorów Y i X:", r_YX)

# i)
i = X.intersection(Y)
print("i) Iloczyn zbiorów X i Y:", i)

# j)
r_s = X.symmetric_difference(Y)
print("j) Różnica symetryczna zbiorów X i Y:", r_s)

# k)
n_X = max(X)
n_Y = max(Y)
print("k) Najwyższy element w zbiorze X:", n_X)
print("   Najwyższy element w zbiorze Y:", n_Y)

# l)
if X:
    p_X = X.pop()
    Y.add(p_X)
    print("Usunięto", p_X, "ze zbioru X i dodano do zbioru Y.")
else:
    print("Zbiór X jest pusty, nie można usunąć pierwszego elementu.")

# m)
Y.update(X)
print("Przekopiowano wszystkie elementy zbioru X do zbioru Y:", Y)

# n)
X.clear()
Y.clear()
print("Zbiorywyczyszczone.")