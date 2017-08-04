def sweet(a, b):
    print('How do you do? %r' % int(a))
    return(int(a)+int(b))
    
y = sweet(4, 6)

print(y)

def how_old(son, dad):
    print("let's guess the age of daddy"),
    print('first, son is %d years old.' % son)
    print('And daddy is twice as old as he is, which is:')
    return dad
    
z = how_old(30, 60)
print(z)

# formula: ((35+44)*(120/45))/(40-23)
print(((35+44)*(120/45))/(40-23))
def add(a, b):
    print("Adding %d + %d" %(a, b))
    return a + b
    
def multiply(a,b):
    print("Multiplying %d * %d"  %(a, b))
    return a * b
    
def subtract(a, b):
    print("Subtracting %d - %d" %(a, b))
    return a - b
    
def divide(a, b):
    print("Dividing %d / %d" % (a, b))
    return a / b
    
print(divide(multiply(add(35,44),divide(120,45)),subtract(40,23)))
