from random import choices

zakres = int(input('Podaj zakres: '))
k = int(input('Liczba elementów: '))

lista = choices(range(zakres), k=k)

print('Wylosowane liczby:', lista)
# oblicz średnią tych liczb

suma = 0
for x in lista:
    suma += x
srednia = suma / k
print('średnia:', srednia)

# sposoby wykorzystaujące gotowe funkcje:
srednia = sum(lista) / len(lista)
print('średnia:', srednia)

import statistics
print('średnia:', statistics.mean(lista))
