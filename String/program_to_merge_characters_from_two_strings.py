# write a program to merge characters from two strings.

i,j = 0, 0
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
merged_string = ""

while i < len(str1) and j < len(str2):
    merged_string += str1[i] + str2[j]
    i += 1
    j += 1

print("Merged string:", merged_string)