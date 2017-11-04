
# Lab 10 :Matrix Multiplication

[TOC]

## Problem statement 

Write a Python Program to implement Matrix Multiplication

    Sample Input0    : [[1, 2], [1, 2]], [[1, 2], [1, 2]]
    Sample Output0   : [[3, 6], [3, 6]]

    Sample Input1    : [[1, 1], [1, 1]], [[1, 2, 1], [1, 2, 1]]
    Sample Output1   : [2, 4, 2], [2, 4, 2]

    Sample Input2    : [[1, 1], [1, 1]], [[1, 2], [1, 2], [1, 2]]
    Sample Output2   : Cannot multiply the matrices. Incorrect dimensions.	




## Solution Key

```python 

def format_matrix(matrix):
    return "\n".join((("{:<5}"*len(row)).format(*row))for row in matrix)
    
def matrixmulti(X, Y):
    result = [[0 for col in range(len(Y[0]))] for row in range(len(X))]

    if  len(X[0]) != len(Y):
        print ("Cannot multiply the matrices. Incorrect dimensions.")
        return

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    print(format_matrix(result))
    return result



```


## CloudCoder Exercise 

http://j.mp/matrixMultiplyCC 


## Pre-Lab Questions 

0. How to initialize a matrix (5 by 5) so that all its entries are equal to the number 10? What is the one line code for this?
1. Write a program to test whether the given matrix is a square matrix or not.
2. Write a program to test whether the given two matrices (say `a` and `b`), the matrix product operation `a * b` is possible or not. 



## Post-lab Questions

## Bonus 1 

1. Fix the failing test case in the following cyberdojo session - http://j.mp/randomMatrixCD
2. Use the functions to write a `randomize_matrix` function to generate a square matrix of size 5
3. Is the matrix creation the most efficient? Are you able to create a size of `22000 by 22000` before CyberDojo times out?

## Bonus 2 

Consider a two-dimensional matrix containing integer entries in which all rows and all columns are sorted in ascending order. For example:

```
 1 12 43 87
 9 25 47 88
17 38 48 92
45 49 74 95
```
Your task is to write a program that takes a matrix as describe above, and a target integer, and determines if the target integer is present in the matrix. 



## Related Material 


### CD Link 

http://10.100.8.8/kata/edit/3A77017D5C?avatar=dolphin  (Poongothai)  
http://cyberdojo1.kgfsl.com/kata/edit/F52E98217E?avatar=raccoon (Ashok)


### Transpose a matrix 

- CloudCoder Problem:  http://j.mp/stransposeCC and http://j.mp/transposeCC 
- The video key for it (using visualizer) -  http://j.mp/transposeVideoKey 

