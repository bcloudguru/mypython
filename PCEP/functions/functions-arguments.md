### Arguments
---

1. Python allows values to be passed into functions
2. Values are passed between paranthesis
3. Functions can have multiple paramters that can be passed

```
>>> def input_number(num):
...     return int(input())*num
... 
>>> input1=input_number(4)
60
>>> print(input1)
240
>>> 
```

<h6>Multiple arguments</h6>
```
>>> def input_number(num1,num2):
...     return int(input())*num1-num2
... 
>>> input1=input_number(4,10)
15
>>> print(input1)
50
>>> # 4*15 - 10 =50
>>> input2=input_number(num2=20,num1=30)
3
>>> print(input2)
70
>>> # 3*30 - 20
```
---
> TypeError: input_number() got multiple values for argument
```
>>> input3=input_number(20,num1=30)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: input_number() got multiple values for argument 'num1'
```
<h6> Default values for parameters </h6>

```
>>> def input_num(num=15):
...     return int(input())*num
... 
>>> input_num()
5
75
>>> input_num(5)
5
25
```


