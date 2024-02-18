z = {'makaron': 4, 'jaja': 7, 'guseppe': 10, 'perełka': 3, 'ser': 6}

print("Lista zakupów:")
for a, k in z.items():
    print(f"- {a}: {k} zł")


s = sum(k for k in z.values())
print("Koszt:", s, "zł")