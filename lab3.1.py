lista=["Ola","Ala","Jan","Ania"]
sLista=sorted(lista)
for name in sLista:
    print(name)
sLista.append("Krzyś")
sLista.append("Zosia")
for name in sLista:
    print(name)
imie=sLista.pop()
print(imie)
for name in sLista:
    print(name)
sLista.insert(3,"Ola")
for name in sLista:
    print(name)
sLista.reverse()

for name in sLista:
    print(name)
dsLista=sLista*2
for name in dsLista:
    print(name)