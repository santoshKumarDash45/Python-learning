# write a program to convert the string "a4k3b2" to "aeknbd"
#  input = "a4k3b2"
#  output = "aeknbd"


string = "a4k3b2"
output = ""

for char in string:
    if char.isalpha():
        output = output + char
        x = char

    else:
        digit = int(char)
        new_char = chr(ord(x) + digit)
        output = output + new_char

print(output)

# aeknbd

