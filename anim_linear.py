import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pause = False
original_array = []
speed = 1  # default speed for animation
animation = None
target_copy = 0

def l_toggle_pause():
    global pause
    pause = not pause

def l_reset():
    global animation, pause, original_array, speed, figure, target_copy
    if animation:
        animation.event_source.stop()
    pause = False
    plt.close(figure)
    animate_linear_search(original_array.copy(), target_copy ,speed)

'''
    ---------- algorithm ----------
    modified to include yield, yield is needed for animation
'''
def linear_search(L,T):
    indices = []
    for i in range(len(L)):
        yield i, L, indices
        if L[i] == T:
            indices.append(i)
            yield i, L, indices
    yield -1, L, indices # when finished i = -1

    # ---------- animation ----------
def update_graph(frame, bars):
    global pause
    while pause:
        plt.pause(0.1)
        
    i, array, indices = frame # get yieled values

    # change bar height
    for bar, height in zip(bars, array):
        bar.set_height(height)

    # change colors
    for bar in bars:
        bar.set_color("black")
    # highlight all found positions
    for index in indices:
        bars[index].set_color("blue")

    if i != -1:
        bars[i].set_color("red")
    # else: # finished searching


def animate_linear_search(array, target, interval):
    # graph details
    global original_array, speed, figure, animation, target_copy
    original_array = array.copy()
    speed = interval
    target_copy = target
    figure, axis = plt.subplots()
    axis.set_xlim(0, len(array))
    axis.set_ylim(min(array), max(array)+10)

    # bars, each bar is an element in array
    bars = axis.bar( range(len(array)), array, color="black")

    animation = FuncAnimation(fig=figure, func=update_graph, fargs=(bars,),frames=linear_search(array, target), interval=speed,
                              repeat=False, cache_frame_data=False)
    plt.show()