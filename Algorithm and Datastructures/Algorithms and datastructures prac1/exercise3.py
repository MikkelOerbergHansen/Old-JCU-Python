"""
(C-1.15) Write a Python function that takes a sequence of numbers
and determines if all the numbers are different from each other
(that is, they are distinct).
"""

number_sequence = [int(x) for x in input(" write the numbers of your list: ").split()]

print(number_sequence)
if len(number_sequence) == len(set(number_sequence)):
    print("True!! all numbers are distinct")
else:
    print("False!! all numbers are not distinct")
