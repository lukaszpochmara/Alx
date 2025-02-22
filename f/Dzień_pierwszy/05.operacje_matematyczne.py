##########
# Operatory arytmetyczne
##########

# + (dodawanie)
# - (odejmowanie)
# * (mnożenie)
# / (dzielenie - zwykłe dzielenie)
# // (dzielenie całkowite)
# ** (potęgowanie)
# % (modulo)

#############
# Operacje arytmetyczne na LICZBACH
#############
a = 10
b = 3
c = 2.5

# print(a + b) # 13
# print(a + c) # 12.5
# print(a - c) # 7.5
# print(a * b) # 30
# print(a / b) # 3,333333...
# print(a // b) # 3
# print(a ** b) # 1000
# print(a % b) # 1

##############
# Operacje arytmetyczne na NAPISACH (czyli na typie str)
##############

s1 = "Python"
s2 = "rządzi!"

# print(s1 + s2) # Pythonrządzi

# print(s1 + " " + s2) # Python rządzi

# print(s1 - s2) # blad - nie mozna odejmowac!
# print(s1 * s2) # blad
# print(s1 / s2) # blad

# Wniosek: na napisach możemy wykonywać tylko działania z dodawaniem (+)
# Łączenie napisów nazywamy konkatenacją

###############
# Operacje arytmetyczne na NAPISACH i LICZBACH
###############

imie = "Mateusz"
wiek = 26

# print(imie + wiek) # nie można dodawać napisu i liczby
# print(imie - wiek) # odjemowac tez nie (bo co mialoby wyjsc?)
# print((imie + '\n') * wiek) # JEST OKEJ (LICZBA * NAPIS) \n - dodaje enter
# print(imie / wiek) # blad

# WNIOSEK: Przy operacji na napisie i liczbie możemy wykonywać TYLKO mnożenie!

#################
# Operacje arytmetyczne na wartościach typu BOOL (czyli True lub False)
##################

# print(True + True) # 2
# print(True - True) # 0
# print(True * False) # 0
# print(True ** True) # 1

# Wniosek: Działania arytmetyczne na wartościach logicznych są możliwe, ponieważ
# są wtedy one traktowane jako liczby (True jest konwertowane na 1, a False na 0)

############
# Podsumowanie
############

# Co nie działa?
# 1. Odejmowanie, dzielenie, modulo, potęgowanie i dzielenie całkowite pomiędzy napisami
# lub napisem i liczbą (tu działa tylko mnożenie!!!).
# 2. Mimo że można wykonywać operacje matematyczne na wartościach boolowskich,
# wynika to z ich reprezentacji liczbowej, a nie typowego użycia typu bool.

######
# ZADANIA
######

# 1. Oblicz pole trójkąta o podstawie 10 i wysokości 5. Wypisz wynik.

# dlugosc_podstawy = 10
# wysokosc = 5
#
# pole = 0.5 * dlugosc_podstawy * wysokosc
# print(pole)

# 2.Oblicz pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5. Wypisz wynik.
# Pole trapezu = ((a + b) * h)/2 lub (a+b)*h*0.5

# dlugosc_podstawy_a= 3
# dlugosc_podstawy_b = 9
# wysokosc = 6.5
#
# pole = ((dlugosc_podstawy_a + dlugosc_podstawy_b) * wysokosc) / 2
# print(pole)

# 3.
# Napisz program wyliczający kwotę należną za zakupiony towar na podstawie
# ceny za kilogram oraz liczby zakupionych kilogramów.

# Do przechowywania informacji o cenie oraz liczbie kilogramów użyj zmiennych.

# Wypisz wszystkie informacje na konsolę.
# Komunikat programu:
# Cena za kg: 10.0
# Waga: 2.5
# Należność: 25.0

# cena_za_kg = 10.0
# waga = 2.5
# naleznosc = cena_za_kg * waga
#
# print('Cena za kg:', cena_za_kg)
# print('Waga:', waga)
# print('Należność:', naleznosc)
#
#
# cena = 10
# waga = 2.5
# naleznosc = cena*waga
# print("Cena za kg: " + str(cena), "\n" + "waga: " + str(waga), "\n" + "Należność: " + str(naleznosc))