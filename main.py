from random import randint
from timeit import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort


def generate_random_list_numbers(num: int = 100) -> list:
    return [randint(1, 100) for _ in range(num)]


array1 = generate_random_list_numbers(10)
array2 = generate_random_list_numbers(500)

sort_types = {
    "merge sort": merge_sort,
    "insertion sort": insertion_sort,
    "Timsort": sorted,
}

for sort_name, sort_type in sort_types.items():

    execution_time = timeit(lambda: sort_type(array1.copy()), number=10000)
    print(f"Execution time of {str(sort_name)} 1: {execution_time} seconds")

    execution_time = timeit(lambda: sort_type(array2.copy()), number=10000)
    print(f"Execution time of {str(sort_name)} 2: {execution_time} seconds")
    