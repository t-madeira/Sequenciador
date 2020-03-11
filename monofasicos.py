import pandas as pd
from appJar import gui

def _thread_pegar_relatorios():
    app.thread(_pegar_relatorios())

def _pegar_relatorios():
    global lista_relatorios
    lista_relatorios = app.openBox(title=None, dirName=None, fileTypes=None, asFile=False, parent=None, multiple=True,
                               mode='r')

def _thread_adicionar_itens():
    app.thread(_adicionar_itens())

def _adicionar_itens():
    global lista_relatorios

    cfops_vendas = [5101, 5102, 5103, 5104, 5105, 5106, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5118,
                    5119, 5120, 5122, 5123, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304,
                    5305, 5306, 5307, 5351, 5352, 5353, 5354, 5355, 5356, 5357, 5359, 5360, 5401, 5402, 5403, 5405,
                    5551, 5651, 5652, 5653, 5654, 5655, 5656, 5667, 5922, 5932, 5933, 6101, 6102, 6103, 6104, 6105,
                    6106, 6107, 6108, 6109, 6110, 6111, 6112, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 6120, 6122,
                    6123, 6251, 6252, 6253, 6254, 6255, 6256, 6257, 6258, 6301, 6302, 6303, 6304, 6305, 6306, 6307,
                    6351, 6352, 6353, 6354, 6355, 6356, 6357, 6359, 6360, 6401, 6402, 6403, 6404, 6551, 6651, 6652,
                    6653, 6654, 6655, 6656, 6667, 6922, 6932, 6933, 7101, 7102, 7105, 7106, 7127, 7251, 7301, 7358,
                    7501, 7551, 7651, 7654, 7667]

    base = pd.read_csv("monofasicos/base_monofasicos.csv", encoding = "ISO-8859-1", sep=";")

    base_descricao = base["Descrição"].tolist()
    j = 0

    for relatorio in lista_relatorios:

        df = pd.read_csv(relatorio, encoding='latin-1', sep=';')

        print (df.columns)

        for i in df.index:
            # print (i, "/", len(df.index))

            try:
                cfop = int(str(df.at[i, "CFOP"]).replace("-", ""))
            except ValueError:
                continue

            descricao = df.at[i, "Descrição"]

            if pd.isna(descricao) == False and descricao != "Descrição"\
                    and cfop in cfops_vendas and descricao not in base_descricao: # encontrou uma descricao nova

                # procurar o NCM
                # i_aux = i
                # while "NCM" not in str(df.at[i_aux, "Ncm"]):
                #     i_aux -= 1
                # ncm = df.at[i_aux, "Ncm"][4:15]
                ncm = df.at[i, "Unnamed: 11"][4:15]

                if "Produtos Não Monofásicos" in str(df.at[i, "Unnamed: 11"]):
                    monofasico = "Não"
                elif "Produtos Monofásicos" in str(df.at[i, "Unnamed: 11"]):
                    monofasico = "Sim"

                base_descricao.append(df.at[i, "Descrição"])
                base.at[j, "NCMs"] = ncm
                base.at[j, "CFOPs"] = round (cfop, 0)
                base.at[j, "Descrição"] = descricao
                base.at[j, "Monofásico"] = monofasico

                j += 1

    base.to_csv("monofasicos/base_monofasicos.csv", encoding='latin-1', sep=';', index=False)

    app.infoBox("Concluído", "Todos os itens dos relatorios foram adicionados à base de dados", parent=None)


lista_relatorios = []

# Criando a interface Gráfica
app = gui("que-Fásico")
app.setFont(10)

########################################################################################################################
coluna = 0
linha = 0
# app.addLabel("label_"+str(linha)+"_"+str(coluna), "Pegar os relatórios", row = linha, column = coluna)
linha += 1

########################################################################################################################
coluna = 1
linha = 0
app.addButton("Pegar relatórios", _thread_pegar_relatorios, row = linha, column = coluna)
linha += 1

########################################################################################################################
coluna = 2
linha = 0
app.addButton("Adicionar itens ao banco de dados", _thread_adicionar_itens, row = linha, column = coluna)
linha += 1

########################################################################################################################

# start the GUI
app.go()