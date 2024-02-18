import math
import keyword

print("Funkcje w module math:")
for name in dir(math):
    if not name.startswith("__"):
        print(name)

print("\nFunkcje w module tuple:")
for name in dir(tuple):
    if not name.startswith("__"):
        print(name)

print("\nFunkcje w module keyword:")
for name in keyword.kwlist:
    print(name)