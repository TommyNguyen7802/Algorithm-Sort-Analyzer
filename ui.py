import tkinter as tk
import random
import sys

def generate_random_array(min_value, max_value, num_of_elements):
    random_array = [random.randint(min_value, max_value) for _ in range(num_of_elements)]
    return random_array

# button functions
def show_results_window(): # new window with result/visualization
    # create new window
    result_window = tk.Toplevel()
    result_window.title("Result")

    minimum_value = int(min_value_input.get())
    maximum_value = int(max_value_input.get())
    elements = int(number_of_elements_input.get())

    #TODO: replace prints with ui components

    if minimum_value > maximum_value:
        print("Error: minimum value is greater than maximum value")
        result_window.destroy()
    else:
        array = generate_random_array(minimum_value, maximum_value, elements)
        print(array)

    # check selected
    if wantBubbleSort.get() == 1:
        print("User selected Bubble Sort")
    if wantMergeSort.get() == 1:
        print("User selected Merge Sort")
    if wantQuickSort.get() == 1:
        print("User selected Quick Sort")
    if wantRadixSort.get() == 1:
        print("User selected Radix Sort")
    if wantLinearSort.get() == 1:
        print("User selected Linear Sort")

# create UI window
root = tk.Tk()

# title, name of application
root.title("Sorting Alogrithms Visualization")

# custom font settings
header_font = ("Arial", 14, "bold")
body_font = ("Arial", 12)

# configure input array
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

# select algorithms + UI placement
select_algorithms_label = tk.Label(root, text="Select Algorithms", font=header_font)
select_algorithms_label.grid(row=4, column=0, columnspan=2, sticky="n")

wantBubbleSort = tk.IntVar()
tk.Checkbutton(root, text="Bubble Sort", font=body_font, variable=wantBubbleSort).grid(row=5, column=0, sticky="w")

wantMergeSort = tk.IntVar()
tk.Checkbutton(root, text="Merge Sort", font=body_font, variable=wantMergeSort).grid(row=5, column=1, sticky="w")

wantQuickSort = tk.IntVar()
tk.Checkbutton(root, text="Quick Sort", font=body_font, variable=wantQuickSort).grid(row=5, column=2, sticky="w")

wantRadixSort = tk.IntVar()
tk.Checkbutton(root, text="Radix Sort", font=body_font, variable=wantRadixSort).grid(row=6, column=0, sticky="w")

wantLinearSort = tk.IntVar()
tk.Checkbutton(root, text="Linear Sort", font=body_font, variable=wantLinearSort).grid(row=6, column=1, sticky="w")

# buttons
start_button = tk.Button(root, text="Start", font=body_font, width=20, command=show_results_window)
quit_button = tk.Button(root, text="Quit", font=body_font, width=20, command=root.destroy)

# buttons UI placement
start_button.grid(row=7, column=0, sticky="w")
quit_button.grid(row=7, column=2, sticky="w")


# start application
tk.mainloop()