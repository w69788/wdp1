i = input("Podaj imię: ")
print("Witaj", i)

w = input("Podaj swój wiek: ")
print("Twój wiek to:", w)

n = input("Podaj nazwisko: ")
ii = i[0] + n[0]
print("Twoje inicjały to:", ii)

l = input("Podaj łańcuch: ")
print(l * 5)

l1 = input("Podaj pierwszy łańcuch: ")
l2 = input("Podaj drugi łańcuch: ")
aa = l1 + l2
print("Połączone łańcuchy:", aa)

l1 = input("Podaj pierwszy łańcuch: ")
l2 = input("Podaj drugi łańcuch: ")
p1 = l1[:len(l1)//2]
p2 = l2[len(l2)//2:]
aa = p1 + p2
print("Połączone połowy łańcuchów:", aa)

