for i in range (100): #For loop
  print(f'Isso é um loop! Lula 13 na veia\n') 

soma = 0 #For loop com contador
for n in range (0,13):
  soma +=1 
print(f'O valor da soma é {soma}')


numero = 0 #While loop
while True:
  numero = int(input(f'Digite um número par: '))
  if numero % 2 == 0:
    print ('Número par')
    break
  else:
    print('Número ímpar, burro')

jojos = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Giorno', 'Jolyne', 'Johnny', 'Josuke2', 'Jodio'] #Lista jojos
for i in jojos:
  print(i)

#Um iterador é um objeto do python que permite que façamos loops com ele

#Fazer exercícios do vídeo!!

#Usar while para exibir números de 1 a 10
soma=0
while True:
  soma += 1
  if soma == 11:
    break
  print(soma)

#Tabuada: Usuário digita um número e a tabuada desse número é exibida
 
print("======================")

n = int(input("TABUADA\n .Insira um número: "))

while True:
  for i in range (11):
    tabuada = (n*i)
    print(tabuada)

  break

#Contar quantas vogais existem na string que o usuário digita

l=0
vogais = ["a","e","i","o","u"]
nome = (input("Digite seu nome: "))
soma = 0

for l in nome:
  
  if l in vogais:
    soma +=1

print(f"A quantidade de vogais em {nome} é {soma}")

#Tabuada: exibe a tabuada de 1 a 100

n = 0
tabuada = 0

for t in range (1, 101):
  for i in range (1, 11):
    n = i+1
    tabuada =(t*i)
    print (tabuada)