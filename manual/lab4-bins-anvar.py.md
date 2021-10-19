# Solution for Binary Search

```python
def answer(list, key):
    if len(list) <= 0:
       return -1
    if len(list) == 1:
       return 0
    if key == list[0]:
       return 0
    length = len(list)
    if key == list[length -1]:
       return length-1
    length = len(list)
    low = 0
    high = length-1
    mid = int(length/2)
    if key < list[mid]:
       return(BinarSearch(list, low, mid, key))
    elif key > list[mid]:
       return(BinarSearch(list, mid, high, key))
    elif key == list[mid]:
        return mid
def BinarSearch(list, low, high, key):
        for low in range(high):
           if list[low] == key:
              return low
        return -1
```

## Cyber Dojo Link

http://10.100.8.8/kata/edit/86A713A750?avatar=walrus
