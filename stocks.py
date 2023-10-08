import requests

api_key = '25KI283QX1PSWXXC'

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

endpointAT2 = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&apikey={api_key}'

responseAT2 = requests.get(endpointAT2)

if responseAT2.status_code == 200 :
    data2 = responseAT2.json()
    annualReports = data2.get('annualReports')



#create balance sheet class
class BalanceSheetReport:
    def __init__(self, fiscal_date, reported_currency, total_assets, total_current_assets,
                 cash_and_cash_equivalents_at_carrying_value, cash_and_short_term_investments, inventory,
                 current_net_receivables, total_non_current_assets, property_plant_equipment,
                 accumulated_depreciation_amortization_ppe, intangible_assets, intangible_assets_excluding_goodwill,
                 goodwill, investments, long_term_investments, short_term_investments, other_current_assets,
                 other_non_current_assets, total_liabilities, total_current_liabilities, current_accounts_payable,
                 deferred_revenue, current_debt, short_term_debt, total_non_current_liabilities, capital_lease_obligations,
                 long_term_debt, current_long_term_debt, long_term_debt_non_current, short_long_term_debt_total,
                 other_current_liabilities, other_non_current_liabilities, total_shareholder_equity, treasury_stock,
                 retained_earnings, common_stock, common_stock_shares_outstanding):
        self.fiscal_date = fiscal_date
        self.reported_currency = reported_currency
        self.total_assets = total_assets
        self.total_current_assets = total_current_assets
        self.cash_and_cash_equivalents_at_carrying_value = cash_and_cash_equivalents_at_carrying_value
        self.cash_and_short_term_investments = cash_and_short_term_investments
        self.inventory = inventory
        self.current_net_receivables = current_net_receivables
        self.total_non_current_assets = total_non_current_assets
        self.property_plant_equipment = property_plant_equipment
        self.accumulated_depreciation_amortization_ppe = accumulated_depreciation_amortization_ppe
        self.intangible_assets = intangible_assets
        self.intangible_assets_excluding_goodwill = intangible_assets_excluding_goodwill
        self.goodwill = goodwill
        self.investments = investments
        self.long_term_investments = long_term_investments
        self.short_term_investments = short_term_investments
        self.other_current_assets = other_current_assets
        self.other_non_current_assets = other_non_current_assets
        self.total_liabilities = total_liabilities
        self.total_current_liabilities = total_current_liabilities
        self.current_accounts_payable = current_accounts_payable
        self.deferred_revenue = deferred_revenue
        self.current_debt = current_debt
        self.short_term_debt = short_term_debt
        self.total_non_current_liabilities = total_non_current_liabilities
        self.capital_lease_obligations = capital_lease_obligations
        self.long_term_debt = long_term_debt
        self.current_long_term_debt = current_long_term_debt
        self.long_term_debt_non_current = long_term_debt_non_current
        self.short_long_term_debt_total = short_long_term_debt_total
        self.other_current_liabilities = other_current_liabilities
        self.other_non_current_liabilities = other_non_current_liabilities
        self.total_shareholder_equity = total_shareholder_equity
        self.treasury_stock = treasury_stock
        self.retained_earnings = retained_earnings
        self.common_stock = common_stock
        self.common_stock_shares_outstanding = common_stock_shares_outstanding

#create income sheet report
class IncomeSheetReport:
    def __init__(self, fiscal_date, reported_currency, gross_profit, total_revenue, cost_of_revenue,
                 cost_of_goods_and_services_sold, operating_income, selling_general_and_administrative,
                 research_and_development, operating_expenses, investment_income_net, net_interest_income,
                 interest_income, interest_expense, non_interest_income, other_non_operating_income,
                 depreciation, depreciation_and_amortization, income_before_tax, income_tax_expense,
                 interest_and_debt_expense, net_income_from_continuing_operations,
                 comprehensive_income_net_of_tax, ebit, ebitda, net_income):
        self.fiscal_date_ending = fiscal_date
        self.reported_currency = reported_currency
        self.gross_profit = gross_profit
        self.total_revenue = total_revenue
        self.cost_of_revenue = cost_of_revenue
        self.cost_of_goods_and_services_sold = cost_of_goods_and_services_sold
        self.operating_income = operating_income
        self.selling_general_and_administrative = selling_general_and_administrative
        self.research_and_development = research_and_development
        self.operating_expenses = operating_expenses
        self.investment_income_net = investment_income_net
        self.net_interest_income = net_interest_income
        self.interest_income = interest_income
        self.interest_expense = interest_expense
        self.non_interest_income = non_interest_income
        self.other_non_operating_income = other_non_operating_income
        self.depreciation = depreciation
        self.depreciation_and_amortization = depreciation_and_amortization
        self.income_before_tax = income_before_tax
        self.income_tax_expense = income_tax_expense
        self.interest_and_debt_expense = interest_and_debt_expense
        self.net_income_from_continuing_operations = net_income_from_continuing_operations
        self.comprehensive_income_net_of_tax = comprehensive_income_net_of_tax
        self.ebit = ebit
        self.ebitda = ebitda
        self.net_income = net_income

