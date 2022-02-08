from linked_binary_tree import LinkedBinaryTree


class MutableLinkedBinaryTree(LinkedBinaryTree):
    def __init__(self):
        super().__init__()

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def attach(self, p, t1, t2):
        return self.attach(p, t1, t2)


if __name__ == '__main__':

    # exercise 4
    t = MutableLinkedBinaryTree()
    root = t.add_root(1)
    node2 = t.add_left(root, 2)
    t.add_left(node2, 4)
    t.add_right(node2, 5)
    node3 = t.add_right(root, 3)
    node6 = t.add_left(node3, 6)
    node7 = t.add_right(node3, 7)
    t.add_left(node6, 8)
    t.add_right(node6, 9)
    t.add_right(node7, 10)

    # create tree from exercise 2

    in_order = [p.element() for p in t.inorder()]
    print("in-order", end=": ")
    print(in_order, sep="")

    post_order = [p.element() for p in t.postorder()]
    print("post-order", end=": ")
    print(post_order, sep="")

    pre_order = [p.element() for p in t.preorder()]
    print("pre-order", end=": ")
    print(pre_order, sep="")
