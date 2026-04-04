import time
import yfinance as yf
import streamlit as st
import requests

#titulo da pagina

st.set_page_config(page_title="Top 10 Empresas", layout="wide", page_icon="📈")

st.title("10 Maiores Empresas do Mundo")
st.write("por valor de mercado - preços aproximados em USD")





# siglas das empresas
empresas = ["NVDA","AAPL","GOOGL","MSFT","AMZN","TSM","2222.SR","AVGO","META","TSLA",
    "BRK-B","WMT","LLY","JPM","XOM","V","JNJ","MA","COST","ORCL"]

# função para pegar a taxa de câmbio
def get_taxa_cambio(moeda):
    if moeda == "USD":
        return 1.0
    else:
        url = "https://v6.exchangerate-api.com/v6/e31352a229eabff366b77b76/latest/USD"
        taxa = requests.get(url)
        taxa = taxa.json()
        taxa = taxa["conversion_rates"].get(moeda)
        return taxa or 1.0  # fallback para 1.0 caso a moeda não seja encontrada





# função para formatar os valores
def formatar_valor(valor):
    if valor >= 1e12:
        return f"{valor / 1e12:.2f} tri"
    elif valor >= 1e9: 
        return f"{valor / 1e9:.2f} bi"
    elif valor >= 1e6:
        return f"{valor / 1e6:.2f} mi"
    else:
        return f"{valor:.0f}"



# função pra pegar dados
@st.cache_data
def get_info(empresa):
    stock = yf.Ticker(empresa)
    informacao = stock.info
    
    nome = informacao.get('displayName') or informacao.get('shortName') or informacao.get("longName") or empresa # fallback para o nome da empresa caso displayName ou shortName sejam None

    # normaliza nomes que queremos substituir manualmente
    apelidos = {
        "Amazon.com": "Amazon",
        "Alphabet Inc.": "Google",
        "Meta Platforms": "Meta",
        "Saudi Arabian Oil Co.":"saudiaramco",
        "berkshire hathaway":"berkshirehathaway",
        "Taiwan Semiconductor Manufacturing Company":"TSMC"       
    }
    nome = apelidos.get(nome, nome)

    seguimento = informacao.get('industry')
    valorCota = informacao.get('currentPrice')
    valorMercado = informacao.get('marketCap') or 0 #as vezes o valor de mercado pode ser None, então usamos 0 como fallback
    site = informacao.get("website")  # ex: https://www.apple.com
    moeda = informacao.get("currency")  # ex: USD, SAR, etc



    taxa = get_taxa_cambio(moeda)
    if moeda != "USD" and taxa:
        valorMercado = valorMercado / taxa  # Converte para USD
        valorCota = valorCota / taxa  # Se quiser converter também
    return nome, seguimento, valorCota, valorMercado, site, moeda


data = []

# percorre empresas
for empresa in empresas:
    nome, seguimento, valorCota, valorMercado, site, moeda = get_info(empresa)
    
    data.append({
        "empresa": empresa,
        "nome": nome,
        "seguimento": seguimento,
        "valorCota": valorCota,
        "valorMercado": valorMercado,
        "site": site
    })

# 🔥 ordena pelo valor de mercado (maior primeiro)
ranking = sorted(data, key=lambda x: x["valorMercado"], reverse=True)

# top 10
top_10 = ranking[:10]



st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>1º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[0][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[0][ "nome" ]}</h2>
                <h2>{top_10[0]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[0]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)



st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>2º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[1][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[1][ "nome" ]}</h2>
                <h2>{top_10[1]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[1]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)



st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>3º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[2][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[2][ "nome" ]}</h2>
                <h2>{top_10[2]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[2]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>4º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[3][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[3][ "nome" ]}</h2>
                <h2>{top_10[3]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[3]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>5º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[4][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[4][ "nome" ]}</h2>
                <h2>{top_10[4]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[4]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>6º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[5][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[5][ "nome" ]}</h2>
                <h2>{top_10[5]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[5]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>7º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[6][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[6][ "nome" ]}</h2>
                <h2>{top_10[6]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[6]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)



st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>8º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[7][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[7][ "nome" ]}</h2>
                <h2>{top_10[7]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[7]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>9º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[8][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[8][ "nome" ]}</h2>
                <h2>{top_10[8]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[8]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div style=" border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1); diplay:flex; justify-content:space-between;">
            <h1>10º Lugar</h1>
            <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="https://img.logo.dev/{top_10[9][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                <h2>{top_10[9][ "nome" ]}</h2>
                <h2>{top_10[9]["valorCota"]}</h2>
                <h2>{f"${formatar_valor(top_10[9]["valorMercado"])}"}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)





# COLA
#f"{valor:.2f}"
# nome = displayName
# seguimento = industry
# valor da cota = pricing -> currentPrice
# valor de mercado = marketData -> marketCap

