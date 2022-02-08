"""
In experiment 2 we are comparing the fill function from LinkedSparseArray
with the append function from Dynamic Array
in each plot we are looking at fixed values of n with different sparseness
the value of n changes in different plots.
both function are appending values from a random SparseArray created with the SparseArray class
"""


from SparseArray import LinkedSparseArray
from SparseArray import SparseArray
import matplotlib.pyplot as plt
from dynamic_array import DynamicArray

from time import time

n = 100000
m = [20000, 40000, 60000, 80000]


def time_experiment(n, m):
    time_measures = []
    time_measures2 = []

    print("experiment 1")

    for i in range(len(m)):
        sparse = SparseArray(n, m[i]).create()
        s = LinkedSparseArray(len(sparse))
        start = time()
        s.fill(sparse)
        end = time()
        time_measures.append(end - start)
        print(s.__len__()[0])
        print("total time to create linked list is {0:.20f}".format((end - start)))
        print("average time to create linked list is {0:.20f}".format((end - start)/m[i]))
        print()

        data = DynamicArray()
        start = time()
        for k in range(n):
            data.append(sparse[k])
        end = time()
        time_measures2.append(end - start)
    return [time_measures, time_measures2]


time_result = time_experiment(n, m)
print(time_result)
plt.figure(100)
plt.plot(m, time_result[0], "r")
plt.plot(m, time_result[1], "g")
plt.title('n is 10^5, while m varies between 20%, 40%, 60%, 80%')


time_result = time_experiment(n*10, [x * 10 for x in m])
print(time_result)
plt.figure(200)
plt.plot(m, time_result[0], "r")
plt.plot(m, time_result[1], "g")
plt.title('n is 10^6, while m varies between 20%, 40%, 60%, 80%')


time_result = time_experiment(n*100, [x * 100 for x in m])
print(time_result)
plt.figure(300)
plt.plot(m, time_result[0], "r")
plt.plot(m, time_result[1], "g")
plt.title('n is 10^7, while m varies between 20%, 40%, 60%, 80%')

plt.show()




