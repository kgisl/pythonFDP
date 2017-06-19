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

```python - Selection sort

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
```python - Insertion sort
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
1.What is the output of selection sort after the 1st iteration given the following sequence of numbers: 14 9 4 18 45 2 37 63
a. 4 14 9 18 45 2 37 63
b. 2 9 14 18 45 4 37 63
c. 4 9 14 18 45 2 37 63
d.2 14 9 18 45 4 37 63
Ans:d

2. What is the worst case complexity for selection sort algorithm
a.O(n) b.O(n*n) c.O(nlogn) d.O(logn)
Ans:b

3.What is the average case complexity for selection sort algorithm
a.O(n) b.O(n*n) c.O(nlogn) d.O(logn)
Ans:b

4.What is the output of selection sort after the 2nd iteration given the following sequence of numbers: 16 3 46 9 28 14
a.3 9 46 16 28 14
b.3 9 14 16 28 46
c.3 9 16 14 46 28
d.none of the above
Ans:a

5.What is the best case complexity for selection sort algorithm
a.O(n) b.O(n*n) c.O(nlogn) d.O(logn)
Ans:b

6.The following loop is used for
For i<- 1 to N
For j<- i+1 to N
If(a(i)>a(j))
{
Temp=a(i);
A(i)=a(j);
A(j)=temp;
}
a.bubble sort b.selection sort c.insertion sort d.merge sort
Ans:b

7.Here is an array of six integers: 
5 3 8 9 1 7 
This array after the FIRST iteration in a selection sort (sorting from smallest to largest) is
a. 5 1 8 4 3 7
b. 1 8 5 4 3 7
c.1 5 8 4 3 7
d. 1 5 8 4 7 3
Ans:c
8.In a selectionsort of n elements, how many times is the swap function called in the complete execution of the algorithm? 
A. 1 
B. n – 1 
C. n log n 
D. n² 
Ans:B
9.A sorting technique in which successive elements are selected in order and placed into their proper sorted positions is called
a.selection sort
b.quick sort 
c.bubble sort
d.merge sort
Ans:a

10.The selection sort that uses descending priority queue as an unordered array is_____
Ans:straight selection sort

11.Straight selection sort is also called
a.Push-down sort
b. Push-up sort
c.both
d.none
Ans:a

12.The types of selection sort are
a.General selection sort b.Pull-up selection sort c. Push-up selection sort d.none
Ans:a

13.In which cases are the time complexities same in selection sort?
a. Worst and Best
b. Best and Average
c. Worst and Average
d. Worst, average and Best
Ans:d

## Post Lab Questions
1. How to remove the duplicates from the resultant array?


## Bonus 1 
1. Rewrite the selection sort code above to sort in ascending order 


CD Material: http://10.100.8.8/kata/edit/169305975E?avatar=eagle
             http://10.100.8.8/kata/edit/B62817AC60?avatar=hippo
