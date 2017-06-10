# Lab 4 : Linear and Binary Search 

Given a list containing a list of numbers, find a number in the list using linear search and binary search algorithms. 


```python
def binary_search(myl, token):
    left = 0
    right = len(myl)-1
    found = False

    while left <= right and not found:
        mid = (right+left)//2
        if myl[mid] == token:
            found = True

        if myl[mid] > token:
            right = mid - 1
        else:
            left  = mid + 1

    return found

```

## Pre-Lab Questions: 

0. How to calculate midpoint of a list? Which operator is most relevant? 
1. Both `Linear search` and `Binary search` expect that the input list to be always sorted. If the list is not sorted, both algorithms will not work. True or False? 


## Post-Lab Questions

## Bonus 

The code for binary search recursive is as follows: 
![code](https://rawgit.com/kgisl/pythonFDP/master/img/binarySearchRecursiveCode.png) 

The test  image looks like this: 
![code](https://rawgit.com/kgisl/pythonFDP/master/img/binarySearchTest.png)

The binary search test output looks like this:
![code](https://rawgit.com/kgisl/pythonFDP/master/img/binarySearchTestOutput.png)

There are four calls made to the `binary_search_recursive` function. What change must be made to the code to reduce the number of calls to three? 



## Related Material

Binary search Visualization - http://j.mp/binarySearch
For visualizer debugging - https://goo.gl/aKE2ow 
Online execution - https://goo.gl/Z6z33B



