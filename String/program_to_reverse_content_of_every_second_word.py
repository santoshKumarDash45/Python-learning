# write a program to reverse internal content of every second word in a given string

sentence = "The quick brown fox jumps over the lazy dog"

list = sentence.split()

for word in list:
    if list.index(word) % 2 != 0:
        reversed_word = word[::-1]
        print(reversed_word, end=' ') 
    else:
        print(word, end=' ')

        # Output: The kciuq brown xof jumps revo the yzal dog