def num_atoms(grams, atomic_weight= 196.97):
    avogrado_number = 6.022 * (10 ** 23)
    return (grams * avogrado_number) / atomic_weight

g = float(input("The amount of the element in grams: "))
aw = float(input("Atomic weight of the element: "))

result = num_atoms(g, aw)

print(result)
