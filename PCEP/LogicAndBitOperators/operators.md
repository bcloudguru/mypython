## Operators
and
or 
not

```
>>> age1 = 25
>>> age2 = 61
>>> if ( age1 >=18 and age2>= 18):
...     print("Both are adults")
... elif( age1>=18 or age2>=18):
...     print("one of you is an adult")
... else:
...     print("you are both children")
... 
Both are adults
```

> NOT Operator
not true -> false
not false -> true
```
>>> is_hungry = False
>>> if(not is_hungry):
...   print("You are not hungry")
... else:
...   print("You are hungry")
... 
You are not hungry
``