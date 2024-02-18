r = {'styczeń': 250, 'luty': 280, 'marzec': 220, 'kwiecień': 270, 'maj': 290}

# a)
w = list(r.values())
m = max(w)
n = min(w)
s = sum(w)
ś = s / len(w)

# b)
o = w[-1]
if o > ś:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny;)")