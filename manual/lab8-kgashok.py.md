# Lab 8: Selection Sort and Insertion Sort 

Sort the given list using selection sort and insertion sort. 


## Solution Key 

```python

def selectionSort(alist):
    # start filling from the end of the list
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        # find the position of the maximum value
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        # swap the fillslot with the maximum value
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):

  # scan every element to determined where it must be inserted
  for index in range(1, len(alist)):
	currentvalue = alist[index]
	# current location where it is situated
	location = index

	# determine which location it should be at 
	while location > 0:
	  if alist[location - 1] > currentvalue:
	      alist[location] = alist[location - 1]
	      location = location - 1
	  else:
		  break
	# end of inner while loop 
	 
	# update the list with the current element in consideration
	alist[location] = currentvalue
  # end of outer for loop

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

```

## Related Material 

- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

