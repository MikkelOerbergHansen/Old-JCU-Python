
from SparseArray import LinkedSparseArray
from SparseArray import SparseArray

# example

n = 5
S = LinkedSparseArray(n)
S.__setitem__(3, 4)
S.__setitem__(1, 2)

print(S.__getitem__(1))

print(S.__len__()[0])

for j in range(0, n):
    data = S.__getitem__(j)
    print('The data at index {} is {}'.format(j, data))

print()
print()
# second example

sparse_array = [None, 14, 17, 8, 21, None, 15, 2, 11, 24]
S = LinkedSparseArray(len(sparse_array))
print(S.__len__()[0])
S.fill(sparse_array)
for j in range(0, S.__len__()[1]):
    data = S.__getitem__(j)
    print('The data at index {} is {}'.format(j, data))
print(S.__len__()[0])

S.print_linked()

print()
print()

# a third example
sparse = SparseArray(10, 5).create()
print(sparse)
S = LinkedSparseArray(len(sparse))
S.fill(sparse)
print(S.__len__()[0])
S.print_linked()
for j in range(0, S.__len__()[1]):
    data = S.__getitem__(j)
    print('The data at index {} is {}'.format(j, data))
