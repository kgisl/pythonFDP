# UNIT III CONTROL FLOW, FUNCTIONS
**Conditionals: Boolean values and operators, conditional (if), alternative (if-else), chained conditional (if-elif-else); Iteration: state, while, for, break, continue, pass; Fruitful functions: return values, parameters, local and global scope, function composition, recursion; Strings: string slices, immutability, string functions and methods, string module; Lists as arrays. Illustrative programs: square root, gcd, exponentiation, sum an array of numbers, linear search, binary search**

## 3.1. CONDITIONALS:
### 3.1.1 BOOLEAN VALUES AND OPERATORS:

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

### Boolean and Logical operators
### 1. *and* Operator:

| Op1 |Op2  |Op1 and Op2	|
|--|--|--|
|TRUE	|TRUE	|TRUE
|TRUE	|FALSE 	|FALSE
|FALSE	|TRUE	|FALSE
|FALSE	|FALSE	|FALSE

### 1. *or* Operator:
| Op1 |Op2  |Op1 or Op2	|
|--|--|--|
|TRUE	|TRUE	|TRUE
|TRUE	|FALSE 	|TRUE
|FALSE	|TRUE	|TRUE
|FALSE	|FALSE	|FALSE

**Example 3.1: “and” operator**

A python program to display the National holidays.
For example:
   January 26-Republic day
   August 15-Indepependance day 
   October 2-Gandhi Jayanthi*
If user input is other than the given condition,Error will be displayed as “Invalid input”.

**Program:**
				
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

**Output**
		
			Enter Month and Day
			august
			15
			independence day


**Example 3.2: “or” operator**

Number of days in a month varies from 30 to 31 days. 
Write a python program to read the name of the month and display corresponding days. 
If he input is other than the given month, then display error message as “Invalid”.

**Program:**
	    	
			import sys
			month=input("Enter the name of the month")
			if(month=="may" or month=="july" or month=="august"):
				 print ("31")
			elif(month=="jun"):
				 print ("30")
			else:
				 print ("invalid")

**Output**
		
			Enter name of the month
			may
			31
			
	
	   
### 3.1.2. OPERATORS

- [ ] Each built-in data types come with its set of operators.
- [ ] Operators are the constructs which can manipulate the value of  operands.
- [ ] They are generally classified into binary and unary operators based on the number of arguments.
- [ ] Binary operators require two operands
- [ ] Python language supports the following types of  operators.

 
 i.  Arithmetic  Operators
 
 ii. Comparison (Relational) Operators
	 
iii. Assignment  Operators
	 
 iv. Logical  Operators
	 
  v.  Membership  Operators
	 
 vi. Identity  Operators
	 
### i. Arithmetic operators

- [ ] Arithmetic  operators  are  used  to  perform  mathematical  operations  like  addition,  subtraction,  Multiplication
- [ ] Assume variable ‘_a’_ holds 10 and variable ‘_b_’ holds 20  then the following table shows the result of arithmetic operators.
 
 
|Operator|Description |	Example|
|--|--|--|
|+ Addition	|Adds values on either side of the operator.	|a + b = 30
|-Subtraction	|Subtracts right hand operand from left hand operand.	|a – b = -10
|* Multiplication	|Multiplies values on either side of the operator	|a * b = 200
|/ Division	|Divides left hand operand by right hand operand |b / a = 2
|% Modulus	|Divides left hand operand by right hand operand and returns remainder	|b % a = 0
|** Exponent	|Performs exponential (power) calculation on operators	|a**b =10 to the power 20
|// Floor Division	|The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −	|9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

### ii.	Comparison Operators
- [ ]	These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
- [ ]	The result of these operators is a Boolean value (True / False)
- [ ]	Assume variable a holds 10 and variable b holds 20, then

| Operator |Description  |Example
|--|--|--|
| == Equal	 | If the values of two operands are equal, then the condition becomes true. |(a == b) is not true.
|!= Not Equal	|If values of two operands are not equal, then condition becomes true.	|(a != b) is true.
|> Greater than	|If the value of left operand is greater than the value of right operand, then condition becomes true.	|(a > b) is not true.
|<	|If the value of left operand is less than the value of right operand, then condition becomes true.|(a < b) is true.
|>=	|If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	|(a >= b) is not true.
|<=	|If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	|(a <= b) is true.

### iii. Assignment  and Compound Operators
- [ ]	Used to assign values to variables
- [ ]	Compound operator performs arithmetic operation and then assigns the value
- [ ]	Assume variable a holds 10 and variable b holds 20, then 

