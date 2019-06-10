# Lists, Tuples and Dictionaries 

Pre-requisite: http://j.mp/pythonREPLcourse


_Refer to the glossary below to become familiar with the terms relevant to this unit_

- Lists: list operations, list slices, list methods, list loop, mutability, aliasing, cloning lists, list parameters; Tuples: tuple assignment, tuple as return value; Dictionaries: operations and methods; 
- Advanced list processing - list comprehension

## Concept Map 
_A picture is worth a 1000 words_

![mutableList](https://files.gitter.im/kgashok/advik/TYg6/mutableLists.png)


## Sequences and their main attributes 

Here are some important methods that are associated with `tuple`, `list` and `dictionary` - all types that are covered in Unit 4. 

|Type | Attributes | 
|:------|:-------|
|` 'tuple'`|8 **`count`**, `index` |
|` 'list'`|9 **`append`**, `clear`, `copy`, 10 **`count`**, 11 **`extend`**, `index`, 12 **`insert`**, 13 **`pop`**, 14 **`remove`**, 15 **`reverse`**, 16 **`sort`** |
|` 'dict'`|`clear`, `copy`, `fromkeys`, 17 **`get`**, 18 **`items`**, 19 **`keys`**, 20 **`pop`**, `popitem`, `setdefault`, 21 **`update`**, 22 **`values`** |
 

## List Methods and Operations

The following table has been created by **_clustering_** multiple items based on some criteria. This is easier to internalize and deliver to maximize retention among students. Moreover, there is going to be _better_ chance of overall engagement.

|Intent | Method / Operation | Description |
|:-------|:--------------|:----------------|
|**Initialize** |  | initialize an empty list, using a tuple, using another list | 
 | _operation_ | `[]`, `list()` or `list(sequence)`, the `=` operator | `bl = al` initializes `bl` as an **alias** for the`al` list object
|**Access** | [_idx_], `.find(elem)`, `.index(elem)` `.count()`  | `find` returns `-1`, `index` throws an exception if not present| 
|   _operation_| `in` and `not in`, `any` and `all`, `max`, `min`, `len`, `sum`| membership `in` list, `all` or `any` if element(s) is `True`
|**Modify** | _addition_ `.append(val)`, `.insert(loc, val)`, `.extend()` | add elements to the list at specific locations; `extend` adds multiple elements from sequence 
| | _extraction_ `.pop(loc)`, `.remove(elem)`, `.clear()`| take out from specified index, or element or all elements |
| | _ordering_  `.reverse()`, `.sort()` | rearrange elements in the list|
| _operation_|  `del`, `sorted`| same effect as the methods with better performance?|
|**Allocate** | `.copy()` `[:]`, [_s_:_s_:_s_], repetition (using `*`) and concatenation (using `+`) | Create distinct list objects by duplicating existing ones
|  _operation_ |  slice(_start_, _stop_, _step_), `zip`, `enumerate`, **cloning** (_copy.copy and deepcopy_) and **list comprehension** | same as slice operator `[]`, `zip` creates a new list with tuples from two lists`, `enumerate` provides list with (_index_, _element_) tuple  



## List Mutability 

Pre-requisite: http://j.mp/immutablePython

From [https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/)

This brings us to an important point: there are actually two kinds of objects in Python. A  _mutable_  object exhibits time-varying behavior. Changes to a mutable object are visible through all names bound to it. Python's lists are an example of mutable objects. An  _immutable_  object does not exhibit time-varying behavior. The value of immutable objects can not be modified after they are created. They  _can_  be used to compute the values of  **new**  objects, which is how a function like string.join works. When you think about it, this dichotomy is necessary because, again, everything is an object in Python. If integers were not immutable I could change the meaning of the number '2' throughout my program.

It would be incorrect to say that "mutable objects can change and immutable ones can't", however. Consider the following:


## Slicing

- **A Python slice** extracts elements from an `iterable` based on a start and stop.  It returns a `iterable` (or sequence) containing the extracted elements. 
- We take slices on many types (`string, list and/or tuple`) in Python. 
- We specify an optional `start` index, an optional `stop` index, and an optional `step` value (`0` is not acceptable as step value).

**Syntax notes.** The special syntax for this operation is at first confusing. But with practice, slicing becomes easy. When we omit a value, a default is used.

### [Start: Stop: Step]

|Slice| Description|
|---------|--------|
|`values[1:3]`  | Index 1 through index 3.
|`values[2:-1]`| Index 2 through index one from last.
|`values[:2]`   | Start through index 2.
|`values[2:]`   | Index 2 through end.
|`values[::2]`  | Start through end, skipping ahead 2 places each time.

```python
rlist = [88, 44, 65, 68, 78, \
	23, 72, 28, 50, 72, 21, 47, 27, 50, 15]

What does rlist[:-10] evaluate to? 
# [88, 44, 65, 68, 78]
What does rlist[:-10:3] evaluate to?
# [88, 68]

alist = [25, 20, 25, 84, 67, 99, 96, 67,\
			 27, 78, 73] [-3:7:-1]

What does `alist` contain? 

```

[https://www.dotnetperls.com/slice-python](https://www.dotnetperls.com/slice-python)


- Slice operator [https://runestone.academy/runestone/static/thinkcspy/Strings/TheSliceOperator.html](https://runestone.academy/runestone/static/thinkcspy/Strings/TheSliceOperator.html)

- Slicing of Lists
- [https://runestone.academy/runestone/static/thinkcspy/Lists/ListSlices.html](https://runestone.academy/runestone/static/thinkcspy/Lists/ListSlices.html)

- Slice Detailed Slides [https://v4.software-carpentry.org/python/slice.pdf](https://v4.software-carpentry.org/python/slice.pdf)



## List Comprehension 
Pre-requisite; http://j.mp/listBenefit  and https://j.mp/listComprehensions
List comprehensions are concise ways to create lists. The general syntax is:

	[<expression> for <item> in <sequence> if  <condition>]

where the `if` clause is optional. For example,

```python
mylist = [1,2,3,4,5]
yourlist = [item ** 2 for item in mylist]
print(yourlist)
# [1, 4, 9, 16, 25]
```

### Quiz
What is printed by the following statements? Or, what is the output of the following statements? 

```python
alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)
```

	(A) [4,2,8,6,5]  
	(B) [8,4,16,12,10]  
	(C) 10  
	(D) [10]


## List Parameters 

j.mp/parameterThis 

[Python has no pass by value](https://medium.com/@george.smith2024/there-is-no-pass-by-value-in-python-5a0efa544736?source=responses---------13-----------------------)

There is no pass by value in Python. Functions arguments are always passed by reference (or object reference, to be exact). The reason that numbers don’t change even if they are passed by reference is because of their immutability.

[Refer book section for more details](https://runestone.academy/runestone/static/thinkcspy/Lists/UsingListsasParameters.html)

## Dictionary

A collection of key-value pairs that maps from keys to values. The keys can be any immutable type, and the values can be any type. Dictionaries implement the  [associative array](http://en.wikipedia.org/wiki/Associative_array)  abstract data type. 

**key**:  A data item that is  _mapped to_  a value in a dictionary. Keys are used to look up values in a dictionary.

**key-value pair**:  One of the pairs of items in a dictionary. Values are looked up in a dictionary by key.


```
adict = dict() # initialization
adict['Sam'] = 233-2333
adict['Victor'] = 900-2222
```

### Exercises
- http://j.mp/reverseDictionary
- http://j.mp/friendsCC 


## Glossary

**aliases** Multiple variables that contain references to the same object.
  - aliasing - nicknames - multiple names for the same object 
	- Rajesh is the name of a boy; 'Ramki' might be the name used by his close relatives; "Bondaaaa" might be the name used by his close friends; 'Ramki' and "Bondaaa" are **aliases** (nicknames) for Rajesh

**clone** To create a new object that has the same value as an existing object. Copying a reference to an object creates an alias but doesn’t clone the object.
  - Cloning a goat using stem cells is about duplicating what is already available 


**delimiter** A character or string used to indicate where a string should be split.

**element** One of the values in a list (or other sequence). The bracket operator selects elements of a list.

**index** An integer variable or value that indicates an element of a list.

**list** A collection of objects, where each object is identified by an index. Like other types  `str`,  `int`,  `float`, etc. there is also a  `list`  type-converter function that tries to turn its argument into a list.

**list traversal** The sequential accessing of each element in a list.

**modifier** A function which changes its arguments inside the function body. Only mutable types can be changed by modifiers.

**mutable data type** A data type in which the elements can be modified. All mutable types are compound types. Lists are mutable data types; strings are not.
 -	mutability - > ability to mutated, to be changed, to be modified 
 - immutability -> cannot be changed 


**nested list** A list that is an element of another list.

**object** A thing to which a variable can refer.

**pure function** A function which has no side effects. Pure functions only make changes to the calling program through their return values.

**sequence** Any of the data types that consist of an ordered collection of elements, with each element identified by an index.

**side effect** A change in the state of a program made by calling a function that is not a result of reading the return value from the function. Side effects can only be produced by modifiers.

**tuple** A sequential collection of items, similar to a list. Any python object can be an element of a tuple. However, unlike a list, tuples are immutable.


## Exercises
1 [Runestone exercises](https://runestone.academy/runestone/static/thinkcspy/Lists/Exercises.html)
2. **Remove duplicates.** A list contains duplicate elements. How can we remove them? Some approaches may lead to the elements becoming reordered, but this is not necessary.


## Slice Exercises - Part 1

```python
0. [35, 67, 41, 25, 31, 100, 97, 80][1:7]
slice(1,7,2) or [1:7:2]

