# Data Types - demonstrates int, float, string, and large integer types in Python

a = 10                              # assign integer value 10 to variable a
print(type(a))                      # prints <class 'int'>

b = 90.10                           # assign float value 90.10 to variable b
print(type(b))                      # prints <class 'float'>

c = "santosh"                       # assign string value "santosh" to variable c
print(type(c))                      # prints <class 'str'>

d = 11223333333333334444499999999999 # assign a very large integer to variable d (no size limit in Python 3)
print(type(d))                      # prints <class 'int'> - Python 3 handles big integers automatically


# in python 2 long data type was there but in python 3 it is removed 



# Everything in python is object .

e = 20
print(type(e))  
              # Used to get the type of a 
              # prints <class 'int'>
              # e is a refrencing variable which is pointing to 20

print(id(e))  
            #   used to get the address of object

print(e)                     # prints 20
