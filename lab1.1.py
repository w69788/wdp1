w = int(input("Podaj wiek osoby: "))

if w < 4:
    print("Wstęp bezpłatny")
elif 4 <= w <= 18:
    print("Cena biletu: 10 zł")
else:
    print("Cena biletu: 20 zł")