2. [37, 17, 24, 82, 10, 52, 62, 36, 77, 88, 30, 13][-9:]
slice(-9,None,-3) or [-9::-3]

3. [37, 52, 52, 54, 97, 88, 76, 28, 45][10:11]
slice(10,11,0) or [10:11:0]

4. [40, 21, 54][2:]
slice(2,None,1) or [2::1]

5. [69, 34, 94, 55, 41, 10, 83, 43][-2:]
slice(-2,None,-2) or [-2::-2]

6. [50, 86, 76, 10, 37, 74, 71, 99, 87, 73, 13, 17, 45]
slice(-12,None,6) or [-12::6]

7. [42, 13, 79, 33, 45, 72, 51, 26, 34][7:]
slice(7,None,-2) or [7::-2]

8. [70, 26, 33, 35, 67][-7:]
slice(-7,None,1) or [-7::1]

9. [98, 88, 96, 32, 27, 66, 65, 79, 99]
slice(-9,None,-1) or [-9::-1]

15. [58, 77]
slice(-1,-5,-1) or [-1:-5:-1]

20. [31, 83, 70, 44, 16, 29, 100, 88, 10, 96, 37, 53, 58][-2:]
slice(-2,None,3) or [-2::3]

23. [10, 71][1:]
slice(1,None,-1) or [1::-1]

