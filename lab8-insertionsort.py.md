
Problem Statement
write a python program to implement insertion sort

sample input1: [0,10]
sample output1: [2,5,7,8]

sample input2: [-10,-1]
sample output2: [-9,-7,-5]

sample input3: [1.0,10.0]
sample output3: [2.0,5.0,7.0]

Solution key
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
    
    Pre lab Questions
    1.How to use ascii_code in insertion sort?
    2.How to sort megative and positive numbers in insertion sort?
        
    Post lab Questions
    1.Is possible to sort math operators in insertion sort? 
    
    Related Link
    
    http://10.100.8.8/kata/edit/B62817AC60?avatar=hippo
