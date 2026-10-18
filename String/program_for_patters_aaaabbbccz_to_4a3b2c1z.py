# write a program to convert the string "aaaabbbccz" to "4a3b2c1z"

# input = "aaaabbbccz"
#  output = "4a3b2c1z"

string = "aaaabbbccz"
previous = string[0]
count = 1
index = 1
output = ""


while index < len(string):
    if string[index] == previous:
        count = count + 1

    else :
        output = output + str(count) + previous
        previous = string[index]
        count = 1

    if index == len(string) - 1:
        output = output + str(count) + previous

    index = index + 1

print(output)

# 4a3b2c1z