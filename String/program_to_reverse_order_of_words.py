# Write a program to reverse order of words of the given string .

string = "learning python is very easy"

# using slice operator

string_with_split = string.split()  # ["learning" , "python" , "is" ,  "very" , "easy"]

output_string_reverse = string_with_split[::-1]

output_string_join = ' '.join(output_string_reverse)

print(output_string_join) # easy very is python learning


# using for loop

output_string_result = []

for word in string_with_split:
    output_string_result.insert(0, word) # insert each word at the front

    # list.insert(index, value) inserts value into the list at position index, shifting everything already at or 
    # after that index one spot to the right. insert(0, word) always inserts at the very front — 
    # so each new word pushes the previous ones further back.

reversed_string = ' '.join(output_string_result)

print(reversed_string) # easy very is python learning


# insert(0, ...) is O(n) every single call, because Python has to shift all existing elements one position to the right to make room at the front. 
# So this loop is O(n²) overall — fine for a short sentence, but inefficient for large lists. 
# That's exactly why [::-1] or reversed() (both O(n)) are the preferred approach in real code — the manual loop is really just for building intuition about
#  how reversal works under the hood.


