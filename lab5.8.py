import math


def pole_trojkata(a, b, kat):
    if a <= 0 or b <= 0 or kat <= 0 or kat >= 90:
        print("Błędne dane! Trójkąt o podanych wymiarach nie istnieje.")
        return None

    if kat == 90:
        print("Trójkąt o podanych wymiarach nie jest ostrokątny.")
        return None


    k_rad = math.radians(kat)


    p = 0.5 * a * b * math.sin(k_rad)

    return p



a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
k = float(input("Podaj szerokość kąta ostrego (w stopniach): "))

wynik = pole_trojkata(a, b, k)

if wynik is not None:
    print("Pole trójkąta ostrokątnego wynosi:", wynik)