#Para descobrir qual setor de uma empresa consome mais energia mensalmente

consumo1=float(input("Informe o consumo de energia(kWh) total do último mês no setor 1: "))
consumo2=float(input("Informe o consumo de energia(kWh) total do último mês no setor 2: "))

if consumo1>consumo2:
  print("O setor 1 apresentou maior gasto de energia mensal.")
else:
  print("O setor 2 apresentou maior gasto de energia mensal.")