from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, Ich bin das Script {script}.")
print("Ich habe ein paar Fragen an dich.")
print(f"Magst du mich {user_name}?")
likes = input(prompt)

print(f"Wo lebst du {user_name}?")
lives = input(prompt)

print(f"Was für ein Betriebssystem hat dein Computer?")
computer = input(prompt)

print(f"""
Alles klar, also auf die Frage ob du mich magst, sagtest du {likes}.
Du lebst in {lives}. Ich habe keine Ahnung wo das ist. Ich könnte das googlen, hab aber keine Lust.
Du hast also einen {computer} Computer. Crazy
""")
