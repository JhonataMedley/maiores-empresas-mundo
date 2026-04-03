# Maiores Empresas do Mundo

**Projeto para treinar Git, GitHub, Requests e Streamlit.**

## Objetivo do Projeto

Chegar em um projeto semelhante à imagem abaixo:

![alt text](image.png)

---

## Mudanças, Dificuldades e Soluções Enfrentadas Durante o Projeto

Aqui está um resumo organizado e limpo de todo o progresso, dificuldades identificadas e soluções aplicadas até o momento:

### 02/04/2026

**Dificuldades encontradas:**
- API de logos não estava encontrando o nome correto das empresas automaticamente.
- Filtro de empresas permitia entradas inválidas (ex: “Saudin Arabian” aparecendo no ranking).

**Soluções implementadas:**
- Criado um **de/para** (mapeamento) dos nomes que vêm da API para os nomes esperados pela API de logos.
- Melhorado o filtro de empresas: agora é possível adicionar **qualquer empresa** manualmente. Se o logo não for encontrado no top 10, basta incluir o ticker no de/para.

**Status:** ✅ Concluído

### 03/04/2026

**Dificuldades encontradas:**
- A API do **yfinance** nem sempre retorna os valores em USD (ex: SAR – Riyal Saudita).
- Isso alterava completamente o ranking de market cap.
- Necessidade de formatar os valores de mercado e cotação de forma legível (Tri, Bi, Mi).

**Soluções implementadas:**
- Lógica criada para detectar a moeda retornada pela API.
- Se a moeda for diferente de USD, converter o valor usando a API de câmbio (arquivo `teste_coin.py`).
- Função de formatação de valores em Trilhão, Bilhão e Milhão (Tri, Bi, Mi) já preparada.

**Status:** Em andamento / Parcialmente concluído

### 04/04/2026

**Feats realizados:**

1. **Ajustes no de/para** dos nomes das empresas (melhoria na integração com a API de logos).
2. **Função de formatação** de valores implementada (Tri, Bi, Mi).
3. Identificada a necessidade de conversão de moedas (já mapeada para usar a API do arquivo `teste_coin`).

---

**Próximos passos sugeridos (para organizar o README):**
- Finalizar a conversão completa de moedas e testar o novo ranking em USD.
- Implementar o filtro dinâmico de empresas no Streamlit.
- Testar o layout final comparando com a imagem de referência.

Quer que eu ajuste alguma parte, adicione mais seções (como Tecnologias Usadas, Como Rodar, etc.) ou deixe mais curto/mais detalhado?