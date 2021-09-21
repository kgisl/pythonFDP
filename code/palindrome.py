def is_palindrome(aseq):
    '''check whether a sequence is palindromic using unpacking

    @author kgashok
    @param aseq is a sequence, for e.g. string or list
    '''
    while len(aseq) > 1:
        first, *aseq, last = aseq
        if first != last:
            break
    else:
        return True

    return False


def is_palindrome_rec(aseq):
    '''check for palindrome using unpacking, recursively

    @author kgashok
    @param aseq is a sequence of elements, string or list
    '''

    # terminal case 1
    if len(aseq) < 2:
        return True

    first, *aseq, last = aseq
    # terminal case 2
    if first != last:
        return False

    return is_palindrome_rec(aseq)


def is_palindrome_rec_slice(aseq, first=None, last=None):
    '''check for palindrome using slicing, recursively

    @author kgashok
    @param aseq is a sequence of elements, string or list
    @param first is first element in seq
    @param last is last element in seq
    '''
    
    # Terminal case 1
    if len(aseq) < 2:
        return True
    # Terminal case 2
    if first != last:
        return False

    return is_palindrome_rec_slice(aseq[1:-1], aseq[0], aseq[-1])
