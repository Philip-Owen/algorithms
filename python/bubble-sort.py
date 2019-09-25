import time

start_time = time.time()

arr = [77, 32, 99, 17, 2, 95]


def bubble_sort(arr):
    swapped = True
    passes = 0
    while swapped:
        swapped = False
        passes = passes + 1
        for i in range(len(arr) - passes):
            if i != (len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr.insert(i, arr.pop(i + 1))
                    swapped = True

    print(arr)
    print(f"Bubble sort took {time.time() - start_time} seconds to complete with {passes} passes.")

bubble_sort(arr)
