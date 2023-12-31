import tkinter as tk
from tkinter import font
import requests
import stocks
from PIL import Image, ImageTk

# Create a global variable to store PhotoImage (stops garbage collection)
fakePhoto = None

def create_new_window(parent):
    global fakePhoto # Call global variable

    # Create new window with tkinter
    new_window = tk.Toplevel(parent)
    new_window.title("View Stocks")
    new_window.config(bg="#1e1e1e")
    new_window.geometry("400x300")

    # Specify fonts
    titleFont = font.Font(size=28, weight="bold")
    labelFont = font.Font(size=14, weight="normal")

    # Specify window fonts and create frame for top, then add padding
    title_frame = tk.Frame(new_window)
    home_title = tk.Label(title_frame, text="Your Stocks", font=titleFont, bg="#1e1e1e", fg="#ffffff")
    title_frame.grid(column=0, row=0, padx=25, pady=25)
    home_title.pack()

    # Add fake image to the right
    image_frame = tk.Frame(new_window)
    performance_title = tk.Label(image_frame, text="Overall Performance", font=titleFont, bg="#1e1e1e", fg="#ffffff")
    performance_title.grid(column=0, row=1, padx=25, pady=5)
    image_frame.grid(column=1, row=1, padx=25, pady=25)

    fakeImage = Image.open("overallperformance.png")
    fakePhoto = ImageTk.PhotoImage(fakeImage)

    label = tk.Label(image_frame, image=fakePhoto)
    label.grid(row=0, column=0)

    # Function to handle button click for a specific stock
    def display_stock_info(stock_data):
        # Create a new Tkinter window and set its size
        stock_window = tk.Toplevel(new_window)
        stock_window.config(bg="#1e1e1e")
        stock_window.title("Information for Stock")
        stock_window.geometry("1200x800")

        top_left = tk.Frame(stock_window)
        middle = tk.Frame(stock_window)
        top_right = tk.Frame(stock_window)
        top_left.grid(column=0, row=0, padx=25, pady=25)
        middle.grid(column=1, row=1)
        top_right.grid(column=2, row=0, padx=25, pady=25, sticky=(tk.N, tk.E))

        # Update symbol in stocks python file
        stocks.update_symbol_value(stock_data)

        # Create a title to display stock basics
        stock_title = tk.Label(top_left, text="", font=titleFont, bg="#1e1e1e", fg="#ffffff")
        stock_title.pack()

        stock_price = tk.Label(top_right, text="", font=titleFont, bg="#1e1e1e", fg="#ffffff")
        stock_price.pack()
        stock_recent = tk.Label(top_right, text="", font=labelFont, bg="#1e1e1e", fg="#ffffff")
        stock_recent.pack()

        # Create a label to display stock information
        stock_label = tk.Label(top_left, text="", font=labelFont, bg="#1e1e1e", fg="#ffffff")
        stock_label.pack()

        # Create image for stock and display
        newImage = stocks.create_graph()
        img_label = tk.Label(middle, image=newImage)
        img_label.image = newImage
        img_label.pack()

        # Access the stock data and display it
        symbol = stock_data['ticker']
        price = stock_data['price']

        # Access the stock data and display it
        stock_title.config(text=f"{stock_data['ticker']}")
        stock_price.config(text=f"Current Price: ${stock_data['price']}")
        stock_recent.config(text=f"Change: ${stock_data['change_amount']}")


    # Access the stock data from the imported module
    stock_data_list = stocks.most_actively_traded

    i: int = 0

    button_frame = tk.Frame(new_window)
    button_frame.grid(column=0, row=1, padx=25, pady=25)
    # Create buttons for each stock
    for stock_data in stock_data_list:
        i += 1
        stock_button = tk.Button(button_frame, text=f"{i}. {stock_data['ticker']}", command=lambda s=stock_data: display_stock_info(s), bg="#1e1e1e", fg="ffffff", padx=10, pady=5)
        stock_button.pack()
