## lists
---

list 
- collection of mulitple elements
- each element has index
- first element has index[0]
- access the value by writing the index
- use built-in python methods like append/insert
    - append to add element at the end of the list
    - Insert to add element between values


```
>>> countries=["USA","Canada","India"]
>>> print (countries[0])
USA
>>> countries[0]="UK"
>>> print (countries[0])
UK
>>>
>>> print(len(countries))
3
>>> print(countries)
['UK', 'Canada', 'India']
>>> del countries[1]
>>> print(countries)
['UK', 'India']
>>> print(countries[-1])
India
>>> print(countries[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
``` 

```
>>> print(list1)
[2, 5, 3, 1]
>>> print(list1[::-1])
[1, 3, 5, 2]
>>> print(list1[::1])
[2, 5, 3, 1]
>>> print(list1[::2])
[2, 3]
>>> print(list1[2:4])
[3, 1]
```
---
<h6> append and insert</h6>
```
>>> print(countries)
['UK', 'India']
>>> countries.append("USA")
>>> countries.insert(2,"Italy")
>>> print(countries)
['UK', 'India', 'Italy', 'USA']
>>> countries.append("canada")
>>> print(countries)
['UK', 'India', 'Italy', 'USA', 'canada']
```
---
<h6> swapping elements</h6>
```
>>> print(countries)
['UK', 'India', 'Italy', 'USA', 'canada']
>>> countries[1],countries[3]=countries[3],countries[1]
>>> print(countries)
['UK', 'USA', 'Italy', 'India', 'canada']
```
---
<h6>sort and reverse</h6>

_This methods modifies the original array_
```
>>> ages=[34,76,23,79,10,1,65,99,43]
>>> ages.sort()
>>> print(ages)
[1, 10, 23, 34, 43, 65, 76, 79, 99]
>>> ages.reverse()
>>> print(ages)
[99, 79, 76, 65, 43, 34, 23, 10, 1]
```

<h6>pop</h6>

```
>>> list1 = [4, 4, 3, 1]
>>> list1.pop(2)
3
>>> print(list1)
[4, 4, 1]
```

<h6>min</h6>
```
>>> list1=["Go","Java","C","Rust"]
>>> print(min(list1))
C
```
