import random


class Node:
    def __init__(self, index, element, neighbor):
        self.element = element
        self.next = neighbor
        self.index = index


class LinkedSparseArray:

    def __init__(self, n):
        self.size = n
        self.head = None

    def __getitem__(self, i):
        current = self.head
        while current is not None:
            if current.index == i:
                return current.element
            else:
                current = current.next
        return None

    def __setitem__(self, i, e):
        if i >= self.size:
            print("index is to high")
        self.head = Node(i, e, self.head)

    def __len__(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return (str("n = {}, m = {} and level of sparseness = {} %".format(self.size, length, (length/self.size)*100)),
                self.size, length)

    def fill(self, seq):
        i = 0
        for e in seq:
            if e is not None:
                self.__setitem__(i, e)
            i += 1

    def print_linked(self):
        current = self.head
        linked_list = "linked list is: "
        while current is not None:
            element = current.element
            index = current.index
            if current.next is None:
                linked_list = linked_list + " ({}, {}) ".format(index, element)
            else:
                linked_list = linked_list + " ({}, {}) -> ".format(index, element)
            current = current.next
        print(linked_list)


class SparseArray:
    def __init__(self, n, m):
        self.size = n
        self.sparseness = m

    def create(self):
        array = [None] * self.size
        index = random.sample(range(0, self.size), self.sparseness)
        for i in range(len(index)):
            element = random.randint(0, 100 + 1)
            array[index[i]] = element
        return array
