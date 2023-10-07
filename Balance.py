import sys 
sys.path.append('C:\\Users\\noah\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages')
import requests

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

def get_balance_sheet(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

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


# Main program
if __name__ == "__main__":
    # Create an empty list to store balance sheet report instances
    balance_sheet_reports = []

    # Sentinel value to stop entering stocks
    sentinel = "quit"

    
    symbol = input("Enter a stock symbol: ")

    # Fetch balance sheet data for the stock symbol
    api_data = get_balance_sheet(symbol, 'YOUR_API_KEY')

    # Create instances of BalanceSheetReport and append them to the list
    reports = create_balance_sheet_reports(api_data)
    balance_sheet_reports.extend(reports)


# Access attributes of a specific report (for example, the first report)
if (balance_sheet_reports):
    report2022 = balance_sheet_reports[0]
    report2021 = balance_sheet_reports[1]
    report2019 = balance_sheet_reports[2] 
    report2018 = balance_sheet_reports[3]
