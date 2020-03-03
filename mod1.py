import time
import keyboard_controller as kb
import mouse_controller as mc
import check_screens as cs
import pandas as pd
from pynput.keyboard import Key

def limpar_campo(x,y):
    # Clique duplo no campo descricao
    mc.double_left_click_at(x, y)
    # Apertar Home
    kb.press_this(Key.home)
    # Apertar End segurando shift507
    kb.press_this_with_LSHIFT(Key.end)

def get_ids():
    df = pd.read_csv("base.csv")
    lista = []
    for id in df['ids']:
        lista.append(id)
    print(lista)

ids = [4, 5, 6, 7, 8, 11, 13, 22, 24, 31, 32, 34, 46, 47, 57, 59, 60, 61, 63, 67, 79, 87, 89, 107, 111, 119, 140, 144, 181, 192, 227, 231, 233, 234, 252, 255, 257, 262, 266, 269, 281, 296, 310, 311, 312, 315, 316, 323, 338, 346, 352, 354, 365, 369, 378, 380, 385, 386, 397, 403, 406, 407, 408, 410, 411, 413, 415, 416, 417, 418, 419, 422, 427, 438, 439, 445, 446, 452, 453, 454, 459, 463, 465, 469, 470, 473, 475, 476, 480, 481, 482, 483, 484, 485, 486, 487, 488, 490, 493, 494, 495, 496, 497, 499, 501, 502, 503, 507, 515, 516, 522, 529, 533, 535, 541, 545, 553, 554, 567, 568, 577, 581, 582, 586, 587, 590, 592, 593, 594, 595, 596, 598, 599, 603, 604, 606, 662, 664, 665, 667, 669, 670, 674, 680, 681, 682, 683, 684, 688, 689, 691, 692, 693, 695, 696, 699, 700, 702, 705, 707, 709, 730, 731, 749, 757, 759, 760, 761, 762, 763, 767, 768, 769, 770, 772, 774, 776, 779, 785, 786, 787, 789, 791, 792, 793, 794, 796, 799, 800, 801, 802, 803, 805, 808, 818, 819, 822, 826, 827, 828, 830, 832, 835, 836, 837, 838, 840, 841, 842, 843, 844, 845, 847, 850, 851, 854, 857, 858, 860, 861, 862, 863, 864, 865, 866, 869, 870, 871, 873, 874, 875, 877, 878, 879, 881, 882, 884, 885, 887, 888, 889, 893, 894, 896, 1010, 1011, 1012]
# ids = [866, 869, 870, 871, 873, 874, 875, 877, 878, 879, 881, 882, 884, 885, 887, 888, 889, 893, 894, 896, 1010, 1011, 1012]
time.sleep(2)
coordenadas_Arquivo = [220, 50]
coordenadas_Contabilidade = [220, 685]
coordenadas_ConfigurarIntegracao = [500, 685]

lancamentos_Folha = [5150, 5151, 5152, 5153]
lancamentos_Ferias = [5101, 5107, 5108]

