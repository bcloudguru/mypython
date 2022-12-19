## Function - List as Argument

1. list can be passed to functions

```
>>> def multi_values(list):
...     multiply_values=[]
...     for i in list:
...             multiply_values.append(i*2)
...     return multiply_values
... 
>>> 
>>> print(multi_values([1,3,6]))
[2, 6, 12]
>>> 
```
---
> TypeError
```
>>> print(multi_values(1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in multi_values
TypeError: 'int' object is not iterable
```

[X]
```
def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

get_even_func([1, 2, 3, 4, 5, 6])
```

[X]
```
>>> def double_list(numbers):
...   return 2 * numbers
... 
>>> numbers = [1, 2, 3]
>>> print(double_list(numbers))
[1, 2, 3, 1, 2, 3]
>>>
``` 