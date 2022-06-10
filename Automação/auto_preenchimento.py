from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import lorem
import pyautogui
import random


def xpathclick(driver, xpath):
    driver.find_element(By.XPATH, f'{xpath}').click()


def xpathsend(driver, send, var):
    driver.find_element(By.XPATH, f'{send}').send_keys(var)


def ApagarContatos(driver, quantidade):
    for c in range(0, quantidade):
        xpathclick(driver, '/html/body/div/div[3]/div/div[1]/div/div/div/form/div[4]/table/tbody/tr[1]/td[2]/a')
        xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/p/a')
        xpathclick(driver, '/html/body/div/div[3]/div/div[1]/form/div/input[2]')


driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8000/admin/')
sleep(1)
driver.find_element(By.NAME, 'username').send_keys('thiago')
driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
xpathclick(driver, '/html/body/div/div[2]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[1]/a')

# Para apagar contatos:
# ApagarContatos(driver, 36)


# xpathclick(driver, '/html/body/div/div[3]/div/div[1]/div/ul/li/a')

file = open('titulos.txt', encoding='utf-8', mode='r')
lista = file.readlines()
lista_titulo = []
file.close()

for n in lista:
    lista_titulo.append(n.replace('\n', ''))

for c in range(0, 1):
    titulo = lista_titulo[c]
    print(titulo)
    xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input', titulo)
    xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/div/select')
    # sleep(4)
    # print(pyautogui.position())
    sleep(0.5)
    pyautogui.click(x=710, y=502)
    sleep(3)
    print(pyautogui.position())
    sleep(0.5)



    texto1 = lorem.text()
    texto2 = lorem.text()
    # xpathsend(driver, '/html/body/div[2]/div[3]/div[2]', texto1)
    pyautogui.click(x=603, y=810)
    pyautogui.write(f'{texto1}')
    texto3 = lorem.text()
    xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[5]/div/textarea', texto3)



    # nome2_homem = random.choice(lista_homem)
    #
    # num = random.randint(900000000,999999999)
    # xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[3]/div/input', num)
    # email = random.choice(lista_email)
    # email_completo = nome1_homem + nome2_homem + email
    # xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[4]/div/input', email_completo)
    # xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/div/select')
#
#     num1 = random.randint(1,2)
#
#     if num1 == 1:
#         sleep(0.5)
#         pyautogui.click(x=564, y=906)
#     else:
#         sleep(0.5)
#         pyautogui.click(x=564, y=922)
#
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]').click()
#
#     driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/ul/li/a').click()