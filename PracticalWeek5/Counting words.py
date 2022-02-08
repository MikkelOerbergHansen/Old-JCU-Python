"""
From scratch exercise!

Write a program to count the occurrences of words in a string.
The program should ask the user for a string,
then print the counts of how many of each word are in the file.
"""
import collections

my_string = str(input("enter your String: "))
my_words = my_string.split()

COUNTS = dict()
for word in my_words:
    if word in COUNTS:
        COUNTS[word] += 1
    else:
        COUNTS[word] = 1

COUNTS = collections.OrderedDict(sorted(COUNTS.items()))
char_length = max((len(word) for word in my_words))
for k, v in COUNTS.items():
    print("{:{}} : {}".format(k, char_length, v))
