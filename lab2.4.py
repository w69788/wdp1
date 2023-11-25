a = int(input("Podaj pierwszą liczbę:"))
s = int(input("Podaj drugą liczbę:"))
if a>s:
    while s<=a:
        if s%2==0:
            print(s)
        s+=1
elif a==s:
    print("Liczby są równe: ", a)
else:
    while a<=s:
        if a%2==0:
            print(a)
        a+=1
