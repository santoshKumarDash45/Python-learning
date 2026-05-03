# A name in the python program is called as identifier. It can be a variable name ,
# a class name or a method name . This is basically used for identity purpose .


# Rules:-
#  1 - It can be between a-z , A-Z , 0-9 , _(underscore).
#  2 - It must not start with digit.
#  3 - case sensitive .
#  4 - We cannot use reserved keywords as like if, if elif, etc.
#  5 - We cannot use space .
#  6 - Special symbols are not allowed .
#  7 - No length limit for identifier.
#  8 - If a variable is declared as normal variable then it is valid.
#  9 - If a variable is declared as protected variable then it should be started with _(underscore).
#  10 - If a variable is declared as private variable then it should be started with __(double underscore).
#  11 - If a variable is declared as magic variable then it should starts with double __(underscore) and ends with double__(underscore).

 

#  Example---

x = 10      # normal variable - valid identifier, starts with a letter
print(x)    # prints 10

_x = 20     # protected variable - starts with single underscore, convention for internal use
print(_x)   # prints 20

__x = 30    # private variable - starts with double underscore, name mangling applies inside classes
print(__x)  # prints 30

if = 30     # invalid identifier - 'if' is a reserved keyword, this will raise a SyntaxError
print(if)   # here if is reserved keyword so it will show error .