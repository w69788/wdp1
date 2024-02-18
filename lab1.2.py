l = input("Podaj literę: ")

if l.isalpha():
    if l.islower():
        print("Wprowadzona litera jest mała.")
    elif l.isupper():
        print("Wprowadzona litera jest duża.")


