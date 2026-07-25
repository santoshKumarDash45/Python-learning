string = "ABABABABA"
result_string = string.replace('A', 'b')
print(result_string)
# bBbBbBbBb


long_string = "santosh kumar dash"
result_string1 = long_string.replace(' ', '')
print(result_string1)
# santoshkumardash

# count number of spaces in the given string

spaces_string = "santosh kumar dash"
string_without_spaces = spaces_string.replace(' ', '')

print("Count of spaces in the string:", spaces_string.count(' '))
print("count of spaces in the string:", len(spaces_string) - len(string_without_spaces))