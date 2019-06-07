```python
alist = list(range(10))
print(alist)
for i in range(len(alist)):
    key = alist.pop()
    print(alist, key)
print("   -> Using pop()\n")

alist = list(range(10))
print(alist)
for i in range(len(alist)):
    key = alist.pop(0)
    print(key, alist)
print("    -> Using pop(0)\n")


alist = list(range(10))
for i in range(len(alist)):
    try:
        key = alist.pop(i)
        print(key, alist)
    except IndexError:
        print("Bad index!", f"i={i}, not < {len(alist)}")
        print(f"alist = {alist}", end=" ")
        break
print("      -> Using pop(i)\n")

alist = list(range(10))
print(alist)
for i in range(1, len(alist)):
    key = alist.pop(i)
    print(key, alist[:i], "_", alist[i:])
    #print(key, alist)
    alist.insert(i, key)
print("    -> Using pop(i)")
print(alist)

print("Doing insertsort on sorted list")
alist = list(range(10))
print(alist)
for i in range(1, len(alist)):
    key = alist.pop(i)
    print(key, alist[:i], "_", alist[i:])
    #print(key, alist)
    j = i
    while j > 0 and alist[j - 1] > key:
        j -= 1
    alist.insert(j, key)
print("    -> Using pop(i)")
print(alist)

from random import shuffle
print("\nDoing insertsort on shuffled list")
shuffle(alist)
print(alist)
for i in range(1, len(alist)):
    key = alist.pop(i)
    print(key, alist[:i], "_", alist[i:])
    #print(key, alist)
    j = i
    while j > 0 and alist[j - 1] > key:
        j -= 1
    alist.insert(j, key)
print(alist)

```
# TDD Code

```python
import timeit

# Preparing test list
from random import shuffle
alist = list(range(1000))
shuffle(alist)

start = timeit.default_timer()
# Actual code for insertsort
for _ in range(100):
    shuffle(alist)
    # print(alist)  # unsorted list

    for i in range(1, len(alist)):
        key = alist.pop(i)
        j = i
        while j > 0 and alist[j - 1] > key:
            j -= 1
        alist.insert(j, key)

    # print(alist) # sorted list
print("TDD Code")
print("Time taken", timeit.default_timer() - start)
```

## TextBook Code
```python
shuffle(alist)
start = timeit.default_timer()
# Actual code for insertsort
for _ in range(100):
    shuffle(alist)
    # print(alist)  # unsorted list

    # Actual code for insertsort
    for i in range(1, len(alist)):
        #key = alist.pop(i)
        key = alist[i]
        j = i
        while j > 0 and alist[j - 1] > key:
            alist[j] = alist[j - 1]
            j -= 1
        alist[j] = key
        #alist.insert(j, key)

        # print(alist) # sorted list

print("Typical Text Book Code")
print("Time taken", timeit.default_timer() - start)

```

```bash
	TDD Code
	Time taken 5.4949
	Typical Text Book Code
	Time taken 9.0260
	The Ultimate
	Time taken 0.4143
```

```python

alist = list(range(10))
print(alist)
for i in range(len(alist)):
    key = alist.pop()
    print(alist, key)
print("   -> Using pop()\n")

alist = list(range(10))
print(alist)
for i in range(len(alist)):
    key = alist.pop(0)
    print(key, alist)
print("    -> Using pop(0)\n")


alist = list(range(10))
for i in range(len(alist)):
    try:
        key = alist.pop(i)
        print(key, alist)
    except IndexError:
        # print("Bad index!", f"i={i}, not < {len(alist)}")
        # print(f"alist = {alist}", end=" ")
        break
print("      -> Using pop(i)\n")

alist = list(range(10))
print(alist)
for i in range(1, len(alist)):
    key = alist.pop(i)
    print(key, alist[:i], "_", alist[i:])
    #print(key, alist)
    alist.insert(i, key)
print("    -> Using pop(i)")
print(alist)

print("Doing insertsort on sorted list")
alist = list(range(10))
print(alist)
for i in range(1, len(alist)):
    key = alist.pop(i)
    print(key, alist[:i], "_", alist[i:])
    #print(key, alist)
    j = i
    while j > 0 and alist[j - 1] > key:
        j -= 1
    alist.insert(j, key)
print("    -> Using pop(i)")
print(alist)

from random import shuffle
print("\nDoing insertsort on shuffled list")
shuffle(alist)
print(alist)
for i in range(1, len(alist)):
    key = alist.pop(i)
    print(key, alist[:i], "_", alist[i:])
    #print(key, alist)
    j = i
    while j > 0 and alist[j - 1] > key:
        j -= 1
    alist.insert(j, key)
print(alist)


import timeit

# Preparing test list
from random import shuffle
alist = list(range(10))
times = 10
shuffle(alist)

start = timeit.default_timer()
# Actual code for insertsort
for _ in range(times):
    shuffle(alist)
    # print(alist)  # unsorted list

    for i in range(1, len(alist)):
        key = alist.pop(i)
        j = i
        while j > 0 and alist[j - 1] > key:
            j -= 1
        alist.insert(j, key)

    # print(alist) # sorted list
print("TDD Code")
print("Time taken", timeit.default_timer() - start)

shuffle(alist)
start = timeit.default_timer()
# Actual code for insertsort
for _ in range(times):
    shuffle(alist)
    # print(alist)  # unsorted list

    # Actual code for insertsort
    for i in range(1, len(alist)):
        #key = alist.pop(i)
        key = alist[i]
        j = i
        while j > 0 and alist[j - 1] > key:
            alist[j] = alist[j - 1]
            j -= 1
        alist[j] = key
        #alist.insert(j, key)
    # print(alist) # sorted list

print("Typical Text Book Code")
print("Time taken", timeit.default_timer() - start)

start = timeit.default_timer()
#print(alist, id(alist))
for _ in range(times):
    shuffle(alist)
    # print(alist)  # unsorted list

    # Actual code for insertsort
    for i in range(1, len(alist)):
        #key = alist.pop(i)
        already_sorted = alist[:i]
        key = alist[i]
        for j in range(i):
            if key < already_sorted[j]:
                alist[j + 1:i + 1] = alist[j:i]
                alist[j] = key
                # alist.insert(j, key)
                break
        # else:
        #	alist.insert(i, key)
        # if j != i:
# print(alist)
assert(alist == list(range(10)))
print("Another variant")
print("Time taken", timeit.default_timer() - start)
```

