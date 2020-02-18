#Gerar lista com números aleatórios
#Opção 1
import random as rd
contador=1
lista = []
while contador <= 20:
    lista.append(rd.randrange(0,100))
    contador+=1
print ('Lista 1: ', lista)
print ('Maior número da lista 1:', max (lista))
print('Menor número da lista 1: ', min(lista))

#Opção 2
from random import randint
Lista = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
print ('Lista 2: ', Lista)

#Opção 3
lista3 = rd.sample(range(1,20), 10)
print ('Lista 3: ', lista3)