class StockQuote:
    def __init__(self, symbol, open_price, high_price, low_price, current_price, volume, latest_trading_day, previous_close, price_change, percent_change):
        self.symbol = symbol
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.current_price = current_price
        self.volume = volume
        self.latest_trading_day = latest_trading_day
        self.previous_close = previous_close
        self.price_change = price_change
        self.percent_change = percent_change

def get_balance_sheet(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_stock_quote(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data


def get_income_sheet(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def create_income_sheet_reports(api_data):
    reports = []
    if 'annualReports' in api_data:
        annual_reports = api_data['annualReports']
        for report_data in annual_reports:
            report = IncomeSheetReport(
                fiscal_date=report_data.get('fiscalDateEnding', 'N/A'),
                reported_currency=report_data.get('reportedCurrency', 'N/A'),
                gross_profit=report_data.get('grossProfit', 'N/A'),
                total_revenue=report_data.get('totalRevenue', 'N/A'),
                cost_of_revenue=report_data.get('costOfRevenue', 'N/A'),
                cost_of_goods_and_services_sold=report_data.get('costofGoodsAndServicesSold', 'N/A'),
                operating_income=report_data.get('operatingIncome', 'N/A'),
                selling_general_and_administrative=report_data.get('sellingGeneralAndAdministrative', 'N/A'),
                research_and_development=report_data.get('researchAndDevelopment', 'N/A'),
                operating_expenses=report_data.get('operatingExpenses', 'N/A'),
                investment_income_net=report_data.get('investmentIncomeNet', 'N/A'),
                net_interest_income=report_data.get('netInterestIncome', 'N/A'),
                interest_income=report_data.get('interestIncome', 'N/A'),
                interest_expense=report_data.get('interestExpense', 'N/A'),
                non_interest_income=report_data.get('nonInterestIncome', 'N/A'),
                other_non_operating_income=report_data.get('otherNonOperatingIncome', 'N/A'),
                depreciation=report_data.get('depreciation', 'N/A'),
                depreciation_and_amortization=report_data.get('depreciationAndAmortization', 'N/A'),
                income_before_tax=report_data.get('incomeBeforeTax', 'N/A'),
                income_tax_expense=report_data.get('incomeTaxExpense', 'N/A'),
                interest_and_debt_expense=report_data.get('interestAndDebtExpense', 'N/A'),
                net_income_from_continuing_operations=report_data.get('netIncomeFromContinuingOperations', 'N/A'),
                comprehensive_income_net_of_tax=report_data.get('comprehensiveIncomeNetOfTax', 'N/A'),
                ebit=report_data.get('ebit', 'N/A'),
                ebitda=report_data.get('ebitda', 'N/A'),
                net_income=report_data.get('netIncome', 'N/A')
            )
            reports.append(report)

    return reports

def create_balance_sheet_reports(api_data):
    reports = []

    if 'annualReports' in api_data:
        annual_reports = api_data['annualReports']
        for report_data in annual_reports:
            report = BalanceSheetReport(
                fiscal_date=report_data.get('fiscalDateEnding', 'N/A'),
                reported_currency=report_data.get('reportedCurrency', 'N/A'),
                total_assets=report_data.get('totalAssets', 'N/A'),
                total_current_assets=report_data.get('totalCurrentAssets', 'N/A'),
                cash_and_cash_equivalents_at_carrying_value=report_data.get('cashAndCashEquivalentsAtCarryingValue', 'N/A'),
                cash_and_short_term_investments=report_data.get('cashAndShortTermInvestments', 'N/A'),
                inventory=report_data.get('inventory', 'N/A'),
                current_net_receivables=report_data.get('currentNetReceivables', 'N/A'),
                total_non_current_assets=report_data.get('totalNonCurrentAssets', 'N/A'),
                property_plant_equipment=report_data.get('propertyPlantEquipment', 'N/A'),
                accumulated_depreciation_amortization_ppe=report_data.get('accumulatedDepreciationAmortizationPPE', 'N/A'),
                intangible_assets=report_data.get('intangibleAssets', 'N/A'),
                intangible_assets_excluding_goodwill=report_data.get('intangibleAssetsExcludingGoodwill', 'N/A'),
                goodwill=report_data.get('goodwill', 'N/A'),
                investments=report_data.get('investments', 'N/A'),
                long_term_investments=report_data.get('longTermInvestments', 'N/A'),
                short_term_investments=report_data.get('shortTermInvestments', 'N/A'),
                other_current_assets=report_data.get('otherCurrentAssets', 'N/A'),
                other_non_current_assets=report_data.get('otherNonCurrentAssets', 'N/A'),
                total_liabilities=report_data.get('totalLiabilities', 'N/A'),
                total_current_liabilities=report_data.get('totalCurrentLiabilities', 'N/A'),
                current_accounts_payable=report_data.get('currentAccountsPayable', 'N/A'),
                deferred_revenue=report_data.get('deferredRevenue', 'N/A'),
                current_debt=report_data.get('currentDebt', 'N/A'),
                short_term_debt=report_data.get('shortTermDebt', 'N/A'),
                total_non_current_liabilities=report_data.get('totalNonCurrentLiabilities', 'N/A'),
                capital_lease_obligations=report_data.get('capitalLeaseObligations', 'N/A'),
                long_term_debt=report_data.get('longTermDebt', 'N/A'),
                current_long_term_debt=report_data.get('currentLongTermDebt', 'N/A'),
                long_term_debt_non_current=report_data.get('longTermDebtNoncurrent', 'N/A'),
                short_long_term_debt_total=report_data.get('shortLongTermDebtTotal', 'N/A'),
                other_current_liabilities=report_data.get('otherCurrentLiabilities', 'N/A'),
                other_non_current_liabilities=report_data.get('otherNonCurrentLiabilities', 'N/A'),
                total_shareholder_equity=report_data.get('totalShareholderEquity', 'N/A'),
                treasury_stock=report_data.get('treasuryStock', 'N/A'),
                retained_earnings=report_data.get('retainedEarnings', 'N/A'),
                common_stock=report_data.get('commonStock', 'N/A'),
                common_stock_shares_outstanding=report_data.get('commonStockSharesOutstanding', 'N/A')
            )
            reports.append(report)

    return reports

def create_stock_quote(api_data):
    quotes = []

    if 'Global Quote' in api_data:
        global_quote = api_data['Global Quote']
        quote = StockQuote(
            symbol=global_quote.get('01. symbol', 'N/A'),
            open_price=global_quote.get('02. open', 'N/A'),
            high_price=global_quote.get('03. high', 'N/A'),
            low_price=global_quote.get('04. low', 'N/A'),
            current_price=global_quote.get('05. price', 'N/A'),
            volume=global_quote.get('06. volume', 'N/A'),
            latest_trading_day=global_quote.get('07. latest trading day', 'N/A'),
            previous_close=global_quote.get('08. previous close', 'N/A'),
            price_change=global_quote.get('09. change', 'N/A'),
            percent_change=global_quote.get('10. change percent', 'N/A')
        )
        quotes.append(quote)

    return quotes

# Create an empty list to store balance sheet report instances
balance_sheet_reports = []

#create list to store income sheet report instances
income_sheet_reports = []

#create list to store stock quotes
stock_quotes = []


symbol = "initial value" # if we would do CLI input

def update_symbol_value(new_value):
    global symbol
    symbol = new_value

# Fetch balance sheet data for the stock symbol
api_balance = get_balance_sheet(symbol, api_key)
api_income = get_income_sheet(symbol, api_key)
api_stock_quote = get_stock_quote(symbol, api_key)


#Create instances of BalanceSheetReport and append them to the list
balance_reports = create_balance_sheet_reports(api_balance)
balance_sheet_reports.extend(balance_reports)
income_reports = create_income_sheet_reports(api_income)
income_sheet_reports.extend(income_reports)
quotes = create_stock_quote(api_stock_quote)
stock_quotes.extend(quotes)


'''

# Access attributes of a specific report (for example, the first report)

if (balance_sheet_reports):
    report2022 = balance_sheet_reports[0]
    report2021 = balance_sheet_reports[1]
    report2019 = balance_sheet_reports[2] 
    report2018 = balance_sheet_reports[3]
'''

#metrics

#Rank 1: Is it ran well

#debt-to-equity
debt_to_equity = []

for i in range(len(balance_sheet_reports)):
    if i < len(balance_sheet_reports):
        # Convert the string values to floats before subtraction
        total_assets = float(balance_sheet_reports[i].total_assets)
        total_liabilities = float(balance_sheet_reports[i].total_liabilities)

        # Calculate debt to equity ratio
        debt_to_equity_ratio = total_assets / total_liabilities

        # Append the result to the list
        debt_to_equity.append(debt_to_equity_ratio)

        print(f"Debt to Equity for {balance_sheet_reports[i].fiscal_date}: {debt_to_equity_ratio}")
        '''
        Ideal current ratio: > 1.5; “$1.5 received in cash every time debt of $1 must be paid within twelve months.” (range: 1.5 – 2.5) 
        Goal: company receives more in cash than it pays in debt 
        Ratio of < 1; “company acquires new debt to pay off existing debt obligation 
        Ratio > 2.5; extremely high liquidity; “inability to collect payment from vendors” * 
        '''
    else:
        print("unable to fetch")


#High current ratio
high_current_ratios = []
for i in range(len(balance_sheet_reports)):
    if i < len(balance_sheet_reports):
        total_current_asset = float(balance_sheet_reports[i].total_current_assets)
        total_current_liability = float(balance_sheet_reports[i].total_current_liabilities)

        #calculate high current ratio
        high_current = total_current_asset / total_current_liability

        high_current_ratios.append(high_current)

        print(f"High current ratio for {balance_sheet_reports[i].fiscal_date}: {high_current}")
        '''
        Ideal current ratio: > 1.5; “$1.5 received in cash every time debt of $1 must be paid within twelve months.” (range: 1.5 – 2.5) 
        Goal: company receives more in cash than it pays in debt 
        Ratio of < 1; “company acquires new debt to pay off existing debt obligation 
        Ratio > 2.5; extremely high liquidity; “inability to collect payment from vendors” * 
        '''
    else:
        print("unable to fetch")

''' 
#return on equity 
return_on_equity = []

for i in range(len(balance_sheet_reports)):
    for j in range(len(income_sheet_reports)):
        # Check if both i and j are within valid indices
        if i < len(balance_sheet_reports) and j < len(income_sheet_reports):
            net_income = float(income_sheet_reports[j].net_income) 
            shareholder_equity = float(balance_sheet_reports[i].total_shareholder_equity)

            roe = net_income / shareholder_equity

            return_on_equity.append(roe)

            print(f"Return on equity for balance_sheet_reports[{i}] and income_sheet_reports[{j}]: {roe}")
            
            Ideal ROE: consistent ROE > 8% or steadily increasing over span of 10 years 
            When ROE declines: company isn’t earning higher income when earnings are retained/reinvested 
            Evaluate D/E first, then ROE; companies with low D/E don’t have as high ROEs but they are often more sustainable 
            
'''
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
    plt.title(f'Historical Stock Data for {symbol}')
    plt.grid(True)

    # Create a Figure and Axes for the plot (same as before)
    fig, ax = plt.subplots()
    ax.plot(dates, closing_prices)
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.set_title(f'Historical Stock Data for {symbol}')
    ax.grid(True)

    # Save the plot as an image
    plt.savefig('stock_graph.png')

    # Load the saved image (same as before)
    img = Image.open('stock_graph.png')
    img = ImageTk.PhotoImage(img)

    return img