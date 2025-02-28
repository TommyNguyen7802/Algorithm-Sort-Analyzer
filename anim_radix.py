import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
import random

pause = False
original_array = []
speed = 1  # default speed for animation
sorting_steps = []  # store progress
ani = None

def r_toggle_pause():
    global pause
    pause = not pause

def r_reset():
    global ani, pause, original_array, speed, fig
    if ani:
        ani.event_source.stop()
    pause = False
    plt.close(fig)
    animate_radix_sort(original_array.copy(), speed)

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
        sorting_steps.append((arr.copy(), i))

def radix_sort(arr):
    global sorting_steps
    sorting_steps = []
    arr = arr.copy()

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

def update(frame):
    global pause
    while pause:
        plt.pause(0.1)
    arr, current_index = frame
    plt.clf()
    bars = plt.bar(range(len(arr)), arr, color='black')

    for bar, value in zip(bars, arr):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                 str(value), ha='center', va='bottom', fontsize=12, color='red')
        if bars.index(bar) == current_index:
            bar.set_color('red')

    plt.ylim(0, max(arr) * 1.2)

def animate_radix_sort(arr, interval):
    global sorting_steps, ani, original_array, speed, fig
    sorting_steps = []

    original_array = arr.copy()  # store the original array
    speed = interval  # set speed to the interval value

    radix_sort(arr)

    fig, ax = plt.subplots()
    ax.set_title("Radix Sort Animation")

    ani = FuncAnimation(fig, update, frames=sorting_steps, repeat=False, interval=speed)
    plt.show()

    return ani
