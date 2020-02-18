#Exercício 4: Crie um programa que o usuário irá digitar um valor inteiro, e com base nesse valor construa uma escada.
print ('Monte sua escada')
caracter = str(input ('Digite o caracter que será utilizado: ')).upper()

degraus = input ('Digite a quantidade de degraus que deseja: ')

nome = str(input(‘Digite o seu nome: ‘)).upper()
for i in range(0, len(nome)+1):
print(nome[:i])

