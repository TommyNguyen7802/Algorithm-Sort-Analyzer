import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

pause = False

def m_toggle_pause():
    global pause
    pause = not pause

def merge_sort(arr, ax, bars, text, speed):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, ax, bars, text, speed)
        merge_sort(right_half, ax, bars, text, speed)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            update_plot(arr, bars, text, speed)
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            update_plot(arr, bars, text, speed)
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            update_plot(arr, bars, text, speed)
    
    return arr

def update_plot(arr, bars, text, speed):
    global pause
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    text.set_text('Array: ' + str(arr))
    plt.draw()
    while pause:
        plt.pause(0.1)
    plt.pause(speed)

def animate_merge_sort(arr, speed):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='center')
    text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    ax.set_title('Merge Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    merge_sort(arr, ax, bars, text, speed)
    plt.show()

# Demo for testing
#arr = np.random.randint(1, 100, 10)
#animate_merge_sort(arr)
