import time
import keyboard_controller as kb
import mouse_controller as mc
import check_screens as cs

from pynput.keyboard import Key


def limpar_campo(x,y):
    # Clique duplo no campo descricao
    mc.double_left_click_at(x, y)
    # Apertar Home
    kb.press_this(Key.home)
    # Apertar End segurando shift
    kb.press_this_with_LSHIFT(Key.end)


# ids = [4, 5, 6, 7, 8, 11, 13, 22, 24, 31, 32, 34, 46, 47, 57, 59, 60, 61, 63, 67, 79, 87, 89, 107, 111, 119, 140, 144, 181, 192, 227, 231, 233, 234, 252, 255, 257, 262, 266, 269, 281, 296, 310, 311, 312, 315, 316, 323, 338, 346, 352, 354, 365, 369, 378, 380, 385, 386, 397, 403, 406, 407, 408, 410, 411, 413, 415, 416, 417, 418, 419, 422, 427, 438, 439, 445, 446, 452, 453, 454, 459, 463, 465, 469, 470, 473, 475, 476, 480, 481, 482, 483, 484, 485, 486, 487, 488, 490, 493, 494, 495, 496, 497, 499, 501, 502, 503, 507, 515, 516, 522, 529, 533, 535, 541, 545, 553, 554, 567, 568, 577, 581, 582, 586, 587, 590, 592, 593, 594, 595, 596, 598, 599, 603, 604, 606, 662, 664, 665, 667, 669, 670, 674, 680, 681, 682, 683, 684, 688, 689, 691, 692, 693, 695, 696, 699, 700, 702, 705, 707, 709, 730, 731, 749, 757, 759, 760, 761, 762, 763, 767, 768, 769, 770, 772, 774, 776, 779, 785, 786, 787, 789, 791, 792, 793, 794, 796, 799, 800, 801, 802, 803, 805, 808, 818, 819, 822, 826, 827, 828, 830, 832, 835, 836, 837, 838, 840, 841, 842, 843, 844, 845, 847, 850, 851, 854, 857, 858, 860, 861, 862, 863, 864, 865, 866, 869, 870, 871, 873, 874, 875, 877, 878, 879, 881, 882, 884, 885, 887, 888, 889, 893, 894, 896, 1010, 1011, 1012]
ids = [866]
time.sleep(3)

for id in ids:
        #  Abrir busca de empresas
        kb.press_this(Key.f8)

        # Digitar id da empresa
        kb.type_this(str(id))
        kb.press_this(Key.enter)
        time.sleep(6)

        # Fechar possiveis avisos
        kb.press_this(Key.esc)

        # Apertar F7
        kb.press_this(Key.f7)
        print ('f7')

        # Apertar 'o'
        kb.press_this('o')
        # Apertar 'o'
        kb.press_this('o')
        print ('double o')

        # time.sleep(2)

        # Apertar enter
        kb.press_this(Key.enter)

        # Clicar em cancelar (658, 713)
        mc.left_click_at(658, 713)

        # Clicar em novo (664, 710)
        mc.left_click_at(664, 710)

        # Digitar codigo: '21116'
        limpar_campo(468, 255)
        kb.type_this('21116')
        kb.press_this(Key.enter)
        time.sleep(2)

        # Verifica se a conta ja existe
        if cs.teste_imagens() > 2000: # nao existe
            # Digitar classificacao: '2.0.05.00.06'
            kb.type_this('20050006')
            kb.press_this(Key.enter)
            time.sleep(1)

            # Extra enter
            kb.press_this(Key.enter)

            # Digitar descricao PIS INCORRIDOS S/FÉRIAS
            kb.type_this('PIS INCORRIDOS S/FÉRIAS')
            kb.press_this(Key.enter)
            time.sleep(1)

            # Digitar data '31122015'
            kb.type_this('31122015')
            kb.press_this(Key.enter)
            time.sleep(1)

            # Clicar gravar (822, 711)
            mc.left_click_at(822, 711)

            # Aperta esc
            kb.press_this(Key.esc)

        else: #ja existe

            # Aperta enter
            kb.press_this(Key.enter)

            # Aperta esc
            kb.press_this(Key.esc)
