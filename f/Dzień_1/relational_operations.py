##########
# ZADANIA
##########
# Zadanie 1. Poproś użytkownika o wpisanie dwóch różnych liczb,
# a następnie wypisz na ekranie, czy pierwsza liczba jest większa od drugiej.

# liczba_1 = float(input("Wpisz pierwszą liczbę: "))
# liczba_2 = float(input("wpisz drugą liczbę: "))
#
# print(f"Czy pierwsza liczba jest większa od drugiej?? { liczba_1 > liczba_2}")

#
# liczba1= int(input("Podaj liczbę"))
# liczba2 = int(input("Podaj drugą liczbę"))
#
# print(f'Czy liczba pierwsza jest większa od drugiej {liczba1 > liczba2}')
#
# # Zadanie 2
# Napisz program sprawdzający czy podana przez użytkownika liczba jest:
# - większa od 10
# - mniejsza równa 15
# - podzielna przez 2

# Podaj liczbę: 15 (z inputa)

# Przykładowy komunikat programu:
# Większa od 10: True
# Mniejsza równa 15: True
# Podzielna przez 2: False
# Podzielna przez 3: True

# liczba = int(input("Podaj liczbę: "))
#
# wieksza_od_10 = liczba > 10
#
# mniejsza_rowna_15 = liczba <= 15
#
# podzielna_przez_2 = liczba % 2 == 0
#
# podzielna_przez_3 = liczba % 3 == 0
#
# print(f"Wieksza od 10: {wieksza_od_10}, mniejsza rowna 15: {mniejsza_rowna_15}, "
#       f"podzielna przez 2: {podzielna_przez_2}, podzielna przez 3: {podzielna_przez_3}")

liczba= int(input("Podaj liczbę"))

if liczba >10:
    print("Liczba większa od 10")
if liczba ==10:
    print('Liczba równa 10')
if liczba % 2 == 0:
    print ('Liczba podzielna przez 2')


print(f'Większa od 10 {liczba > 10} \nNiejsza od 10 {liczba < 10}\nPodzielna przez 2 {liczba %2 == 0}'
      f'\nMniejsza równa 15 {liczba<=15}\nPodzielna przez 3 {liczba %3==0}12 ')
