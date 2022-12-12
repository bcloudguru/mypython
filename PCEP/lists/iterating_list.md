## Iterating Lists
---
1. for loop can be used to iterate over list

```
>>> print(ages)
[99, 79, 76, 65, 43, 34, 23, 10, 1]
>>> total = 0
>>> for age in ages:
...     total = total + age
... 
>>> avg_age = total / len(ages)
>>> print(avg_age)
47.77777777777778
```
