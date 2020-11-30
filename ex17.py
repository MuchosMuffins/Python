from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Kopiere von {from_file} zu {to_file}")

indata = open(from_file).read()

print(f"Die Eingangsdatei ist {len(indata)} Bytes lang.")

print(f"Existiert die Enddatei? {exists(to_file)}")
print("Wenn du fertig bist drücke Enter, ansonsten STRG-C.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alles klar, alles fertig.")

out_file.close()
