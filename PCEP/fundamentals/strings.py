# len function can be used to calculate the number of characters in string
print(len("hello"))
print("123"+"345")
print( 123 + 345)

# type()

num_char=len(input("What is your name? "))
# print("Your Name has "+num_char+" characters.")  - uncomment while reviewing

# print("Your Name has "+num_char+" characters.")
# TypeError: can only concatenate str (not "int") to str

print(type(num_char))
new_num=str(num_char)
print("Your Name has "+new_num+" characters.")

# convert all data types
a=123
print(type(a))
b=str(a)
print(type(b))
c=float(a)
print(type(c))

print(70 + float("100.45"))
print(str(70) + str(100.45))

two_digit_number = input("Type a two digit number: ")
a=int(two_digit_number[0])
b=int(two_digit_number[1])
print(a+b)

