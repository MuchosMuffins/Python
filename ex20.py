def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"Du hast {cheese_count} Käse!")
	print(f"Du hast {boxes_of_crackers} Packungen Crackers!")
	print("Schnapp dir ne Decke, das ist ja genug für eine Party.")
print("====================================================\n")
print("Wir können der Funktion die Nummern direkt geben:")
cheese_and_crackers(20, 30)
print("====================================================\n")
print("Oder wir nehmen Variablen aus dem Script:")
amount_of_cheese = 10
amount_of_crackers = 50
print("====================================================\n")
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("====================================================\n")
print("Innerhalb können wir sogar Mathe benutzen:")
cheese_and_crackers(10 + 20, 5 + 6)
print("====================================================\n")
print("Und wir können Mathe und Variablen kombinieren:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
