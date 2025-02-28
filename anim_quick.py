import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pause = False

def q_toggle_pause():
    global pause
    pause = not pause

sorting_steps = []  # store progress

def q_close():
    plt.close()

def quick_sort(arr):
    global sorting_steps
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    sorted_arr = quick_sort(left) + middle + quick_sort(right)
    sorting_steps.append((sorted_arr.copy(), pivot))
    return sorted_arr

def update(frame):
    global pause
    while pause:
        plt.pause(0.1)
    arr, pivot = frame
    plt.clf()
    bars = plt.bar(range(len(arr)), arr, color='black')

    for bar, value in zip(bars, arr):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                 str(value), ha='center', va='bottom', fontsize=12, color='red')
        if value == pivot:
            bar.set_color('blue')

    plt.ylim(0, max(arr) * 1.2)

def animate_quick_sort(arr, speed):
    global sorting_steps
    sorting_steps = []

    sorting_steps.append((arr.copy(), None))

    quick_sort(arr)

    fig, ax = plt.subplots()
    anim = FuncAnimation(fig, update, frames=sorting_steps, repeat=False, interval=speed)
    plt.show()

    return anim