| Operator	|Description	|Example
|--|--|--|
| = Assignment	|Assigns values from right side operands to left side operand   |c = a + b assigns value of a + b into c
|+= Add & Assign|It adds right operand to the left operand and assign the result to left operand |c += a is equivalent to c = c + a
|-= Subtract & Assign	|It subtracts right operand from the left operand and assign the result to left operand	|c -= a is equivalent to c = c - a
| * = Multiply and Assign	|It multiplies right operand with the left operand and assign the result to left operand |c * = a is equivalent to c = c * a
| /= Divide and Assign	|It divides left operand with the right operand and assign the result to left operand	|c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
|%= Modulus & Assign	|It takes modulus using two operands and assign the result to left operand	|c %= a is equivalent to c = c % a
| ** = Exponent & Assign	|Performs exponential (power) calculation on operators and assign value to the left operand |c ** = a is equivalent to c = c ** a

### iv. Logical Operators
- [ ]	There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then
- [ ]	Used to reverse the logical state of its operand.
- [ ]	There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then –

|Operator  |Description	  |Example
|--|--|--|
|*and* Logical AND  |If both the operands are true then condition becomes true.   |(a and b) is true.
|*or* Logical OR	|If any of the two operands are non-zero then condition becomes true.|(a or b) is true.
|*not* Logical NOT	| Used to reverse the logical state of its operand.	|Not(a and b) is false.

### v. Membership Operators
- [ ]	Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
- [ ]	There are two membership operators as explained below –


| Operator |Descrription  |Example 
|--|--|--|
| in | True if value/variable is found in the sequence|5 in numlist, returns true if 5 is in the numlist.
|not in	|True if value/variable is not found in the sequence	|5 in numlist, returns false if 5 is not in the numlist.

### vi. Identity Opertors
- [ ]	‘is’ operator – Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
- [ ]	‘is not’ operator – Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.


|Operator|Description |Example
|--|--|--|
| is |Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.|x is y, here is results in 1 if id(x) equals id(y).
|is not	|Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.|x is not y, here is not results in 1 if id(x) is not equal to id(y).


### 3.1.3. CONDITIONAL STATEMENTS
- [ ]	In programming language conditional statements are used to perform different computations or actions depending on whether a condition evaluates to true or false
- [ ]	The conditions use comparisons and arithmetic expressions with variables
- [ ]	The expressions are evaluated to Boolean values True or False

Available conditional statements in python are

 i.   if statement
 
 ii.  if..else statement
 
 iii. if..elif..else statement
 
  iv. Nested if statement

**Rules for conditional statements:**
- [ ]	The colon(:) is required at the end of the condition
- [ ]	The body of the if statement is indicated by the indentation(four spces are used for indentation)
- [ ]	Python interprets non-zero values as true and 0 as false

### 3.1.3.1. ‘if’  STATEMENT (CONDITIONAL STATEMENT)
- [ ]	Sometimes we want to execute a code or a block of code only if a certain condition is satisfied.
- [ ]	the program evaluates the condition and will execute statement(s) only if the condition is True.
- [ ]	If the condition is False, the statement(s) is not executed.
- [ ]	In Python, the body of the if statement is indented. 
- [ ]	Python interprets non-zero values as True. None and 0 are interpreted as False.
							
 **Syntax**

				if (test expression/condition):
					statement(s)
		
**Example 3.3:**
												
Python program to check whether a person is eligible for vote.

**Program:**
	
				print("Enter Your age")
				n=int(input()) 
				if(n>=18):
					print("Eligible for voting") 
					
**Output**
				
				Enter Your age
				21
				Eligible for voting
	   
### 3.1.3.2. ‘if...else’ STATEMENT(ALTERNATIVE CONDITIONAL STATEMENT)

- [ ]	The if..else statement evaluates test expression and will execute body of if only when test condition is True.
- [ ]	If the condition is False, body of else is executed. Indentation is used to separate the blocks.

**Syntax of if...else**

				if (test expression/condition) : 
					statement(s)
				else:
					statement(s)
 
**Example 3.4:**

Python program to checks if the number is positive or negative

**Program**
				
				num = 3
				if num >= 0: 
					print("Positive or Zero")
				else:
					print("Negative number")
					

**Output**
		
				Positive or Zero
					

**Example 3.5:**

**Program**

				print("Enter a number")
				num=int(input())
				if(num%2)==0: 
				   print("Even Number")
				else:
				    print("Odd Number")
				    
**Output**

				Enter a number
				10
				Even Number
				

### 3.1.3.3. ‘if...elif...else’(CHAINED CONDITIONAL STATEMENT)

