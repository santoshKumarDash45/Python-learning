# write a program to reverse the content of the given string using slicing method.

String = "santosh kumar dash"
reversed_string = String[::-1]
print(reversed_string)


#  write a program to reverse the content of the given string using reversed method.


String = "santosh kumar dash"
reversed_string = ''.join(reversed(String))
print(reversed_string)

 # write a program to reverse the content of the given string using while loop

string = "santosh kumar dash"
reversed_string = ""
index = len(string) - 1 #this will give the last index of the string
while index >= 0:
    reversed_string += string[index]
    index -= 1
print(reversed_string)