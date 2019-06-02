
# Insertion into Sorted List

## Description

1. It is assumed that there is a list `A` which has elements which are already sorted. 
2. The task at hand is to insert another element (referred to as `key`) into the sorted list `A` so that after the insertion, the list must continue to remain sorted. 
3. The `key` is made part of the sorted list by increasing the size by 1 and placing it as the last element of the list. Therefore, space complexity is `O(1)`.  
4. An iteration of `j` is begun from `i-1` all the way to `0`
	-  The `key` is compared with the last element `A[j-1]` of the sorted list. If the element is greater than the key, it is shifted right to A[j].
5. If key is greater than the element in the list, insertion happens at the location `j` and the iteration is exited 
6. The function returns with the list containing `key` and maintaining the sort order.  

## Algorithm in pseudocode 

	func INSERT_INTO_SORTEDARRAY: 
	    (input) sorted list, and key to be inserted
	    (output) sorted list with key inserted 
	    
	    key: <- last element in A  // A is already sorted
	    index: <- length(List) - 1 
		
        iterate j from index to 1
	        if A[j-1] > key then 
	            shift the element right 
	        else
	            break
      
        if j != index: 
            A[j] = key // inserted at the right location
        return A 
    end func 

## Example 
Assume sorted list `ar = [3, 5, 6, 7]` and element to insert is `2`. 

During the intermediary steps, the contents of `ar` are as shown below. The `key` is value `2` and eventually it gets inserted at beginning of the list.

	Start: 3 4 6 7 2 
		3 5 6 7 7  // 7 shifted right
		3 5 6 6 7  // 6 shifted right
		3 5 5 6 7  // 5 shifted right
		3 3 5 6 7  // 3 shifted right
		2 3 5 6 7  // 2 inserted in position 1 (index 0)
	Final: 2 3 4 6 7
		
## Source Code
```python
def printarray(arr):
    for e in arr: print (e, end = " ")
    print()

def insert_into_sortedArray(ar):    
    key = ar[-1]  # the candidate to insert
    i = len(ar)-1 # position of candidate
    j = i

    while j > 0 and ar[j-1] > key: 
        ar[j] = ar[j-1] # move bigger element right
        j = j-1
        printarray(ar)
    if j != i: 
        ar[j] = key
        printarray(ar)

```
## Output
```bash 
# sorted array 
ar = [1, 2, 5,  6, 7, 9]
insert_into_sortedArray (ar + [4])
'''	
	1 2 5 6 7 9 9 
	1 2 5 6 7 7 9 
	1 2 5 6 6 7 9 
	1 2 5 5 6 7 9 
	1 2 4 5 6 7 9 
'''
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTYxNDU4MywxODM2OTcyODQ1LDEwMD
IwNDI3NzAsLTM0Njg1MDYwOSw4ODg1NjM3OThdfQ==
-->