# Solution for Linear Search
```python
def answer(list, key):
    if len(list) <= 0:
       return -1
    if len(list) == 1:
       return 0
    if key == list[0]:
       return 1
    length = len(list)
    if key == list[length -1]:
       return length-1
    position = 0
    for position in range(len(list)):
       if list[position] == key:
          return position
    return -1
 ```
 
 # CyberDojo Link
 http://10.100.8.8/kata/edit/86A713A750?avatar=walrus
