def insertion_sort(seq):
    #print (seq)
    i=1
    while i < len(seq):
        j=i
        while j!=0 and seq[j]< seq[j-1]:
                seq[j] , seq[j-1] = seq[j-1], seq[j]
                j -=1
        i +=1
    print(seq)
    return seq
