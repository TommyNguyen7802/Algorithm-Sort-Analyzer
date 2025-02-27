import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
# other python files
from AnalyzingAlgorithms import *
from anim_bubble import animate_bubble_sort, b_toggle_pause
from anim_linear import animate_linear_search, l_toggle_pause
from anim_merge import animate_merge_sort, m_toggle_pause
from anim_radix import animate_radix_sort, r_toggle_pause
from anim_quick import animate_quick_sort, q_toggle_pause

# consts
SPEED = 250

# ---------- functions ----------
def generate_random_array(min_value, max_value, num_of_elements):
    random_array = [random.randint(min_value, max_value) for _ in range(num_of_elements)]
    return random_array

def show_results_windows():
    # -- error handling --
    if want_bubble_sort.get() == 0 and want_merge_sort.get() == 0 and want_quick_sort.get() == 0 \
        and want_quick_sort.get() == 0 and want_linear_search.get() == 0:
        error_message_label.config(text="Error: No algorithm selected", fg="red")
        return

    if want_display_arrays.get() == 0 and want_display_graphs.get() == 0 and want_display_animations.get() == 0:
        error_message_label.config(text="Error: No display selected", fg="red")
        return
    
    inputs = {
        "minimum_value": min_value_input.get(),
        "maximum_value": max_value_input.get(),
        "elements": elements_input.get()
    }

    # Check if any input is an empty string
    if any(value == "" for value in inputs.values()):
        error_message_label.config(text="Error: please enter values into minimum value, maximum value, and number of elements", fg="red")
        return
    
    # Convert inputs to integers
    minimum_value = int(inputs["minimum_value"])
    maximum_value = int(inputs["maximum_value"])
    elements = int(inputs["elements"])

    if minimum_value > maximum_value:
        error_message_label.config(text="Error: minimum value is greater than maximum value", fg="red")
        return

    # Clear error message if all checks passed
    error_message_label.config(text="")
    array = generate_random_array(minimum_value, maximum_value, elements)

    '''
        -- create new window(s) --
        order of creation: 1. arrays 2. animations 3. graphs
    '''
    # -- Arrays Window --
    if want_display_arrays.get() == 1:
        display_arrays_window = tk.Toplevel()
        display_arrays_window.title("Result")

        # original array
        original_arr_label = tk.Label(display_arrays_window, text=f"Original Array: {array}", font=BODY_FONT)
        original_arr_label.pack(padx=10)

    algorithms_to_graph = []
    search_times = {}
    # lower value makes animation faster and vice versa - not intuitive so need to convert
    if want_display_animations.get() == 1:
        speed_input = float(animation_speed_input.get())
        if speed_input == 0.5:
            animation_speed = SPEED * 2.0
        elif speed_input == 1.5:
            animation_speed = SPEED * 0.66
        elif speed_input == 2.0:
            animation_speed = SPEED * 0.5
        else:
            animation_speed = SPEED * speed_input

    if want_bubble_sort.get() == 1:
        if want_display_arrays.get() == 1:
            sorted_array = bubble_sort(array.copy())
            result_label = tk.Label(display_arrays_window, text=f"Sorted Bubble Array: {sorted_array}", font=BODY_FONT)
            result_label.pack()
        if want_display_animations.get() == 1:
            animate_bubble_sort(array.copy(), animation_speed)
        if want_display_graphs.get() == 1:
            algorithms_to_graph.append(("Bubble Sort", bubble_sort))
    if want_merge_sort.get() == 1:
        if want_display_arrays.get() == 1:
            sorted_array = merge_sort(array.copy())
            result_label = tk.Label(display_arrays_window, text=f"Sorted Merge Array: {sorted_array}", font=BODY_FONT)
            result_label.pack()
        if want_display_animations.get() == 1:
            animate_merge_sort(array.copy(), animation_speed)
        if want_display_graphs.get() == 1:
            algorithms_to_graph.append(("Merge Sort", merge_sort))
    if want_quick_sort.get() == 1:
        if want_display_arrays.get() == 1:
            sorted_array = quick_sort(array.copy())
            result_label = tk.Label(display_arrays_window, text=f"Sorted Quick Array: {sorted_array}", font=BODY_FONT)
            result_label.pack()
        if want_display_animations.get() == 1:
            animate_quick_sort(array.copy(), animation_speed)
        if want_display_graphs.get() == 1:
            algorithms_to_graph.append(("Quick Sort", quick_sort))
    if want_radix_sort.get() == 1:
        if want_display_arrays.get() == 1:
            sorted_array = radix_sort(array.copy())
            result_label = tk.Label(display_arrays_window, text=f"Sorted Radix Array: {sorted_array}", font=BODY_FONT)
            result_label.pack()
        if want_display_animations.get() == 1:
            animate_radix_sort(array.copy(), animation_speed)
        if want_display_graphs.get() == 1:
            algorithms_to_graph.append(("Radix Sort", radix_sort))
    if want_linear_search.get() == 1:
        if want_display_arrays.get() == 1:
            target_locations = linear_search(array.copy(), linear_search_target_input)
            result_label = tk.Label(display_arrays_window, text=f"{linear_search_target_input} is at index: {target_locations}", font=BODY_FONT)
            result_label.pack()
        if want_display_animations.get() == 1:
            animate_linear_search(array.copy(), animation_speed)
        if want_display_graphs.get() == 1:
            search_time = measure_search_time(linear_search, array.copy(), linear_search_target_input)
            search_times["Linear Search"] = search_time

    # -- Graph Window --
    if want_display_graphs.get() == 1:
        # Gather execution times
        times = {name: measure_sort_time(func, array.copy()) for name, func in algorithms_to_graph}
        # Combine execution times with search time
        combined_times = {**times, **search_times}

        # Create graph
        plt.figure(figsize=(10, 5))
        plt.bar(combined_times.keys(), combined_times.values(), color=['blue', 'green'])
        plt.xlabel('Sorting Algorithm')
        plt.ylabel('Time (seconds)')
        plt.title('Execution Time of Sorting Algorithms and Linear Search')
        plt.show()

