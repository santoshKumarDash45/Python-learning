# Application to print index of all occurence of the given string

# logic to be followed here is as follows

# step 1 => find the first occurence of the sub string 
# step 2 => find the next occurence of the sub string then search the substring using boudaries from that index to the last
# step 3 => then again find the next occurence
# step 4 => search the sub string using boudaries till the find mehod returns -1 after that stops the execution

string = "ABCABCABCA"
sub_string = "ABC"

index = string.find(sub_string)

if index == -1:
    print("sub string not found")

while index != -1:
    print("{} sub string is found in {}".format(sub_string, index))
    index = string.find(sub_string, index + len(sub_string), len(string)) 
    #  the main logic lies in above line where it is searching for next occurence of the substring using index + len(sub_String) and it is
    # searching using boudaries till the last element of the string .