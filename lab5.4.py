from datetime import datetime, timedelta


d = datetime.now()

# Data ostatnich laboratoriów
l = datetime(2024, 1, 15)

# Data kolokwium
k = datetime(2024, 2, 15)

# Obliczanie różnicy czasu
c_l = d - l
c_k = k - d

# Wyświetlanie wyniku
print("Od ostatnich laboratoriów minęło:", c_l.days, "dni")
print("Do kolokwium pozostało:", c_k.days, "dni")