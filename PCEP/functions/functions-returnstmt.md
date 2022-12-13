## Return Statement
---
1. Functions **not necessary to return** any values


```
>>> def print_sum(a,b):
...     sum=a+b
...     print("The sum is :" + str(sum))
... 
>>> print_sum(10,20)
The sum is :30
```

> **return** can be used to return early (not to run the code beyond)

```
>>> def print_sum(a,b):
...     sum=a+b
...     if(sum==0):
...             return
...     print("The sum is :" + str(sum))
... 
>>> print_sum(10,-10)
>>> print_sum(10,10)
The sum is :20
```

<h6>None - Return </h6>
* can be used to return some kind of value

```
>>> def is_even(num):
...     if(num % 2 == 0):
...             return True
... 
>>> is_even(10)
True
>>> is_even(11)
>>> print(is_even(7))
None
>>> 
```
Returning Bool
```
>>> def is_true(a): 
...   return bool(a) 
... 
>>> result = is_true(3<6) 
>>> print("The result is", result)
The result is True
```