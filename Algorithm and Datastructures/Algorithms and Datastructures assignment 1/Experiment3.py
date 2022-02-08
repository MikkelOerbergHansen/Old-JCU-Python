"""
In this experiment we are examining the setitem function from
LinkedSparseArray
and comparing it to the append function from DynamicArray
they are both appending random integers
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
        start = time()
        for j in range(0, NumberOfNodes):
            s.__setitem__(j, random.randint(0, 100))
        end = time()
        time_measures.append(end - start)
        print(s.__len__()[0])
        print("total time to create linked list is {0:.20f}".format((end - start)))
        print("average time to create linked list is {0:.20f}".format((end - start) / NumberOfNodes))
        print()

        data = DynamicArray()
        start = time()
        for k in range(0, NumberOfNodes):
            data.append(random.randint(0, 100))
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


n = 10**6
m = [200000, 400000, 600000, 800000]
time_result = time_experiment(n, m)
print(time_result)
plt.figure(200)
plt.plot(m, time_result[0], "r")
plt.plot(m, time_result[1], "g")
plt.title('n is 10^6, while m varies between 20%, 40%, 60%, 80%')


n = 10**7
m = [2000000, 4000000, 6000000, 8000000]
time_result = time_experiment(n, m)
print(time_result)
plt.figure(300)
plt.plot(m, time_result[0], "r")
plt.plot(m, time_result[1], "g")
plt.title('n is 10^7, while m varies between 20%, 40%, 60%, 80%')


plt.show()
