from PIL import ImageGrab
from PIL import Image
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pyautogui

def teste_imagens_2():
    windowRegion = (105, 233, 956 - 105 + 1, 718 - 233 + 3)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save("imgs/temp2.png")
    imagem_screenshot = cv2.imread("imgs/temp2.png")
    imagem_erro = cv2.imread("imgs/aviso.png")

    imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
    imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)

    plt.imshow(imagem_screenshot)
    return mse(imagem_screenshot, imagem_erro)

def teste_imagens_3():
    windowRegion = (208, 679, 341 - 208, 694 - 679)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save("imgs/temp3.png")
    imagem_screenshot = cv2.imread("imgs/temp3.png")
    imagem_erro = cv2.imread("imgs/contabilidade.png")

    imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
    imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)

    plt.imshow(imagem_screenshot)
    return mse(imagem_screenshot, imagem_erro)

def teste_imagens_4():
    windowRegion = (527, 379, 917 - 527, 526 - 379)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save("imgs/temp4.png")
    imagem_screenshot = cv2.imread("imgs/temp4.png")
    imagem_erro = cv2.imread("imgs/aviso_fase2Cadastramento.png")

    imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
    imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)

    plt.imshow(imagem_screenshot)
    return mse(imagem_screenshot, imagem_erro)

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def _teste_imagens(path_referencia, X1, Y1, X2, Y2):
    windowRegion = (X1, Y1, X2 - X1, Y2 - Y1)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save("imgs/temp.png")
    imagem_screenshot = cv2.imread("imgs/temp.png")
    imagem_erro = cv2.imread(path_referencia)

    imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
    imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)

    return mse(imagem_screenshot, imagem_erro)

def _print_and_save (path_salvar, X1, Y1, X2, Y2):
    windowRegion = (X1, Y1, X2 - X1, Y2 - Y1)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save(path_salvar)

# time.sleep(2)
# print_and_save("imgs/temp.png", X1=611,Y1=379, X2=826,Y2=523)

# print(_teste_imagens("imgs/GFIP_gerada_sucesso.png", X1=611,Y1=379, X2=826,Y2=523 ))