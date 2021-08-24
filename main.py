import time
import os
Dados = ["Robson Pereira""\n""CPF:17514521-87""\n""Endereço: Rua das Arauquaras", "Joe Chill""\n""CPF:488221478-96""\n""Endereço: Rua Dom Pedro II"]
Clientes = ["Robson", "Joe"]
while (True):
 print("1 - Novo Cliente ou 2 - Ver Clientes?")
 option = int(input())

 if option == 1:
  print("Qual o nome do seu novo Cliente?""\n")
  nome = (input)
  Clientes.append(nome)
  time.sleep (0.5)
  os.system("cls")
  print("Qual o cpf do seu novo Cliente?""\n")
  
  
  
  
 if option == 2:
  print("Qual o nome do cliente desejado?")
  costumer = input()
  if costumer == "Robson":
    print(Dados[0])
  if costumer == "Joe":
    print(Dados[1])


 if option == 3:
    break