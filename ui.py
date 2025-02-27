import tkinter as tk
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
# other python files
from AnalyzingAlgorithms import *
from anim_bubble import run_bubble_anim
from anim_bubble import b_toggle_pause
from anim_linear import run_linear_anim
from anim_linear import l_toggle_pause
from anim_merge import animate_merge_sort
from anim_merge import m_toggle_pause
from anim_radix import animate_radix_sort
from anim_radix import r_toggle_pause
from anim_quick import animate_quick_sort
from anim_quick import q_toggle_pause

def generate_random_array(min_value, max_value, num_of_elements):
    # generate random array
    random_array = [random.randint(min_value, max_value) for _ in range(num_of_elements)]
    return random_array

# ---------- button functions ----------
def show_results_window(): # new window with result/visualization
    # ----- error checking -----
    # if no algo selected = error
    if wantBubbleSort.get() == 0 and wantMergeSort.get() == 0 and wantQuickSort.get() == 0 \
        and wantRadixSort.get() == 0 and wantLinearSearch.get() == 0:
        errors_label.config(text="Error: No Algorithm selected", fg="red")
        return
    else:
        errors_label.config(text="") # clear error message

     # if no display selected = error
    if wantDisplayArrays.get() == 0 and wantDisplayGraphs.get() == 0 and wantDisplayAnimations.get() == 0:
        errors_label.config(text="Error: No display selected", fg="red")
        return
    else:
        errors_label.config(text="") # clear error message

    inputs = {
        "minimum_value": min_value_input.get(),
        "maximum_value": max_value_input.get(),
        "elements": number_of_elements_input.get()
    }

    # Check if any input is an empty string
    if any(value == "" for value in inputs.values()):
        errors_label.config(text="Error: please enter values into minimum value, maximum value, and number of elements", fg="red")
        return

    # Convert inputs to integers
    minimum_value = int(inputs["minimum_value"])
    maximum_value = int(inputs["maximum_value"])
    elements = int(inputs["elements"])

    # Clear error message if all checks passed
    errors_label.config(text="")

    # if min is greater than max = error
    if minimum_value > maximum_value:
        errors_label.config(text="Error: minimum value is greater than maximum value", fg="red")
        return
    else:
        errors_label.config(text="") # clear error message
        array = generate_random_array(minimum_value, maximum_value, elements)

    # ---------- new window(s) ----------
    # create new window that displays arrays
    if wantDisplayArrays.get() == 1:
        display_arrays_window = tk.Toplevel()
        display_arrays_window.title("Result")

        # original array
        original_arr_label = tk.Label(display_arrays_window, text=f"Original Array: {array}", font=body_font)
        original_arr_label.pack()

    original_array = array.copy()
    
    algorithms = []
    search_times = {}

    # ----- check selected -----
    if wantBubbleSort.get() == 1:
        algorithms.append(("Bubble Sort", bubble_sort))
        sorted_array = bubble_sort(array)
        if wantDisplayArrays.get() == 1:
            result_label = tk.Label(display_arrays_window, text=f"Sorted Bubble Array: {sorted_array}", font=body_font)
            result_label.pack()
        if wantDisplayAnimations.get() == 1:
            run_bubble_anim(array.copy())
    if wantMergeSort.get() == 1:
        algorithms.append(("Merge Sort", merge_sort))
        sorted_array = merge_sort(array)
        if wantDisplayArrays.get() == 1:
            result_label = tk.Label(display_arrays_window, text=f"Sorted Merge Array: {sorted_array}", font=body_font)
            result_label.pack()
        if wantDisplayAnimations.get() == 1:
            animate_merge_sort(array.copy())
    if wantQuickSort.get() == 1:
        algorithms.append(("Quick Sort", quick_sort))
        sorted_array = quick_sort(array)
        if wantDisplayArrays.get() == 1:
            result_label = tk.Label(display_arrays_window, text=f"Sorted Quick Array: {sorted_array}", font=body_font)
            result_label.pack()
        if wantDisplayAnimations.get() == 1:
            animate_quick_sort(array.copy())
    if wantRadixSort.get() == 1:
        algorithms.append(("Radix Sort", radix_sort))
        sorted_array = radix_sort(array)
        if wantDisplayArrays.get() == 1:
            result_label = tk.Label(display_arrays_window, text=f"Sorted Radix Array: {sorted_array}", font=body_font)
            result_label.pack()
        if wantDisplayAnimations.get() == 1:
            animate_radix_sort(array.copy())
    if wantLinearSearch.get() == 1:
        target_element = int(target_element_input.get())
        target_location = linear_search(original_array, target_element)
        if wantDisplayArrays.get() == 1:
            result_label = tk.Label(display_arrays_window, text=f"{target_element} is at index: {target_location}", font=body_font)
            result_label.pack()
        if wantDisplayGraphs.get() == 1: # part of - Graph Window -
            # Measure Search Time
            search_time = measure_search_time(linear_search, array, target_element)
            search_times["Linear Search"] = search_time
        if wantDisplayAnimations.get() == 1:
            run_linear_anim(array.copy(), target_element)

    # ----- Graph Window -----
    if wantDisplayGraphs.get() == 1:
        # Gather execution times
        times = {name: measure_sort_time(func, array) for name, func in algorithms}
        # Combine execution times with search time
        combined_times = {**times, **search_times}

        # Create graph
        plt.figure(figsize=(10, 5))
        plt.bar(combined_times.keys(), combined_times.values(), color=['blue', 'green'])
        plt.xlabel('Sorting Algorithm')
        plt.ylabel('Time (seconds)')
        plt.title('Execution Time of Sorting Algorithms and Linear Search')
        plt.show()


