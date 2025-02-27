# Analyzing Algorithms in Big O

import time

# Bubble Sort O(n^2)
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Merge Sort O(n log n)
def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2 # find middle index
        left_half = arr[:mid] # dividing list into halves
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Quick Sort O(n log n)
def quick_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Radix Sort O(nk)
def counting_sort(arr, exp):

    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurences of each digit in the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    # Update count[i] so that it contains actual position in the output[]
    for i in range(1,10):
        count[i] += count[i - 1] # Cumulative sum for stable sorting

    # Build the output array by placing elements in the correct order    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1 # Decrement count to handle duplicates

    # Copy sorted output back to original array
    for i in range(n):
        arr[i] = output[i] # Overwrite orginal array with sorted values

def radix_sort(arr):
    arr = arr.copy()
    # Least Significant Digit approach (LSD)
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1

    # Continue sorting for each digit place value
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Linear Search O(n)
def linear_search(L,T):
    indices = []
    for i in range(len(L)):
        if L[i] == T:
            indices.append(i)
    return indices

# Measure execution time
def measure_sort_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

def measure_sorting_time(sort_func, arr):
    size = len(arr)
    sort_name = sort_func.__name__

    print(f"Running {sort_name} on array of size {size}...")

    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Completed {sort_name} on size {size} in {time_taken:.5f} sec")

    return time_taken

def measure_search_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    search_time = end_time - start_time
    return search_time