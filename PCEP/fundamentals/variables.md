## Variables
---
Variables allows you to store values

Variable naming:

1. case sensitive
2. cannot be python reserved keywords
3. valid variable name (letters, digits and underscore)
4. variables can be redeclared and can use shortcut operators 
---
```
>>> amount_of_apples=5
>>> cost_of_apple=2
>>> print ( amount_of_apples * cost_of_apple)
10
>>> COST_OF_APPLE=6
>>> print (amount_of_apples * COST_OF_APPLE)
30
>>> cost_of_apple = cost_of_apple+1
>>> print ( amount_of_apples * cost_of_apple)
15
>>> cost_of_apple += 1
>>> print ( amount_of_apples * cost_of_apple)
20
```