def update_plot_with_pause(arr, bars, text):
    global pause
    while pause:
        plt.pause(0.1)
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    text.set_text('Array: ' + str(arr))
    plt.pause(0.1)

# ---------- main UI window ----------
root = tk.Tk()

# title, name of application
root.title("Sorting Alogrithms Visualization")

# custom font settings
header_font = ("Arial", 14, "bold")
body_font = ("Arial", 12)

# SECTION::::: configure input array
configure_input_array_label = tk.Label(root, text="Configure input array settings", font=header_font)
min_value_label = tk.Label(root, text="Enter minimum value: ", font=body_font)
max_value_label = tk.Label(root, text="Enter maximum value: ", font=body_font)
number_of_elements_label = tk.Label(root, text="Enter number of elements: ", font=body_font)

min_value_input = tk.Spinbox(root, from_=0, to=sys.maxsize, font=body_font)
max_value_input = tk.Spinbox(root, from_=0, to=sys.maxsize, font=body_font)
number_of_elements_input = tk.Spinbox(root, from_=0, to=sys.maxsize, font=body_font)

# configure input array UI placement
configure_input_array_label.grid(row=0, column=0, columnspan=2, sticky="n")

min_value_label.grid(row=1, column=0, sticky="w")
min_value_input.grid(row=1, column=1, sticky="w")

max_value_label.grid(row=2, column=0, sticky="w")
max_value_input.grid(row=2, column=1, sticky="w")

number_of_elements_label.grid(row=3, column=0, sticky="w")
number_of_elements_input.grid(row=3, column=1, sticky="w")

# SECTION::::: select algorithms + UI placement
select_algorithms_label = tk.Label(root, text="Select Algorithms", font=header_font)
select_algorithms_label.grid(row=4, column=0, columnspan=2, sticky="n")

wantBubbleSort = tk.IntVar()
tk.Checkbutton(root, text="Bubble Sort", font=body_font, variable=wantBubbleSort).grid(row=5, column=0, sticky="w")

wantMergeSort = tk.IntVar()
tk.Checkbutton(root, text="Merge Sort", font=body_font, variable=wantMergeSort).grid(row=5, column=1, sticky="w")

wantQuickSort = tk.IntVar()
tk.Checkbutton(root, text="Quick Sort", font=body_font, variable=wantQuickSort).grid(row=6, column=0, sticky="w")

wantRadixSort = tk.IntVar()
tk.Checkbutton(root, text="Radix Sort", font=body_font, variable=wantRadixSort).grid(row=6, column=1, sticky="w")

wantLinearSearch = tk.IntVar()
tk.Checkbutton(root, text="Linear Search", font=body_font, variable=wantLinearSearch).grid(row=7, column=0, sticky="w")
# target element input for Linear Sort
target_element_label = tk.Label(root, text="Enter target element for Linear Search: ", font=body_font)
target_element_input = tk.Spinbox(root, from_=0, to=sys.maxsize, font=body_font, width=10)
target_element_label.grid(row=7, column=1, sticky="w")
target_element_input.grid(row=7, column=2, sticky="w")

# SECTION::::: select what to display
select_to_display = tk.Label(root, text="Select Display", font=header_font).grid(row=8, columnspan=2, sticky="n")

wantDisplayArrays = tk.IntVar()
tk.Checkbutton(root, text="Display Arrays", font=body_font, variable=wantDisplayArrays).grid(row=9, column=0, sticky="w")

wantDisplayGraphs = tk.IntVar()
tk.Checkbutton(root, text="Display Graphs", font=body_font, variable=wantDisplayGraphs).grid(row=9, column=1, sticky="w")

wantDisplayAnimations = tk.IntVar()
tk.Checkbutton(root, text="Display Animations", font=body_font, variable=wantDisplayAnimations).grid(row=9, column=2, sticky="w")

# SECTION::::: errors
errors_label = tk.Label(root, text="", font=body_font)
errors_label.grid(row=10, columnspan=3, sticky="w")

# SECTION::::: buttons
start_button = tk.Button(root, text="Start", font=body_font, width=20, command=show_results_window)
pause_button = tk.Button(root, text="Pause", font=body_font, width=20, command=lambda:[m_toggle_pause(), q_toggle_pause(), r_toggle_pause(), b_toggle_pause(), l_toggle_pause()])
quit_button = tk.Button(root, text="Quit", font=body_font, width=20, command=root.destroy)

# buttons UI placement
start_button.grid(row=11, column=0, sticky="w")
pause_button.grid(row=11, column=1, sticky="w")
quit_button.grid(row=11, column=2, sticky="w")


# ---------- start application ----------
tk.mainloop()
