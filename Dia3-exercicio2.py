#exercicio2
dicionario = {'1':'Domingo', '2': 'Segunda-feira', '3':'Terça-feira', '4':'Quarta-feira', '5': 'Quinta-feira','6':'Sexta-feira', '7': 'Sábado' }
dia = input ('Digite um número entre 1 e 7: ')

if int(dia) >7 or int(dia) <1:
    print ('Tente um número entre 1 e 7.')
else:
    print ('Dia: ', dicionario[dia])