types_of_people = 10
x = f"Es gibt {types_of_people} Arten von Menschen."

binary = "binär"
do_not = "nicht"

y = f"Solche die {binary} verstehen und solche die es {do_not} tun."

print(x)
print(y)

print(f"I sagte: {x}")
print(f"I sagte zudem: '{y}'")

hilarious = False

joke_evalution = "War dieser Witz nicht spitze?! {}"

print(joke_evalution.format(hilarious))

w = "Das ist die linke Seite eines ..."
e = "Strings mit einer rechten Seite."

print (w+e)
