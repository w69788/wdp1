a = int(input("Podaj pierwszą liczbę:"))
s = int(input("Podaj drugą liczbę:"))
if a>s:
    while s<=a:
        print(s)
        s+=1
elif a==s:
    print("Liczby są równe: ", a)
else:
    while a<=s:
        print(a)
        a+=1
