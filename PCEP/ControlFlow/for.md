# FOR

> TypeError: 'int' object is not iterable

1. for loop uses range function
> for i in range(10): -> o,1,2,,,9


```
>>> for i in range(5):
...     print("i is: ", i)
... 
('i is: ', 0)
('i is: ', 1)
('i is: ', 2)
('i is: ', 3)
('i is: ', 4)
```

```
>>> x = 'abcd'
>>> print(len(x))
4
>>> for i in range(len(x)):
...     print(i)
... 
0
1
2
3
```



```
>>> for i in range(5):
...     if (i ==2):
...             break
...     print("i is: ", i)
... 
('i is: ', 0)
('i is: ', 1)
```

```
>>> for i in range(5):
...     if i == 2:
...             continue
...     print ("i is : ",i)
... 
('i is : ', 0)
('i is : ', 1)
('i is : ', 3)
('i is : ', 4)
```
[X] Check this

```
>>> x='abcd'
>>> for i in range(len(x)):
...     i.upper()
... print(x)
  File "<stdin>", line 3
    print(x)
        ^
SyntaxError: invalid syntax

>>> for i in x:
...     print(i.upper())
... 
A
B
C
D
>>> 
```
<h6> Spot the difference in below queries </h6>
```
>>> for num in range(0,11):
...     if(num %2 == 0):
...             continue
...     print(num)
... 
1
3
5
7
9
>>> for num in range(0,11):
...     if(num %2 != 0):
...             print(num)
... 
1
3
5
7
9
>>> 
```

