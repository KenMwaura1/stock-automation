import pandas as pd
import requests

def getdata(stock):
    # Company get group of items
    company_quote = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{stock}")
    company_quote = company_quote.json()
    share_price = float("{0:.2f}".format(company_quote[0]['price']))
    # Balance Sheet group of items
    BS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{stock}?period=quarter")
    BS = BS.json()
    print(company_quote, share_price, BS)

    # Get Total Company debt
    debt = float("{0:.2f}".format(float(BS['financials'][0]['Total debt'])/10**9))

    #Get Total Cash
    cash = float("{0:.2f}".format(float(BS['financials'][0]['Cash and short-term investments'])/10**9))

    # Income Statement Group of Items
    IS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock}?period=quarter")
    IS = IS.json()

    #Most Recent Quarterly revenue
    qRev = float("{0:.2f}".format(float(IS['financials'][0]['Revenue'])/10**9))

    #Company Profile Group of items
    company_info = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{stock}")
    company_info = company_info.json()

    #CEO
    ceo = company_info['profile']['ceo']

    print(share_price, cash, debt, qRev, ceo)
    return (share_price, cash, debt, qRev, ceo)
   

getdata('MSFT')

