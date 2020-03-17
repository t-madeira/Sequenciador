import mouse_controller as mc
import keyboard_controller as kb
from pynput.keyboard import Key
import pandas as pd
import check_screens as cs
import os
import time

def _limpar_campo(X, Y):
    # Clique duplo no campo descricao
    mc.double_left_click_at(X, Y)
    # Apertar Home
    kb.press_this(Key.home)
    # Apertar End segurando shift
    kb.press_this_with_LSHIFT(Key.end)

empresas = [4, 7, 11, 13, 24, 34, 47, 57, 63, 82, 86, 87, 89, 112, 119, 178, 227, 233, 244, 252, 255, 257, 262, 266,
            281, 297, 310, 346, 352, 369, 378, 385, 403, 407, 422, 427, 445, 446, 438, 452, 457, 459, 463, 465, 469,
            473, 475, 480, 482, 483, 484, 485, 486, 488, 490, 494, 495, 496, 507, 522, 533, 535, 541, 545, 553, 567,
            577, 581, 582, 587, 592, 594, 595, 598, 599, 603, 662, 664, 665, 667, 669, 676, 684, 688, 692, 696, 700,
            730, 731, 749, 757, 758, 760, 761, 763, 767, 769, 772, 785, 791, 794, 799, 800, 801, 802, 803, 805, 814,
            819, 767, 822, 826, 827, 829, 830, 834, 836, 837, 843, 845, 850, 851, 854, 858, 860, 861, 863, 862, 865,
            869, 879, 895, 896, 899, 904, 1010, 1012, 1054, 1077, 1081]

directory = os.path.join("P:\documentos\OneDrive - Novus Contabilidade\Doc Compartilhado\Pessoal\Relatórios Sefip")
dictionary = {}
path = "P:\documentos\OneDrive - Novus Contabilidade\Doc Compartilhado\Pessoal\Relatórios Sefip"

for x in os.listdir(path):
    for i in range (0, len(empresas)):
        if str(empresas[i]) == str(x)[:str(x).find("-")]:
            dictionary[empresas[i]] = str(x)[str(x).find("-")+1:]

time.sleep(2)

for empresa in empresas:

    if empresa in dictionary:

        # Abrir busca de empresas
        kb.press_this(Key.f8)

        # Digitar id da empresa
        kb.type_this(str(empresa))
        kb.press_this(Key.enter)
        time.sleep(7)

        # Clique em Relatório
        mc.left_click_at(X=380,Y=51)

        # Clique em Informativo
        mc.left_click_at(X=376,Y=122)

        # Clique em Mensais
        mc.left_click_at(X=718,Y=125)

        # Clique em GFIP
        mc.left_click_at(X = 842, Y = 127)

        # Limpar campo do caminho
        _limpar_campo(X = 860, Y = 452)

        # Digitar caminho
        path += "\\" + str(empresa) + "-" + str(dictionary[empresa])
        kb.type_this(path)

        # Clicar em "Ok"
        mc.left_click_at(X=1008,Y=225)

        # Esperar gerar
        while cs._teste_imagens("imgs/GFIP_gerada_sucesso.png", X1=611,Y1=379, X2=826,Y2=523 ) > 500:
            time.sleep(1)

        # Clicar em "Ok"
        mc.left_click_at(X=774,Y=504)

        # Apertar ESC
        kb.press_this(Key.esc)




