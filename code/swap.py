print("Enter two values to swap")
a = int(input())
b = int(input())

# using a temporary variable
t = a
a = b
b = t

print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))


def swap():
    '''swap the contents of a and b

    @author kgashok
    @param a is global
    @param b is global
    @returns None
    '''
    global a, b
    print("Swap function called")
    a, b = b, a


swap()  # go back to their original values
print("Did swap work?")
print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))
