import time
import yfinance as yf
import streamlit as st

#titulo da pagina

st.set_page_config(page_title="Top 10 Empresas", layout="wide", page_icon="📈")

st.title("10 Maiores Empresas do Mundo")
st.write("por valor de mercado - preços aproximados em USD")





# siglas das empresas
empresas = [    "NVDA","AAPL","GOOGL","MSFT","AMZN","TSM","2222.SR","AVGO","META","TSLA",
    "BRK-B","WMT","LLY","JPM","XOM","V","JNJ","MA","COST","ORCL"]

# função pra pegar dados
@st.cache_data
def get_info(empresa):
    stock = yf.Ticker(empresa)
    informacao = stock.info
    
    nome = informacao.get('displayName') or informacao.get('shortName') or informacao.get("longName") or empresa # fallback para o nome da empresa caso displayName ou shortName sejam None
    seguimento = informacao.get('industry')
    valorCota = informacao.get('currentPrice')
    valorMercado = informacao.get('marketCap') or 0 #as vezes o valor de mercado pode ser None, então usamos 0 como fallback
    site = informacao.get("website")  # ex: https://www.apple.com

    return nome, seguimento, valorCota, valorMercado, site


data = []

# percorre empresas
for empresa in empresas:
    nome, seguimento, valorCota, valorMercado, site = get_info(empresa)
    
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
                <h2>{top_10[0]["valorMercado"]}</h2>
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
                <h2>{top_10[1]["valorMercado"]}</h2>
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
                <h2>{top_10[2]["valorMercado"]}</h2>
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
                <h2>{top_10[3]["valorMercado"]}</h2>
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
                <h2>{top_10[4]["valorMercado"]}</h2>
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
                <h2>{top_10[5]["valorMercado"]}</h2>
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
                <h2>{top_10[6]["valorMercado"]}</h2>
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
                <h2>{top_10[7]["valorMercado"]}</h2>
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
                <h2>{top_10[8]["valorMercado"]}</h2>
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
                <h2>{top_10[9]["valorMercado"]}</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)





# COLA
#f"{valor:.2f}"
# nome = displayName
# seguimento = industry
# valor da cota = pricing -> currentPrice
# valor de mercado = marketData -> marketCap

