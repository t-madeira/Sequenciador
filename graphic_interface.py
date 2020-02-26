from appJar import gui
from pynput.mouse import Listener

coordenadas = [0, 0]
def on_click(x, y, button, pressed):
    coordenadas[0]=x
    coordenadas[1]=y
    return False

def pegarCoordenadasDoClick(button):
    with Listener(on_click=on_click) as listener:
        listener.join()
    print(coordenadas)
    if button == "Definir vertice 1":
        app.setLabel("label_0_1", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
    elif button == "Definir vertice 2":
        app.setLabel("label_1_1", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
    return

def start(button):
    with Listener(on_click=on_click) as listener:
        listener.join()
    if button == "Vai, robozin!":
        return


# Criando a interface Gráfica
app = gui("Robozinho")
app.setFont(10)

app.addLabel("label_0_0", "Coordenadas: ", 0, 0)
app.addLabel("label_0_1", "[0, 0]", 0, 1)
app.addButton("Definir vertice 1", pegarCoordenadasDoClick, 0, 2)

app.addLabel("label_1_0", "Coordenadas da Comida: ", 1, 0)
app.addLabel("label_1_1", "[0, 0]", 1, 1)
app.addButton("Definir vertice 2", pegarCoordenadasDoClick, 1, 2)

app.addLabel("coordenadasNorte", "Coordenadas do Norte: ", 2, 0)
app.addLabel("coordenadasNorte2", "[0, 0]", 2, 1)
app.addButton("Definir coordenadas norte", pegarCoordenadasDoClick, 2, 2)

app.addLabel("label_0_3", "Sequencia de Comandos", 0, 3)
app.addListBox("list", ["apple", "orange", "pear", "kiwi"], row=1, column=3)

def press(btn):
    items = app.getListItems("list")
    print (items)
    if len(items)> 0:
        app.removeListItem("list", items[0])

app.addButton("press",  press)

app.addButton("Vai, robozin!", start, row=3, column=3)

# start the GUI
app.go()

# Dicionário de labels
# label_1: coordenada vértice superior esquerdo