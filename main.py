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
 print("Digite a opção correspondente ao que deseja""\n""1 - Novo Cliente 2 - Ver Clientes 3 - Remover e Editar Cliente 4 - Sobre 5 - Mais opções 6 - Relatório 7 - Sair")
 option = int(input())

 if option == 1:
   print("Qual o nome do seu novo Cliente?""\n")
   Nome = input()
  
   print("Qual o Cnpj do seu novo Cliente? Digite apenas os números, sem pontuação.""\n")
   CNPJ = int(input())
    
   print("Qual o Endereço do seu novo Cliente?""\n")
   Endereco = input()
  
   print("Qual o produto que seu cliente compra?")
   Produto = input()
   23
  
   lista.append(DadosCostumer(Nome, CNPJ, Endereco, Produto))
   os.system("cls")
   continue

 if option == 2:
  for i in lista:
    print("------------------------")
    i.printName()
  
  print("Digite o nome do cliente para mais informações")
  nome = input()
  
  for i in lista:
    if i.Nome == nome:
     i.printData()
  continue
    
 if option == 3:
   print("Deseja editar ou remover um cliente?""\n" " 1 - Remover 2 - Editar")
   choose = int(input())
   
   if choose == 1:
    print("Qual o Cnpj do cliente a ser removido?")
    Cnpj = str(input())
    for i in lista:
     if i.CNPJ == Cnpj:
      lista.remove(i)
      os.system("cls")
    continue
    
   if choose == 2:
     for i in lista:
      print("Qual o Cnpj do cliente a ser editado?")
      Cnpj = input()
      
      if i.CNPJ == Cnpj:
       print("Oq vc quer editar: 1 Nome 2 Cnpj 3 Endereco 4 Produto")
       choose = int(input())
       if choose == 1:
        print("Digite o novo nome: ")
        newname = input()
        i.Nome = newname
        time.sleep(0.8)
        i.printData()
        input("Digite qq tecla para continuar:")
        os.system("cls")
        continue
      
       if choose == 2:
        print("Digite o novo Cnpj: ")
        newCnpj = input()
        i.CNPJ = newCnpj
        time.sleep(0.8)
        i.printData()
        input("Digite qq tecla para continuar:")
        os.system("cls")
        continue
      
       if choose == 3:
        print("Digite o novo endereço: ")
        newEdn = input()
        i.Endereco = newEdn
        time.sleep(0.8)
        i.printData()
        input("Digite qq tecla para continuar:")
        os.system("cls")
        
      
       if choose == 4:
        print("Digite o novo produto: ")
        newitem = input()
        i.Produto = newitem
        time.sleep(0.8)
        i.printData()
        input("Digite qq tecla para continuar:")
        os.system("cls")
   continue
  
   
 if option == 4:
   print("Esse sistema foi desenvolvido em 25 de Agosto de 2021, foi criado e está sendo mantido por Ian Rodrigo, veja mais projetos meus em https://github.com/KaliRodri ")
   continue
 if option == 5:
   print("O que deseja ver? ""\n" "1 - Manual de Instruções 2 - FAQ")
   choose = int(input())
   if choose == 1:
     os.system("cls")
     print("Assim que começar a usar nosso sistema você terá as opções 1, 2, 3, 4, e 5. Caso escolha a opção 1, deverá então cadastrar seu novo cliente, se escolher a opção 2, verá os clientes já cadastrados, caso seja a opção três, poderá editar e/ou remover um cliente, no 4 verá informações sobre o desenvolvedor do sistema, e no 5 encontrará este manual e a seção de Perguntas, no 6 gerará um relatório e no 7 ou quaisquer outro número encerrará o programa.")
   elif choose == 2:
     print("Deu trabalho fazer esse programa?""\n""R:Sim""\n""Foi divertido?""\n""R:Sim""\n""Quando vou finalizar o jogo da forca?""\n""R:Não sei""\n")
     time.sleep(2)
     os.system("cls")
     continue

 if option == 6:
  lines = []
  header = "Nome, CNPJ, End., Produto"
  lines.append(header)
  for i in lista:
    line = i.Nome +", " +str(i.CNPJ)
    lines.append(line)
  with open('relatorio.txt', 'w') as f:
    for line in lines:
      f.write(line)
      f.write('\n')
     
 if option < 7:
  break
