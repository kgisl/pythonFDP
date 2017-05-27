
# Lab 6 

Define a python function `getMaxNumber(numbers)` that takes in a list of numbers and that returns the maximum number in that list. If the list happens to be empty, then return the string `"N.A."`

	Sample Input1: []
	Sample Output1: "N.A."
	
	Sample Input2: [1,2]
	Sample Output2: 2
	
	Sample Input3: [1,2,3,4]
	Sample Output3: 4


# Lab 6 Solution 

```python 

	def getMaxNumber(numbers):

	    max = None
	    for num in numbers:
	        if not max or max < num:
	            max = num
	    return max if max else "N.A"
```


# CloudCoder exercise 

http://cloudcoder.kgisl.com/cloudcoder/#exercise?c=1,p=81 

