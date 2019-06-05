# Lists, Tuples and Dictionaries 

Pre-requisite: http://j.mp/pythonREPLcourse


_Refer to the glossary below to become familiar with the terms relevant to this unit_

- Lists: list operations, list slices, list methods, list loop, mutability, aliasing, cloning lists, list parameters; Tuples: tuple assignment, tuple as return value; Dictionaries: operations and methods; 
- Advanced list processing - list comprehension;

## Concept Map 
_A picture is worth a 1000 words_

![mutableList](https://files.gitter.im/kgashok/advik/TYg6/mutableLists.png)


## List Methods 

Here are some important methods that are associated with `tuple`, `list` and `dictionary` - all types that are covered in Unit 4. 

|Type | Attributes | 
|:------|:-------|
|` <class 'tuple'>`|8 **`count`**, `index` |
|` <class 'list'>`|9 **`append`**, `clear`, `copy`, 10 **`count`**, 11 **`extend`**, `index`, 12 **`insert`**, 13 **`pop`**, 14 **`remove`**, 15 **`reverse`**, 16 **`sort`** |
|` <class 'dict'>`|`clear`, `copy`, `fromkeys`, 17 **`get`**, 18 **`items`**, 19 **`keys`**, 20 **`pop`**, `popitem`, `setdefault`, 21 **`update`**, 22 **`values`** |
 

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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NzMxNDQxMjQsMTk2NjUxMjk4OSwtMT
QxODU4MDIzMCwtMTA5NDc5MTQ4NSwtMTA1NzMyNjU0NCwyNDc2
MzA0MiwxNDMxOTI4NjQ2LC0xOTk3NDI4MTE5LDE1MzM0NjAzMz
AsLTQ5NjA1NzQwOSwxODA3NzMzODQ0LC0zNzU3NTQ3MTEsLTE5
MzE3NDY1MzEsLTc0ODQ2MTE1MCwxNDYyMjczNzc4LC0xNDk4ND
g5MTU0XX0=
-->