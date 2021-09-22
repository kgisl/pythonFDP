
def sequence_gen(number):
    '''generate the Lucas Sequence and return upto n elements in a list
    and ref: https://cyber-dojo.org/kata/edit/s4Z3PL
    '''
    a, b, c = 0, 0, 1
    alist = [a, b, c]

    number -= 3
    while number > 0:
        nextv = a + b + c
        alist.append(nextv)
        a, b, c = b, c, nextv
        number -= 1
    return alist


def sequence_gen_alt(number):
    '''generate the Lucas sequence using another 3 element list

    @author kgashok
    @param number is an int

    @return list containing the lucas sequence

    '''
    a, b, c = 0, 0, 1
    alist = [a, b, c]
    temp = alist.copy()

    number -= 3
    while number > 0:
        nextv = sum(temp)
        alist.append(nextv)
        temp = temp[1:] + [nextv]
        print(temp)
        number -= 1
    return alist
