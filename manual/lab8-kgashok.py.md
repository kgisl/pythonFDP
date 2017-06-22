# Lab 8: Sorting
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



## Recursive version of SelectionSort 

```python
	def selsort(l):
	    if not l: return []
	    idx, v = min(enumerate(l), key=operator.itemgetter(1))
	    return [v] + selsort(l[:idx] + l[idx + 1:])
```

## Recursive QuickSort 

http://mcsp.wartburg.edu/zelle/python/sigcse-workshop/mgp00064.html

```python 

def qsort(L): 
	if len (L) <= 1: return L
	
	return qsort([n for n in L[1:] if n < L[0]]) + \
					[L[0]] + \
					qsort([n for n in L[1:] if n >= L[0]])

```

or 
```python
def qsort(L):
		if len(L) <= 1: return L
		
		def subList(pivot, op):
			return [elem for elem in L[1:] if op(elem, pivot)]

		return qsort(subList(L[0], operator.lt)) + \
			[L[0]] + \
			qsort(subList(L[0], operator.ge))

```

or using `lambda` and `filter`

```python
def qsort(L): 
	if len(L) <= 1: return L
	pivot = L[0]
	sublist = lambda op: [*filter(lambda num: op(num, pivot), L[1:])]
	
	return qsort(sublist(lt))+ [pivot] + qsort(sublist(ge))
		
print (qsort([3,1,4,2,5]) == [1,2,3,4,5])
```

## What exactly does this accomplish? 


```python 
	from threading import Timer
	l = [8, 2, 4, 6, 7, 1]
	for n in l:
	    Timer(n, lambda x: print(x), [n]).start()
```

