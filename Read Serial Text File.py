import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import os
import mplcursors

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Scale Plotter")

# Set the size of the window
root.geometry("350x150")

# Define a function to handle the file selection
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as f:
            x = []
            y = []
            max_y = float('-inf')  # initialize max_y to negative infinity
            for line in f:
                # Split the line into date, data, and number
                date, data, number, _ = line.strip().split(',')
                 # Append the data and number to the x and y lists
                x.append(float(number))
                y.append(float(data))
                # Update max_y if necessary
                max_y = max(max_y, float(data))
            # Display the max_y on the GUI
            max_y_label.config(text=f"Highest data point: {max_y}")
            # Create the plot
            filename = os.path.basename(file_path).replace(".txt", "")  # get the filename without the .txt extension
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_xlabel("Number")
            ax.set_ylabel("Data")
            ax.set_title(filename)  # set the title of the graph to the filename
            ax.grid(True)  # add a grid to the plot
            # Add a label to the highest data point
            max_index = y.index(max_y)
            ax.annotate(f"Highest data point: {max_y}", xy=(x[max_index], max_y), xytext=(x[max_index] + 5, max_y + 0), arrowprops=dict(facecolor='black', shrink=0.05))
            # Use mplcursors to display the x-value of the data point that the cursor is hovering over
            cursor = mplcursors.cursor(ax, hover=True)
            cursor.connect("add", lambda sel: sel.annotation.set_text(f"y={y[int(sel.target.index)]}"))
            plt.show()

# Create a label to display the highest data point
max_y_label = tk.Label(root, text="")
max_y_label.pack(pady=10)

# Create a button to open the file dialog
button = tk.Button(root, text="Open File", command=open_file)
button.pack(pady=20)

# Start the main event loop
root.mainloop()