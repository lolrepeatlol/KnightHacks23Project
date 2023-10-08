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

    # Update symbol in stocks python file
    stocks.update_symbol_value(stock_data)

    # Create a label to display stock information
    stock_label = tk.Label(stock_window, text="")
    stock_label.pack()

    latest_dte = stocks.dTECalc()

    # Access the stock data and display it
    stock_label.config(text=f"Symbol: {stock_data['ticker']}\nPrice: {stock_data['price']}, DtE: {latest_dte}\n")


# def update_backend_variable(stock_data):


# Access the stock data from the imported module
stock_data_list = stocks.most_actively_traded

# Create buttons for each stock
for stock_data in stock_data_list:
    stock_button = tk.Button(root, text=stock_data['ticker'], command=lambda s=stock_data: display_stock_info(s))
    stock_button.pack()

# Start Tkinter main loop
root.mainloop()
