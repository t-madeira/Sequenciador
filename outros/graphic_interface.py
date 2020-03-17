from appJar import gui
from pynput.mouse import Listener


from appJar import appjar

import mouse_controller as mc
import keyboard_controller as kb
import time

coordenadas = [0, 0]
stop = False
intervalo = 5
_stop = False

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
    return

def thread_start():
    global stop
    _stop = False
    while _stop == False:
        print (_stop)
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
        time.sleep(intervalo)

def start():
    app.thread(thread_start)
    # with Listener(on_click=on_click) as listener:
    #     listener.join()
    # if button == "Vai, robozin!":
    #     return

def stop():
    global _stop
    app.stop()
    _stop = True

def _export():
    app.thread(_thread_export)

def _import():
    app.thread(_thread_import)
    return 0

def _thread_export():
    nome = app.getEntry("label_3_4")
    file = open(nome+".txt", "w+")
    for command in commands_list:
        file.write(command + "\n")
    file.close()

def _thread_import():
    nome_arquivo = app.openBox(title=None, dirName=None, fileTypes=None, asFile=False, parent=None, multiple=False,
                               mode='r')
    file = open(nome_arquivo, "r")
    for row in file:
        commands_list.append(row)
        app.addListItem("commands_list", row)

    print(commands_list)

def erase_list():
    app.clearListBox("commands_list", callFunction=True)
    commands_list.clear()

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
app.addButton("Pare, robozin!", stop, row=3, column=1)
app.addButton("Apagar sequencia", erase_list, row=3, column=2)
app.addButton("Exportar sequência", _export, row=3, column=3)
app.addButton("Importar sequência", _import, row=4, column=3)

app.addEntry("label_3_4", row= 3, column = 4)
app.setEntryDefault("label_3_4", "Nome da sequência")


# Create an app instance to get the screen dimensions
root = appjar.Tk()

# Save the screen dimensions
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Destroy the app instance after retrieving the screen dimensions
root.destroy()

print (width, height)
# start the GUI
app.go()

# Dicionário de labels
# label_1: coordenada vértice superior esquerdo