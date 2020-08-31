#from selenium import webdriver
from time import sleep as wait
from sys import exit as stop
import keyboard
import webbrowser as wb

#url = "https://cpstest.org/"

#driver = webdriver.Chrome()
#driver.get(url)

#clicar_test = driver.find_element_by_xpath('//*[@id="start"]')

#while True:
#    clicar_test.click()
#    wait(0.1)


#alterar setup, se o user digitar "config"
def config():
    hotkeys_num = int(input(('Quantos atalhos vc vai querer (0-9)?')))

    # Mesmo while que esta la em baixo
    lista = []
    i = 1
    while i <= hotkeys_num:
        a = input('digite o link/diretório: ')
        lista.append(a)
        print('='*40)
        print('Configuração concluida. Stream deck de pobre ativo.')
        print('='*40)
        i += 1
    main()

#main code
def main():
    while True:
        #verificação telca prefixo
        if keyboard.is_pressed('f'):

            #verificação teclas fun
            if keyboard.is_pressed('1'):
                wb.open(lista[0])
                wait(0.5)
            elif keyboard.is_pressed('2'):
                wb.open(lista[1])
                wait(0.5)
            elif keyboard.is_pressed('3'):
                wb.open(lista[2])
                wait(0.5)
            elif keyboard.is_pressed('4'):
                wb.open(lista[3])
                wait(0.5)
            elif keyboard.is_pressed('5'):
                wb.open(lista[4])
                wait(0.5)
            elif keyboard.is_pressed('6'):
                wb.open(lista[5])
                wait(0.5)
            elif keyboard.is_pressed('7'):
                wb.open(lista[6])
                wait(0.5)
            elif keyboard.is_pressed('8'):
                wb.open(lista[7])
                wait(0.5)
            elif keyboard.is_pressed('9'):
                wb.open(lista[8])
                wait(0.5)
            elif keyboard.is_pressed('0'):
                print('abrindo menu de personalização...')
                config()
                wait(0.5)

#setup inical
print('='*100)
print('Stream Deck para quem não tem um Stream Deck. Você irá configurar a quantidade de atalhos')
print('e a função que eles farão. Para ativar os atalhos, presione a tecla F + os numeros do seu telcado,')
print('de acordo com a ordem em que você adicionará nas configurações.')
print('='*100)

hotkeys_num = int(input(('Quantos atalhos vc vai querer (0-9)? ')))

# Mesmo while q esta la em cima no def config
lista = []
i = 1
while i <= hotkeys_num:
    a = input('digite o link/diretório: ')
    lista.append(a)
    i += 1
print('='*51)
print('Configuração concluida. Stream deck de pobre ativo.')
print('='*51)
main()