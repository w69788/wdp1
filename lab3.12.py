import random
n=int(input("Ile elementów ma mieć lista? "))
x=int(input("Maksymalna liczba znaków w łańcuchu: "))
#ASCII 65-90
#random

koniec=0
slowo=[]
lista=[]
for i in range(n):
    for i in range(x):
        if koniec>=0.8:
            break
        else:
            slowo.append(chr(random.randint(65,90)))
            print(slowo)
        koniec=random.random()
        print(koniec)

    print(slowo)
    lista.append(slowo)
    koniec=0
    slowo=[]
print(lista)
print(koniec)
krotka=tuple(lista)
print(krotka)
#a
print(len(lista))
znaki=0
for i in range(len(krotka)):
    znaki+=len(krotka[i-1])


print(znaki)

#b
k=0
for i in range(len(lista)):
    k+=lista[i].count("K")

    print(lista.count("K"))
print(k)


