import pandas as pd

df = pd.read_csv("estorno icms/Movimentação Fiscal - Entradas e Saidas.csv", encoding='latin-1', sep=';')
new_df = pd.DataFrame()

for i in df.index:
    if df.at[i, "Tipo"] == "Entrada"

print(df.columns)
