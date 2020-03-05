from appJar import gui
import pandas as pd
import controle_estoque

def _pegar_relatorio():
    global nome_arquivo
    nome_arquivo = app.openBox(title=None, dirName=None, fileTypes=None, asFile=False, parent=None, multiple=False, mode='r')

def _gerar_estorno():
    app.thread(_thread_gerar_estorno)

def _thread_gerar_estorno():
    global nome_arquivo
    df = pd.read_csv(nome_arquivo, encoding='latin-1', sep=';')
    controle_estoque._controle(df)
    app.infoBox("Acabou", "Fim!", parent=None)

nome_arquivo = ""

# Criando a interface Gráfica
app = gui("Estorno do ICMS")
app.setFont(10)

app.addLabel("label_0_0", "1) Remover as primeiras linhas da planilha", row = 0, column = 0)
app.addLabel("label_1_0", "2) Salvar a planilha como CSV (Separado por vírgulas)", row = 1, column = 0)
app.addLabel("label_2_0", "3) Deletar a planilha no formato antigo ", row = 2, column = 0)
app.addButton("Pegar relatório gerado pela Domínio", _pegar_relatorio,row = 3, column = 0)
app.addButton("Gerar planilha de estorno", _gerar_estorno, row = 3, column = 1)

# start the GUI
app.go()

# Dicionário de labels
# label_1: coordenada vértice superior esquerdo