def calc_weight_on_planet(weight, surface_gravity=23.1):
    return (weight / 9.8) * surface_gravity

W = float(input("Weight: "))
SG = float(input("Surface gravity: "))

result = calc_weight_on_planet(W, SG)

print(result)

