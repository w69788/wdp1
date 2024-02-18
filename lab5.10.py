import datetime

def dzien_rk(y, m, d):
    data = datetime.date(y, m, d)
    return data.timetuple().tm_yday

def nr_tyg(y, m, d):
    data = datetime.date(y, m, d)
    return data.isocalendar()[1]

def data_pp(y, m, d):
    data = datetime.date(y, m, d)
    delta = datetime.timedelta(weeks=2)
    pp = data - delta
    po = data + delta
    return pp, po

def najbl_niedz(y, m, d):
    data = datetime.date(y, m, d)
    dzien = data.weekday()
    delta = datetime.timedelta(days=(6 - dzien))
    if dzien == 6:
        delta += datetime.timedelta(days=7)
    return data + delta

def czas_unix(y, m, d):
    data = datetime.datetime(y, m, d)
    return int(data.timestamp())


y = int(input("Podaj rok: "))
m = int(input("Podaj miesiąc: "))
d = int(input("Podaj dzień: "))


print("Dzień roku:", dzien_rk(y, m, d))
print("Numer tygodnia:", nr_tyg(y, m, d))
pp, po = data_pp(y, m, d)
print("Data na 2 tygodnie przed:", pp)
print("Data na 2 tygodnie po:", po)
print("Najbliższa niedziela:", najbl_niedz(y, m, d))
print("Czas unixowy bieżącej godziny w podanym dniu:", czas_unix(y, m, d))