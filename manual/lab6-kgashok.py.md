
# Lab 6: find the maximum of a list of numbers. 

Implement a python program that finds the maximum in a list of numbers. The program must call a python function `getMaxNumber(numbers)` that takes as argument a list of numbers (maximum of 10 integers). It must then return the maximum number in that list. 

	Sample Input1: []
	Sample Output1: "N.A."
	
	Sample Input2: [1,2]
	Sample Output2: 2
	
	Sample Input3: [1,2,3,4]
	Sample Output3: 4


# Lab 6 Solution 

```python 

def getMaxNumber(numbers):

    maxval = None
    for num in numbers:
        if not maxval or maxval < num:
            maxval = num
    return maxval if maxval else "N.A."


def getListOfNumbers():
    ilist = []
    for _ in range(0, 10):
        try:
            userVal = int(input())
            ilist.append(int(userVal))
        except ValueError:
            # if user enters a non-integer, then break
            break

    return ilist


userList = getListOfNumbers()
print("List of numbers: ", userList)
print(getMaxNumber(userList))

```


# CloudCoder exercise 

http://cloudcoder.kgisl.com/cloudcoder/#exercise?c=1,p=81 


# Viva Questions 

1. How will you find the minimum of the values in a list of numbers? What change will you make to the code? 
2. If the list is empty, what will be the value returned from the function? 
3. If the list happens to be empty, then return the string `"N.A.".`. What changes will you make to the code? 
3. For Point 2, refactor the code that you have written using a ternary operator. 


## Bonus 1 
4. Suppose the user wanted the freedom not to be restricted to a maximum of 10 numbers, what change would you do to the code? 

## Bonus 2 
1. How will you rewrite the function `getMaxNumber()` using the in-built function `max` (https://docs.python.org/3/library/functions.html?highlight=max#max)? 
2. Can you reduce the function to a one-liner? 

## Bonus 3

1. How will you find out the 2nd largest number in the list of numbers? Take into consideration that the list may contain duplicate numbers as well. 

 
