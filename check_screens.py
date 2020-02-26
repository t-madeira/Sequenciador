from PIL import ImageGrab
from PIL import Image
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pyautogui

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def teste_imagens():
    windowRegion = (624,382,822-624+3,524-382+4)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save("temp.png")
    imagem_screenshot = cv2.imread("temp.png")
    imagem_erro = cv2.imread("erro_esteCodigoJaExiste.png")

    imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
    imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)

    return mse(imagem_screenshot, imagem_erro)

def teste_imagens_2():
    windowRegion = (105, 233, 956 - 105 + 1, 718 - 233 + 3)
    imagem_screenshot = pyautogui.screenshot(region=windowRegion)
    imagem_screenshot.save("temp2.png")
    imagem_screenshot = cv2.imread("temp2.png")
    imagem_erro = cv2.imread("aviso.png")

    imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
    imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)

    plt.imshow(imagem_screenshot)
    return mse(imagem_screenshot, imagem_erro)

# print(teste_imagens_2())
#
# time.sleep(2)
# windowRegion = (105, 233, 956 - 105, 718 - 233)
# imagem_screenshot = pyautogui.screenshot(region=windowRegion)
# imagem_screenshot.save("temp.png")
# imagem_screenshot = cv2.imread("temp.png")
# imagem_erro = cv2.imread("aviso.png")
#
# imagem_screenshot = cv2.cvtColor(imagem_screenshot, cv2.COLOR_BGR2GRAY)
# imagem_erro = cv2.cvtColor(imagem_erro, cv2.COLOR_BGR2GRAY)
#
# plt.imshow(imagem_screenshot)
# plt.show()
# plt.imshow(imagem_erro)
# plt.show()