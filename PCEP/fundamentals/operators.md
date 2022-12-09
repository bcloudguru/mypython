## Arithmetic Operators:

---
**Exponential** -> **
interger ** interger = integer
float ** interger = float
```
>>> print(2 ** 3)
8
>>> print(2. ** 3)
8.0
>>> print(2. ** 3.)
8.0
```
---
**Multiplication** -> *
interger * interger = integer
float * interger = float
```
>>> print(2*3)
6
>>> print(2*.3)
0.6
>>> print(2.*3.)
6.0
>>> print(2.5*3)
7.5
```
---
**Division** -> /
interger / interger = **float**
float / interger = float
```
>>> print(5/5)
1.0
>>> print(5/2)
2.5
>>> print(9/3.0)
3.0
>>> print(10./5.)
2.0
```
---
**Floor Division** -> //
interger // interger = **_integer_**
float // interger = float
results rounded to less interger
```
>>> print(5//5)
1
>>> print(5//2.)
2.0
>>> print(10.//5.)
2.0
>>> print(9//3.)
3.0
```
---
**Modulo** -> %
Calculate the remainder
```
>>> print(5/2)
2.5
>>> print(4%2)
0
>>> print(5%2)
```
---
**Addition** -> +
to add values
```
>>> print(4+9)
13
>>> print(4+9.0)
13.0
>>> print(2.0+3.0)
5.0
```
---
**Subraction** -> -
to subtract Values
```
>>> print(2-4)
-2
>>> print(4- -2)
6
>>> print(4.5-2)
2.5
>>> print(4.5-2.5)
2.0
```
---
**Unary operator** to express negative values
```
>>> print (6- -6)
12
>>> print(-6 -6)
-12
```
---
##Priority

1. Unary
2. exponential **
3. Multipy *, Division / , floor division //, Modulo %
4. binary (+/-)

```
>>> print (10 - 6**2 / 9 * 10 + 1)
-29.0
>>> print (10 - 36 / 9 * 10 + 1)
-29.0
>>> print (10 - 4 * 10 + 1 )
-29
>>> print (10 - 40 + 1)
-29
```
---
## Sub-Expression 
> Subexpression takes higher priority
---