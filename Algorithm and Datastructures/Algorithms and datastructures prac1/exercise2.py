"""
(R-1.11) Demonstrate how to use Python’s list comprehension syntax
to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
"""


New_List = [2**i for i in range(0, 9)]
print(New_List)