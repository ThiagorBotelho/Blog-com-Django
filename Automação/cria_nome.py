from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import random
import lorem


def xpathclick(driver, xpath):
    driver.find_element(By.XPATH, f'{xpath}').click()


def xpathsend(driver, send, var):
    driver.find_element(By.XPATH, f'{send}').send_keys(var)


driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8000/admin/')
sleep(1)
driver.find_element(By.NAME, 'username').send_keys('thiago')
driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
xpathclick(driver, '/html/body/div/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/a')


file = open('nomesMas.txt', encoding='utf-8', mode='r')
lista = file.readlines()
lista_homem = []
file.close()

file = open('nomesFem.txt', encoding='utf-8', mode='r')
lista2 = file.readlines()
lista_mulher = []
file.close()

lista_email = ['@gmail.com', '@hotmail.com', '@yahoo.com']

for n in lista:
    lista_homem.append(n.replace('\n', ''))

for m in lista2:
    lista_mulher.append(m.replace('\n', ''))

cont = 0

for c in range(0, 5):
    num_escolha = random.randint(1,2)
    if num_escolha == 1:  # É homem
        nome1_homem = random.choice(lista_homem)
        nome2_homem = random.choice(lista_homem)
        while nome2_homem == nome1_homem:
            nome2_homem = random.choice(lista_homem)
        nome = nome1_homem + ' ' + nome2_homem
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input', nome)
        email = random.choice(lista_email)
        email_completo = nome1_homem + nome2_homem + email
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/input', email_completo)

    else:
        nome1_mulher = random.choice(lista_mulher)
        nome2_mulher = random.choice(lista_mulher)
        while nome2_mulher == nome1_mulher:
            nome2_mulher = random.choice(lista_mulher)
        nome = nome1_mulher + ' ' + nome2_mulher
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input', nome)
        email = random.choice(lista_email)
        email_completo = nome1_mulher + nome2_mulher + email
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/input', email_completo)

    comentario = lorem.paragraph()
    xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[3]/div/textarea', comentario)

    xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[4]/div/div/select')

    num1 = random.randint(1, 10)


    if num1 == 1:
        sleep(0.5)
        pyautogui.click(x=1033, y=574)

    if num1 == 2:
        sleep(0.5)
        pyautogui.click(x=795, y=598)

    if num1 == 3:
        sleep(0.5)
        pyautogui.click(x=739, y=617)
    if num1 == 4:
        sleep(0.5)
        pyautogui.click(x=795, y=637)
    if num1 == 5:
        sleep(0.5)
        pyautogui.click(x=788, y=652)
    if num1 == 6:
        sleep(0.5)
        pyautogui.click(x=789, y=673)
    if num1 == 7:
        sleep(0.5)
        pyautogui.click(x=768, y=697)
    if num1 == 8:
        sleep(0.5)
        pyautogui.click(x=796, y=716)
    if num1 == 9:
        sleep(0.5)
        pyautogui.click(x=781, y=741)
    if num1 == 10:
        sleep(0.5)
        pyautogui.click(x=742, y=756)

    xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[5]/div/div/select')

    if cont == 0:

        sleep(0.5)
        pyautogui.click(x=703, y=907)

        sleep(0.5)
        pyautogui.click(x=1304, y=938)

        sleep(0.5)
        pyautogui.click(x=465, y=779)

        sleep(0.5)
        pyautogui.click(x=809, y=888)

        cont += 1

    else:

        sleep(0.5)
        pyautogui.click(x=703, y=968)

        sleep(0.5)
        pyautogui.click(x=1304, y=938)

        sleep(0.5)
        pyautogui.click(x=465, y=779)

        sleep(0.5)
        pyautogui.click(x=809, y=888)

sleep(3)
print(pyautogui.position())
#
#     num1 = random.randint(1, 2)
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