25. [80, 39, 71, 29, 38, 98, 47, 63, 89, 38, 90, 91, 20][-16:]

29. [76, 26, 14, 45][3:]
slice(3,None,-3) or [3::-3]

32. [25, 71, 15, 78, 53]
slice(-1,-5,-1) or [-1:-5:-1]

34. [94, 21, 69, 25, 20, 69, 75, 13, 55, 83, 44][-14:]

42. [83, 43, 21, 70, 18, 52, 53, 89][7:]

43. [56, 34, 23, 18, 96, 29, 49, 82, 12][6:]
slice(6,None,-3) or [6::-3]

46. [71, 80, 86, 31, 91, 86][4:]
slice(4,None,-1) or [4::-1]

48. [38, 19, 98, 20, 29, 63, 24, 60, 53, 80][-3:]
slice(-3,None,-2) or [-3::-2]

49. [49, 77, 55, 58, 75, 66, 97, 12, 77, 80, 44, 54][-5:]
slice(-5,None,2) or [-5::2]

50. [94, 86, 51, 95, 87, 70][-1:]

51. [56, 82, 13, 61, 79, 99, 62, 48, 66, 61, 40][-9:]
slice(-9,None,-2) or [-9::-2]

54. [16, 86, 42, 47, 75, 88, 17, 66, 60, 95, 97, 48][7:11]
slice(7,11,-1) or [7:11:-1]

56. [81, 95, 99, 26, 85, 91, 25, 97, 69, 53, 92, 51]
slice(-3,-14,-3) or [-3:-14:-3]

60. [91, 96, 35, 18, 63, 83][1:]

63. [37, 99, 31][-2:]

65. [22, 48, 80, 72, 28, 16, 60, 21, 54, 24, 57][-9:]
slice(-9,None,2) or [-9::2]

67. [84, 80, 38, 51, 44, 57, 25, 56, 82, 14, 37][1:4]
slice(1,4,0) or [1:4:0]

68. [70, 90, 71, 67, 78, 99, 18, 44][5:]
slice(5,None,-2) or [5::-2]



```

## Slice Keys - Part 1 
```python
0.[35, 67, 41, 25, 31, 100, 97, 80][1:7]
[67, 41, 25, 31, 100, 97]
0. slice(1,7,2) or [1:7:2]
[67, 25, 100]

2.[37, 17, 24, 82, 10, 52, 62, 36, 77, 88, 30, 13][-9:]
[82, 10, 52, 62, 36, 77, 88, 30, 13]
2. slice(-9,None,-3) or [-9::-3]
[82, 37]

3.[37, 52, 52, 54, 97, 88, 76, 28, 45][10:11]
[]
3. slice(10,11,0) or [10:11:0]
[82, 37]

4.[40, 21, 54][2:]
[54]
4. slice(2,None,1) or [2::1]
[54]

5.[69, 34, 94, 55, 41, 10, 83, 43][-2:]
[83, 43]
5. slice(-2,None,-2) or [-2::-2]
[83, 41, 94, 69]

6. [50, 86, 76, 10, 37, 74, 71, 99, 87, 73, 13, 17, 45]
slice(-12,None,6) or [-12::6]
[86, 99]

