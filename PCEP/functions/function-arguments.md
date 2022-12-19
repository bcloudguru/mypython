### Arguments passed in functions

---

> Arguments works differently for scalar values vs list 



<h6>UnboundLocalError: local variable 'result' referenced before assignment</h6>

```
>>> def sum(*args):
...     for arg in args:
...         result += arg
...     return result 
... 
>>> print(sum(2,3,1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in sum
UnboundLocalError: local variable 'result' referenced before assignment

>>> def sum(*args):
...     result = 0
...     for arg in args:
...             result += arg
...     return result
... 
>>> print(sum(2,3,1))
6
```
---
[X] - More practice