## Create a sorted list containing numbers from 0 to 6. 
 - Draw a representation diagram of the list, indicating values and indexes corresponding to the values
 - Take the 3rd element and the last element and multiply them. Write code that does this.

 
## Insert the `element  3.5` into the sorted list at index 4
 - Draw a representation diagram of the list, indicating values and indexes corresponding to the values 
 - What is the python code which will achieve this? Print the list before the insertion and print the list after the insertion
 - Try doing the above step using `enumerate` to display the index and value pairs and validate your diagram with it 
## 

## Place the last element `3.5`in an `almost` sorted list into the list at index 4 
 - Build a sorted list containing numbers 0 to 6. Append 3.5 into the list at the very end. 
 - Draw a representation diagram for the above list 
 - Write Python code to remove `3.5` from its current location and then insert it at index 4. Print the list before and after insertion. 

## Place the last element `2.5` in an `almost` sorted list into the list at the appropriate index so it fully sorted 
  - Build a sorted list containing 0 to 6. Append `2.5` into the list at the very end. 
  - Write pseudocode for determining how to find the index at which it needs to be inserted 



```python

"Ground up explanation for InsertSort"
al = list(range(7))
bl = al[:]  # make a copy
bl[5:] = bl[4:]
print("bl after right shift", bl)
bl[4] = 3.4
print("bl", bl)


"What if 3.4 happens to be at the end of the list?"
bl = al[:] + [3.4]
bl[5:] = bl[4:]
print("bl after right shift", bl)
bl[4] = 3.4
try:
    assert(bl == [0, 1, 2, 3, 3.4, 4, 5, 6])
except BaseException:
    print("ERROR: bl", bl)

bl = al[:] + [3.4]
bl[5:7] = bl[4:6]
print("bl after right shift", bl)
bl[4] = 3.4
try:
    assert(bl == [0, 1, 2, 3, 3.4, 4, 5, 6])
    print("Insert success!")
except BaseException:
    print("ERROR: bl", bl)

bl = al[3:] + al[:3]
print("bl", bl)

i = 4  # sorted upto 4
j, key = 4, bl[4]
# print(f"key = {key} into {bl}")

while j > 0 and key < bl[j - 1]:
    j = j - 1
# print(f'Index to insert {j}')
bl[j + 1:i + 1] = bl[j:i]
# print(f'After right shift {bl}')
bl[j] = key
# print(f'After insertion {bl}')

''' Alternate for loop based method
for j in range(i):
	if key < bl[j]:
		print(f'Index to insert {j}')
		bl[j+1:i+1] = bl[j:i]
		print(f'After right shift {bl}')
		bl[j] = key
		print(f'After insertion {bl}')
	break
'''

print("\n\n\n")

bl = al[3:] + al[:3]
print("bl", bl)
# i = 4 # sorted upto 4
for i in range(4, len(bl)):
    #j, key = 4, bl[4]
    j, key = i, bl[i]
    while j > 0 and key < bl[j - 1]:
        j = j - 1
    # print(f'Index to insert {j}')
    bl[j + 1:i + 1] = bl[j:i]
    # print(f'After right shift {bl}')
    bl[j] = key
    # print(f'After insertion {bl}')
    # print(f'intermediary: {bl}')

'''
print(f' *************************\n\
	INSERT SORT in verbose mode\n\
	************************')
'''

bl = al[:]  # + al[:]
shuffle(bl)
# bl.sort(reverse=True)
# bl.sort()
print("bl", bl)
for i in range(1, len(bl)):
    # i = 4 # sorted upto 4
    j, key = i, bl[i]
    #key = bl[4]
    # print(f"-> key = {key} into {bl})")

    while j > 0 and key < bl[j - 1]:
        # print(f' -> sorted: {bl[:i]} and key:{key} not good for idx:{j} //
        # i{i} j{j}')
        j -= 1

    # print(f'j is {j} after loop')
    # print(f'    -> Index to insert {j}')
    bl[j + 1:i + 1] = bl[j:i]
    # print(f'    -> After right shift {bl}')
    bl[j] = key
    # print(f'    -> After insertion {bl}')
    print('intermediary: {0} before next key'.format(bl))
    '''
	#if key > bl[i-1]:
	#  print(f'***A HACK! {key} > {bl[i-1]}')
	#  continue
	for j in range(i):
		print(f' -> sorted: {bl[:i]} and key:{key} good for idx:{j}?')
		if key < bl[j]:
			print(f'    -> Index to insert {j}')
			bl[j+1:i+1] = bl[j:i]
			print(f'    -> After right shift {bl}')
			bl[j] = key
			print(f'    -> After insertion {bl}')
			break
	print(f'intermediary: {bl} before next key')
  '''



```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ0NzUyOTE1NSwyNTUxMDE3MTgsMTM0OT
U0OTcyLC04MDQ5NjI4NTIsMTg5NTQwNjAyNl19
-->