import time
import os

class DadosCostumer:
 def __init__(self, Nome, CNPJ, Endereco, Produto):
  self.CNPJ = CNPJ 
  self.Nome = Nome
  self.Endereco = Endereco
  self.Produto = Produto
 def printData(self):
   print("Nome: " + self.Nome)
   print("CNPJ: " + str(self.CNPJ))
   print("Endereço: " + self.Endereco)
   print("Produto: " + self.Produto)
 def printName(self):
   print("Cliente: " + self.Nome)
   print("CNPJ: " + str(self.CNPJ))
   
lista = []
p1 = DadosCostumer("Supermercado RJ", "048984498807", "Rua das Arauquaras", "Feijão")
p2 = DadosCostumer("TODODIA", "447851715588", "Jardim Dourado", "Arroz")
lista.append(p1)
lista.append(p2)

while (True):
 print("*******CENTRO DE DISTRIBUIÇÃO*******""\n")
 print("Digite a opção correspondente ao que deseja""\n""1 - Novo Cliente 2 - Ver Clientes 3 - Remover Cliente 4 - Sobre 5 - Mais opções 6 - Sair")
 option = int(input())

 if option == 1:
  print("Qual o nome do seu novo Cliente?""\n")
  Nome = input()

  print("Qual o Cnpj do seu novo Cliente? Digite apenas os números, sem pontualção.""\n")
  CNPJ = int(input())
  
  print("Qual o Endereço do seu novo Cliente?""\n")
  Endereco = input()
  
  print("Qual o produto que seu cliente compra?")
  Produto = input()
  
  lista.append(DadosCostumer(Nome, CNPJ, Endereco, Produto))
  os.system("cls")
  continue

 if option == 2:
  for i in lista:
    i.printData()
    time.sleep(1.0)
    continue
    
 if option == 3:
   print("Qual o cpf do cliente a ser removido?")
   Cnpj = str(input())
   for i in lista:
    if i.CNPJ == Cnpj:
     lista.remove(i)
     os.system("cls")
     continue
  
 if option == 4:
   print("Esse sistema foi desenvolvido em 25 de Agosto de 2021, foi criado e está sendo mantido por Ian Rodrigo, veja mais projetos meus em https://github.com/KaliRodri ")
    
 if option == 5:
   print("O que deseja ver? ""\n" "1 - Manual de Instruções 2 - FAQ")
   choose = int(input())
   if choose == 1:
     os.system("cls")
     print("Assim que começar a usar nosso sistema você terá as opções 1, 2, 3, 4, e 5. Caso escolha a opção 1, deverá então cadastrar seu novo cliente, se escolher a opção 2, verá os clientes já cadastrados, caso seja a opção três, poderá remover um cliente, no 4 verá informações sobre o desenvolvedor do sistema, e no 5 encontrará este manual e a seção de Perguntas.")
   elif choose == 2:
     print("Deu trabalho fazer esse programa?""\n""R:Sim""\n""Foi divertido?""\n""R:Sim""\n""Quando vou finalizar o jogo da forca?""\n""R:Não sei""\n")
     time.sleep(2)
     os.system("cls")
     continue

 if option < 5:
    break
