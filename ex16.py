from sys import argv

script, filename = argv

print(f"Wir entfernen nun {filename}.")
print("Noch kannst du es verhindern, drücke STRG-C (^C).")
print("Wenn du es willst, drücke ENTER.\n")

input("Na traust du dich?\n")

print("Öffne die Datei...")
target = open(filename, 'w')

print("Ich entferne den Inhalt. Adios Inhalt.")
target.truncate()
print("...")
print("Erledigt.\n")

print("Bitte gib mir nun 4 Lines feinsten Battlerap.")

line1 = input("1: ")
line2 = input("2: ")
line3 = input("3: ")
line4 = input("4: ")

print("Ich schreibe das nun in die Datei.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")

print("Und zu aller letzt, schließen wir sie.\n")
target.close()

print("Schauen wir mal, was du so gezaubert hast.")
print("==========================================")
txt = open(filename)
print(txt.read())
input()
print("Ich bin sprachlos, grandios.")
