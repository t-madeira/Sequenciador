import pandas as pd
from appJar import gui
import time
from tqdm import tqdm

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
            df.at[i, coluna] = removeFirstOccur(df.at[i, coluna], ".")

        if pd.isna(df.at[i, coluna]) == True: # se o valor não for nan
            print (df.at[i, coluna])
            df.at[i, coluna] = float(df.at[i, coluna])

    return df

def _ponto_por_virgula(df, coluna):
    df[coluna] = df[coluna].astype(str)
    for i in df.index:
        # Trocar pontos por virgulas na coluna passada
        df.at[i, coluna] =(df.at[i, coluna].replace(".", ","))

    return df

def _thread_pegar_relatorios():
    app.thread(_pegar_relatorios())

def _pegar_relatorios():
    global lista_relatorios
    lista_relatorios = app.openBox(title=None, dirName=None, fileTypes=None, asFile=False, parent=None, multiple=True,
                               mode='r')

def _thread_adicionar_banco_dados():
    app.thread(_adicionar_banco_dados())

def _adicionar_banco_dados():
    global lista_relatorios
    global caminho_salvar_planilha
    global cfops_vendas

    base = pd.read_csv("base_monofasicos.csv", encoding="ISO-8859-1", sep=";")
    j = len(base["Descrição"])

    for relatorio in lista_relatorios:

        df = pd.read_excel(relatorio, encoding='latin-1', sep=';')

        # for i in :
        for i in tqdm(df.index):
            # if ( i % 500 == 0):
            #     print (i, "/", len(df.index))

            try:
                cfop = int(str(df.at[i, "CFOP"]).replace("-", ""))
            except ValueError:
                continue

            descricao = df.at[i, "Descrição"]

            if pd.isna(descricao) == False and descricao != "Descrição"\
            and cfop in cfops_vendas:  # encontrou uma descricao

                if descricao in base["Descrição"].tolist():
                    aux = base["Descrição"].tolist().index(descricao) # posicao do produto na base
                    data_base = time.strptime(str(base.at[aux, "Data"]), "%Y-%m-%d %H:%M:%S")
                    data_relatorio = time.strptime(str(df.at[i, "Data"]), "%Y-%m-%d %H:%M:%S")

                    if data_relatorio > data_base:

                        base.at[aux, "NCMs"] = df.at[i, "Unnamed: 12"][4:15] # pega o ncm
                        base.at[aux, "CFOPs"] = round (cfop, 0)
                        base.at[aux, "Descrição"] = descricao

                        if "Produtos Monofásicos" in str(df.at[i, "Unnamed: 12"]):
                            base.at[aux, "Monofásico?"] = "Sim"
                        elif "Produtos Não Monofásicos" in str(df.at[i, "Unnamed: 12"]) :
                            base.at[aux, "Monofásico?"] = "Não"

                        base.to_csv("base_monofasicos.csv", encoding='latin-1', sep=';', index=False)


                else:
                    base.at[j, "NCMs"] = df.at[i, "Unnamed: 12"][4:15] # pega o ncm
                    base.at[j, "CFOPs"] = round (cfop, 0)
                    base.at[j, "Descrição"] = descricao
                    base.at[j, "Data"] = df.at[i, "Data"]

                    if "Produtos Monofásicos" in str(df.at[i, "Unnamed: 12"]):
                        base.at[j, "Monofásico?"] = "Sim"
                    elif "Produtos Não Monofásicos" in str(df.at[i, "Unnamed: 12"]) :
                        base.at[j, "Monofásico?"] = "Não"

                    base.to_csv("base_monofasicos.csv", encoding='latin-1', sep=';', index=False)
                    j += 1

            # else:
            #     print ("Não adicionado: ", descricao)


    app.infoBox("Concluído", "Todos os itens dos relatorios foram adicionados à base de dados", parent=None)

def _thread_gerar_planilha_monofasicos():
    app.thread(_gerar_planilha_monofasicos)

def _aux():
    global adicionar
    global base

