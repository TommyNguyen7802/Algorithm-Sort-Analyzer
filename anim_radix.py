import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


sorting_steps = []  # store progress

def counting_sort(arr, exp):
    global sorting_steps
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
        sorting_steps.append(arr.copy())  # append current state inside sorting_steps

def radix_sort(arr):
    global sorting_steps
    sorting_steps = []  # Reset sorting steps
    arr = arr.copy()

    max_num = max(arr)  # Find the largest number to determine digit count
    exp = 1  # Start with least significant digit (LSD)

    while max_num // exp > 0:
        counting_sort(arr, exp)  # Sort by current digit
        exp *= 10  # Move to next significant digit

    return arr  # The array is now sorted

def update(frame):
    """Update function for animation, displaying numbers on top of bars."""
    plt.clf()
    bars = plt.bar(range(len(frame)), frame, color='black')

    # Add text labels on top of each bar
    for bar, value in zip(bars, frame):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                 str(value), ha='center', va='bottom', fontsize=12, color='red')

    plt.ylim(0, max(sorting_steps[-1]) * 1.2)

def animate_radix_sort(arr):
    """Main function to animate Radix Sort using an externally provided array."""
    global sorting_steps
    sorting_steps = []

    radix_sort(arr)

    fig, ax = plt.subplots()
    ax.set_title("Radix Sort Animation")

    ani = FuncAnimation(fig, update, frames=sorting_steps, repeat=False, interval=1000)
    plt.show()