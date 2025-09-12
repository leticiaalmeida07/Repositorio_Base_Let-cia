import csv 

with open ("dados.csv","a",newline="") as arquivo:
    arquivo_csv = csv.writer(arquivo)
    arquivo_csv.writerow(["vestido midi"])
    arquivo_csv.writerow(["M"])
    arquivo_csv.writerow(["G"])



arquivo.close()


# Vamos fazer camisas personalizadas do flamengo!
import json
def carregar():
    with open(arquivo, "r") as arquivo:
        return json.load(arquivo)
    
def salvar(dados):
    with open(arquivo, "w") as arquivo:
        json.dump(dados, arquivo)

def criar():
    nome = input("Nome do jogador: ")
    número = input("Número na camisa: ")
    tamanho = input("tamanho: ")
    modelo = input("modelo: ")
    deletar= input("Deletar produto:")

    dados = carregar()
    dados.append({"nome": nome, "número": número, "tamanho": tamanho, "modelo": modelo, "deletar": deletar})
    salvar(dados)
    print("Salvo sucesso!!!")

def menu():
    opção=0 
    while opção !=4:
        pergunta_nome = input("Você vai querer nome do jogador na camisa? 1- Sim \n 2- Não")
        pergunta_número = input("Você vai querer número na camisa? 1- Sim \n 2- Não ")
        pergunta_tamanho = input("Você vai querer tamanho no manto? 1- Sim \n 2- Não")
        pergunta_modelo = input("Você vai querer modelo no manto? 1- Sim \n 2- Não")
        pergunta_deletar = input("Perdeu a oportunidade de comprar a melhor CAMISA")
        opção= int(input("escolhe a opção:"))
        if pergunta_nome == 1:





import pyautogui

pyautogui.press("win")
pyautogui.sleep(2)
pyautogui.write("google")
pyautogui.sleep(1)
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.moveTo(947,565)
pyautogui.click()
pyautogui.sleep(2)
pyautogui.write("instagram")
pyautogui.sleep(1)
pyautogui.press("enter")
pyautogui.moveTo(369,322)
pyautogui.moveTo(1202,1071)
pyautogui.write("Flamengo_123")
pyautogui.sleep(2)
pyautogui.moveTo(1199,1051)
pyautogui.write("123456")
pyautogui.sleep(2)
pyautogui.moveTo(831,486)



import pyautogui

# pyautogui.mouseInfo()
pyautogui.press("win")
pyautogui.sleep(2)
pyautogui.write("calculadora")
pyautogui.sleep(2)
pyautogui.press("enter")
pyautogui.sleep(2)
pyautogui.click(171,369)
pyautogui.sleep(2)
pyautogui.press("+")
pyautogui.sleep(2)
pyautogui.click(168,481)
pyautogui.sleep(2)
pyautogui.press("Enter")



