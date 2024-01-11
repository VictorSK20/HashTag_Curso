import pyautogui
from time import sleep

sleep(5)
posicao = pyautogui.position()  # pega a posição do mouse na tela

print(posicao)  # imprimir no terminal a posição do x e y do mouse na tela