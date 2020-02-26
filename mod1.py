import time
import keyboard_controller as kb
import mouse_controller as mc

from pynput.keyboard import Key

def limpar_campo(x,y):
    # Clique duplo no campo descricao
    mc.double_left_click_at(x, y)
    # Apertar Home
    kb.press_this(Key.home)
    # Apertar End segurando shift
    kb.press_this_with_LSHIFT(Key.end)

time.sleep(2)
# ids = [418, 419, 422, 427, 438, 439, 445, 446, 452, 453, 454, 459, 463, 465, 469, 470, 473, 475, 476, 480, 481, 482, 483, 484, 485, 486, 487, 488, 490, 493, 494, 495, 496, 497, 499, 501, 502, 503, 507, 515, 516, 522, 529, 533, 535, 541, 545, 553, 554, 567, 568, 577, 581, 582, 586, 587, 590, 592, 593, 594, 595, 596, 598, 599, 603, 604, 606, 662, 664, 665, 667, 669, 670, 674, 680, 681, 682, 683, 684, 688, 689, 691, 692, 693, 695, 696, 699, 700, 702, 705, 707, 709, 730, 731, 749, 757, 759, 760, 761, 762, 763, 767, 768, 769, 770, 772, 774, 776, 779, 785, 786, 787, 789, 791, 792, 793, 794, 796, 799, 800, 801, 802, 803, 805, 808, 818, 819, 822, 826, 827, 828, 830, 832, 835, 836, 837, 838, 840, 841, 842, 843, 844, 845, 847, 850, 851, 854, 857, 858, 860, 861, 862, 863, 864, 865, 866, 869, 870, 871, 873, 874, 875, 877, 878, 879, 881, 882, 884, 885, 887, 888, 889, 893, 894, 896, 1010, 1011, 1012]

ids = [502, 503, 507, 515, 516, 522, 529, 533, 535, 541, 545, 553, 554, 567, 568, 577, 581, 582, 586, 587, 590, 592, 593, 594, 595, 596, 598, 599, 603, 604, 606, 662, 664, 665, 667, 669, 670, 674, 680, 681, 682, 683, 684, 688, 689, 691, 692, 693, 695, 696, 699, 700, 702, 705, 707, 709, 730, 731, 749, 757, 759, 760, 761, 762, 763, 767, 768, 769, 770, 772, 774, 776, 779, 785, 786, 787, 789, 791, 792, 793, 794, 796, 799, 800, 801, 802, 803, 805, 808, 818, 819, 822, 826, 827, 828, 830, 832, 835, 836, 837, 838, 840, 841, 842, 843, 844, 845, 847, 850, 851, 854, 857, 858, 860, 861, 862, 863, 864, 865, 866, 869, 870, 871, 873, 874, 875, 877, 878, 879, 881, 882, 884, 885, 887, 888, 889, 893, 894, 896, 1010, 1011, 1012]
coordenadas_Arquivo = [220, 50]
coordenadas_Contabilidade = [220, 685]
coordenadas_ConfigurarIntegracao = [500, 685]

lancamentos_Folha = [5150, 5151, 5152]
lancamentos_Ferias = [5101, 5107, 5108]

for id in ids:
    # 1. Abrir busca de empresas
    kb.press_this(Key.f8)
    # time.sleep(1)
    # # Limpar campo
    # limpar_campo(579, 229)

    # 2. Digitar id da empresa
    kb.type_this(str(id))
    # time.sleep(1)

    # 3. Enter
    kb.press_this(Key.enter)
    time.sleep(7)

    # 4. Arquivo
    mc.left_click_at(coordenadas_Arquivo[0],coordenadas_Arquivo[1])
    # time.sleep(1)

    # 5. Contabilidade
    mc.left_click_at(coordenadas_Contabilidade[0], coordenadas_Contabilidade[1])
    # time.sleep(1)

    # 6. Configurar Integração
    mc.left_click_at(coordenadas_ConfigurarIntegracao[0], coordenadas_ConfigurarIntegracao[1])
    # time.sleep(1)

    # 7. Clicar em 'Lancamento'
    mc.left_click_at(545, 305)
    # time.sleep(1)

    for lancamento in lancamentos_Folha:

        # 8. Digitar um lancamento folha
        kb.type_this(str(lancamento))
        # time.sleep(1)

        # 9. Enter
        kb.press_this(Key.enter)
        # time.sleep(1)

        # 10. Clicar em 'Conta Debito'
        mc.left_click_at(551, 356)
        # time.sleep(1)

        if lancamento == 5150 or lancamento == 5151:
            # 11. Digitar 21980
            kb.type_this('21980')
            # time.sleep(1)

            # 12. Enter
            kb.press_this(Key.enter)
            # time.sleep(1)

            # # 13. Clicar em 'Conta Credito'
            # mc.left_click_at(551, 385)
            # time.sleep(1)

            # 14. Digitar 21118
            kb.type_this('21118')
            # time.sleep(1)

            # 15. Enter
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Clicar em 'Gravar'
            mc.left_click_at(1011, 321)
            # time.sleep(2)

        elif lancamento == 5152:
            # 11. Digitar 21985
            kb.type_this('21985')
            # time.sleep(1)

            # 12. Enter
            kb.press_this(Key.enter)
            # time.sleep(1)

            # # 13. Clicar em 'Conta Credito'
            # mc.left_click_at(551, 385)
            # time.sleep(1)

            # 14. Digitar 21005
            kb.type_this('21005')
            # time.sleep(1)

            # 15. Enter
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Clicar em 'Gravar'
            mc.left_click_at(1011, 321)
            # time.sleep(2)

    # Clicar em 'Ferias'
    mc.left_click_at(468, 279)
    # time.sleep(1)

    for lancamento in lancamentos_Ferias:

        # Digitar um lancamento ferias
        kb.type_this(str(lancamento))
        kb.press_this(Key.enter)
        # time.sleep(1)

        limpar_campo(525, 335)

        if lancamento == 5101:
            # Digitar descricao
            kb.type_this("EMISSÃO DE RECIBO DE FERIAS PARA PAGAMEN")
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar conta debito
            limpar_campo(553, 358)
            kb.type_this('21981')
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar conta credito
            limpar_campo(553, 383)
            kb.type_this('21110')
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar historico
            kb.type_this(str(lancamento))
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Clicar em 'Gravar'
            mc.left_click_at(1011, 321)
            # time.sleep(2)

        if lancamento == 5107:
            # Digitar descricao
            kb.type_this("FGTS S/ FERIAS GOZADAS")
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar conta debito
            limpar_campo(553, 358)
            kb.type_this('21989')
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar conta credito
            limpar_campo(553, 383)
            kb.type_this('21006')
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar historico
            kb.type_this(str(lancamento))
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Clicar em 'Gravar'
            mc.left_click_at(1011, 321)
            # time.sleep(2)

        if lancamento == 5108:
            # Digitar descricao
            kb.type_this("PIS S/ FERIAS GOZADAS")
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar conta debito
            limpar_campo(553, 358)
            kb.type_this('21116')
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar conta credito
            limpar_campo(553, 383)
            kb.type_this('22907')
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Digitar historico
            kb.type_this(str(lancamento))
            kb.press_this(Key.enter)
            # time.sleep(1)

            # Clicar em 'Gravar'

            mc.left_click_at(1011, 321)
            # time.sleep(2)


        # Clicar em 'Lancamento'
        # time.sleep(1)

    # Clicar no x
    mc.left_click_at(1045, 252)
    time.sleep(2)




21116
