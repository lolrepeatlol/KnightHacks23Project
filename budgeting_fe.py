from tkinter import *
import budgeting
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Create a function to display the pie chart
def show_pie_chart():
    # Sample data for the pie chart (you can replace this with your data)
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [random.randint(1, 10) for _ in categories]

    # Create a Matplotlib Figure and a subplot for the pie chart
    fig = Figure(figsize=(3, 3), dpi=80)
    subplot = fig.add_subplot(111)
    


    # Create the pie chart using Matplotlib
    subplot.pie(values, autopct='%1.1f%%', startangle=90)
    subplot.set_facecolor('black')
    fig.patch.set_facecolor('#1e1e1e')

    # Create a Tkinter canvas to display the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x= 500, y = 0)

def show_pie_chartExpected():
    # Sample data for the pie chart (you can replace this with your data)
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [random.randint(1, 10) for _ in categories]

    # Create a Matplotlib Figure and a subplot for the pie chart
    fig = Figure(figsize=(3, 3), dpi=80)
    subplot = fig.add_subplot(111)
    


    # Create the pie chart using Matplotlib
    subplot.pie(values, autopct='%1.1f%%', startangle=90)
    subplot.set_facecolor('black')
    fig.patch.set_facecolor('#1e1e1e')

    # Create a Tkinter canvas to display the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x= 800, y = 0)
    
    
root = tk.Tk()
root.title("Basic GUI Layout")  # title of the GUI window
root.config(bg="#1e1e1e")  # specify background color

# Create Name box
'''appName = Frame(root, width=250, height=80)
appName.grid(row=0, column=0, padx=0, pady=0)
appName.config(bg = "#3e3e42")'''

# Create 1st box
checking = Frame(root, width=350, height=150)
checking.place(x= 21, y = 80)
checking.config(bg = "#3e3e42")
# Create 2nd box
spareSum = Frame(root, width=350, height=150)
spareSum.place(x= 21, y = 275)
spareSum.config(bg = "#3e3e42")
# Create 3rd box
monthlySpending = Frame(root, width=350, height=150)
monthlySpending.place(x= 21, y = 470)
monthlySpending.config(bg = "#3e3e42")
# transactions list
transactionList = Frame(root, width = 350, height=400)
transactionList.place(x= 420)
transactionList.pack(side="bottom")
show_pie_chart()
show_pie_chartExpected()
text_widget = tk.Text(root, width=30, height=10)
text_widget.insert(tk.END, "This is a Text widget.\nYou can add and edit text here.")
# Pack or place the Text widget in the window
text_widget.place()

"""
# Create Label widgets
label1 = tk.Label(root, text="Label 1", bg="#3e3e42")
label2 = tk.Label(root, text="Label 2", bg="#3e3e42")
label3 = tk.Label(root, text="Label 3", bg="#3e3e42")
label1.config(width=100, height=5)
# label2.config(width=350, height=150)
# label3.config(width=350, height=150)
# Pack the labels vertically (stacked)
label1.pack()
label2.pack()
label3.pack()
"""


root.mainloop()
