import random

lista = random.choices(range(100), k=10)
print("Wylowane liczby:",lista)
print(len(lista))

for x in lista:
    if x %10 ==0:
        print(f'Pierwsza liczba ze zbioru podzielna przez 10 to {x}')
        break
else:
    print('W liście nie ma liczby podzielnej przez 10')
print('Koniec programu')

