"""
exercise 4 and test of exercise 5
"""

from positional_list import PositionalList


def list_to_positional_list(a_list):
    pos_list = PositionalList()
    for element in a_list:
        pos_list.add_last(element)
    return pos_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_pos_list = list_to_positional_list(my_list)
# added function "print_list" to positional_list.py
print(my_pos_list.print_list(my_pos_list))


# testing exercise 5
# also see function "max" in positional_list.py
print(my_pos_list.max(my_pos_list))
