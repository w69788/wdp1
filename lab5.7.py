import random
from functools import reduce


def geom_mean(nums):
    product = reduce(lambda x, y: x * y, nums)
    return product ** (1 / len(nums))


s = int(input("Podaj początek przedziału: "))
e = int(input("Podaj koniec przedziału: "))


n = 10
t = tuple(random.randint(s, e) for _ in range(n))


m = geom_mean(t)


print("Wylosowana krotka:", t)
print("Średnia geometryczna krotki:", m)