## Function Scopes

1. variables declared inside the function body are scoped to that function


```
>>> def in_num():
...     result=int(input())*100
...     return result
... 
>>> print(result)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'result' is not defined
```
---

**global** 

keyword used to declare the variable inside the functions to be scoped globally. i.e) these variables can be accessed from outside the functions

---
[X] - practical examples ??
