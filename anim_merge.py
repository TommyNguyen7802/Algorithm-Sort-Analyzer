import matplotlib.pyplot as plt
import matplotlib.animation as animation

pause = False
sorting_steps = []

def m_toggle_pause():
    global pause
    pause = not pause

def m_close():
    sorting_steps = [] # clear
    plt.close()

def merge_sort(arr, ax, bars, text, speed, start_index=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, ax, bars, text, speed, start_index)
        merge_sort(right_half, ax, bars, text, speed, start_index + len(left_half))

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            sorting_steps.append((arr.copy(), start_index + k - 1))  # Record each step

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            sorting_steps.append((arr.copy(), start_index + k - 1)) # Record each step

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            sorting_steps.append((arr.copy(), start_index + k - 1)) # Record each step
    
    return arr

def update_plot(frame, bars, text):
    global pause
    if pause:
        plt.pause(0.1)
        return
    
    arr, current_index = frame
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    text.set_text('Array: ' + str(arr))
    for bar in bars:
        bar.set_color('blue')  # Set color for all bars
    bars[current_index].set_color('red')  # Highlight the current bar
    plt.draw()

def animate_merge_sort(arr, speed):
    global sorting_steps
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='center')
    text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    ax.set_title('Merge Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    sorting_steps = []  # Clear previous steps
    merge_sort(arr, ax, bars, text, speed)

    ani = animation.FuncAnimation(fig, update_plot, frames=sorting_steps, fargs=(bars, text), interval=speed, repeat=False)
    plt.show()