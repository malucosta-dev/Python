#Autoexplicativo

codigo=str(input("Informe o código do equipamento: "))
codigoLen =len(codigo) #Quantos caracteres tem a variável

if codigoLen % 2 == 0: #Verifica se o resto da divisão por 2 é 0
  print("O código digitado é par")
else:
  print("O código digitado é ímpar")