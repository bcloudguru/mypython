## Nested list 

1. Elements of list can be also be another list
2. 2D-array - list consists of other list

```
>>> students=[
... ['Anna','Bob','Clark','Dinesh'],
... ['Elizabeth','Flower','Ganpat','Hershey'],
... ['Issac','James','Kelly','Lawrance'],
... ['Maddy','Neil','Oshane','Peter'],
... ]
>>> print(students)
[['Anna', 'Bob', 'Clark', 'Dinesh'], ['Elizabeth', 'Flower', 'Ganpat', 'Hershey'], ['Issac', 'James', 'Kelly', 'Lawrance'], ['Maddy', 'Neil', 'Oshane', 'Peter']]
>>> k=students[2][2]
>>> print(k)
Kelly
>>> 
```

[X]
```
>>> matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
>>> 
>>> matrix2 = []
>>> 
>>> for submatrix in matrix:
...   for val in submatrix:
...     matrix2.append(val)
... 
>>> print(matrix2[2])
2
>>> 
```
[X]
```
matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix[2][1])
```

