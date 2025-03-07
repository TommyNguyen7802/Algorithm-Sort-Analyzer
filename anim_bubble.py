import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pause = False

def b_toggle_pause():
    global pause
    pause = not pause

def b_close():
    plt.close()

'''
    ---------- algorithm ----------
    modified to include yield, yield is needed for animation
'''
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, j
    yield arr, -1 # when finished j = -1

# ---------- animation ----------
def update_graph(frame, bars):
    global pause
    while pause:
        plt.pause(0.1)
        
    array, j = frame # get yieled values

    # change bar height
    for bar, height in zip(bars, array):
        bar.set_height(height)

    # change colors
    for bar in bars:
        bar.set_color("black")
    if j != -1:
        bars[j].set_color("red")
        bars[j+1].set_color("red")
    # else: # finished sorting
        # for bar in bars:
        #     bar.set_color("blue")


def animate_bubble_sort(array, speed):
    # graph details
    figure, axis = plt.subplots()
    axis.set_xlim(0, len(array))
    axis.set_ylim(min(array), max(array)+10)

    # bars, each bar is an element in array
    bars = axis.bar( range(len(array)), array, color="black")

    animation = FuncAnimation(fig=figure, func=update_graph, fargs=(bars,),frames=bubble_sort(array), interval=speed,
                              repeat=False, cache_frame_data=False)
    plt.show()