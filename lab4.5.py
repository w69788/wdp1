def bmi(w, h):


    bmi_w = w / (h ** 2)

    if bmi_w < 18.5:
        print("Twoje BMI wynosi", bmi_w, "- niedowaga")
    elif 18.5 <= bmi_w < 25:
        print("Twoje BMI wynosi", bmi_w, "- Waga w normie")
    elif 25 <= bmi_w < 30:
        print("Twoje BMI wynosi", bmi_w, "- Nadwaga")
    else:
        print("Twoje BMI wynosi", bmi_w, "- otyłość")

    return bmi_w

# Przykładowe użycie funkcji
w = float(input("Podaj wagę (kg): "))
h = float(input("Podaj wzrost (m): "))
bmii = bmi(w, h)