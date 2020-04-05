print("Enter two values to swap")
a = int(input())
b = int(input())

# using a temporary variable
print("Swapping using temporary variable...")
t = a
a = b
b = t

print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))

# using XOR operator, eliminating the need for 3rd variable
print("Swapping using XOR operator...")
a = a ^ b
b = a ^ b
a = a ^ b

print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))


def swap_func():
    '''swap the contents of a and b

    @author kgashok
    @param a is global
    @param b is global
    @returns None
    '''
    global a, b
    print("swap_func function called")
    a, b = b, a


swap_func()  # go back to their original values
print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))
