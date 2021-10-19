# Lab 8: Selection and Insertion sort using Python

## Problem statement

Write a Python program to perform selection and insertion sort

```
sample input 0: [5,4,0,29,2]
sample output 0:[0,2,4,5,29]

sample input 1: [5,-4,0,29,2]
sample output 1:[-4,0,2,5,29]

sample input 2: [5,4.3,0,29,4.2]
sample output 2:[0,4.2,4.3,5,29]

sample input 2: ['b','a','c']
sample output 2:['a','b','c']

```

## Solution Key

```

Selection sort

def sel(alist):
    for mylist in range(len(alist)-1,0,-1):
        max_pos=0
        for loc in range(1,mylist+1):
            if alist[loc]>alist[max_pos]:
                max_pos = loc

        temp = alist[mylist]
        alist[mylist] = alist[max_pos]
        alist[max_pos]=temp
    return alist


```

```

Insertion sort

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

```

## CloudCoder Exercise

- To be updated.

## Pre Lab Questions

0. What is the output of selection sort after the 1st iteration given the following sequence of numbers: 14 9 4 18 45 2 37 6
1. What is the worst case complexity for selection sort algorithm?
2. What is the average case complexity for selection sort algorithm?
3. What is the output of selection sort after the 2nd iteration given the following sequence of numbers: 16 3 46 9 28 14?
4. What is the best case complexity for selection sort algorithm?
5. In a selectionsort of n elements, how many times is the swap function called in the complete execution of the algorithm?
6. A sorting technique in which successive elements are selected in order and placed into their proper sorted positions is called?
7. In which cases are the time complexities same in selection sort?

## Post Lab Questions

1. How to remove the duplicates from the resultant array?

## Bonus 1

1. Rewrite the selection sort code above to sort in ascending order

## CD Material:

http://10.100.8.8/kata/edit/169305975E?avatar=eagle

http://10.100.8.8/kata/edit/B62817AC60?avatar=hippo
