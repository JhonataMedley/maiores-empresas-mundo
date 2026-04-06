import time
import yfinance as yf
import streamlit as st
import requests
import datetime
import locale

#titulo da pagina
st.set_page_config(page_title="Top 10 Empresas", layout="wide", page_icon="📈")


# Atualiza data mes e ano atuomaticamente
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')  # fallback para Windows

now = datetime.datetime.now()
month = now.strftime("%B")




# Carrega o CSS personalizado
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()



# Título centralizado (arruma isso no css depois)
st.markdown(f"""
    <div style="text-align: center;">
        <h2 style = "font-size: 30px; color: rgb(128, 0, 255)">RANKING GLOBAL - {month.upper()} {now.year}</h2>
        <h1 style = "font-size: 75px;">10 Maiores Empresas do Mundo</h1>
        <p style = "font-size: 25px;">por valor de mercado - preços aproximados em USD</p>
    </div>            



            """, unsafe_allow_html=True)





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
    codigo = informacao.get("symbol")  # ex: AAPL, 2222.SR, etc
    pais = informacao.get("country")  # ex: United States, Saudi Arabia, etc


    taxa = get_taxa_cambio(moeda)
    if moeda != "USD" and taxa:
        valorMercado = valorMercado / taxa  # Converte para USD
        valorCota = valorCota / taxa  # Se quiser converter também
    return nome, seguimento, valorCota, valorMercado, site, moeda, codigo, pais


data = []

# percorre empresas
for empresa in empresas:
    nome, seguimento, valorCota, valorMercado, site, moeda, codigo, pais = get_info(empresa)
    
    data.append({
        "empresa": empresa,
        "nome": nome,
        "seguimento": seguimento,
        "valorCota": valorCota,
        "valorMercado": valorMercado,
        "site": site,
        "moeda": moeda,
        "codigo": codigo,
        "pais": pais

    })

# ordena pelo valor de mercado (maior primeiro)
ranking = sorted(data, key=lambda x: x["valorMercado"], reverse=True)

# top 10
top_10 = ranking[:10]


# a alteração vai ser a seguinte orderm
# Ranking encima junto com o nome
# abaixo o logo e ao lado superior o codigo e abaixo do codigo
#teremos o seguimento e pais




st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>1º Lugar - {top_10[0]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[0][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[0][ "codigo" ]}</h3>
                        <p>{top_10[0]["seguimento"]}</p>
                        <p>{top_10[0]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>${top_10[0]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>${formatar_valor(top_10[0]["valorMercado"])}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>2º Lugar - {top_10[1]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[1][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[1][ "codigo" ]}</h3>
                        <p>{top_10[1]["seguimento"]}</p>
                        <p>{top_10[1]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[1]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[1]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)







st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>3º Lugar - {top_10[2]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[2][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[2][ "codigo" ]}</h3>
                        <p>{top_10[2]["seguimento"]}</p>
                        <p>{top_10[2]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[2]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[2]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)



st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>4º Lugar - {top_10[3]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[3][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[3][ "codigo" ]}</h3>
                        <p>{top_10[3]["seguimento"]}</p>
                        <p>{top_10[3]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[3]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[3]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>5º Lugar - {top_10[4]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[4][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[4][ "codigo" ]}</h3>
                        <p>{top_10[4]["seguimento"]}</p>
                        <p>{top_10[4]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[4]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[4]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>6º Lugar - {top_10[5]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[5][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[5][ "codigo" ]}</h3>
                        <p>{top_10[5]["seguimento"]}</p>
                        <p>{top_10[5]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[5]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[5]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>7º Lugar - {top_10[6]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[6][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[6][ "codigo" ]}</h3>
                        <p>{top_10[6]["seguimento"]}</p>
                        <p>{top_10[6]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[6]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[6]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>8º Lugar - {top_10[7]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[7][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[7][ "codigo" ]}</h3>
                        <p>{top_10[7]["seguimento"]}</p>
                        <p>{top_10[7]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[7]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[7]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>9º Lugar - {top_10[8]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[8][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[8][ "codigo" ]}</h3>
                        <p>{top_10[8]["seguimento"]}</p>
                        <p>{top_10[8]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[8]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[8]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
        <div class="card">
            <div class="header">
                <h1>10º Lugar - {top_10[9]["nome"]}</h1>
            </div>
            <div class="content">
                <!-- Logo e código ESQUERDA -->
                <div class="left">
                        <img src="https://img.logo.dev/{top_10[9][ "nome" ]}.com?token=pk_SlI7v-mxRsCxrTc0brx3_w&retina=true" width="90">
                    <div class="info">
                        <h3>{top_10[9][ "codigo" ]}</h3>
                        <p>{top_10[9]["seguimento"]}</p>
                        <p>{top_10[9]["pais"]}</p>
                    </div>
                </div>
                <div class="right">
                    <div class="metric">
                        <h3>Valor cota</h3>
                        <h2>{top_10[9]["valorCota"]}</h2>
                    </div>
                    <div class="metric">
                        <h3>Market Cap</h3>
                        <h2>{f"${formatar_valor(top_10[9]["valorMercado"])}"}</h2>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
