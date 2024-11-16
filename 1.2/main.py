from timeit import timeit
from random import randint
from functools import partial


def bubble_sort(arr):
    arr = arr.copy()

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    array = [randint(0, 100) for i in range(1_000_000)]

    print(timeit(partial(bubble_sort, array), number=1))
    print(timeit(partial(quick_sort, array), number=1))
    print(timeit(partial(sorted, array), number=1))
    
    assert bubble_sort(array) == sorted(array)
    assert quick_sort(array) == sorted(array)
