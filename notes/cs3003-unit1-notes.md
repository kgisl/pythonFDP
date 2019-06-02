
# Insertion into Sorted List

## Algorithm 

	func INSERT_INTO_SORTEDARRAY: 
	    input: sorted list, and key to be inserted
	    output: sorted list with key inserted 
	    
	    key <= last element in A  // A is a list
	    index = length(List) - 1 
		
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

During the intermediary steps, the contents of `ar` are as shown below, `0` getting inserted at beginning of the list.

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
eyJoaXN0b3J5IjpbMTA2NjAwMTk1MywtMzQ2ODUwNjA5LDg4OD
U2Mzc5OF19
-->