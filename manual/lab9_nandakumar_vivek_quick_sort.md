# Quick Sort
​
## Problem statement
Write a python program to sort the given list using `quick sort` algorithm
CD EXtrenal Link : http://cyberdojo1.kgfsl.com/kata/edit/8EE56C12AC?avatar=parrot
CD Local Link : http://10.100.8.8/kata/edit/8EE56C12AC?avatar=parrot

```
Examples:
Sample Input0: [1, 2, 3, 4]
Sample Output0: [1, 2, 3, 4]

Sample Input1: [5, 12, 3, 21, 4]
Sample Output1: [3, 4, 5, 12, 21] 

Sample Input2: [7.1, 9.2, 3.1]
Sample Output2: [3.1, 7.1, 9.2]
```

## Solution key

```python

def partition(lst, start, end, pivot):
  
  lst[pivot], lst[end] = lst[end], lst[pivot]
  store_index = start
  for i in range(start, end):
    if lst[i] < lst[end]:
     lst[i], lst[store_index] = lst[store_index], lst[i]
    store_index += 1
  lst[store_index], lst[end] = lst[end], lst[store_index]
  return store_index

def quick_sort(lst, start, end):
    if start >= end:
      return lst
    pivot = round((start+end)/2)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)

def sort(lst):
  for i in lst:
    result=isinstance(i,str)
  if result==True:
    return "invalid input"
    break
  quick_sort(lst,0, len(lst) - 1)
  return lst
  
  ```


## CloudCoder exercises
[To be updated]



## Pre-Lab Questions

0. Quick sort uses ___________. 

                a. Divide and Conquer Technique             b.Greedy Approach       
                c. Back Tracking                 d. None of the above

1.How to select a pivot element?

2.Given the following list of numbers [1, 20, 11, 5, 2, 9, 16, 14, 13, 19] what would be the first pivot value using the median method?

3. Given the following list of numbers [14, 17, 13, 15, 19, 10, 3, 16, 9, 12] what is the contents of the list after the second partitioning according to the quicksort algorithm?

4. What is the average case complexity for quick sort algorithm

  a.O(n)                   b.O(n*n)            c.O(nlogn)          d.O(logn)

5. What is the worst case complexity for quick sort algorithm

  a.O(n)    b.O(n*n)            c.O(nlogn)           d.O(logn)


## Post-Lab Questions

 
1. What are the advantages and disadvantages of quick sort?

2. List out the applications of quick sort.

3. If the list is empty, what will be the value returned from the function?

4. If the list contain any string element, what will be the value returned from the function?

5. Does the selection of pivot element help to optimize the quick sort algorithm performance?


## Bonus


## Interview Grade



