n=int(input("do którego wyrazu ciągu policzyć?"))
a=int(input("Podaj pierwszy wyraz ciągu"))
r=int(input("Podaj różnicę ciągu:"))
for i in range(1, n-1):
    an=a+(i-1)*r
    print(an)