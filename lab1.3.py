while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Zakończ")

    aa = input("Twój wybór: ")

    if aa == '6':
        break

    if aa not in ('1', '2', '3', '4', '5'):
        print("Wybierz opcję od 1 do 6, to nie takie trudne ;)")
        continue

    l = float(input("Podaj pierwszą liczbę: "))
    ll = float(input("Podaj drugą liczbę: "))

    if aa == '1':
        print(l + ll)
    elif aa == '2':
        print(l - ll)
    elif aa == '3':
        print(l * ll)
    elif aa == '4':
        if ll == 0:
            print("nice try ;)")
        else:
            print(l / ll)
    elif aa == '5':
        print(l ** ll)