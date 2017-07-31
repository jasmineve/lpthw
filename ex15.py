# import argv from sys module.
from sys import argv

# unpacks argv variable and assigns the argument to two variables. 
script, filename = argv

# open a file and assigns it to a variable.
txt = open(filename)

# print a line with a formatter
print "Here's your file %r:" % filename
# give the variable(file) a command
print txt.read()
txt.close()

# print a string
print "Type the filename again:"
# after a prompt type an input named file_again
file_again = raw_input("> ")

# repeat opening a file and assigns it to txt_again
txt_again = open(file_again)

# repeat line13 
print txt_again.read()
txt_again.close()

# there are two ways to get user inputs, raw_input and argv, raw_input 
# allows the user to input in the middle of the program, whereas argv invites the user 
# to input in the beginning.
