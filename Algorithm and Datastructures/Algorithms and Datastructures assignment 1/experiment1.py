"""
In experiment 1 we are comparing the fill function from LinkedSparseArray
with the append function from Dynamic Array
in each plot we are looking at different values of n with fixed sparseness
the sparseness changes in different plots.
both function are appending values from a random SparseArray created with the SparseArray class
"""


from SparseArray import LinkedSparseArray
from SparseArray import SparseArray
import matplotlib.pyplot as plt
from dynamic_array import DynamicArray

from time import time


def time_experiment(n, m):
    time_measures = []
    time_measures2 = []

    sparse = SparseArray(n, m).create()
    s = LinkedSparseArray(len(sparse))
    start = time()
    s.fill(sparse)
    end = time()
    time_measures.append(end - start)
    print(s.__len__()[0])
    print("total time to create linked list is {0:.20f}".format((end - start)))
    print("average time to create linked list is {0:.20f}".format((end - start)/m))
    print()

    data = DynamicArray()
    start = time()
    for k in range(len(sparse)):
        data.append(sparse[k])
    end = time()
    time_measures2.append(end - start)

    return [time_measures, time_measures2]


#
# Experiment 1
#
n = 10**4           # 10^4
m = int(2.5 * 10**3)
time_result1 = time_experiment(n, m)
n = 10**5          # 10^5
m = int(2.5 * 10**4)
time_result2 = time_experiment(n, m)
n = 10**6         # 10^6
m = int(2.5 * 10**5)
time_result3 = time_experiment(n, m)
n = 10**7         # 10^7
m = int(2.5 * 10**6)
time_result4 = time_experiment(n, m)

plt.figure(100)
# time comparison between SparseArray, and dynamic_array for different values of n
# and a sparseness of 25%
# we can see that LinkedSparseArray is faster than DynamicArray to fill an array with values
plt.plot([10**4, 10**5, 10**6, 10**7], [time_result1[0][0], time_result2[0][0], time_result3[0][0],
                                        time_result4[0][0]], "r")
plt.plot([10**4, 10**5, 10**6, 10**7], [time_result1[1][0], time_result2[1][0], time_result3[1][0],
                                        time_result4[1][0]], "g")
plt.title('n varies, while m is fixed on 25%')

#
# Experiment 2
#
n = 10**4           # 10^4
m = int(5 * 10**3)
time_result1 = time_experiment(n, m)
n = 10**5          # 10^5
m = int(5 * 10**4)
time_result2 = time_experiment(n, m)
n = 10**6         # 10^6
m = int(5 * 10**5)
time_result3 = time_experiment(n, m)
n = 10**7         # 10^7
m = int(5 * 10**6)
time_result4 = time_experiment(n, m)

plt.figure(200)
# time comparison between SparseArray, and dynamic_array for different values of n
# and a sparseness of 25%
# we can see that LinkedSparseArray is faster than DynamicArray to fill an array with values
plt.plot([10**4, 10**5, 10**6, 10**7], [time_result1[0][0], time_result2[0][0], time_result3[0][0],
                                        time_result4[0][0]], "r")
plt.plot([10**4, 10**5, 10**6, 10**7], [time_result1[1][0], time_result2[1][0], time_result3[1][0],
                                        time_result4[1][0]], "g")
plt.title('n varies, while m is fixed on 50%')

#
# Experiment 3
#
n = 10**4           # 10^4
m = int(7.5 * 10**3)
time_result1 = time_experiment(n, m)
n = 10**5          # 10^5
m = int(7.5 * 10**4)
time_result2 = time_experiment(n, m)
n = 10**6         # 10^6
m = int(7.5 * 10**5)
time_result3 = time_experiment(n, m)
n = 10**7         # 10^7
m = int(7.5 * 10**6)
time_result4 = time_experiment(n, m)

plt.figure(300)
# time comparison between SparseArray, and dynamic_array for different values of n
# and a sparseness of 25%
# we can see that LinkedSparseArray is faster than DynamicArray to fill an array with values
plt.plot([10**4, 10**5, 10**6, 10**7], [time_result1[0][0], time_result2[0][0], time_result3[0][0],
                                        time_result4[0][0]], "r")
plt.plot([10**4, 10**5, 10**6, 10**7], [time_result1[1][0], time_result2[1][0], time_result3[1][0],
                                        time_result4[1][0]], "g")
plt.title('n varies, while m is fixed on 75%')

plt.show()



