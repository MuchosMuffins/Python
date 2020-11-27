cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("Es gibt", cars, "Autos verfügbar.")
print("Es gibt lediglich", drivers, "Fahrer.")
print("Folglich bleiben", cars_not_driven, "Autos ungefahren heute.")
print("Wir können", carpool_capacity, "Menschen befördern.")
print("Wir haben", passengers, "Menschen zu befördern.")
print("Dazu müssen wir ca.", average_passengers_per_car, "Passagiere in jedem Auto haben.")
