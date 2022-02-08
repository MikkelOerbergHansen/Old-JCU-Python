from probe_hash_map import ProbeHashMap
from avl_tree import AVLTreeMap
import random
import time


def create_random_dict(size):
    my_dict = {}
    keys = list(range(1, size+1))
    for key in keys:
        element = random.randint(0, 100 + 1)
        my_dict[str(key)] = element
    return my_dict


def run_experiment1(func, data):
    overall_time = 0.0
    for key, value in data.items():
        start_time = time.clock()
        func.__setitem__(key, value)
        end_time = time.clock()
        overall_time += end_time - start_time
    return overall_time


def run_experiment2(func, data):
    overall_time = 0.0
    for key, value in data.items():
        start_time = time.clock()
        func.__getitem__(key)
        end_time = time.clock()
        overall_time += end_time - start_time
    return overall_time


print("")
print("Experiments with setitem -- -- -- ProbeHashMap")
print("==============================================================================================")
print("")

n = 10**2
new_hash_map1 = ProbeHashMap()
new_dict = create_random_dict(n)
result = run_experiment1(new_hash_map1, new_dict)
print("Experiment with setitem")
print("overall time taken is: {}".format(result))
print("average time: {0:.30f}".format(result/n))


print("")
print("")
print("Experiments with getitem -- -- -- ProbeHashMap")
print("==============================================================================================")
print("")

result = run_experiment2(new_hash_map1, new_dict)
print("Experiment with getitem")
print("overall time taken is: {}".format(result))
print("average time: {0:.30f}".format(result/n))


print("")
print("")
print("Experiments with setitem -- -- -- AVL Tree")
print("==============================================================================================")
print("")

n = 10**2
new_tree = AVLTreeMap()
new_dict = create_random_dict(n)
result = run_experiment1(new_tree, new_dict)
print("Experiment with setitem")
print("overall time taken is: {}".format(result))
print("average time: {0:.30f}".format(result/n))

print("")
print("")
print("Experiments with getitem -- -- -- AVL Tree")
print("==============================================================================================")
print("")

result = run_experiment2(new_tree, new_dict)
print("Experiment with getitem")
print("overall time taken is: {}".format(result))
print("average time: {0:.30f}".format(result/n))
