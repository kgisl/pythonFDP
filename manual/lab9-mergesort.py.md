# Merge Sort

## Problem statement
Write a python program to sort the given list using `mergesort` algorithm
CD EXtrenal Link : http://cyberdojo1.kgfsl.com/kata/edit/B006BC6DA0?avatar=bee
CD Local Link : http://10.100.8.8/kata/edit/B006BC6DA0?avatar=bee
```code
Examples:
Input:[5,8,2]
Output:[2,5,8]

Input:[6,2,8,4,3,7,5,1]
Output:[1,2,3,4,5,6,7,8]

Input=[6,-2,8,4,-3,7,-5,1]
Output=[-5,-3,-2,1,4,6,7,8]

Input=[6,-2,"8.8",4.4,-3,7.5,-5,1]
Output="Invalid input"

Input=23
Output="Invalid input"
```
## Solution key

```python
def mergesort(numbers):           
    if not numbers or len(numbers)==1:
        return numbers
    else:        
        mid=len(numbers)//2        
        left=mergesort(numbers[:mid])        
        right=mergesort(numbers[mid:])        
        return merge(left,right)

def merge(left,right):    
    merged=[]
    while left and right:
        if left[0]<right[0]:
            merged.append(left[0])
            left.remove(left[0])            
        else:
            merged.append(right[0])
            right.remove(right[0])
    merged+=left   
    merged+=right     
    return merged

```


## CloudCoder exercises
[To be updated]


## Related material
Merge sort -  http://bit.ly/KG_mergesort

## Pre-Lab Questions
1. Find the number of elements in the list
2. Write the code to split the list [6,2,8,4,3,7,5,1] into two halves.
3. Write the code to merge two lists [2,4,3] and [7,5,6]
4. Write the code to merge two sorted lists [2,6,7] and [3,5,8] in the sorted order
5. Validate whether given input is of ***list*** type.
6. Validate whether all the elements in the input are of ***int*** type.
7. Validate whether given list is empty
8. What are the first two elements to be merged from the input list [6,2,8,4,3,7,5,1] in the mergesort

## Post-Lab Questions
1. Modify the program to validate whether given input is a valid list.
2. Modify the code to avoid removing elements from `left` and `right` lists in the `merge` function.

## Bonus
1. What is the worst case complexity for merge sort algorithm?

## Interview Grade
1.Why quicksort is better than mergesort?
