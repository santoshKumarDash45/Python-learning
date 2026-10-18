# write a program to print the following patters a3z2b4 to aaabbbbz2


string = "a3z2b4"
output = ""

for char in string:
    if char.isalpha():
        char_string = char
    else:
        string_count = int(char)
        output = output + char_string * string_count

sorted_output = ''.join(sorted(output))
print(sorted_output)