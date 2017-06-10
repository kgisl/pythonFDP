# Lab 4 : Linear and Binary Search 

Given a list containing a list of numbers, find a number in the list using linear search and binary search algorithms. 


```python
def binary_search(myl, token):
    found = False

    left = 0
    right = len(myl)-1

    while left <= right and not found:
        mid = (right+left)//2
        if myl[mid] == token:
            found = True

        if myl[mid] > token:
            right = mid - 1
        else:
            left  = mid + 1

    return found

def linear_search(myl, token):
    found = False
    for number in myl:
        if number == token:
            found = True
            break
    return found

# Recursive Version
def binary_search_r(myl, token):
    print ("Searching for ", token, "in ", myl)
    left  = 0
    right = len(myl)-1
    mid   = (right + left)//2

    if len(myl) == 0:
        return False
    if myl[mid] == token:
        return True

    if myl[mid] > token:
        myl = myl[:mid]
    else:
        myl = myl[mid:]

    return binary_search_r(myl, token)


# Program starts here

if __name__ == '__main__':

    choice = input("Linear or Binary Search (l/b)? ")
    alist  = input("Enter the list of numbers ")
    token  = input("What to search for? ")

    if (choice == 'b'):
        alist = sorted(alist)
        print (binary_search(alist, token))
    else:
        print (linear_search(alist, token))

```

## Pre-Lab Questions

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

As per the test output, there are four calls made to the `binary_search_recursive` function before the result is arrived at. What change(s) must be made to the code to reduce the number of calls to three? 


## Related Material

- Binary search Visualization - http://j.mp/binarySearch
- For visualizer debugging - https://goo.gl/aKE2ow 
- Online execution - https://goo.gl/Z6z33B



