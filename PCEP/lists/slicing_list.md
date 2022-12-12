## Slicing List
---
list [**start**:_end_]
start -> will be included in list
end -> will **not** be included in list

---
```
>>> letters=['A','B','C','D','E']
>>> print(letters)
['A', 'B', 'C', 'D', 'E']
>>> firsttwo=letters[0:2]
>>> print(firsttwo)
['A', 'B']
>>> # 2 ~ C is not there in output
... 
>>> print(letters[3:])
['D', 'E']
>>> print(letters[:3])
['A', 'B', 'C']
>>> 
```
---
<h6>Del</h6>

```
>>> age=[21,56,34,89,74]
>>> ages=age
>>> print(ages)
[21, 56, 34, 89, 74]
>>> del ages[:]
>>> print(age)
[]
>>>
``` 
---

```
>>> my_list = [0, 1, 2, 3, 4]
>>> print(my_list[::-1])
[4, 3, 2, 1, 0]
>>> 
```
---
<h6>AttributeError: 'list' object has no attribute 'upper'</h6>
```
>>> list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
>>> print(list1.upper())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'upper'
```
---
