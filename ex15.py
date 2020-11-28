from sys import argv

script, filename = argv

txt = open(filename)

print(f"Hier ist deine Datei {filename}:")
print(txt.read())

print("Schreib den Dateinamen erneut:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
