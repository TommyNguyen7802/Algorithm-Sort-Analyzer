# Analyzing Algorithms in Big O

# Bubble Sort
def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] > students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]

# Insertion Sort
def insertion_sort(cards):
    for i in range(1, len(cards)):
        key = cards[i] # The card to be placed in the correct position
        j = i - 1 # Index of last card in the sorted position

        # Move elements of the sorted portion
        while j >= 0 and key < cards[j]:
            cards[j + 1] = cards[j] # Shift the elements to the right
            j -= 1 # Move one step to the left
            
        cards[j + 1] = key # Place key in its correct position

# Linear Search
def linear_search(L,T):
    for index in range(len(L)):
        if L[index] == T:
            return index
    return -1

# Selection Sort
def selection_sort(books):
    n = len(books)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if books[j][1] < books[min_index][1]:
                min_index = j
        books[i], books[min_index] = books[min_index], books[i]

# Radix Sort
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
    # Least Significant Digit approach (LSD)
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1

    # Continue sorting for each digit place value
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr