from appJar import gui
from pynput.mouse import Listener

import mouse_controller as mc
import keyboard_controller as kb
import time

coordenadas = [0, 0]

def on_click(x, y, button, pressed):
    coordenadas[0]=x
    coordenadas[1]=y
    return False

def pegarCoordenadasDoClick(button):
    with Listener(on_click=on_click) as listener:
        listener.join()
    print(coordenadas)
    if button == "Definir coordenada":
        app.setLabel("label_0_2", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
    elif button == "Definir vertice 2":
        app.setLabel("label_1_1", "["+str(coordenadas[0])+", "+str(coordenadas[1])+"]")
    return

def start():
    # with Listener(on_click=on_click) as listener:
    #     listener.join()
    # if button == "Vai, robozin!":
    #     return
    print("Sequencia de comandos: " + str(commands_list))
    for command in commands_list:
        if command[:15] == "clique esquerdo":
            temp_coord = command[command.find('[')+1:command.find(']')]
            temp_x = temp_coord[:temp_coord.find(',')]
            temp_y = temp_coord[temp_coord.find(',')+2:]
            mc.left_click_at(temp_x, temp_y)

        elif command[:14] == "clique direito":
            temp_coord = command[command.find('[')+1:command.find(']')]
            temp_x = temp_coord[:temp_coord.find(',')]
            temp_y = temp_coord[temp_coord.find(',')+2:]
            mc.right_click_at(temp_x, temp_y)

        elif command[:7] == 'esperar':
            if app.getEntry("label_1_2") == "" or int(app.getEntry("label_1_2")) < 0:
                tempo = 0
            else:
                tempo = int(command[8:])
            time.sleep (int(tempo))

        elif command[:7] == 'digitar':
            digitar = command[8:]
            kb.type_this(digitar)

def add_leftClick():
    app.addListItem("commands_list", "Clique esquerdo em " + str(coordenadas))
    commands_list.append("clique esquerdo em " + str(coordenadas))

def add_rightClick():
    app.addListItem("commands_list", "Clique direito em " + str(coordenadas))
    commands_list.append("clique direito em " + str(coordenadas))

def add_waiting():
    if app.getEntry("label_1_2") == "" or int(app.getEntry("label_1_2")) < 0:
        tempo = 0
    else:
        tempo = app.getEntry("label_1_2")

    app.addListItem("commands_list", "Esperar " + str(tempo) + " segundos")
    commands_list.append("esperar " + str(tempo))

def add_type_this():
    digitar = app.getEntry("label_2_2")
    app.addListItem("commands_list", "Digitar " + digitar)
    commands_list.append("digitar " + digitar)
    print(digitar)

# Lista de comandos
commands_list = []

# Criando a interface Gráfica
app = gui("Robozinho")
app.setFont(10)

app.addLabel("label_0_0", "Sequencia de Comandos", 0, 0)
app.addListBox("commands_list", "", row=1, column=0)

app.addLabel("label_0_1", "Coordenada: ", row = 0, column = 1)
app.addLabel("label_0_2", "[0, 0]", row = 0, column = 2)
app.addButton("Definir coordenada", pegarCoordenadasDoClick, 0, 3)

app.addButton("Clique Esquerdo", add_leftClick, row=1, column=1)

app.addButton("Clique Direito", add_rightClick, row=2, column=1)

app.addButton("Esperar", add_waiting, row=1, column=2)
app.addEntry("label_1_2", row= 1, column = 3)

app.addButton("Digitar", add_type_this, row=2, column=2)
app.addEntry("label_2_2", row= 2, column = 3)

app.addButton("Vai, robozin!", start, row=3, column=0)

# start the GUI
app.go()

# Dicionário de labels
# label_1: coordenada vértice superior esquerdo