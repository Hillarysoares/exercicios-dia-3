lista = [2 ,56 ,88, 24, 55, 30, 5, 10, 76, 52]
lista_Pares =[]
lista_ímpares = []

for item in lista:
    if item%2 == 0:
        lista_Pares.append(item)
    else:
        lista_ímpares.append(item)

print ('Lista: ', lista)
print('Pares: ', lista_ímpares)
print('Ímpares: ', lista_Pares)
