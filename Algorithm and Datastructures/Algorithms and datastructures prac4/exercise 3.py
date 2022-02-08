
from array_stack import ArrayStack


def transfer(s, t):
    while not s.is_empty():
        t.push(s.pop())


S = ArrayStack()
print(S.is_empty())
S.push(1)
S.push(2)
S.push(3)
print(S.is_empty())
print(S.top())      # top of S is 3
print(S.printStack())
T = ArrayStack()
transfer(S, T)
print(T.top())      # top of T is 1
print(T.printStack())

print()
print()
print("trying exercise 1")

S = ArrayStack()
S.push(5)
S.push(3)
print(S.pop())
S.push(2)
S.push(8)
print(S.pop())
print(S.pop())
S.push(9)
S.push(1)
print(S.pop())
S.push(7)
S.push(6)
print(S.pop())
print(S.pop())
S.push(4)
print(S.pop())
print(S.pop())

print(S.printStack())
