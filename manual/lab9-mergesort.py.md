# Merge Sort

## Problem statement
Write a python program to sort the given list using `mergesort` algorithm

CD Extrenal Link : http://cyberdojo1.kgfsl.com/kata/edit/B006BC6DA0?avatar=bee

CD local Link : http://10.100.8.8/kata/edit/B006BC6DA0?avatar=bee

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
    # check for the empty list or the list with single element
    if not numbers or len(numbers) == 1:
        return numbers
    # recursive splitting (Divide)
    else:
        mid = len(numbers)//2
        left = mergesort(numbers[:mid])
        right = mergesort(numbers[mid:])
        return merge(left, right)


def merge(left, right):
    # left and right are the sorted lists to be merged
    # The merged list after sorting
    merged = []
    # Loop till left or right becomes empty
    while left and right:
        # remove the minimum of left[0] and right[0]
        # and add it to the merged list
        if left[0] < right[0]:
            merged += [left.pop(0)]
        else:
            merged += [right.pop(0)]
    # add the remaining elements of left, if any
    merged += left
    # add the remaining elements of right, if any
    merged += right
    return merged

```


## CloudCoder exercises
[To be updated]


## Related material
Merge sort -  http://bit.ly/KG_mergesort

## Pre-Lab Questions
1. How do you get the number of elements in the list
2. Write the code to split the list [6,2,8,4,3,7,5,1] into two halves.
3. Write the code to merge two lists [2,4,3] and [7,5,6]
4. Write the code to merge two sorted lists [2,6,7] and [3,5,8] in the sorted order
5. Validate whether given input is of **list** type.
6. Validate whether all the elements in the input are of **int** type.
7. Validate whether given list is empty
8. What are the first two elements to be merged from the input list [6,2,8,4,3,7,5,1] in the mergesort

## Post-Lab Questions
1. Modify the program to validate whether given input is a valid list.
2. Modify the code to sort the list of string elements.
```
example:
input=['python','c','c++','java']
expected output=['c','c++','python','java']
```

## Bonus
1. What is the worst case complexity for merge sort algorithm?


## Interview Grade
1.Why quicksort is better than mergesort?


## Test cases
```python
from mergesort import mergesort
import unittest
import random

class Test_mergesort(unittest.TestCase):

    def test_one_number(self):
        print("test 1")
        expected=[5]
        actual=mergesort([5])
        self.assertEqual(expected,actual)

    def test_two_numbers(self):
        print("test 2")
        expected=[2,5]
        actual=mergesort([5,2])
        self.assertEqual(expected,actual)   

    def test_three_numbers_ordered_right(self):
        print("test 3")
        expected=[2,5,8]
        input=[5,2,8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)       

    def test_three_numbers_unordered(self):
        print("test 4")
        expected=[2,5,8]
        actual=mergesort([5,8,2])
        self.assertEqual(expected,actual) 

    def test_bigger_list(self):
        print("test 5")
        input=[6,2,8,4,3,7,5,1]
        expected=[1,2,3,4,5,6,7,8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          


    def test_empty(self):
        print("test 6")
        input=[]
        expected=[]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          
    

    def test_negative_numbers(self):
        print("test 7")
        input=[6,-2,8,4,-3,7,-5,1]
        expected=[-5,-3,-2,1,4,6,7,8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          

    def test_float(self):
        print("test 8")
        input=[6,-2,8.8,4.4,-3,7.5,-5,1]
        expected=[-5,-3,-2,1,4.4,6,7.5,8.8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          

    def test_non_number(self):
        print("test 9")
        input=[6,-2,"8.8",4.4,-3,7.5,-5,1]
        expected="Invalid input"
        actual=mergesort(input)
        self.assertEqual(expected,actual)          

    def test_non_list(self):
        print("test 10")
        input=23
        expected="Invalid input"
        actual=mergesort(input)
        self.assertEqual(expected,actual) 

    def test_random(self):
        print("Random test input")
        input=[random.uniform(1,10) for _ in range(10)]
        expected=sorted(input)
        actual=mergesort(input)  
        self.assertEqual(expected,actual) 

if __name__ == '__main__':
    unittest.main()
```

## Answer key for validating the input

```python
def mergesort(numbers):
    # Top level function to validate the input once
    if not is_valid(numbers):
        return "Invalid input"
    # Original `mergedsort` function is renamed as `split`    
    return split(numbers) 
    
def is_valid(numbers):
    if(type(numbers) != list):
        return False
    for elem in numbers:
        if not isinstance(elem, int) and not isinstance(elem, float):
            return False
    return True
```
