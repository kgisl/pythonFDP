
# Incremental Approach

## 0 Create a sorted list containing numbers from 0 to 6. 
 - Draw a representation diagram of the list, indicating values and indexes corresponding to the values
 - Take the 3rd element and the last element and multiply them. Write code that does this and prints the actual value of the multiplication.
 
## 1 Insert the `element  3.5` into the sorted list at index 4
 - Draw a representation diagram of the list, indicating values and indexes corresponding to the values 
 - What is the python code which will achieve this? Print the list before the insertion and print the list after the insertion
 - Try doing the above step using `enumerate` to display the index and value pairs and validate your diagram with it 
## 

## 2 Place the last element `3.5`in an `almost` sorted list into the list at index 4 
 - Build a sorted list containing numbers 0 to 6. Append 3.5 into the list at the very end. 
 - Draw a representation diagram for the above list 
 - Write Python code to remove `3.5` from its current location and then insert it at index 4. Print the list before and after insertion. 

## 3 Place the last element `2.5` in an `almost` sorted list into the list at the appropriate index so it fully sorted 
  - Build a sorted list containing 0 to 6. Append `2.5` into the list at the very end. 
  - In your notebook, write pseudo-code for determining how to find the index at which it needs to be inserted. 
	  - Convert the pseudo code into Python code.  
	  - Print the list before and after your insertion has happened

## 4 Place the 4th element in the list into the first part part of the list (0:3) at the appropriate location
  - Build a list in this order `[4, 5, 6, 0, 3, 1, 2]` - the 4th element being `0`. Represent this using a diagram in your notebook 
  - Initialize `idx = 4` and iterate through the first part of the list (which is already sorted) and insert it into the array at the appropriate location. Write the code for this. 

## 5 Place the last four elements in the list so that the list is fully sorted 
  - Build a list in this order `[4, 5, 6, 0, 3, 1, 2]`
  - Iterate through the last four elements and perform the same operations you did in the previous exercise
  - Validate through proper print statements that your list is actually properly sorted 

## 6 Place your code inside a function  `insertsort`and write test cases to test the functionality 


## 7 Replace the list method calls and instead use `slicing` to achieve the same sorting operation 


# Notes
1. Bring your code and notes to the FDP session in a notebook of your own. 
2. Write code so that it is self explanatory. 
3. Use appropriate names for the variables so there might be very little comments that might be required to further explain what the code does
4. Share with me your code through `repl.it` even prior to coming to class 



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg3NzQ3MjA2OCwxNTA1NDI5NzAsLTEzMD
A3NTkzOTddfQ==
-->