- [ ]  The elif is short for else if. It allows us to check for multiple expressions.
- [ ]   If the condition for if is False, it checks the condition of the next elif block and so on.
- [ ]	If all the conditions are False, body of else is executed.
- [ ]	Only one block among the several if...elif...else blocks is executed according to the condition.
- [ ]	The if block can have only one else block. But it can have multiple elif blocks.
  
**Syntax of if...elif...else**


				if (test expression/condition):
					Body of if
				elif (test expression/condition):
					Body of elif
				else:
					Body of else
 
 **Example 3.6:**
 
 Python program to check if the number is positive or negative or zero

**Program**
	
				num = 3.4 
				if num > 0:
					print("Positive number") 
				elif num == 0:
					print("Zero") 
				else: 
					print("Negative number")
					

**Output**

				Negative number
				
				
 **Example 3.7:**

**Program**
 
				n=int(input("Enter a number between seven and ten"))
				if(n==7):
				    print("heptagon") 
				elif(n==8):
				    print("octogon") 
				elif(n==9):
				    print("nanogon") 
				elif(n==10):
				    print("decagon")
				else:
				    print("input should be from 7 to 10")
				    

**Output**

				Enter a number between seven and ten
				8
				octogon
				
							    
### 3.1.3.4. NESTED CONDITIONAL

- [ ]	A conditional statement defined inside another conditional statement is called nested conditional statement.
- [ ]	Any number of these statements can be nested inside one another.
- [ ]	Indentation is the only way to figure out the level of nesting.
- [ ]	Similarly,  alternative and chained conditionals can also be nested

**Example 3.8:**

Python program to check if the number is positive or negative or zero using nested if.

**Program**


				num = float(input("Enter a number: ")) 
				if num >= 0:
				    if num == 0:
					print("Zero")
				    else:
					print("Positive number") 
				else:
				    print("Negative number")

**Output**

				Enter a number: 10
				Positive number
				
				
## 3.2. REPETITION STRUCTURE/LOOPING/ITERATIVE STATEMENTS

i.  ‘for‘ Statement
	
ii. ‘while’ Statement 


### 3.2.1. ‘for’ LOOP
- [ ]	The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable
objects.
- [ ]	Iterating over a sequence is called traversal.
- [ ]	val is the variable that takes the value of the item inside the sequence on each iteration.
- [ ]	Loop continues until we reach the last item in the sequence. 
- [ ]	The body of for loop is separated from the rest of the code using indentation.

**Syntax of for Loop**

				for val in sequence:
					Body of for

**Example 3.9:**

Python Program to find the sum of all numbers stored in a list

**Program**
	
				#number list
				numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
				sum = 0
				for val in numbers:
				    sum = sum+val 
				print("The sum is", sum)
				
**Output**
	
				The sum is 48
				

### 3.2.2. ‘while’ LOOP:

- [ ] In while loop, test expression is checked first.
- [ ] The body of the loop is entered only if the test expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.
- [ ] In Python, the body of the while loop is determined through indentation.
- [ ] Body starts with indentation and the first unintended line marks the end.
- [ ] Python interprets any non-zero value as True. None and 0 are interpreted as False.

**Syntax**

				while test_expression:
					Body of while

**Example 3.10:**

Python program using while Loop to add natural numbers upto n 

**Program**

				n = int(input("Enter a number: "))
				sum = 0
				i= 1
				while i <= n:
				    sum = sum + i 
				    i = i+1
				print("The sum is", sum)
				
**Output**

				Enter a number: 10
				The sum is 55


In the above program, the test expression will be True as long as our counter variable i is less than or equal to n (10 in our program).

**while loop with else**
- [ ]	An optional else block with while loop can also be used.
- [ ]	The else part is executed if the condition in the while loop evaluates to False.
- [ ]	The while loop can be terminated with a break statement.

**Example 3.11:**

Python program to illustrate the use of else statement with the while loop

**Program**

				counter = 0
				while counter < 3: 
					print("Inside loop")
					counter = counter + 1 
				else:
					print("Inside else")
**Output**

				Inside loop
				Inside loop
				Inside loop
				Inside else

- [ ]	A counter variable to print the string inside loop three times.
- [ ]	On the forth iteration, the condition in while becomes False. Hence, the else part is executed.

**Difference between while and for loop**
|while loop|for loop  |
|--|--|
|Indefinite loop |Definite loop  |
|The exit condition will be evaluated again and execution resumes from the top(repeatedly executes a set of code)|The for is to iterate over a sequence (List, Tuple and dictionary etc)

### 3.2.3. UNCONDITIONAL STATEMENTS

- [ ]	Unconditional statements are used in the situations, there is a need to exit the loop completely when an external condition is triggered or there may be a situation to skip a part of the code and start the next execution.
- [ ]	Python provide the following statements
       
