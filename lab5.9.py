import random


def gra_zgadywanie(s, k, max_p):
    if k <= s:
        print("zły zakres")
        return


    l = random.randint(s, k)


    print("Witaj użytkowniku! Zagramy w grę??")
    print(f"Zgadnij liczbę z zakresu od {s} do {k}")
    print(f"Masz aż {max_p} próby ;)")

    for proba in range(1, max_p + 1):

        while True:
            prop = input("Wprowadź liczbę twardzielu: ")
            if prop.isdigit():
                prop = int(prop)
                break
            else:
                print("Czego nie rozumiesz w poleceniu >podaj liczbę<")


        if s <= prop <= k:

            if prop < l:
                print("za mało")
            elif prop > l:
                print("za dużoo")
            else:
                print(f"Gratulacje! Odgadłeś liczbę {l} w {proba} próbach! Wygrałeś grę <3")
                return
        else:
            print(f"Twoja propozycja jest spoza zakresu od {s} do {k}")

    print("Niestety, raz się przegrywa, raz się przegrywa. Szukana liczba to:", l)



s = int(input("Podaj początek zakresu losowania: "))
k = int(input("Podaj koniec zakresu losowania: "))
p = 3

gra_zgadywanie(s, k, p)