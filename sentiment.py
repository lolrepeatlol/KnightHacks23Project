import sys 
sys.path.append('C:\\Users\\noah\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages')
import requests

def get_sentiment(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Main program
if __name__ == "__main__":
    symbol = input("Enter a stock symbol: ")

    # Fetch balance sheet data for the stock symbol
    api_data = get_sentiment(symbol, 'OAYEJAYM39RAB0ZN')
    print(api_data)