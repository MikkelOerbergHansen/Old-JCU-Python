"""
In this experiment we are examining the getitem function from
LinkedSparseArray
and comparing it to the getitem function from DynamicArray
they are both appending random integers and then we measure the time taken
to retrieve all of these integers.
"""

from SparseArray import LinkedSparseArray
import matplotlib.pyplot as plt
from dynamic_array import DynamicArray
import random
from time import time


def time_experiment(n, m):
    time_measures = []
    time_measures2 = []

    for NumberOfNodes in m:
        s = LinkedSparseArray(n)
        for j in range(0, NumberOfNodes):
            s.__setitem__(j, random.randint(0, 100))
        start = time()
        for j in range(0, NumberOfNodes):
            value = s.__getitem__(j)
        end = time()
        time_measures.append(end - start)
        print(s.__len__()[0])
        print("total time to retrieve linked list is {0:.20f}".format((end - start)))
        print("average time to retrieve elements from linked list is {0:.20f}".format((end - start) / NumberOfNodes))
        print()

        data = DynamicArray()
        for k in range(0, NumberOfNodes):
            data.append(random.randint(0, 100))
        start = time()
        for k in range(0, NumberOfNodes):
            value = data.__getitem__(k)
        end = time()
        time_measures2.append(end - start)
    return [time_measures, time_measures2]


n = 10**5
m = [20000, 40000, 60000, 80000]
time_result = time_experiment(n, m)
print(time_result)
plt.figure(100)
plt.plot(m, time_result[0], "r")
plt.plot(m, time_result[1], "g")
plt.title('n is 10^5, while m varies between 20%, 40%, 60%, 80%')

plt.show()
