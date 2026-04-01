import requests
import yfinance as yf

#siglas das empresas
empresas = ['NVDA', 'AAPL', 'GOOG', 'MSFT', 'AMZN']


data = []

for empresa in empresas:
    stock = yf.Ticker(empresa)
    informacao = stock.info
    nome = informacao['displayName']
    seguimento = informacao['industry']
    valorCota = informacao['currentPrice']
    valorMercado = informacao['marketCap']

    print(f"A empresa {nome} que atua no seguimento de {seguimento} fechou o dia com a cota a {valorCota} e seu valor de mercado é de {valorMercado}")
    print("-" * 40)






#f"{valor:.2f}"

# nome = displayName
# seguimento = industry
# valor da cota = pricing -> currentPrice
# valor de mercado = marketData -> marketCap

