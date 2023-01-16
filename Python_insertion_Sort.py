from random import randint
from timeit import repeat
import time

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    start = time.time()

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    end = time.time()

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    print(f"Algorithm: {algorithm}. Execution time: {end - start}")


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    start = time.time()

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    end = time.time()

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    print(f"Algorithm: {algorithm}. Execution time: {end - start}")

#//////////////////////////////////////////////////////////////////////////////

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break


#//////////////////////////////////////////////////////////////////////////////

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):

        if array[i]<array[i-1]:
            array[i-1], array[i] = array[i], array[i-1]

        for j in range(i-1, 0, -1):

            if array[j]<array[j-1]: 
                array[j-1], array[j] = array[j], array[j-1]


#//////////////////////////////////////////////////////////////////////////////


ARRAY_LENGTH = 10_00

if __name__ == "__main__":
    array = [randint(0, 1_000) for i in range(ARRAY_LENGTH)]
    # array = [8, 2, 6, 4, 5]

    run_sorting_algorithm(algorithm="sorted", array=array)
    run_sorting_algorithm(algorithm="bubble_sort", array=array)
    run_sorting_algorithm(algorithm="insertion_sort", array=array)
