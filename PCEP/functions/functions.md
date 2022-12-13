## Functions
---


def name (): # definition , definition name and ():
    function body
    return # not mandatory, should return values


```
>>> def input_number():
...     return int(input("Enter a Number : "))
... 
>>> input1=input_number()
Enter a Number : 25
>>> input2=input_number()
Enter a Number : 56
>>> print(input1)
25
>>> print(input2)
56
>>> 
```

[X] - The function can have only one parameter. If any data (parameters) are passed, they are passed explicitly.

---

```
>>> def my_function(*students):
...   print("The tallest student is " + students[2])
... 
>>> my_function("James", "Ella", "Jackson")
The tallest student is Jackson
```
[X] - *students

---