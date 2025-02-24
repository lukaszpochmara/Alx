# print('Początek programu')
#
# lista = [11, 22, 33, 44, 55, 66, 77]
#
# for x in lista:
#     print('\nPodana liczba:', x)
#     if x % 3 == 0:
#         print('Liczba jest podzielna przez 3, robię continue')
#         continue
#     print('Nie było podzielności przez 3')
#     if x % 5 == 0:
#         print('Liczba jest podzielna przez 5, robię break')
#         break
#     print('Nie było podzielności przez 5')
#     print('Ładna pogodna')
#
# print('Jestem już za pętlą')
# print('Koniec programu')

from random import choices
print('Początek programu')

lista = choices(range(1,21), k= 20)

for x in lista:
    print('\nPodana liczba',x)
    if x % 3 == 0:
        print(f'Liczba {x}, jest podzielna przez 3, robię continue')
        continue
    print("Nie było podzielności przez 3")
    if x % 5 == 0:
        print(f'Liczba {x}, jest podzielna przez 5, robię break')
    print('Nie było podzielności przez 5')
    print('Ładna pogoda')

print('Jestem za pętlą')
print("Koniec programu")

