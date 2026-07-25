# write a program to reverse content of the given string using slice operator?

s = "santosh kumar dash"
output = s[::-1]
print(output)  # hsad ramuk hsotnas

# Write a program to reverse content of the given string by using reversed() function?

s = input("Enter the string which you want to reverse ?")
reversed_output = reversed(s)
reversed_output_with_join = ''.join(reversed_output)
print(reversed_output)

# Write a program to reverse content of the given string by using while loop .

loop_string = "santosh"

loop_output = ''

i = len(loop_string) - 1

while i >= 0:
    loop_output = loop_output + loop_string[i]
    i = i - 1

print(loop_output)    #hsotnas

