"""
prac 5 exercise 1
i added function to find second to last node in a linked list
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p is not None:
            while p.next is not None:
                if p.data == k:
                    return p
                p = p.next
            if p.data == k:
                return p
        return None

    def second_to_last(self):
        p = self.head
        if p is not None:
            while p.next is not None:
                k = p.next
                if k.next is None:
                    return p.data
                p = p.next
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.next.prev = tmp

    def __str__(self):
        s = ""
        p = self.head
        if p is not None:
            while p.next is not None:
                s += p.data
                p = p.next
            s += p.data
        return s


# example code
l = LinkedList()

l.add('a')
l.add('b')
l.add('c')
l.add("d")
l.add('e')
l.add('f')
l.add('g')
l.add("h")
print(l)

print(l.second_to_last())

l.remove(l.search('b'))
print(l)
