import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pause = False

def l_toggle_pause():
    global pause
    pause = not pause

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


def animate_linear_search(array, target, speed):
    # graph details
    figure, axis = plt.subplots()
    axis.set_xlim(0, len(array))
    axis.set_ylim(min(array), max(array)+10)

    # bars, each bar is an element in array
    bars = axis.bar( range(len(array)), array, color="black")

    animation = FuncAnimation(fig=figure, func=update_graph, fargs=(bars,),frames=linear_search(array, target), interval=speed,
                              repeat=False, cache_frame_data=False)
    plt.show()