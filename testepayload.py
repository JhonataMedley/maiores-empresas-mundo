import yfinance as yf
import json

empresa = "2222.SR"
stock = yf.Ticker(empresa)
info = stock.info
print(json.dumps(info, indent=4))