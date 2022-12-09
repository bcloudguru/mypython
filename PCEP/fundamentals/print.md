## Print Function
1. Built-in function: can be used without importing it.
2. Allows us to print values to the console.
3. We can invoke it with parenthesis.
4. We can pass the value we want to print as arugment
5. function(arguments) and Values between quotes is a string
6. Backslash tells python that next character has special meaning
7. Keywords Argments such as **sep** and **end** can format the string
```
>>> print("Hello world!") 
Hello world!
>>> print('Hello World!')
Hello World!
```
\n - n represents newline & \ character after backlash has special meaning
```
>>> print ("Hello \nWelcome to the world of Python Programming")
Hello 
Welcome to the world of Python Programming
```
Multiple aruguments in print functions
```
>>> print("Hello!","Welcome to the world","of Python Programming")
Hello! Welcome to the world of Python Programming
```
**end** keyword argument in print function
```
>>> print("Hello",end="!");\
... print("Welcome to the World of Python Programming")
Hello!Welcome to the World of Python Programming
>>> print("Hello",end="$$$");\
... print("Welcome to the World of Python Programming")
Hello$$$Welcome to the World of Python Programming
```
**sep** keyword argument in print function
```
>>> print("Hello","Welcome to the world","of Python Programming",sep="-")
Hello-Welcome to the world-of Python Programming
>>> print("Hello","Welcome to the world","of Python Programming",sep="**")
Hello**Welcome to the world**of Python Programming
```