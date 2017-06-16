# Lab 3: Compute power of a number (Exponentiation)

## Problem statement

Write a Python program to compute the power of a given number.

```
Sample Input1: 2,3
Sample Output1: 8

Sample Input2: 0, 3
Sample Output2: 0

Sample Input3: 3,0
Sample Output3: 1 
	
Sample Input4: 2, -3
Sample Output4: 0.125

Sample Input4: 2, "ab"
Sample Output4: Invalid Input
```


## Solution Key

### Using `for` loop

```python

def expo(base, expo):
    ans = 1.0
    if type(base) == str or type(expo) == str:
        return "Invalid Input"
    elif expo >= 0:
        for i in range(1, expo + 1):
            ans = base*ans
    else:
        for i in range(expo, 0):
            ans = 1/base*ans
    return ans
```

### Using while loop:

```python 
def expo(base, expo):
    ans = 1.0
    if type(base) == str or type(expo) == str:
        return "Invalid Input"
    elif expo >= 0:
        while expo != 0:
            ans *= base
            expo -= 1
    else:
        while expo != 0:
            ans *= (1/base)
            expo += 1
    return ans
```

### Using builtin function

```python
import math


def expo(base, expo):
    if type(base) == str or type(expo) == str:
        return "Invalid Input"
    else:
        n = math.pow(base, expo)
        return n
```

### Using ** operator:

```python 
def expo(base, expo):
    if type(base) == str or type(expo) == str:
        return "Invalid Input"
    else:
        base **= expo
        return base
```

## CD links
http://cyberdojo.kgfsl.com/kata/edit/90A83D4231?avatar=peacock - for loop
http://cyberdojo.kgfsl.com/kata/edit/06D7B4092A?avatar=elephant - Builtin func
http://cyberdojo.kgfsl.com/kata/edit/06D7B4092A?avatar=bear - using ** operator
http://cyberdojo.kgfsl.com/kata/edit/06D7B4092A?avatar=squirrel - while loop