i.   Break
      
ii.  Continue
     
iii. Pass
     
			
- [ ]	In Python, break and continue statements can alter the flow of a normal loop.
- [ ]	Loops iterate over a block of code until test expression is false, to terminate the current iteration or even the whole loop without checking test expression.
- [ ]	The break and continue statements are used in these cases.

**i. Python break statement**

- [ ]	The break statement terminates the loop containing it.
- [ ]	Control of the program flows to the statement immediately after the body of the loop.
- [ ]	If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.

**Syntax of break**

				break

**Example 3.12:**

Python program to illustrate break statement inside loop

**Program**

				for val in "string":
					if val == "i":
							break
					print(val)  
				print("The end")

**Output**

				s
				t
				r
				The end


**Example 3.13:**

Python program to demonstrate break

**Program**

				i=1
				while i<=10:
				    if(i==5):
					break
				    print(i)
				    i = i + 1
				print("completed")

**Output**

				1
				2
				3
				4
				completed
				

**ii.	Python continue statement**

-[] The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
-[] Loop does not terminate but continues on with the next iteration.

**Syntax of Continue**

				continue
				
**Example 3.14:**

Python Program to show the use of continue statement inside loops

**Program**

				for val in "string": 
					if val == "i":
						continue 
					print(val)
				print("The end")
				
**Output**

				s
				t
				r
				n
				g
				The end
				
- [ ] This program is same as the above example except the break statement has been replaced with continue.
- [ ] continue with the loop, if the string is "i", not executing the rest of the block. Hence, we see in our output that all the letters except "i" gets printed.

**Example 3.15:**

Python Program to show the use of continue statement inside loops

**Program**

				n=int(input("Enter total number of numbers\n"))
				for i in range(0,n):
					a=int(input("Enter the number:")) 
					if(a<0):
						continue
					print("Number is "+str(a))
			
**Output**

				Enter total number of numbers
				5
				Enter the number:12
				Number is 12
				Enter the number:14
				Number is 14
				Enter the number:16
				Number is 16
				Enter the number:-1
				Enter the number:23
				Number is 23

**iii.	Pass STATEMENT**
- [ ] It is used when a statement is required syntactically but you do not want any command or code to execute.
- [ ] The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet.

Syntax of pass

			pass

**Example 3.16:**

Python program to illustrate pass

**Program**

				sequence = {'p', 'a', 's', 's'}
				for val in sequence:
				    pass
				print("pass is just a placeholder for functionality to be added later.")
				
**Output**

				pass is just a placeholder for functionality to be added later.

**Example 3.17:**

**Program**

				for num in [20, 11, 9, 66, 4, 89, 44]:
					if num%2 == 0:
						pass
					else:
						print(num)
						
**Output**

				11
				9
				89
						

## 3.3. FRUITFUL FUNCTIONS: RETURN VALUES, PARAMETERS, LOCAL AND GLOBAL SCOPE, FUNCTION COMPOSITION, RECURSION
### 3.3.1. Functions
- [ ] Function is a group of statements that together perform a task.
- [ ] A function is a block of organized, reusable code that is used to perform a single, related action.
**i. Defining a Function**
Simple rules to define a function in Python.
- [ ] Function blocks begin with the keyword **def** followed by the function name and parentheses ( ).
- [ ] Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
- [ ] The first statement of a function can be an optional statement - the documentation string of the function or docstring.
- [ ] The code block within every function starts with a colon (:) and is indented.
- [ ] The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return none.

**i. Creating a Function**

**Syntax**

				def functionname( parameters ): 
					"function_docstring"
					function body
					return [expression]
**Example 3.18:**

				def my_function(): 
					print("Hello from a function")

**ii. Calling a Function**
	To call a function, use the function name followed by parenthesis.

**Example 3.19:**

**Program**

				def my_function(): 
					print("Hello from a function") 
				my_function()

**Output**

				Hello from a function
				

**iii. Parameters**

