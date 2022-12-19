### Tuples
----

1. **list** is mutable [can be updated] , list [1,2,3]
2. **Tuples** is a immutable , tuple (1,2,3) ~ between parenthesis
3. Tuples is a collection of items that are ordered, unchangeable, and allow duplicate values.


```
>>> tuple1=(1,2,3)
>>> for i in tuple1:
...     print (i)
... 
1
2
3
```
<h6>'tuple' object has no attribute 'append'</h6>
```
>>> tuple1.append(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
```
<h6>'tuple' object does not support item</h6>
```
>>> tuple1[4]=9
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```