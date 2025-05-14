# IMPORTANDO BIBLIOTECAS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# CARREGANDO DADOS

pedidos = pd.read_csv('olist_orders_dataset.csv')
pedidos_items = pd.read_csv('olist_order_items_dataset.csv')
pagamentos = pd.read_csv('olist_order_payments_dataset.csv')
clientes = pd.read_csv('olist_customers_dataset.csv')
avaliacoes = pd.read_csv('olist_order_reviews_dataset.csv')
produtos = pd.read_csv('olist_products_dataset.csv')
vendedores = pd.read_csv('olist_sellers_dataset.csv')
traducao_categoria = pd.read_csv('product_category_name_translation.csv')


# PRIMEIRA VISUALIZAÇÃO

print(pedidos.head(10))
print(pedidos_items.head(10))
print(pagamentos.head(10))
print(clientes.head(10))
print(avaliacoes.head(10))
print(produtos.head(10))
print(vendedores.head(10))
print(traducao_categoria.head(10))


# UNIFICANDO DADOS COM LEFT JOIN (MERGE)

df = pedidos.merge(clientes, on='customer_id', how='left')
df = df.merge(pagamentos, on='order_id', how='left')
df = df.merge(avaliacoes, on='order_id', how='left')
df = df.merge(pedidos_items, on='order_id', how='left')
df = df.merge(produtos, on='product_id', how='left')
df = df.merge(traducao_categoria, on='product_category_name', how='left')
df = df.merge(vendedores, on='seller_id', how='left')

# CONVERTER COLUNAS PARA DATAS

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])
df['order_delivered_carrier_date'] = pd.to_datetime(df['order_delivered_carrier_date'])
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])

# SALVANDO UM XLSX UNIFICADO

df.to_excel('dados_unificados.xlsx', index=False)

# ANALISES: VENDAS POR CATEGORIA

vendas_categoria = df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)
vendas_categoria.plot(kind='bar', title='As 10 categorias com maior renda.', figsize=(10,5), color='skyblue')
plt.xlabel('Categoria')
plt.ylabel('Receita Total (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# TEMPO MÉDIO POR ENTREGA x CATEGORIA
df_entregas = df[df['order_delivered_customer_date'].notnull() & df['order_approved_at'].notnull()]

df_entregas['tempo_entrega'] = (df['order_delivered_customer_date'] - df['order_approved_at']).dt.days

media_entrega = df_entregas.groupby('product_category_name')['tempo_entrega'].mean().sort_values().head(10)
media_entrega.plot(kind='barh', title='Dez das categorias com menor tempo de entrega', figsize=(10,5), color='skyblue')
plt.xlabel('Categoria')
plt.ylabel('Tempo de Entrega')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# TICKET MÉDIO POR PEDIDO

ticket_medio = df.groupby('order_id')['price'].sum().mean()
print(f'Ticket médio por pedido: R${ticket_medio:.2f}')