7.[42, 13, 79, 33, 45, 72, 51, 26, 34][7:]
[26, 34]
7. slice(7,None,-2) or [7::-2]
[26, 72, 33, 13]

8.[70, 26, 33, 35, 67][-7:]
[70, 26, 33, 35, 67]
8. slice(-7,None,1) or [-7::1]
[70, 26, 33, 35, 67]

9. [98, 88, 96, 32, 27, 66, 65, 79, 99]
slice(-9,None,-1) or [-9::-1]
[98]

15. [58, 77]
slice(-1,-5,-1) or [-1:-5:-1]
[77, 58]

20.[31, 83, 70, 44, 16, 29, 100, 88, 10, 96, 37, 53, 58][-2:]
[53, 58]
20. slice(-2,None,3) or [-2::3]
[53]

23.[10, 71][1:]
[71]
23. slice(1,None,-1) or [1::-1]
[71, 10]

25. [80, 39, 71, 29, 38, 98, 47, 63, 89, 38, 90, 91, 20][-16:]
[80, 39, 71, 29, 38, 98, 47, 63, 89, 38, 90, 91, 20]

29.[76, 26, 14, 45][3:]
[45]
29. slice(3,None,-3) or [3::-3]
[45, 76]

32. [25, 71, 15, 78, 53]
slice(-1,-5,-1) or [-1:-5:-1]
[53, 78, 15, 71]

34. [94, 21, 69, 25, 20, 69, 75, 13, 55, 83, 44][-14:]
[94, 21, 69, 25, 20, 69, 75, 13, 55, 83, 44]

42. [83, 43, 21, 70, 18, 52, 53, 89][7:]
[89]

43.[56, 34, 23, 18, 96, 29, 49, 82, 12][6:]
[49, 82, 12]
43. slice(6,None,-3) or [6::-3]
[49, 18, 56]

46.[71, 80, 86, 31, 91, 86][4:]
[91, 86]
46. slice(4,None,-1) or [4::-1]
[91, 31, 86, 80, 71]

48.[38, 19, 98, 20, 29, 63, 24, 60, 53, 80][-3:]
[60, 53, 80]
48. slice(-3,None,-2) or [-3::-2]
[60, 63, 20, 19]

49.[49, 77, 55, 58, 75, 66, 97, 12, 77, 80, 44, 54][-5:]
[12, 77, 80, 44, 54]
49. slice(-5,None,2) or [-5::2]
[12, 80, 54]

50. [94, 86, 51, 95, 87, 70][-1:]
[70]

51.[56, 82, 13, 61, 79, 99, 62, 48, 66, 61, 40][-9:]
[13, 61, 79, 99, 62, 48, 66, 61, 40]
51. slice(-9,None,-2) or [-9::-2]
[13, 56]

54.[16, 86, 42, 47, 75, 88, 17, 66, 60, 95, 97, 48][7:11]
[66, 60, 95, 97]
54. slice(7,11,-1) or [7:11:-1]
[]

56. [81, 95, 99, 26, 85, 91, 25, 97, 69, 53, 92, 51]
slice(-3,-14,-3) or [-3:-14:-3]
[53, 25, 26, 81]

60. [91, 96, 35, 18, 63, 83][1:]
[96, 35, 18, 63, 83]

63. [37, 99, 31][-2:]
[99, 31]

65.[22, 48, 80, 72, 28, 16, 60, 21, 54, 24, 57][-9:]
[80, 72, 28, 16, 60, 21, 54, 24, 57]
65. slice(-9,None,2) or [-9::2]
[80, 28, 60, 54, 57]

67.[84, 80, 38, 51, 44, 57, 25, 56, 82, 14, 37][1:4]
[80, 38, 51]
67. slice(1,4,0) or [1:4:0]
[53, 52]

68.[70, 90, 71, 67, 78, 99, 18, 44][5:]
[99, 18, 44]
68. slice(5,None,-2) or [5::-2]
[99, 67, 90]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NTE1MTQyMzEsLTE1MTA5MTc3MzQsLT
E2MzA1MjU5MjYsMTYzNTUyNTgyMywtMjEzMjEwOTY1LC0xMjYz
ODAzNTQ2LC0xNDUzNjEwODAsLTE5NzMxNDQxMjQsMTk2NjUxMj
k4OSwtMTQxODU4MDIzMCwtMTA5NDc5MTQ4NSwtMTA1NzMyNjU0
NCwyNDc2MzA0MiwxNDMxOTI4NjQ2LC0xOTk3NDI4MTE5LDE1Mz
M0NjAzMzAsLTQ5NjA1NzQwOSwxODA3NzMzODQ0LC0zNzU3NTQ3
MTEsLTE5MzE3NDY1MzFdfQ==
-->