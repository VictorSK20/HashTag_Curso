import pyautogui
from time import sleep
import pandas

pyautogui.PAUSE = 1 # espera 1 segundo para cada comando da biblioteca pyautogui

# Automatizando a abertura de uma pagina web
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(1)

# Fazendo login no site
pyautogui.click(x=758, y=379)
pyautogui.write('Victor.Souza')
pyautogui.press('tab')
pyautogui.write('123456789')
pyautogui.press('enter')

# importa a base de dados
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    # preencher as informações
    pyautogui.click(x=846, y=251)
    # Código do Produto
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press('tab')
    # Marca do Produto
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')
    # Tipo do Produto
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')
    # categoria do Produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')
    # Preço Unitário do Produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')
    # Custo do Produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    # OBS
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')

    pyautogui.press('enter')  # clicando em enviar informações de todos os produtos
    pyautogui.scroll(5000)
