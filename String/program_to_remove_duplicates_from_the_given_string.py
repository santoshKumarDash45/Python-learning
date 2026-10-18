#  program to remove duplicates from the given string
# input = "aaaabbbccz"
# output = "abcz"


string = "aaaabbbccz"
output = ""

for char in string:
    if char not in output:
        output = output + char

print(output)


string = "aaaabbbccz"
list = []

for char in string:
    if char not in list:
        list.append(char)

output = ''.join(list)
print(output)

