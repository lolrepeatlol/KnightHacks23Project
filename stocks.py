import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

api_key = 'LC7Y4XYIT0FTNI6M'

# Define the API endpoint for retrieving most actively traded US stocks
endpointAT = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}'

# Make the API request
responseAT = requests.get(endpointAT)

if responseAT.status_code == 200 :
    data = responseAT.json()
    # Extract and print the list of most actively traded stocks
    most_actively_traded = data.get('most_actively_traded')

    if most_actively_traded is not None:
        for stock in most_actively_traded:
            print("Name: " + stock['ticker'] + ", Price: " + stock['price'], ", Recent Change: $" + stock['change_amount'])
    else:
        print(f"Failed to fetch most actively traded stocks. Status code: {responseAT.status_code}")

symbol = "initial value"

def update_symbol_value(new_value):
    global symbol
    symbol = new_value


def create_graph():
    print(f"{symbol['ticker']}")
    # Create graph for stocks
    endpointGraph = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol['ticker']}&apikey={api_key}"

    responseGraph = requests.get(endpointGraph)
    dataG = responseGraph.json()

    print(dataG)

    time_series = dataG['Weekly Adjusted Time Series']

    # Extracting historical data from JSON response
    dates = []
    closing_prices = []

    for date, values in time_series.items():
        dates.append(date)
        closing_prices.append(float(values['4. close']))

    plt.plot(dates, closing_prices)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(f"Historical Stock Data for {symbol['ticker']}")
    plt.grid(True)

    # Create a Figure and Axes for the plot (same as before)
    fig, ax = plt.subplots()
    ax.plot(dates, closing_prices)
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.set_title(f"Historical Stock Data for {symbol['ticker']} (Weekly)")
    ax.grid(True)

    # Save the plot as an image
    plt.savefig('stock_graph.png')

    # Load the saved image (same as before)
    img = Image.open('stock_graph.png')
    img = ImageTk.PhotoImage(img)

    return img