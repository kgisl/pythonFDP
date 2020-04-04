def circulate(a, b, c):
    """circulate between three variables

    @author kgashok
    @param a is a integer
    @param b is a integer
    @param c is a integer

    @return nothing
    """
    i = 3
    while i:
        t = a
        a = b
        b = c
        c = t
        print(a, b, c)
        i -= 1


a, b, c = input("enter 3 values ").split()
circulate(a, b, c)
