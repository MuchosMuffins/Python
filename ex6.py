x = "Es gibt %d Arten von Menschen." % 10
binary = "Binaer"
do_not = "nicht"
y = "Die die %s verstehen und die die es %s tun." % (binary, do_not)

print x
print y

print "Ich sagte : %r." % x
print "Ich sagte auch: '%s'." % y

hilarious = False
joke_evaluation = "Ist der Witz nicht lustig?! %r"

print joke_evaluation % hilarious

w = "Das ist links von..."
e = "einem Satz mit einer rechten Seite."
print w + e
