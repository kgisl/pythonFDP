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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgwNDk2Mjg1MiwxODk1NDA2MDI2XX0=
-->