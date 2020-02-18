#Exercício 4: Crie um programa que o usuário irá digitar um valor inteiro, e com base nesse valor construa uma escada.
print ('Monte sua escada')
caracter = input ('Digite o caracter que será utilizado: ')
degraus = int(input ('Digite a quantidade de degraus que deseja: '))
Lista = []

for i in range (1, degraus+1):
    Lista.append(caracter)
    print(Lista)

