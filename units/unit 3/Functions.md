


## UNIT III CONTROL FLOW, FUNCTIONS
**Conditionals: Boolean values and operators, conditional (if), alternative (if-else), chained conditional (if-elif-else); Iteration: state, while, for, break, continue, pass; Fruitful functions: return values, parameters, local and global scope, function composition, recursion; Strings: string slices, immutability, string functions and methods, string module; Lists as arrays. Illustrative programs: square root, gcd, exponentiation, sum an array of numbers, linear search, binary search**

### 3.1. CONDITIONALS:
#### 3.1.1 BOOLEAN VALUES AND OPERATORS:

 - [ ] A Boolean expression is an expression that is either true or  false.
 - [ ] Converting Boolean to integer, the value is always 0 for false and 1 for  true
 - [ ] Converting integer to Boolean, the value is True for all integers except  zero
 - [ ] Python type is **bool**.

    
| Boolean Expression |Meaning  |
|--|--|
| x != y|  x is not equal to y|
|x > y   |x greater than y
|x<y     | x less than y
|x<=y    | x less than or equal to
|x>=y    | x greater than or equal to

#### Boolean and Logical operators
#### 1. *and* Operator:

| Op1 |Op2  |Op1 and Op2	|
|--|--|--|
|TRUE	|TRUE	|TRUE
|TRUE	|FALSE 	|FALSE
|FALSE	|TRUE	|FALSE
|FALSE	|FALSE	|FALSE

#### 1. *or* Operator:
| Op1 |Op2  |Op1 or Op2	|
|--|--|--|
|TRUE	|TRUE	|TRUE
|TRUE	|FALSE 	|TRUE
|FALSE	|TRUE	|TRUE
|FALSE	|FALSE	|FALSE

#### Example 1: “and” operator
       A python program to display the National holidays.
       For example:
           January 26-Republic day
           August 15-Indepependance day 
           October 2-Gandhi Jayanthi*
       If user input is other than the given condition,Error will be displayed as “Invalid input”.
    
			    print("Enter Month and Day")
				month=input()
				day=int(input())
				if(month =="january" and day ==26):
					print ("republic day")
				elif(month =="august" and day ==15):
					print ("independence day")
				elif(month =="october" and day ==2):
					print ("Gandhi Jayanthi")
				else:
					print ("invalid input")
