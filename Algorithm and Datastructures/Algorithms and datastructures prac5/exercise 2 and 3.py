"""
practical 5
exercise 2 and 3
"""


class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        node = Node(data)
        temp = self.head

        node.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = node

        else:
            node.next = node    # For the first node

        self.head = node

    # Function to print nodes in a given circular linked list
    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print("%d" % temp.data),
                temp = temp.next
                if temp == self.head:
                    break

    def count(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def contains(self, data):
        if self.head is None:
            return False
        else:
            p = self.head
            while p is not None:
                if p.data == data:
                    return True
                if p.next != self.head:
                    p = p.next
                else:
                    return False
            return False

    def is_in_the_same_list(self, x, y):
        if self.head is None:
            return False
        if self.contains(x) is True:
            current = self.head
            while current.next.data is not y:
                if current.next.data is x:
                    return "False: y is not in the list"
                else:
                    current = current.next
            return "True: both x and y are in the list"
        return "False: x is not in the list"


# example code

# Initialize list as empty
cl_list = CircularLinkedList()

# Created linked list will be 11->2->56->12
cl_list.push(12)
cl_list.push(56)
cl_list.push(2)
cl_list.push(11)

# print "Contents of circular Linked List"
print("testing the 'print' function")
cl_list.print_list()

print()
print()

# testing the count function
print("testing the 'count' function")
print(cl_list.count())


print()
print()


# testing the "contains" function
print("testing the 'contains' function")
print(cl_list.contains(3))
print(cl_list.contains(2))

print()
print()


# # # exercise 3
# def is_in_same_list(x, y):
#    current = x
#    while current.next is not y:
#        if current.next is x:
#            return False
#        else:
#            current = current.next
#    return True


list1 = CircularLinkedList()
list1.push(3)
list1.push(2)
list1.push(1)

list2 = CircularLinkedList()
list2.push(6)
list2.push(5)
list2.push(4)

print("testing the built in 'is_in_same_list' function")
print(list1.is_in_the_same_list(1,2))   # element are in the same list
print(list1.is_in_the_same_list(4,2))   # elements are not in the same list since x is not in the list
print(list1.is_in_the_same_list(2,4))   # elements are not in the same list since y is not in the list
print(list1.is_in_the_same_list(4,6))   # elements are in the same list but not the specified one