for id in ids:
    # Abrir busca de empresas
    kb.press_this(Key.f8)

    # Digitar id da empresa
    kb.type_this(str(id))
    kb.press_this(Key.enter)
    time.sleep(7)

    if cs.teste_imagens_4() < 1000:
        mc.left_click_at(861, 506)
        time.sleep(2)
        mc.left_click_at(867, 524)
        time.sleep(1)

    # Fechar possiveis avisos
    kb.press_this(Key.esc)

    # Clicar em Arquivo
    mc.left_click_at(coordenadas_Arquivo[0],coordenadas_Arquivo[1])
    time.sleep(1)

    if cs.teste_imagens_3() < 1000: # Testar se existe o botão contabilidade
        # Clicar em Contabilidade
        mc.left_click_at(coordenadas_Contabilidade[0], coordenadas_Contabilidade[1])

        # Clicar em Configurar Integração
        mc.left_click_at(coordenadas_ConfigurarIntegracao[0], coordenadas_ConfigurarIntegracao[1])

        # Clicar em 'Lancamento'
        mc.left_click_at(545, 305)

        for lancamento in lancamentos_Folha:

            # Digitar um lancamento folha
            kb.type_this(str(lancamento))

            # Enter
            kb.press_this(Key.enter)

            limpar_campo(549, 334)

            if lancamento == 5150:
                # Digitar descricao
                kb.type_this("PROVISÃO DO 13º SALÁRIO")
                time.sleep(1)
                kb.press_this(Key.enter)

                # Digitar 21980
                kb.type_this('21980')
                kb.press_this(Key.enter)

                # Digitar 21118
                kb.type_this('21118')
                kb.press_this(Key.enter)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)

                # Clicar em 'Gravar'
                mc.left_click_at(1011, 321)

            elif lancamento == 5151:
                # Digitar descricao
                kb.type_this("EMISSÃO DE RECIBO DO 13º SALÁRIO")
                kb.press_this(Key.enter)

                # Digitar 21980
                kb.type_this('21980')
                kb.press_this(Key.enter)

                # Digitar 21118
                kb.type_this('21118')
                kb.press_this(Key.enter)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)

                # Clicar em 'Gravar'
                mc.left_click_at(1011, 321)

            elif lancamento == 5152:
                # Digitar descricao
                kb.type_this("PROVISÃO DE INSS S/ 13º SALÁRIO")
                kb.press_this(Key.enter)

                # Digitar 21985
                kb.type_this('21985')
                kb.press_this(Key.enter)

                # Digitar 21005
                kb.type_this('21005')
                kb.press_this(Key.enter)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)

                # Clicar em 'Gravar'
                mc.left_click_at(1011, 321)

            elif lancamento == 5153:
                # Digitar descricao
                kb.type_this("PROVISÃO DE FGTS S/ 13º SALÁRIO")
                kb.press_this(Key.enter)

                # Digitar 21988
                kb.type_this('21988')
                kb.press_this(Key.enter)

                # Digitar 21006
                kb.type_this('21006')
                kb.press_this(Key.enter)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)

                # Clicar em 'Gravar'
                mc.left_click_at(1011, 321)

        # Clicar em 'Ferias'
        mc.left_click_at(468, 279)

        for lancamento in lancamentos_Ferias:

            # Digitar um lancamento ferias
            kb.type_this(str(lancamento))
            kb.press_this(Key.enter)

            limpar_campo(525, 335)

            if lancamento == 5101:
                # Digitar descricao
                kb.type_this("EMISSÃO DE RECIBO DE FERIAS PARA PAGAMEN")
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar conta debito
                limpar_campo(553, 358)
                kb.type_this('21981')
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar conta credito
                limpar_campo(553, 383)
                kb.type_this('21110')
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Clicar em 'Gravar'
                mc.left_click_at(1011, 321)
                # time.sleep(2)

            if lancamento == 5107:
                # Digitar descricao
                kb.type_this("FGTS S/ FERIAS GOZADAS")
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar conta debito
                limpar_campo(553, 358)
                kb.type_this('21989')
                kb.press_this(Key.enter)
                #  time.sleep(3)

                # Digitar conta credito
                limpar_campo(553, 383)
                kb.type_this('21006')
                kb.press_this(Key.enter)
                #  time.sleep(3)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Clicar em 'Gravar'
                mc.left_click_at(1011, 321)
                # time.sleep(2)

            if lancamento == 5108:
                # Digitar descricao
                kb.type_this("PIS S/ FERIAS GOZADAS")
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar conta debito
                limpar_campo(553, 358)
                kb.type_this('21116')
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar conta credito
                limpar_campo(553, 383)
                kb.type_this('22907')
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Digitar historico
                kb.type_this(str(lancamento))
                kb.press_this(Key.enter)
                # time.sleep(3)

                # Clicar em 'Gravar'

                mc.left_click_at(1011, 321)
                # time.sleep(2)


            # Clicar em 'Lancamento'
            # time.sleep(1)

        # Clicar no x
        mc.left_click_at(1045, 252)
        time.sleep(2)

    else:
        mc.left_click_at(723, 406)