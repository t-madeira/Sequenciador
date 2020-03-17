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

planilha_dominio = pd.read_csv('conferencia_mei/planilha_dominio.csv', encoding="ISO-8859-1", sep=";")
planilha_pjf = pd.read_csv('conferencia_mei/planilha_pjf.csv', encoding="ISO-8859-1", sep=";")
planilha_salao = pd.read_csv('conferencia_mei/planilha_salao.csv', encoding="ISO-8859-1", sep=";")

planilha_dominio = _virgula_por_ponto(planilha_dominio, "Valor Contábil")
planilha_salao = _virgula_por_ponto(planilha_salao, " TOTAL MEI ")

print (planilha_salao.columns)

# print (planilha_dominio.columns)
# for i in planilha_salao.index:
#     print(planilha_salao.at[i, 'NUMERO DA NOTA FISCAL' ])
#
#
# for i in planilha_dominio.index:
#     print(str(planilha_dominio.at[i, 'Nota' ])[-4:])

dicionario_dominio = {}

for i in planilha_dominio.index:
  dicionario_dominio[str(planilha_dominio.at[i, "Nota"])[-4:]] = 0

for i in planilha_dominio.index:
  dicionario_dominio[str(planilha_dominio.at[i, "Nota"])[-4:]] += float(planilha_dominio.at[i, "Valor Contábil"])

dicionario_salao = {}

for i in planilha_salao.index:
  dicionario_salao[str(planilha_salao.at[i, "NUMERO DA NOTA FISCAL"])] = float(planilha_salao.at[i, " TOTAL MEI "])



print(dicionario_dominio)
print(dicionario_salao)

df = pd.DataFrame()
i = 0
for item in dicionario_dominio:
    df.at[i, "Nota"] = item
    df.at[]
  # if round(dicionario_salao[item], 2) != round(dicionario_dominio[item], 2):
  #   print (item)







# print (planilha_dominio.columns)
# print (planilha_pjf.columns)

# planilha_dominio = _virgula_por_ponto(planilha_dominio, "Valor Contábil")
# planilha_pjf = _virgula_por_ponto(planilha_pjf, "Valor Serviços")
#
# dicionario_dominio = {}
#
# for i in planilha_dominio.index:
#   dicionario_dominio[planilha_dominio.at[i, "Nota"]] = 0
#
# for i in planilha_dominio.index:
#   dicionario_dominio[planilha_dominio.at[i, "Nota"]] += float(planilha_dominio.at[i, "Valor Contábil"])
#
# dicionario_pjf = {}
#
# for i in planilha_pjf.index:
#   dicionario_pjf[planilha_pjf.at[i, "Número"]] = float(planilha_pjf.at[i, "Valor Serviços"])
#
# for item in dicionario_pjf:
#   if round(dicionario_pjf[item], 2) != round(dicionario_dominio[item], 2):
#     print (item)
#
# print(dicionario_dominio)
# print(dicionario_pjf)