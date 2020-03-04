import pandas as pd

def _trocar_virg_pont(df, coluna):
    """
    Funcao para trocar virgulas por pontos na coluna passada
    """
    for i in df.index:
        df.at[i, coluna] = str(df.at[i, coluna]).replace(",", ".")

    return df

cfops_vendas = [5101, 5102, 5103, 5104, 5105, 5106, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5120, 5122, 5123, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304, 5305, 5306, 5307, 5351, 5352, 5353, 5354, 5355, 5356, 5357, 5359, 5360, 5401, 5402, 5403, 5405, 5551, 5651, 5652, 5653, 5654, 5655, 5656, 5667, 5922, 5932, 5933, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6108, 6109, 6110, 6111, 6112, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 6120, 6122, 6123, 6251, 6252, 6253, 6254, 6255, 6256, 6257, 6258, 6301, 6302, 6303, 6304, 6305, 6306, 6307, 6351, 6352, 6353, 6354, 6355, 6356, 6357, 6359, 6360, 6401, 6402, 6403, 6404, 6551, 6651, 6652, 6653, 6654, 6655, 6656, 6667, 6922, 6932, 6933, 7101, 7102, 7105, 7106, 7127, 7251, 7301, 7358, 7501, 7551, 7651, 7654, 7667]

df = pd.read_csv("estorno/Movimentação Fiscal - Entradas e Saidas.csv", encoding='latin-1', sep=';')

# Remove colunas vazias
df.dropna(axis=1, how='any', thresh=2, subset=None, inplace=True)
df = _trocar_virg_pont(df, "Valor do ICMS\n")   

# Cria planilhas para entradas e saidas
df_entradas = pd.DataFrame(columns = df.columns)
df_saidas = pd.DataFrame(columns = df.columns)

# print (df.columns)

# Separa valores de entrada com ICMS maior que zero
for i in df.index:
    if float(df.at[i, "Valor do ICMS\n"]) > 0:
        df_entradas.loc[i] = df.loc[i]

# Nas saidas, filtrar CFOP dentro de cfops_vendase registros com "Valor do ICMS" = 0
for i in df.index:
    if df.at[i, "CFOP"] in cfops_vendas:
        df_saidas.loc[i] = df.loc[i]

# Nas saidas, filtrar CST ICMS == 40
df_saidas = df_saidas[df_saidas["CST ICMS"] == 40]

df_entradas.to_csv("estorno/entradas.csv", encoding='latin-1', sep=';', index=False)
df_saidas.to_csv("estorno/saidas.csv", encoding='latin-1', sep=';', index=False)

