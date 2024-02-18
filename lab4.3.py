def print_info(imie, wiek=20):
    """
        Funkcja wypisująca na ekranie imię i wiek osoby.
        Parametry:
        imie (string) - Imię osoby.
        wiek (int) - Wiek osoby, gdy nie wprowadzony przyjmuje wartość 20.
        """
    print("Imię:", imie)
    print("Wiek:", wiek)


print(print_info.__doc__)


print_info("Andzrzej", 30)
print_info("Ewelinka")