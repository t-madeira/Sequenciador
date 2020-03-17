import pandas as pd

def removeFirstOccur(string, char):
    string2 = ''
    length = len(string)

    for i in range(length):
        if(string[i] == char):
            string2 = string[0:i] + string[i + 1:length]
            break
    return string2

def _virgula_por_ponto(df, coluna):
    for i in df.index:
        # Trocar virgulas por pontos na coluna passada
        df.at[i, coluna] = str(df.at[i, coluna]).replace(",", ".")
        if str(df.at[i, coluna]).count(".") > 1:
            print (df.at[i, coluna].count("."))
            df.at[i, coluna] = removeFirstOccur(df.at[i, coluna], ".")
        df.at[i, coluna] = float(df.at[i, coluna])
    return df

def _ponto_por_virgula(df, coluna):
    df[coluna] = df[coluna].astype(str)
    for i in df.index:
        # Trocar pontos por virgulas na coluna passada
        df.at[i, coluna] =(df.at[i, coluna].replace(".", ","))

    return df

def _controle (df):
    cfops_vendas = [5101, 5102, 5103, 5104, 5105, 5106, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5120, 5122, 5123, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304, 5305, 5306, 5307, 5351, 5352, 5353, 5354, 5355, 5356, 5357, 5359, 5360, 5401, 5402, 5403, 5405, 5551, 5651, 5652, 5653, 5654, 5655, 5656, 5667, 5922, 5932, 5933, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6108, 6109, 6110, 6111, 6112, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 6120, 6122, 6123, 6251, 6252, 6253, 6254, 6255, 6256, 6257, 6258, 6301, 6302, 6303, 6304, 6305, 6306, 6307, 6351, 6352, 6353, 6354, 6355, 6356, 6357, 6359, 6360, 6401, 6402, 6403, 6404, 6551, 6651, 6652, 6653, 6654, 6655, 6656, 6667, 6922, 6932, 6933, 7101, 7102, 7105, 7106, 7127, 7251, 7301, 7358, 7501, 7551, 7651, 7654, 7667]

    # df = pd.read_csv("estorno/Movimentação Fiscal - toda.csv", encoding='latin-1', sep=';')
    # df = pd.read_csv("teste.csv", encoding='latin-1', sep=';')

    # Tratamento
    df.dropna(axis=1, how='any', thresh=2, subset=None, inplace=True)

    # Remove colunas em branco
    df.dropna(axis=1, how='any', thresh=2, subset=None, inplace=True)
    df.drop(columns=['Documento', 'Serie', 'Cód. Emit/Dest.',
           'Nome Emit./Dest.', 'Inscrição', 'Unnamed: 16', 'Cidade Emit./Dest.',
           'UF', 'Grupo', 'Codigo item', 'Unidade\n',

           'Valor unitário\n', 'Valor total\n', 'Base do ICMS\n', 'Aliq. ICMS\n',
           'Base PIS\n', 'Base COFINS\n', 'Valor do PIS\n',
           'Valor COFINS\n', 'CST PIS\n', 'CST COFINS', 'Unnamed: 60', 'Ali. IPI',
           'CST IPI'], inplace=True)

    # Remove saídas com CST ICMS diferente de 40
    indexes_to_drop = df[(df['Tipo'] == "Saída") & (df['CST ICMS'] != 40)].index
    df.drop(indexes_to_drop, inplace=True)

    # Substitui virgula por ponto
    df = _virgula_por_ponto(df, 'Valor do ICMS\n')
    df = _virgula_por_ponto(df, 'Quantidade\n')

    # Remove entradas com Valor do ICMS <= 0
    indexes_to_drop = df[(df['Tipo'] == "Entrada") & ((df['Valor do ICMS\n']) <= 0)].index
    df.drop(indexes_to_drop, inplace=True)

    indexes_to_drop = []

    for i in df.index:
        # Remove saídas com CFOP fora da lista
        if df.at[i, "Tipo"] == "Saída":
            if int(df.at[i, "CFOP"]) not in cfops_vendas:
                indexes_to_drop.append(i)

        # Preenche valor do ICMS por unidade
        elif df.at[i, 'Valor do ICMS\n'] > 0:
            df.at[i, 'Valor do ICMS / Quantidade'] = round(df.at[i, 'Valor do ICMS\n'] / float(df.at[i, 'Quantidade\n']), 2)

    df.drop(indexes_to_drop, inplace=True)
    df['Data Entrada/Saída'] = pd.to_datetime(df['Data Entrada/Saída'])
    df.sort_values('Data Entrada/Saída', inplace=True, ascending=True)


    df.to_csv("Planilha de estorno do ICMS.csv", encoding='latin-1', sep=';', index=False)
    df = pd.read_csv("Planilha de estorno do ICMS.csv", encoding='latin-1', sep=';')

    dictionary = {}
    for i in df.index:
        if df.at[i, 'Descrição item'] not in dictionary:
            dictionary[df.at[i, 'Descrição item']] = 0

        if df.at[i, 'Tipo'] == "Entrada":
            dictionary[df.at[i, 'Descrição item']] += int(df.at[i, 'Quantidade\n'])
            df.at[i, 'Qtd em estoque (por ICMS)'] = int(df.at[i, 'Quantidade\n'])

        if df.at[i, 'Tipo'] == "Saída":
            dictionary[df.at[i, 'Descrição item']] -= int(df.at[i, 'Quantidade\n'])

        if dictionary[df.at[i, 'Descrição item']] < 0:
            dictionary[df.at[i, 'Descrição item']] = 0

        df.at[i, 'Qtd em estoque (geral)'] = dictionary [df.at[i, 'Descrição item']]

    for i in df.index:
        if i % 1000 == 0:
            print (i, "/", len(df.index))
        j = 0
        if df.at[i, "Tipo"] == "Saída":
            while j <= i:
                if df.at[i, 'Descrição item'] == df.at[j, 'Descrição item']:
                    if df.at[j, 'Qtd em estoque (por ICMS)'] > 0:
                        df.at[j, 'Qtd em estoque (por ICMS)'] -= df.at[i, 'Quantidade\n']
                        df.at[i, 'Estorno'] = round(df.at[j, 'Valor do ICMS / Quantidade'] * df.at[i, 'Quantidade\n'], 2)

                        if df.at[j, 'Qtd em estoque (por ICMS)'] < 0:
                            df.at[j, 'Qtd em estoque (por ICMS)'] = 0
                    j += 1
                else:
                    j += 1

    print("Fim!")
    df = _ponto_por_virgula(df, 'Estorno')
    df.to_csv("Planilha de estorno do ICMS.csv", encoding='latin-1', sep=';', index=False)

