
# Lab 3: Exponentiation (power of a number)

[TOC]

## Problem statement 

Write a Python program to compute the power of number.

	Sample Input1: 0,2
	Sample Output1: 0
	
	Sample Input2: 2, 0
	Sample Output2: 1

	Sample Input3: 2, 3.2
	Sample Output3: 9.19
		
	Sample Input3: 2, -3.3
	Sample Output3: 0.11



## Solution Key

```python 

def expo(x,n):
    result=1
    if type(x) == str or type(n) ==str:
            return "Enter integer Value!!!!"
    if n == 0:
     return 1
    elif(n>0):
        while(n!=0):
            result=result*x
            n-=1
        return round(result,2) 
    else:
        while(n!=0):
            result=result*x
            n+=1
    return round(1/result,2)  
def expofloat(x,n):
    result=1
    if(n>0):
        r=int(n)
        c=r
        m=n%r
        while(r!=0):
            result=result*x
            r-=1
        p=pow(x,m)
        return round(result * p,2) 
    if(n<0):
        r=int(n)
        c=r
        m=n%r
        while(r!=0):
            result=result*x
            r+=1
        p=pow(x,m)
        return round(1/result * p,2) 
```


## CloudCoder Exercise 




## Related material 





## Pre-Lab Questions 



## Post-lab Questions



## Bonus 1 

## Related Material 

Review https://stackoverflow.com/questions/327002/which-is-faster-in-python-x-5-or-math-sqrtx

## Cyber Dojo Link
http://cyberdojo.kgfsl.com/kata/edit/06D7B4092A?avatar=rhino

