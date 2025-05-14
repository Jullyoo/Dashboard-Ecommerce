# 📦 Análise de Dados E-commerce - Olist

Este projeto realiza uma análise exploratória dos dados públicos da Olist, um marketplace brasileiro, com foco em comportamento de compra, desempenho de vendas, logística de entrega e principais métricas de negócio.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Status](https://img.shields.io/badge/status-em%20andamento-yellow)

---

## 🔧 Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **VSCode**

---

## 📁 Estrutura dos Dados Utilizados

Os seguintes arquivos CSV foram utilizados:

- `olist_orders_dataset.csv`: informações sobre pedidos
- `olist_order_items_dataset.csv`: itens por pedido
- `olist_order_payments_dataset.csv`: formas e valores de pagamento
- `olist_customers_dataset.csv`: informações dos clientes
- `olist_order_reviews_dataset.csv`: avaliações dos pedidos
- `olist_products_dataset.csv`: informações dos produtos
- `olist_sellers_dataset.csv`: dados dos vendedores
- `product_category_name_translation.csv`: tradução dos nomes das categorias

---

## 🧩 Pré-processamento

- Realizada junção (`merge`) de todos os arquivos usando **left join**.
- Conversão de colunas de data/hora para o formato `datetime`.
- Exportação do DataFrame consolidado para um arquivo Excel `dados_unificados.xlsx`.

---

## 📊 Análises Realizadas

### 1. ✅ **Top 10 Categorias com Maior Receita**

Gráfico de barras representando as 10 categorias que geraram mais receita com base no valor de `price`.

- **Tipo de gráfico**: Barras verticais
- **Objetivo**: Identificar categorias mais lucrativas.

### 2. ⏱️ **Tempo Médio de Entrega por Categoria**

Cálculo da média de tempo de entrega por categoria (com base na diferença entre a data de entrega ao cliente e a data de aprovação do pedido).

- **Tipo de gráfico**: Barras horizontais
- **Filtro**: Apenas pedidos com datas completas de entrega.
- **Objetivo**: Entender quais categorias são mais rápidas na entrega.

### 3. 💰 **Ticket Médio por Pedido**

Cálculo da média do valor total gasto por pedido (`order_id`), somando o preço dos produtos.

```python
"Ticket médio por pedido: R$XXX.XX"

---

## 📈 Dashboard no Power BI

Após as análises exploratórias com Python, os dados unificados foram exportados para um arquivo Excel (`dados_unificados.xlsx`) e utilizados na criação de um **dashboard interativo no Power BI**.

Esse painel permite:

- Visualizar a evolução do tempo de entrega real vs estimado
- Analisar o desempenho por categoria, estado ou vendedor
- Avaliar KPIs como receita total, ticket médio, % de atrasos
- Gerar insights visuais com filtros dinâmicos

> 📂 arquivo em .pbix:


