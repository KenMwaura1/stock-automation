import pandas as pd
import requests

def getdata(stock):
    # Company get group of items
    company_quote = requests.get(f"https:financialmodelingprep.com/v3/quote/{stock}")