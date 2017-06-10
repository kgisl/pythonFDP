
# Lab 5 : find n prime numbers

[TOC]

## Problem statement 

Implement a python program that finds the first `n` prime numbers. 

    Sample Input1: [1,10]
    Sample Output1: [2,3,5,7]

    Sample Input2: [7000,7005]
    Sample Output2: [7001]

    Sample Input3: ["hello","world"]
    Sample Output3: Invalid Range


## Solution Key

```python 

def prime(min, max):
    primeList = []
    if type(min) == str or type(max) == str:
        return "Invalid Range"
    for num in range(min, max + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeList.append(num)
    return primeList
```

## CloudCoder Exercise 



## Pre-Lab Questions 


## Post-Lab Questions 

## Bonus 
## Interview Grade 

## Related Links

### CyberDojo Link

http://10.100.8.8/kata/edit/FECB42D487?avatar=wolf or [alt](http://cyberdojo1.kgfsl.com/kata/edit/FECB42D487?avatar=wolf) 
