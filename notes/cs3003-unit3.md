

# Strings
Strings and recursion and reversal 


## Which program is correct?
We need a string reversal function and it needs to be using recursion. Which achieves the purpose between A and B? If so, does it achieve the objective for any type and length of string? 



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
eyJoaXN0b3J5IjpbNjQ0MjYwNjc4LDIwOTE0NDc2NjVdfQ==
-->