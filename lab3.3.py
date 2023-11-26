tekst="Python jest super"
#a
print(tekst[0])
#v1
print(tekst[-1])
#v2
dl=len(tekst)
print(tekst[dl-1])
#b
for i in range(0,dl,2):
    print(tekst[i])
#c
for i in range(1,dl,3):
    print(tekst[i])
#d
print(tekst[10:])
#e
print(tekst[::-1])