# ---------- main menu ----------
window = tk.Tk()
window.title("Alogrithms Visualization")

frame = tk.Frame(window) # frames are like <div>
frame.pack()

# consts
HEADER_FONT = ("Segoe UI", 14, "bold")
BODY_FONT = ("Segoe UI", 12)
MAXIMUM_VALUE = 1000000000 # 1 mil
MINIMUM_NUMBER = 0

# SECTION : Configure Input Array
# header/frame
input_array_frame = tk.LabelFrame(frame, text="Configure Input Array", font=HEADER_FONT)
input_array_frame.grid(row=0, column=0)

# form
min_value_label = tk.Label(input_array_frame, text="Enter minimum value", font=BODY_FONT)
min_value_label.grid(row=0, column=0, sticky="w")
min_value_input = tk.Spinbox(input_array_frame, from_=MINIMUM_NUMBER, to=MAXIMUM_VALUE, font=BODY_FONT)
min_value_input.grid(row=0, column=1)

max_value_label = tk.Label(input_array_frame, text="Enter maximum value", font=BODY_FONT)
max_value_label.grid(row=1, column=0, sticky="w")
max_value_input = tk.Spinbox(input_array_frame, from_=MINIMUM_NUMBER, to=MAXIMUM_VALUE, font=BODY_FONT)
max_value_input.grid(row=1, column=1)

elements_label = tk.Label(input_array_frame, text="Enter number of elements", font=BODY_FONT)
elements_label.grid(row=2, column=0, sticky="w")
elements_input = tk.Spinbox(input_array_frame, from_=0, to=MAXIMUM_VALUE, font=BODY_FONT)
elements_input.grid(row=2, column=1)

# set padding on input array frame
for widget in input_array_frame.winfo_children():
    widget.grid_configure(padx=10, pady=1)

# SECTION : Select Algorithms
# header/frame
select_algo_frame = tk.LabelFrame(frame, text="Select Alogrithm", font=HEADER_FONT)
select_algo_frame.grid(row=3, column=0)

# form
want_bubble_sort = tk.IntVar()
tk.Checkbutton(select_algo_frame, text="Bubble Sort", variable=want_bubble_sort, font=BODY_FONT).grid(row=3, column=0, sticky="w")

want_merge_sort = tk.IntVar()
tk.Checkbutton(select_algo_frame, text="Merge Sort", variable=want_merge_sort, font=BODY_FONT).grid(row= 4, column=0, sticky="w")

want_quick_sort = tk.IntVar()
tk.Checkbutton(select_algo_frame, text="Quick Sort", variable=want_quick_sort, font=BODY_FONT).grid(row= 5, column=0, sticky="w")

want_radix_sort = tk.IntVar()
tk.Checkbutton(select_algo_frame, text="Radix Sort", variable=want_radix_sort, font=BODY_FONT).grid(row= 6, column=0, sticky="w")

want_linear_search = tk.IntVar()
tk.Checkbutton(select_algo_frame, text="Linear Search +", variable=want_linear_search, font=BODY_FONT).grid(row= 7, column=0, sticky="w")
linear_search_target_label = tk.Label(select_algo_frame, text="Target ", font=BODY_FONT)
linear_search_target_label.grid(row=7, column=1)
linear_search_target_input = tk.Spinbox(select_algo_frame, from_=MINIMUM_NUMBER, to=MAXIMUM_VALUE, width=5, font=BODY_FONT)
linear_search_target_input.grid(row=7, column=2)

# SECTION : Select what to display
# header/frame
select_display_frame = tk.LabelFrame(frame, text="Select Display", font=HEADER_FONT)
select_display_frame.grid(row=8, column=0)

# form
want_display_arrays = tk.IntVar()
tk.Checkbutton(select_display_frame, text="Display Arrays", variable=want_display_arrays, font=BODY_FONT).grid(row=8, column=0, sticky="w")

want_display_graphs = tk.IntVar()
tk.Checkbutton(select_display_frame, text="Display Graphs", variable=want_display_graphs, font=BODY_FONT).grid(row=9, column=0, sticky="w")

want_display_animations = tk.IntVar()
tk.Checkbutton(select_display_frame, text="Display Animations +", variable=want_display_animations, font=BODY_FONT).grid(row=10, column=0, sticky="w")
animation_speed_label = tk.Label(select_display_frame, text="Speed", font=BODY_FONT)
animation_speed_label.grid(row=10, column=1)
animation_speed_input = ttk.Combobox(select_display_frame, values=[0.5, 1, 1.5, 2], width=5, font=BODY_FONT)
animation_speed_input.grid(row=10, column=2)
animation_speed_input.set(1) # set default speed

# SECTION : Show error messages
error_message_label = tk.Label(frame, text="", font=BODY_FONT)
error_message_label.grid(row=11, column=0, columnspan=2)

# SECTION : Buttons
start_button = tk.Button(frame, text="Start", font=BODY_FONT, width=10, command=show_results_windows)
start_button.grid(row=12, column=0, sticky="w")
pause_button = tk.Button(frame, text="Pause", font=BODY_FONT, width=10, command=lambda:[m_toggle_pause(), q_toggle_pause(), r_toggle_pause(), b_toggle_pause(), l_toggle_pause()])
pause_button.grid(row=12, column=0, sticky="n")
quit_button = tk.Button(frame, text="Quit", font=BODY_FONT, width=10, command=window.destroy)
quit_button.grid(row=12, column=0, sticky="e")

window.mainloop()