#### Example 1: “or” operator

    Number of days in a month varies from 30 to 31 days. 
    Write a python program to read the name of the month and display corresponding days. 
    If he input is other than the given month, then display error message as “Invalid”.
   
	    import sys
		month=input()
		if(month=="may" or month=="july" or month=="august"):
			 print ("31")
		elif(month=="jun"):
			 print ("30")
		else:
			 print ("invalid")`
	   
#### 3.1.2. OPERATORS

 - Each built-in data types come with its set of operators.
 - Operators are the constructs which can manipulate the value of  operands.
 - They are generally classified into binary and unary operators based on the number of arguments.
 - Binary operators require two operands
 - Python language supports the following types of  operators.

	 1. Arithmetic  Operators
	 2. Comparison (Relational) Operators
	 3. Assignment  Operators
	 4. Logical  Operators
	 5. Membership  Operators
	 6. Identity  Operators
#### i) Arithmetic operators

 - Arithmetic  operators  are  used  to  perform  mathematical  operations  like  addition,  subtraction,  Multiplication
 - Assume variable ‘_a’_ holds 10 and variable ‘_b_’ holds 20  then the following table shows the result of arithmetic operators.
 
 
|Operator|Description |	Example|
|--|--|--|--|
|+ Addition	|Adds values on either side of the operator.	|a + b = 30
|-Subtraction	|Subtracts right hand operand from left hand operand.	|a – b = -10
|* Multiplication	|Multiplies values on either side of the operator	|a * b = 200
|/ Division	|Divides left hand operand by right hand operand |b / a = 2
|% Modulus	|Divides left hand operand by right hand operand and returns remainder	|b % a = 0
|** Exponent	|Performs exponential (power) calculation on operators	|a**b =10 to the power 20
|// Floor Division	|The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −	|9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

#### (ii)	Comparison Operators
•	These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
•	The result of these operators is a Boolean value (True / False)
•	Assume variable a holds 10 and variable b holds 20, then

| Operator |Description  |Example
|--|--|--|
| == Equal	 | If the values of two operands are equal, then the condition becomes true. |(a == b) is not true.
|!= Not Equal	|If values of two operands are not equal, then condition becomes true.	|(a != b) is true.
|> Greater than	|If the value of left operand is greater than the value of right operand, then condition becomes true.	|(a > b) is not true.
|<	|If the value of left operand is less than the value of right operand, then condition becomes true.|(a < b) is true.
|>=	|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	|(a >= b) is not true.
|<=	|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	|(a <= b) is true.

#### (iii)	Assignment  and Compound Operators
•	Used to assign values to variables
•	Compound operator performs arithmetic operation and then assigns the value
•	Assume variable a holds 10 and variable b holds 20, then 
| Operator	|Description	|Example
|--|--|--|
| = Assignment	|Assigns values from right side operands to left side operand   |c = a + b assigns value of a + b into c
|+= Add & Assign|It adds right operand to the left operand and assign the result to left operand |c += a is equivalent to c = c + a
|-= Subtract & Assign	|It subtracts right operand from the left operand and assign the result to left operand	|c -= a is equivalent to c = c - a
|*= Multiply and Assign	|It multiplies right operand with the left operand and assign the result to left operand |c *= a is equivalent to c = c * a
| /= Divide and Assign	|It divides left operand with the right operand and assign the result to left operand	|c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
|%= Modulus & Assign	|It takes modulus using two operands and assign the result to left operand	|c %= a is equivalent to c = c % a
|**= Exponent & Assign	|Performs exponential (power) calculation on operators and assign value to the left operand |c ** = a is equivalent to c = c ** a

#### iv) Logical Operators
•	There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then
•	Used to reverse the logical state of its operand.
•	There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then –

|Operator  |Description	  |Example
|--|--|--|
|*and* Logical AND  |If both the operands are true then condition becomes true.   |(a and b) is true.
|*or* Logical OR	|If any of the two operands are non-zero then condition becomes true.|(a or b) is true.
|*not* Logical NOT	| Used to reverse the logical state of its operand.	|Not(a and b) is false.

#### v) Membership Operators
•	Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
•	There are two membership operators as explained below –


| Operator |Descrription  |Example 
|--|--|--|
| in | True if value/variable is found in the sequence|5 in numlist, returns true if 5 is in the numlist.
|not in	|True if value/variable is not found in the sequence	|5 in numlist, returns false if 5 is not in the numlist.

#### vi) Identity Opertors
•	‘is’ operator – Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
•	‘is not’ operator – Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.


|Operator|Description |Example
|--|--|--|
| is |Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.|x is y, here is results in 1 if id(x) equals id(y).
|is not	|Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.|x is not y, here is not results in 1 if id(x) is not equal to id(y).


#### 3.1.3	CONDITIONAL STATEMENTS
•	In programming language conditional statements are used to perform different computations or actions depending on whether a condition evaluates to true or false
•	The conditions use comparisons and arithmetic expressions with variables
•	The expressions are evaluated to Boolean values True or False

Available conditional statements in python are

 1. if statement
 2. If..else statement
 3. If..elif..else statement 
 4. Nested if statement

**Rules for conditional statements:**
•	The colon(:) is required at the end of the condition
•	The body of the if statement is indicated by the indentation(four spces are used for indentation)
•	Python interprets non-zero values as true and 0 as false

#### 1. ‘if’  STATEMENT (CONDITIONAL STATEMENT)
•	Sometimes we want to execute a code or a block of code only if a certain condition is satisfied.
•	the program evaluates the condition and will execute statement(s) only if the condition is True.
•	If the condition is False, the statement(s) is not executed.
•	In Python, the body of the if statement is indented. 
•	Python interprets non-zero values as True. None and 0 are interpreted as False.
							
 **Syntax**
> 	   if (test expression/condition):
	> 			 statement(s)


 







