compraDesconto= 0
compra=(float(input("Informe o valor da compra: ")))


if compra >=500:
  compraDesconto= compra-(compra*0.15) #Escolhi um desconto de 15%
  print(f"Parabéns! Sua compra está apta para receber o desconto promocional. Novo valor: R${compraDesconto}.") 
else:
  print(f"o valor da sua compra foi de R${compra}")