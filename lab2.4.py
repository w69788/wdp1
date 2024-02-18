a = int(input("Podaj pierwszą liczbę: "))
s = int(input("Podaj drugą liczbę: "))

if a > s:
    while s <= a:
        if s % 2 != 0:
            s += 1
            continue
        print(s)
        s += 1
elif a == s:
    if a % 2 == 0:
        print("Liczby są równe i obie są parzyste:", a)

else:
    while a <= s:
        if a % 2 != 0:
            a += 1
            continue
        print(a)
        a += 1