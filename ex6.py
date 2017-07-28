# This assigns a string with formatted variables to the variable x
x = "There are %d types of people." % 10
# This assigns a string to variable called 'binary'
binary = "binary"
# This assigns a string to the variable 'do_not'
do_not = "don't"
# The right side is a string with two formatters, the left side is variable y
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# notice how a single sentence can be a formatted variable as well.
print "I said: %r." % x
# notice the difference between %r and %s
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + " " +e
