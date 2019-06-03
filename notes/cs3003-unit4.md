# Lists, Tuples and Dictionaries 

- Lists: list operations, list slices, list methods, list loop, mutability, aliasing, cloning lists, list parameters; 
- Tuples: tuple assignment, tuple as return value; 
- Dictionaries: operations and methods; 
- Advanced list processing - list comprehension;

## Simplifying terms

- mutability - > ability to mutated, to be changed, to be modified 
    - immutability -> cannot be changed 
- aliasing - nicknames - multiple names for the same object 
	- Rajesh is the name of a boy; 'Ramki' might be the name used by his close relatives; "Bondaaaa" might be the name used by his close friends; 'Ramki' and "Bondaaa" are aliases (nicknames) for Rajesh
- Cloning -> making *identical* copies of each other. Cloning a goat using stem cells is about duplicating what is already available 


## Concept Map 
_A picture is worth a 1000 words_

![mutableList](https://files.gitter.im/kgashok/advik/TYg6/mutableLists.png)

## List Mutability 

Pre-requisite: http://j.mp/immutablePython

From [https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/](https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/)

This brings us to an important point: there are actually two kinds of objects in Python. A  _mutable_  object exhibits time-varying behavior. Changes to a mutable object are visible through all names bound to it. Python's lists are an example of mutable objects. An  _immutable_  object does not exhibit time-varying behavior. The value of immutable objects can not be modified after they are created. They  _can_  be used to compute the values of  **new**  objects, which is how a function like string.join works. When you think about it, this dichotomy is necessary because, again, everything is an object in Python. If integers were not immutable I could change the meaning of the number '2' throughout my program.

It would be incorrect to say that "mutable objects can change and immutable ones can't", however. Consider the following:


## List Comprehension 
Pre-requisite; http://j.mp/listBenefit 

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


## List Parameters 

[Python has no pass by value](https://medium.com/@george.smith2024/there-is-no-pass-by-value-in-python-5a0efa544736?source=responses---------13-----------------------)

There is no pass by value in Python. Functions arguments are always passed by reference (or object reference, to be exact). The reason that numbers don’t change even if they are passed by reference is because of their immutability.

[Refer book section for more details](https://runestone.academy/runestone/static/thinkcspy/Lists/UsingListsasParameters.html)


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI4NTAxNzk4NCwtMTkzMTc0NjUzMSwtNz
Q4NDYxMTUwLDE0NjIyNzM3NzgsLTE0OTg0ODkxNTRdfQ==
-->