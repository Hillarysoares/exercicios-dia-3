#Exercício3:Crie uma lista dinâmica com números aleatórios. O programa irá pedir para o usuário a quantidade de itens que deseja na lista. Imprima a lista, seu maior valor e seu menor valor.
quantidade_lista=int(input('Digite o número de itens na lista: '))
import random as rd
contador=1
lista = []
while contador <= quantidade_lista:
    lista.append(rd.randrange(0,100))
    contador+=1
print ('Lista: ', lista)
print ('Maior número:', max (lista))
print('Menor número: ', min(lista))