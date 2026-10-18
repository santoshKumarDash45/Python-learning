# write a program to print character present at even and odd index separately in a given string


s = "durgasoft"

print("character present at even index: ")

i = 0
while(i < len(s)):
    print(s[i])
    i = i+2

print("character present at odd index: ")

i = 1
while(i < len(s)):
    print(s[i])
    i = i+2



# output:

# character present at even i
# ndex: 
# d
# r
# a
# o
# t
# character present at odd index: 
# u
# g
# s
# f