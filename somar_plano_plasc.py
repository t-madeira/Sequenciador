import pandas as pd
import os
from collections import OrderedDict

def insert_key_value(a_dict, key, pos_key, value):
    """"
    Inserir no dicionario e manter ordem
    """
    new_dict = OrderedDict()
    for k, v in a_dict.items():
        if k==pos_key:
            new_dict[key] = value  # insert new key
        new_dict[k] = v
    return new_dict

def _trocar_virg_pont(df, file):
    """
    Funcao para trocar virgulas por pontos
    """
    for i in df.index:
        df.at[i, "Composição de Despesas (R$)"] = str(df.at[i, "Composição de Despesas (R$)"]).replace(",", ".")
    df.to_csv("planilhas/"+file, encoding='latin-1', sep=';', index=False)

def _tratar_espacos(df, file):
    """
    Funcao para remover os espacos em branco antes dos nomes
    """
    for i in df.index:
        string_aux = str(df.at[i, "Nome Beneficiário"])
        if string_aux[0] == "\xa0":
            df.at[i, "Nome Beneficiário"] = df.at[i, "Nome Beneficiário"][2:]
    df.to_csv("planilhas/"+file, encoding='latin-1', sep=';', index=False)

def _soma_parcelas (df):
    if df.at[linha, "Unnamed: 7"] == "MENSALIDADES":
        mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
    elif df.at[linha, "Unnamed: 7"] == "MENSALIDADE AVULSA":

        print("teste")
        mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
    elif df.at[linha, "Unnamed: 7"] == "CO-PARTICIPACAO":
        print("teste")
        coparticipacao += float(df.at[linha, "Composição de Despesas (R$)"])

def pega_mensalidade_coparticipacao (df, dictionary):
    linha = 0
    while linha < len(df["Matrícula"]):
        nome = df.at[linha, "Nome Beneficiário"]
        mensalidade = 0
        coparticipacao = 0
        if df.at[linha, "Matrícula"] > 1:
            if df.at[linha, "Unnamed: 7"] == "MENSALIDADES":
                mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
            elif df.at[linha, "Unnamed: 7"] == "MENSALIDADE AVULSA":
                mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
            elif df.at[linha, "Unnamed: 7"] == "FRANQUIA DE INTERNACAO":
                mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
            elif df.at[linha, "Unnamed: 7"] == "CO-PARTICIPACAO":
                coparticipacao += float(df.at[linha, "Composição de Despesas (R$)"])

        linha += 1

        if linha < len(df["Matrícula"]):
            while (not df.at[linha, "Matrícula"] > 1 and linha < len(df["Matrícula"])):
                if df.at[linha, "Unnamed: 7"] == "MENSALIDADES":
                    mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
                elif df.at[linha, "Unnamed: 7"] == "MENSALIDADE AVULSA":
                    mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
                elif df.at[linha, "Unnamed: 7"] == "FRANQUIA DE INTERNACAO":
                    mensalidade += float(df.at[linha, "Composição de Despesas (R$)"])
                elif df.at[linha, "Unnamed: 7"] == "CO-PARTICIPACAO":
                    coparticipacao += float(df.at[linha, "Composição de Despesas (R$)"])
                linha += 1

        dictionary[nome][0] += mensalidade
        dictionary[nome][1] += coparticipacao

    return dictionary

def _pega_prox_titular (df, nome, i):
    """
    Pega o nome do titular de nome
    """
    while df.at[i, "Tipo Benef."] != "TITULAR":
        i += 1
        # print (df.at[i, "Nome Beneficiário"])

    print(df.at[i, "Nome Beneficiário"])
    return df.at[i, "Nome Beneficiário"]



## BEGIN ##

directory = os.path.join("C:/Users/thiago.madeira/PycharmProjects/Sequenciador/planilhas")
flag = True
dictionary = {}

for root,dirs,files in os.walk(directory):
    if flag:
        for file in files:
            print(file)
            if file.endswith(".csv"):
                df = pd.read_csv("planilhas/"+file, encoding='latin-1', sep=';')

                # _tratar_espacos(df, file)
                # _trocar_virg_pont(df, file)

                for i in df.index:
                    if df.at[i, "Matrícula"] > 1 and df.at[i, "Nome Beneficiário"] not in dictionary:
                        if df.at[i, "Tipo Benef."] == 'TITULAR':
                            dictionary[df.at[i, "Nome Beneficiário"]] = [0, 0, "TITULAR"]
                        elif df.at[i, "Tipo Benef."] == 'DEPENDENTE':

                            nome_prox_titular = _pega_prox_titular (df, df.at[i, "Nome Beneficiário"], i)
                            # insert_key_value(dict, "2", "3", "two")
                            dictionary = insert_key_value(dictionary, df.at[i, "Nome Beneficiário"], nome_prox_titular, [0, 0, "DEPENDENTE"])
                            dictionary[df.at[i, "Nome Beneficiário"]] = [0, 0, "DEPENDENTE"]

                dictionary = pega_mensalidade_coparticipacao(df, dictionary)

                print(dictionary)
        flag = False

df_final = pd.DataFrame()
i = 1

for d in dictionary:
    # if dictionary[d][2] == "TITULAR":
    #     print (d, dictionary[d][2])
    # else:
    #     print ("\t", d, dictionary[d][2])
    df_final.at[i, "Nome"] = d
    df_final.at[i, "Mensalidade"] = round(dictionary[d][0], 2)
    df_final.at[i, "Co-participacao"] = round(dictionary[d][1], 2)
    df_final.at[i, "Tipo Benef."] = dictionary[d][2]
    i+=1
    # print (d, dictionary[d][0], dictionary[d][1])
df_final.to_csv("final.csv", encoding='latin-1', sep=';', index=False)
# for d in dictionary:
#     df_final["Nome"] = d
#     df_final["Mensalidade"] = dictionary[d][0]
#     df_final["Co-participacao"] = dictionary[d][0]
#     print (d, dictionary[d][0], dictionary[d][1])
# df_final.to_csv("planilhas/final.csv", encoding='latin-1', sep=';', index=False)







#
# dict = {"1": "one", "3": "three"}
# print (dict)
# new_dict = insert_key_value(dict, "2", "1", "two")
# print (new_dict)