

# Strings
Strings and recursion and reversal 


## Which program is correct? And what do they accomplish? 

```python
## Program A
def reverse_str(text):
	if len(text) == 0:
		return ""
	return reverse_str(text[1:]) + text[0]
print(reverse_str("abcdefghi"))

## Program B 
def reverse2(text):
	if len(text) == 0:
		return ""
	return text[-1] + reverse2(text[:-1])
print(reverse2("abcdefghi"))
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA5MTQ0NzY2NV19
-->