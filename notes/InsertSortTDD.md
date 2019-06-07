
# TDD Approach to grokking InsertSort 

## 0 Create a sorted list containing numbers from 0 to 6. 
 - Draw a representation diagram of the list, indicating values and indexes corresponding to the values
 - Take the 3rd element and the last element and multiply them. Write code that does this and prints the actual value of the multiplication.
 - Create a list containing numbers 0 through 6. The first 4 elements must be sorted. The last 3 elements must be unsorted. 

## 1 Insert the `element  3.5` into the sorted list at index 4
 - Draw a representation diagram of the list, indicating values and indexes corresponding to the values 
 - What is the python code which will achieve this? Print the list before the insertion and print the list after the insertion
 - Try doing the above step using `enumerate` to display the index and value pairs and validate your diagram with it 
## 

## 2 Place the last element `3.5` in an `almost` sorted list into the list at index 4 
 - Build a sorted list containing numbers 0 to 6. Append 3.5 into the list at the very end. 
 - Draw a representation diagram for the above list 
 - Write Python code to remove `3.5` from its current location and then insert it at index 4. Print the list before and after insertion. 

## 3 Place the last element `2.5` in an `almost` sorted list into the list at the appropriate index so it fully sorted 
  - Build a sorted list containing 0 to 6. Append `2.5` into the list at the very end. 
  - In your notebook, write pseudo-code for determining how to find the index at which it needs to be inserted. 
	  - Convert the pseudo code into Python code.  
	  - Print the list before and after your insertion has happened

## 4 Place the 4th element in the list into the first part of the list `[0:3]` at the appropriate location
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
2. Use appropriate names for the variables so the code is self-explanatory. Additional comments may also be included to further explain the code 
3. Share with me your code through `repl.it` even prior to coming to class
4. In the same file, clearly mark the code corresponding to the various steps that I have detailed above 
5. Alternatively, you may use CyberDojo to document your progress and write test cases for validation 
	- Use [http://cyberdojo1.kgfsl.com/id_join/show](http://cyberdojo1.kgfsl.com/id_join/show) link and the session ID EUUPUS

## Pre-requisites

1. Familiarity with List methods and operations
	- pop()
	- insert() 
	- slicing 


## Verbose Mode Output

```bash
*************************
    INSERT SORT in verbose mode
    ************************
bl [2, 5, 3, 4, 6, 0, 1]
 -> sorted:[2, 5] : value:3 no good for idx:2 -- idx:2 j:2
j is 1 after loop
    -> Index to insert 1
    -> After right shift [2, 5, 5, 4, 6, 0, 1]
    -> After insertion   [2, 3, 5, 4, 6, 0, 1]
intermediary res: [2, 3, 5, 4, 6, 0, 1]

 -> sorted:[2, 3, 5] : value:4 no good for idx:3 -- idx:3 j:3
j is 2 after loop
    -> Index to insert 2
    -> After right shift [2, 3, 5, 5, 6, 0, 1]
    -> After insertion   [2, 3, 4, 5, 6, 0, 1]
intermediary res: [2, 3, 4, 5, 6, 0, 1]

 -> sorted:[2, 3, 4, 5, 6] : value:0 no good for idx:5 -- idx:5 j:5
 -> sorted:[2, 3, 4, 5, 6] : value:0 no good for idx:4 -- idx:5 j:4
 -> sorted:[2, 3, 4, 5, 6] : value:0 no good for idx:3 -- idx:5 j:3
 -> sorted:[2, 3, 4, 5, 6] : value:0 no good for idx:2 -- idx:5 j:2
 -> sorted:[2, 3, 4, 5, 6] : value:0 no good for idx:1 -- idx:5 j:1
j is 0 after loop
    -> Index to insert 0
    -> After right shift [2, 2, 3, 4, 5, 6, 1]
    -> After insertion   [0, 2, 3, 4, 5, 6, 1]
intermediary res: [0, 2, 3, 4, 5, 6, 1]

 -> sorted:[0, 2, 3, 4, 5, 6] : value:1 no good for idx:6 -- idx:6 j:6
 -> sorted:[0, 2, 3, 4, 5, 6] : value:1 no good for idx:5 -- idx:6 j:5
 -> sorted:[0, 2, 3, 4, 5, 6] : value:1 no good for idx:4 -- idx:6 j:4
 -> sorted:[0, 2, 3, 4, 5, 6] : value:1 no good for idx:3 -- idx:6 j:3
 -> sorted:[0, 2, 3, 4, 5, 6] : value:1 no good for idx:2 -- idx:6 j:2
j is 1 after loop
    -> Index to insert 1
    -> After right shift [0, 2, 2, 3, 4, 5, 6]
    -> After insertion   [0, 1, 2, 3, 4, 5, 6]
intermediary res: [0, 1, 2, 3, 4, 5, 6]
```

## Activities

1. Use a set of playing cards and demonstrate how they actually know **insert_sort** already
	2. Ask for a video contribution for **mergesort** since there is good one available on the web. Ask them to be creative and make it engaging video, unlike mine below! 
		3. Sample is available at http://j.mp/compareSort 
2. Use repl.it - form a list containing some random numbers of their choice. 
	3. Use alist.pop() and alist.insert alternatively and manually ask them to sort their own list using the insertsort technique
	4. There is a piece of code that they have to write to reflect what they are doing in their head 
	5. SPOILER ALERT! - http://bit.ly/manInsert

3. Write code on CloudCoder http://j.mp/insertionSortCC

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc2NDMwOTAyOSwtNjk0MDgzNTc4LDE1MT
AyMzcwNDEsLTE2MTU1MDI1NDcsLTk1NTU5MzI2NywtOTI5OTcz
NTA4LDY0NjI4NzgxMCwtMjk3Mjc5NzczLC0xMDYwMjgxMjMsLT
EyMzAyNTY4MjUsMTk2OTM4NTAzMCwtNzA2Njg4Njg3LC0xMjAz
MTQ1ODUxLDE1MDU0Mjk3MCwyNTUxMDE3MTgsMTM0OTU0OTcyLC
04MDQ5NjI4NTIsMTg5NTQwNjAyNl19
-->