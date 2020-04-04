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

def circulate_list(alist):
    """circulate 'n' elements in a list

    @author kgashok
    @param alist contains the 'n' elements

    @return nothing
    """
    i = len(alist)
    while i:
        first = alist.pop(0)
        alist.append(first)
        print(*alist)
        i -= 1


alist = input("enter multiple values ").split()
circulate_list(alist)

