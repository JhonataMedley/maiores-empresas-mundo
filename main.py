import requests
import yfinance as yf
import streamlit as st

#titulo da pagina
st.title("A gigantes empresas")


#siglas das empresas
empresas = ['NVDA', 'TSLA']


data = []

for empresa in empresas:

    caixa = st.container()


    stock = yf.Ticker(empresa)
    informacao = stock.info
    nome = informacao['displayName']
    seguimento = informacao['industry']
    valorCota = informacao['currentPrice']
    valorMercado = informacao['marketCap']
    


    caixa.write(f"A empresa {nome} que atua no seguimento de {seguimento} fechou o dia com a cota a {valorCota:.2f} e seu valor de mercado é de {valorMercado:.2f}")
    caixa.write("--------------------------------------------------")
    caixa.space("large")





#f"{valor:.2f}"

# nome = displayName
# seguimento = industry
# valor da cota = pricing -> currentPrice
# valor de mercado = marketData -> marketCap

