### Bit-Wise Operators
---

1. Manipulate single bit data single-bit data
2. cannot be used in floating point numbers
3. Bit shift can be done with << or >> operators



& 
|
^

<h6> & - returns 1 if both bits are 1 else 0 </h6>
```
>>> 15 & 22
6
>>> print(bin(15))
0b1111
>>> print(bin(22))
0b10110
>>> 
>>> print(bin(6))
0b110
==========
0b01111
0b10110
-------
0b00110
==========
>>> print(int(0b00110))
6
```

```
>>> x=2
>>> x<<4
32
>>> x<<3
16
>>> x<<2
8
>>> x<<1
4
>>> x<<5
64
```

0b10100
0b00101
-------
0b10101