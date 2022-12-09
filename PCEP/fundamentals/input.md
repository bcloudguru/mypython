## input( )
1. Input functions prompts user to input data from console.
2. Program that doesnt use any input functions, is called a **deaf program**

```
>>> favorite_food = input("what is your favorite food!!")
what is your favorite food!!Biryani
>>> print(" Your favourite food is "+ favorite_food)
 Your favourite food is Biryani
 ```
3. Value of the input function always returns **String**

```
>>> age = input("how old are you? ")
how old are you? 24
>>> print(" your age is " + age)
 your age is 24
 >>> print (age-20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
 ```

### Typecasting
4. Typecasting used to change the type of data
    1. int( )
    2. float( )

```
>>> print(age)
24
>>> print (int(age)-20)
4
>>> print(age)
24
>>> print (float(age)-20)
4.0
```