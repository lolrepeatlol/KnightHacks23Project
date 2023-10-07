import requests

api_key = 'apikey'

# Define the API endpoint for retrieving most actively traded US stocks
endpointAT = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}'

# Make the API request
responseAT = requests.get(endpointAT)

if responseAT.status_code == 200 :
    data = responseAT.json()
    # Extract and print the list of most actively traded stocks
    most_actively_traded = data.get('most_actively_traded')
    for stock in most_actively_traded:
        print("Name: " + stock['ticker'] + ", Price: " + stock['price'], ", Recent Change: " + stock['change_amount'])
else:
    print(f"Failed to fetch most actively traded stocks. Status code: {responseAT.status_code}")