import tkinter as tk
import stocks

# Create the main Tkinter window
root = tk.Tk()
root.title("View Stocks")
root.config(bg="#1e1e1e")

# Function to handle button click for a specific stock
def display_stock_info(stock_data):
    # Create a new Tkinter window
    stock_window = tk.Toplevel(root)
    stock_window.title("Information for Stock")

    # Create a label to display stock information
    stock_label = tk.Label(stock_window, text="", bg="3e3e43")
    stock_label.pack()

    # Access the stock data and display it
    stock_label.config(text=f"Symbol: {stock_data['ticker']}\nPrice: {stock_data['price']}")

    stocks.symbol = stock_data


# Access the stock data from the imported module
stock_data_list = stocks.most_actively_traded

# Create buttons for each stock
for stock_data in stock_data_list:
    stock_button = tk.Button(root, text=stock_data['ticker'], command=lambda s=stock_data: display_stock_info(s))
    stock_button.pack()

# Start Tkinter main loop
root.mainloop()
