from tkinter import *
import budgeting
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from tkinter import PhotoImage
import stocks_fe
from PIL import Image, ImageTk

# Create a function to display the pie chart
def show_pie_chart():
    # Sample data for the pie chart
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
    # Sample data for the pie chart
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
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


root = tk.Tk()
root.title("Basic GUI Layout")  # title of the GUI window
root.config(bg="#1e1e1e")  # specify background color
root.title("View Budget")

def open_stocks_viewer():
    stocks_fe.create_new_window(root)

stocks_button = tk.Button(root, text="View Stocks", command=open_stocks_viewer)
stocks_button.pack()

# Create 1st box
checking = Frame(root, width=350, height=150)
checking.place(x= 21, y = 80)
checking.config(bg = "#3e3e42")
customFont = ("Helvetica", 16)
checkingText = tk.Label(root, text="Checking .... 4356", bg="#3e3e42", foreground="white", font=customFont)
checkingText.place(x=21, y=80)
customFont4checkingText1 = ("Helvetica", 30)
checkingText1 = tk.Label(root, text=budgeting.checkingTotal, bg="#3e3e42", foreground="white", font= customFont4checkingText1)
checkingText1.place(x=170, y=150)

# Create 2nd box
spareSum = Frame(root, width=350, height=150)
spareSum.place(x= 21, y = 275)
spareSum.config(bg = "#3e3e42")
spareSumText = tk.Label(root, text="Change Saved This Month", bg="#3e3e42", foreground="white", font=customFont)
spareSumText.place(x=21, y=275)
squareSumText1 = tk.Label(root, text=budgeting.sumOfRoundedUp, bg="#3e3e42", foreground="white", font= customFont4checkingText1)
squareSumText1.place(x=230, y=345)

# Create 3rd box
monthlySpending = Frame(root, width=350, height=150)
monthlySpending.place(x= 21, y = 470)
monthlySpending.config(bg = "#3e3e42")
monthlySpendingText = tk.Label(root, text="Money Spent This Month", bg="#3e3e42", foreground="white", font=customFont)
monthlySpendingText.place(x=21, y= 470)
formatted_float = "{:.2f}".format(budgeting.sumOfTransactionR)
monthlySpendingText1 = tk.Label(root, text=formatted_float, bg="#3e3e42", foreground="white", font= customFont4checkingText1)
monthlySpendingText1.place(x=170, y=540)

# transactions list
transactionList = Frame(root, width = 350, height=900, bg="white")
transactionList.place(x= 420)
transactionList.pack(side="bottom")

# Create a canvas for the scrollable area
canvas = tk.Canvas(transactionList, height=350)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a vertical scrollbar to the canvas
scrollbar = tk.Scrollbar(transactionList, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the list
list_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=list_frame, anchor="nw")

# adding the items in
counterforsomething = 0
for i in budgeting.allOldTransactionFloar: 
    listbox2 = tk.Label(list_frame, text=budgeting.stringArray[counterforsomething], anchor="w")
    listbox2.pack(fill=tk.X, pady=(0, 20), padx=0)
    listbox = tk.Label(list_frame, text=f"{i:.2f}", anchor="w")
    listbox.pack(fill=tk.X, pady=5, padx=310)

    counterforsomething += 1
# Bind the canvas to the frame size
list_frame.bind("<Configure>", on_configure)


# Call pie chart function
show_pie_chart()
show_pie_chartExpected()

#transaction header
transactionListHeader = Frame(root, width= 400, height=50, bg ="#3e3e42")
transactionListHeader.place(x = 440, y = 254)
transactionListHeaderText = tk.Label(root, text="Recent Transactions", bg="#3e3e42", foreground="white", font=customFont)
transactionListHeaderText.place(x=440, y=254)

# Load the image
image = PhotoImage(file="Untitled.png")
new_width = image.width() // 2
new_height = image.height()
resized_image = image.subsample(5,5)
transactionList.config(width=100, height=1500)

# Create a label to display the image
label = tk.Label(root, image=resized_image)
label.place(x= 1050, y=500) 





root.mainloop()
