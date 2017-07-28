tabby_cat = "\tI'm tabbed in."
y = "$"
persian_cat = "I'm split\n\ton a line with different\n\t %s characters." % y
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
%s\t* Catnip\n\t* Grass
''' % "\""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