- [ ] Information can be passed to functions as parameter.
- [ ] Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.
- [ ] The following example has a function with one parameter (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

**Example 3.20:**

**Program**

				def my_function(fname): 
					print(fname + " Refsnes")

				#main function
				my_function("Emil") 
				my_function("Tobias") 
				my_function("Linus")
				
**Output**

				Emil Refsnes
				Tobias Refsnes
				Linus Refsnes

**iv. Default Parameter Value**

- [ ] The following example shows how to use a default parameter value.
- [ ] If we call the function without parameter, it uses the default value:

**Example 3.21:**

**Program**

				def my_function(country = "Norway"): 
					print("I am from " + country)

				#main function
				my_function("Sweden") 
				my_function("India") 
				my_function() 
				my_function("Brazil")

**Output**

				I am from Sweden
				I am from India
				I am from Norway
				I am from Brazil
				
### 3.3.2 Return Values
- [ ] The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
- [ ] All the above examples are not returning any value. You can return a value from a function as follows:

				#Function definition is here 
				def sum( arg1, arg2 ):
					# Add both the parameters and return them." 
					total = arg1 + arg2
					print("Inside the function : ", total)
					return total;

				# Now you can call sum function 
				total = sum( 10, 20 );
				print("Outside the function : ", total)
				
**Example 3.22:**

**Program**

				def my_function(x):
					return 5 * x
				
				#function calling statements
				print(my_function(3)) 
				print(my_function(5)) 
				print(my_function(9))
				
**Output**

				15
				25
				45

### 3.3.3 Function Arguments
The types of formal arguments are:

	  i.	Required arguments
	  
	 ii.	Keyword arguments
	 
	iii.	Default arguments
	
	 iv.	Variable-length arguments

**i. Required arguments**
- [ ] Required arguments are the arguments passed to a function in correct positional order.
- [ ] The number of arguments in the function call should match exactly with the function definition.

**Example 3.23:**

**Program**

				#Function definition where str is the required argument
				def display(str): 
				    print(str)

				#main script
				str="hello"
				display(str)
				
**Output**

				hello		
				

**ii. Keyword arguments**
- [ ] Keyword arguments are related to the function calls.
- [ ] When keyword arguments in a function call, the caller identifies the arguments by the parameter name.
- [ ] This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters.

**Example 3.24:**

**Program**

				def display(name,number,fraction):
				    print("The string is:",name) 
				    print("The integer is:",number) 
				    print("The float is:",fraction)

				#Main script-Fucntion calling with keyword arguments
				display(fraction=58.62,name="hello",number=28)
				
**Output**

				The string is: hello
				The integer is: 28
				The float is: 58.62
				

**iii. Default arguments**
- [ ] A default argument is an argument that assumes a default value if a value is not provided in
the function call for that argument.
- [ ] The following example gives an idea on default arguments, it prints default age if it is not passed 

**Example 3.25:**

**Program**

				def printinfo( name, age = 35 ):
					'''This prints a passed info into this function'''
					print("Name: ",name)
					print("Age ",age)
					return

					#Calling printinfo function 
					printinfo(age=50, name="miki" )
					printinfo(name="miki")
					
**Output**

				Name:  miki
				Age  50
				Name:  miki
				Age  35


**iv. Variable-length arguments**
- [ ] Variable length argument make function calls with many(arbitary).
- [ ] These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

**Syntax:**

				def functionname([formal_args,] *var_args_tuple ):
					"function_docstring"
					function body
					return [expression]

An asterisk is placed before the variable name that holds the values of all non keyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call.

**Example 3.26:**

**Program**

				def printinfo( arg1, *vartuple ):
					'''This prints a variable passed arguments'''
					print("Output is:")
					print(arg1)
					for var in vartuple: 
						print(var)
					return

				#Calling printinfo function
				printinfo( 10 )
				printinfo( 70, 60, 50 )

**Output**

				Output is:
				10
				Output is:
				70
				60
				50

### 3.3.4. Scope of Variables
- [ ] All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.
- [ ] The scope of a variable determines the portion of the program where you can access a particular identifier.
- [ ] There are two basic scopes of variables in Python −
	- [ ] Global variables
	- [ ]	Local variables

**Global vs. Local variables**

- [ ] Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
- [ ] This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions.
- [ ] When you call a function, the variables declared inside it are brought into scope.

**Example 3.27:** 

**Program**

				total = 0; # This is global variable. 
				def sum(arg1, arg2):
				# Add both the parameters and return them."
				    total = arg1 + arg2; # Here total is local variable. 
				    print("Inside the function local total : ", total)
				    return total;

				#Calling sum function 
				sum( 10, 20 );
				print("Outside the function global total : ", total)
				
**Output**

				Inside the function local total :  30
				Outside the function global total : 0

### 3.3.5. Function composition or Anonymous Functions
- [ ] Function composition is the way of combining the functions
- [ ] These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.
- [ ] Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
- [ ] An anonymous function cannot be a direct call to print because lambda requires an expression

**Syntax**

				lambda [arg1 [,arg2,.....argn]]:expression
**Example 3.28:**

**Program**

				# Function definition is here
				sum = lambda arg1, arg2: arg1 + arg2;
				# Now you can call sum as a function 
				print("Value of total : ", sum( 10, 20 ))
				print("Value of total : ", sum( 20, 20 ))
				
**Output**

				Value of total :  30
				Value of total :  40

### 3.3.6. Recursive Function:

- [ ] Recursion is the process of the function call by itself.
- [ ] In Python, a function can call other functions. It is even possible for the function to call itself. These type of construct are termed as recursive functions.
- [ ] Example - recursive function to find the factorial of an integer.

 Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

**Example 3.29:**

**Program**	
	
				def calc_factorial(x):
					'''This is a recursive function
					to find the factorial of an integer''' 
					if(x == 1):
						return 1 
					else:
						return (x * calc_factorial(x-1)) 

				#Main Script
				num = 4
				print("The factorial of", num, "is",calc_factorial(num))
				
**Output**

				The factorial of 4 is 24

- [ ] In the above example, calc_factorial() is a recursive functions as it calls itself.
- [ ] This function with a positive integer, it will recursively call itself by decreasing the number.
- [ ] Each function call multiples the number with the factorial of number 1 until the number is equal to one. This recursive call can be explained in the following steps.



calc_factorial(4)	# 1st call with 4
* calc_factorial(3)	# 2nd call with 3
* 3 * calc_factorial(2)	# 3rd call with 2
* 3 * 2	* calc_factorial(1)	# 4th call with 1
* 3	* 2	* 1	# return from 4th call as number=1
* 3	* 2		# return from 3rd call
* 6			# return from 2nd call
			# return from 1st call

- [ ] Our recursion ends when the number reduces to 1. This is called the base condition.
- [ ] Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.

**Advantages of recursion**
+ Recursive functions make the code look clean and elegant.
+ A complex task can be broken down into simpler sub-problems using recursion.
+ Sequence generation is easier with recursion than using some nested iteration.

**Disadvantages of recursion**
+ Sometimes the logic behind recursion is hard to follow through.
+ Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
+ Recursive functions are hard to debug.

## 3.4. STRINGS
A string is a sequence of characters. You can access the characters one at a time with the bracket operator:

**Example 3.30:**

**Program**

				fruit = 'banana'
				letter = fruit[1]
				print("The letter present at index 1 is:",letter)
				
**Output**
	
				The letter present at index 1 is: a
				
				
The second statement selects character number 1 from fruit and assigns it to letter. The expression in brackets is called an index. The index indicates which character in the sequence you want (hence the name). Always index starts from 0. The value of the index has to be an integer. Otherwise you get:

**Example 3.31:**

**Program**
	
				fruit = 'banana'
				letter = fruit[1.5]
				print("The letter present at index 1 is:",letter)
				
**Output**
				
				Traceback (most recent call last):
				  File "c:\users\administrator\mu_code\or_op.py", line 2, in <module>
				    letter = fruit[1.5]
				TypeError: string indices must be integers


### 3.4.1. String Lengths
len() is a built-in function that returns the number of characters in a string.

**Example 3.32:**

**Program**

				fruit = 'banana'
				length = len(fruit)
				print("The length of the strength is:",str(length))

**Output**

				The length of the strength is: 6				
	
To get the last letter of a string, you might be tempted to try something like this:

**Example 3.33:**

**Program**
				fruit = "banana"
				length = len(fruit)
				last = fruit[length]
				print("The last letter in fruit is:",last)
				
**Output**

				Traceback (most recent call last):
				  File "c:\users\administrator\mu_code\or_op.py", line 3, in <module>
				    last = fruit[length]
				IndexError: string index out of range

The reason for the IndexError is that there is no letter in 'banana' with the index 6. Since we started counting at zero, the six letters are numbered 0 to 5. To get the last character, you have to subtract 1 from length:

				last = fruit[length-1]
				print(last)  #dispalys a

Alternatively, you can use negative indices, which count backward from the end of the string. The expression fruit[-1] yields the last letter, fruit[-2] yields the second to last,
and so on.

### 3.4.2. String slices
A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

				str = 'Monty Python'
				print(str[0:5])      #Prints Monty
				print(str[6:12]      #Prints Python

The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth” character, including the first but excluding the last. 
If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string:
	
				fruit = 'banana'
				print(fruit[:3])  #Prints 'ban'
				print(fruit[3:]   #Prints 'ana'
				
If the first index is greater than or equal to the second the result is an empty string, represented by two quotation marks:

				fruit = 'banana'
				print(fruit[3:3]) #Prints ' '
				
An empty string contains no characters and has length 0, but other than that, it is the same as any other string.
### 3.4.3. Strings are immutable
It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character in a string. For example:

				greeting = 'Hello, world!'
				greeting[0] = 'J'
				#Causes following output
	TypeError: 'str' object does not support item assignment
The “object” in this case is the string and the “item” is the character you tried to assign. For now, an object is the same thing as a value, but we will refine that definition later. An item is one of the values in a sequence.
The reason for the error is that strings are immutable, which means you can’t change an existing string. The best you can do is create a new string that is a variation on the original:


				greeting = 'Hello, world!'
				new_greeting = 'J' + greeting[1:]
				print(new_greeting)       #Prints Jello, world!
This example concatenates a new first letter onto a slice of greeting. It has no effect on the original string.

###  3.4.4. String methods
A method is similar to a function—it takes arguments and returns a value—but the syntax is different. For example, the method upper takes a string and returns a new string with all uppercase letters:
Instead of the function syntax upper(word), it uses the method syntax word.upper().
	
				word = 'banana'
				new_word = word.upper()
				print(new_word)    #Prints BANANA
 
This form of dot notation specifies the name of the method, upper, and the name of the string to apply the method to, word. The empty parentheses indicate that this method
takes no argument.
A method call is called an invocation; in this case, we would say that we are invoking upper on the word.
As it turns out, there is a string method named find that is remarkably similar to the function we wrote:

				 word = 'banana'
				 index = word.find('a')
				 print(index)    #Prints 1
In this example, we invoke find on word and pass the letter we are looking for as a parameter.
#### i. find method
Actually, the find method is more general than our function; it can find substrings, not just characters:
	
				word = 'banana'
				print(word.find('na'))    #Prints 2

It can take as a second argument the index where it should start:
		
				word = 'banana'
				print(word.find('na', 3))   # Prints 4

And as a third argument the index where it should stop:

				name = 'bob'
				print(name.find('b', 1, 2))   #Prints -1
	
This search fails because b does not appear in the index range from 1 to 2 (not including 2).
#### ii. String comparison
The relational operators work on strings. To see if two strings are equal: 
	
				if(word == 'banana'):
					print('All right, bananas.')
Other relational operations are useful for putting words in alphabetical order:

				if(word < 'banana'):
					print('Your word,' + word + ', comes before banana.')
				elif(word > 'banana'):
					print('Your word,' + word + ', comes after banana.')
				else:
					print('All right, bananas.')
	
Python does not handle uppercase and lowercase letters the same way that people do. All the uppercase letters come before all the lowercase letters, so:Your word, Pineapple, comes before banana.
A common way to address this problem is to convert strings to a standard format, such as all lowercase, before performing the comparison. Keep that in mind in case you have to defend yourself against a man armed with a Pineapple.

#### iii. Indexing

Individual characters in a string can be accessed using subscript([ ]) operator. The expression in bracket is called as Index.
#### iv. Traversing a String

A string can be traversed by accessing characters from one index to another.
|P | Y |T|H|O|N
|--|--|--|--|--|--|
| 0 |1  |2|3|4|5
|-6|-5|-4|-3|-2|-1|

### 3.4.4 . String module
-[] The string module consists of number of useful constants,classes and functions
-[] These functions are used to manipulate strings
-[] Some constants are defined in string module are:
	+ string.ascii_lowercase - Refers all lower case letters. Example: a-z
	+ string.ascii_uppercase - Refers all upper case letters. Example: A-Z 
	+ string.digits - Refer digits from 0-9 
	+ string.uppercase - A string that has all the characters that are considered upper case letters Example: A-Z
	+ string.whitespace - A string that has all characters that are considered white space like space,tab etc

Example: Hello world Hai Ajay
Output: HelloworldHaiAjay

**Example 3.34:**
Program that use different string methods

**Program**

				str="welcome to the world of python"
				print("uppercase=",str.upper( )) 
				print("lowercase=",str.lower( )) 
				print("split=",str.split( )) 
				print("join=",'-'.join(str.split( )))
				print("replace=",str.replace("python","java" )) 
				print("count of o=",str.count('o' ))
				print("find of =",str.find("of"))
				
**Output**

				uppercase= WELCOME TO THE WORLD OF PYTHON
				lowercase= welcome to the world of python
				split= ['welcome', 'to', 'the', 'world', 'of', 'python']
				join= welcome-to-the-world-of-python
				replace= welcome to the world of java
				count of o= 5
				find of = 21
				

### 3.4.5. Example Programs:**
**1. Traversing a string**

**Program**
	
				message="hello!"
				index=0
				for i in message:
					print("message[",index,"]=",i) 
					index+=1
					
**Output**

				message[ 0 ]= h
				message[ 1 ]= e
				message[ 2 ]= l
				message[ 3 ]= l
				message[ 4 ]= o
				message[ 5 ]= !

**2. String operations**

**Program**

				str="Hello This is python"
				i=2
				print("Character at index 2: ",str[i]) 
				print("Character at index i*3+1: ",str[i*3+1])
				
**Output**				

				Character at index 2:  l
				Character at index i*3+1:  h


**3. Concatenate two strings**

**Program**

				str1="hello" 
				str2="world" 
				str3=str1+str2
				print("The string is:",str3)
				
**Output**

				The string is: helloworld
				
**4. Append a string**

**Program**

				Greet="Hello"
				n=input("Enter the String to Concatenate:") 
				Greet+=n;
				print(Greet))
				
**Output**
				Enter the String to Concatenate:World
				HelloWorld
				
**5. String slices**

-[] A substring of a string is called a slice
-[] A slice operation is used to refer the subpart of strings
-[] The subset of a string can be taken from string by using [ ] operator

**Example 1: Positive Indexing/Slicing**

**Program**

				str="python"
				print("str[1:5]=",str[1:5])
				print("str[:6]=",str[:6])
				print("str[1:]=",str[1:])
				print("str[:]=",str[:])
				print("str[1:20]=",str[1:20])
				
**Output**

				str[1:5]= ytho
				str[:6]= python
				str[1:]= ython
				str[:]= python
				str[1:20]= ython

**Example 2: Negative Indexing/Slicing**

**Program**
	
				str="python"
				print("str[-1]=",str[-1])
				print("str[-6]=",str[-6])
				print("str[-2:]=",str[-2:])
				print("str[:-2]=",str[:-2])
				print("str[-5:-2]=",str[-5:-2])
				
**Output**

				str[-1]= n
				str[-6]= p
				str[-2:]= on
				str[:-2]= pyth
				str[-5:-2]= yth

**Example:3**
	
**Program**

				str="welcome to the world of python"
				print("str[2:10]=",str[2:10])
				print("str[2:10:1]=",str[2:10:1])
				print("str[2:10:2]=",str[2:10:2])
				print("str[2:13:4]=",str[2:13:4])
				print("str[::3]=",str[::3])
				print("str[::-1]=",str[::-1])
				print("str[::-3]=",str[::-3])
				
**Output**

				str[2:10]= lcome to
				str[2:10:1]= lcome to
				str[2:10:2]= loet
				str[2:13:4]= le 
				str[::3]= wceohwloph
				str[::-1]= nohtyp fo dlrow eht ot emoclew
				str[::-3]= nt  r ttml




### 3.4.6. String functions and methods

-[] Python supports many build-in methods to manipulate strings
-[] A method is like a function

|SNo|Function| Descrition |Example
|--|--|--|--|
|1| capitalize() |Capitalizes first letter of string  |str=”hello” print(str.capitalize()) 
|2|count(str,beg,end)|Count the number of times str occurs in a String|str=”he” m=”hellohellohello” print(m.count(str,0,len(m))|
|3|endwith(suffix,beg,end)|Check the string is end with given end string|m=”she is my friend” print(m.endwith(“end”,0,len(m)) |
|4|startwith(prefix,beg,end)|Check the string starts with given string|m=”the world” print(m.startwith(“th”,0,len(m))
|5|find(str,beg,end)|Check if the str is present in the string|m=”she is my friend” print(m.find(“my”,0,len(m)) 
|6|isalpha()	|Return true,if the string contain only alphabet	| m=”jamesbond007” print(m.isalpha())
|7|isdigit()	|Return true,if the string contain only digit	|m=”007”print(m.isdigit())
|8|isalnum()	|Return True,if string contain both alphabets and number 	|m=”james007” print(m.isalnum())
|9|islower()	|Returns true,if string contain only lower case	|m=”hello” print(m.islower()) 
|10|isupper()	|Returns true,if string contain only upper case	|m=”hello” print(m.isupper())
|11|len(string)	|Returns the length of the string	|str=”hello” print(len(str))
|12|lower()	|Convert all the character into lowercase|m=”HELLO” print(m.lower())
|13|upper()	|Convert all the character into uppercase	|m=” hello” print(m.upper()) 
|14|strip()	| Remove all the white space|m=”he llo” print(m.strip()) 
|15 |max(str)|Returns highest alphabetic character(ASCII value)|m=”hello zuzu” print(max(m))
|16|min(str)|Returns the lowest alphabetical character|m=”hello zuzu” print(min(m)) 
|17|split(delim) |Returns the list of substrings separated by the specified delimiter|m=”hello,hai,sai” print(m.split(‘,’))












	
	

	 







