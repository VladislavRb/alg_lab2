from search_algs import *
from random import randint
from time import time


def time_and_operations_for(search_method, k: int, n: int, p: int):
    overall_time = 0
    overall_operations = 0

    for i in range(0, k):
        arr = sorted([randint(0, p) for i in range(n)])

        rand_index = randint(0, n - 1)
        elem = arr[rand_index]

        start_time = time()

        found_index, operations = search_method(arr, elem)

        overall_time += time() - start_time
        overall_operations += operations

    return overall_time, overall_operations


k = 1
n = 100000
p = 100000

bin_time, bin_operations = time_and_operations_for(binary_search, k, n, p)
int_time, int_operations = time_and_operations_for(interpolation_search, k, n, p)

print("binary search: time =", bin_time, ", operations =", bin_operations)
print("interpolation search: time =", int_time, ", operations =", int_operations)