def _gerar_planilha_monofasicos():
    global cfops_vendas
    global planilha_monofasicos
    global adicionar
    global base
    monofasico = 0
    k = 0

    for relatorio in lista_relatorios:

        df = pd.read_excel(relatorio, encoding='latin-1', sep=';')
        df = _virgula_por_ponto(df, "Valor Produto")

        # for i in df.index:
        for i in tqdm(df.index):

            # if ( i % 200 == 0):
            #     print (i, "/", len(df.index))

            try:
                cfop = int(str(df.at[i, "CFOP"]).replace("-", ""))
            except ValueError:
                continue

            descricao = df.at[i, "Descrição"]
            tam = len(base["Descrição"])
            ncm = df.at[i, "Unnamed: 12"][4:15]  # pega o ncm

            if pd.isna(descricao) == False and descricao != "Descrição"\
            and cfop in cfops_vendas and descricao not in base["Descrição"].tolist(): # encontrou uma descricao nova


                adicionar = app.yesNoBox("Adicionar produto", "O produto "+descricao+", de NCM "+ncm+", não está "
                            "cadastrado no banco de dados. Clique em \"Sim\", caso ele seja monofásico, para "
                            "cadastrá-lo.", parent=None)

                base.at[tam, "NCMs"] = ncm
                base.at[tam, "CFOPs"] = round(cfop, 0)
                base.at[tam, "Descrição"] = descricao

                if adicionar == False:
                    base.at[tam, "Monofásico?"] = "Não"

                elif adicionar == True:
                    base.at[tam, "Monofásico?"] = "Sim"

            base.to_csv("base_monofasicos.csv", encoding='latin-1', sep=';', index=False)

            for j in base.index:
                if base.at[j, 'Monofásico?'] == "Sim" and base.at[j, 'Descrição'] == descricao:
                    monofasico += float(df.at[i, "Valor Produto"])
                    planilha_monofasicos.at[k, "CFOP"] = cfop
                    planilha_monofasicos.at[k, "NCM"] = ncm
                    planilha_monofasicos.at[k, "Descrição"] = descricao
                    planilha_monofasicos.at[k, "Valor Produto"] = str(float(df.at[i, "Valor Produto"])).replace(".", ",")
                    k += 1

        app.infoBox("Valor Final", "O valor dos monofásicos é: R$"+str(monofasico))
        path = app.saveBox(title=None, fileName="Monofásicos de ",
                                              dirName=None, fileExt=".csv", fileTypes=None, asFile=None, parent=None)
        try:
            planilha_monofasicos.to_csv(path, encoding='latin-1', sep=';', index=False)
        except FileNotFoundError:
            app.infoBox("Não salvou", "Planilha não foi salva")

# def _thread_pegar_caminho_salvar_planilha():
#     app.thread(_pegar_caminho_salvar_planilha)
#
# def _pegar_caminho_salvar_planilha():
#     global caminho_salvar_planilha
#     global planilha_monofasicos
#     caminho_salvar_planilha = app.saveBox(title=None, fileName="base_monofasicos", dirName=None, fileExt=".csv", fileTypes=None, asFile=None, parent=None)
#     base.to_csv(caminho_salvar_planilha, encoding='latin-1', sep=';', index=False)

# Inicialização de variáveis globais
lista_relatorios = []
caminho_salvar_planilha = ""
planilha_monofasicos = pd.DataFrame()
adicionar = False
base = pd.read_csv("base_monofasicos.csv", encoding="ISO-8859-1", sep=";")

cfops_vendas = [5101, 5102, 5103, 5104, 5105, 5106, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5118,
                5119, 5120, 5122, 5123, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304,
                5305, 5306, 5307, 5351, 5352, 5353, 5354, 5355, 5356, 5357, 5359, 5360, 5401, 5402, 5403, 5405,
                5551, 5651, 5652, 5653, 5654, 5655, 5656, 5667, 5922, 5932, 5933, 6101, 6102, 6103, 6104, 6105,
                6106, 6107, 6108, 6109, 6110, 6111, 6112, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 6120, 6122,
                6123, 6251, 6252, 6253, 6254, 6255, 6256, 6257, 6258, 6301, 6302, 6303, 6304, 6305, 6306, 6307,
                6351, 6352, 6353, 6354, 6355, 6356, 6357, 6359, 6360, 6401, 6402, 6403, 6404, 6551, 6651, 6652,
                6653, 6654, 6655, 6656, 6667, 6922, 6932, 6933, 7101, 7102, 7105, 7106, 7127, 7251, 7301, 7358,
                7501, 7551, 7651, 7654, 7667]


# Criando a interface Gráfica
app = gui("que-Fásico")
app.setFont(10)

########################################################################################################################
coluna = 0
linha = 0
app.addButton("Pegar relatórios", _thread_pegar_relatorios, row = linha, column = coluna)
linha += 1
app.addButton("Gerar planilha de monofásicos", _thread_gerar_planilha_monofasicos, row = linha, column = coluna)
linha += 1

########################################################################################################################
coluna = 1
linha = 0
df = app.addButton("Adicionar produtos ao banco de dados", _thread_adicionar_banco_dados, row = linha, column = coluna)
linha += 1

# app.addIconButton("title", _thread_pegar_caminho_salvar_planilha,
#                   "C:\\Users\\thiago.madeira\PycharmProjects\Sequenciador\monofasicos\\folder_selection",
#                   align=None, row = linha, column = coluna)
linha += 1

########################################################################################################################

# start the GUI
app.go()