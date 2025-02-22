# Przykład 1 - proste powitanie
# imie = input("Jak masz na imię?")
# print(f"Cześć, {imie}")

#########
# UWAGA! WSZYSTKO CO TRAFIA Z INPUTA DO PROGRAMU JEST TYPU STR - NAWET JAK WPISZEMY 33 TO BĘDZIE TO STR
#########

# Przykład 2 - kalkulator

# Musimy konwertować na float (lub int - jeżeli chcemy tylko operować na liczbach całkowitych),
# ponieważ WSZYSTKO co trafia do inputa jest ZAWSZE (!!!!) typu string.

# liczba1 = float(input("Wprowadź pierwszą liczbę: "))
# liczba2 = float(input("Wprowadź drugą liczbę: "))

# suma = liczba1 + liczba2
# print(f"Suma {liczba1} i {liczba2} to {suma}.")

# Sprawdz, jaki będzie wynik, gdy nie skonwertujemy do float :)


########
# ZADANIA
########

# Zadanie nr 1
# Uzytkownik podaje temperature w stopniach Celsjusza
# Nastepnie Python ma przeliczyć stopnie C na stopnie Fahrenheita
# I na koncu python ma wypisać wynik
# {temp_w_cels} stopni Celsjusza to {temp_w_fahren} stopni Fahrenheita

# WSK. (temp_w_celsjuszach * 9/5) + 32

# temp_w_cels = float(input("Podaj temp. w stopniach Cels.: "))
# temp_w_fahren = (temp_w_cels * 9/5) + 32
# print(f"{temp_w_cels} stopni Cels. to {temp_w_fahren} stopni Fahren.")
#
# temperatura_c= int(input("Podaj temperature w stopiach Celcjusza"))
# stopnie_farenheita= (temperatura_c * 9/5) +32
# print(f'Temperatura w stopniach Celcjusza wynosi {temperatura_c}, i jest to {stopnie_farenheita}, stopni Farenheita.')



# Zadanie nr 2
# Zadanie na polega na obliczeniu BMI.
# Podajemy wagę oraz wzrost (w formacie 1.84)
# następnie python wylicza BMI korzystając ze wzoru: bmi = waga / (wzrost ** 2)
# Napis końcowy ma być: BMI wynosi: <obliczone_bmi>

# waga = float(input("Podaj wagę: "))
# wzrost = float(input("Podaj wzrost: "))
#
# bmi = waga / (wzrost ** 2)
#
# print(f"BMI wynosi: {bmi:.2f}")

# waga= float(input("Podaj wagę:"))
# wzrost = float(input("Podaj wzrost:"))
# bmi = waga / (wzrost ** 2)
# print(f'BMI wynosi: {bmi:.2f}')


# Uwaga! .2f zaokrągla
# x = 1.999
# print(f"{x:.2f}")

# Zadanie nr 3
# Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej
# przez użytkownika liczby kilometrów,
# ceny paliwa oraz spalania. Zapytaj użytkownika także o nazwy miejscowości.

# Przykładowe komunikaty programu:
# Miasto A: Warszawa
# Miasto B: Gdańsk
# Dystans Warszawa-Gdańsk: 420
# Cena paliwa: 4.55
# Spalanie na 100 km: 5.5
# Koszt przejazdu Warszawa-Gdańsk to 105 PLN

# WSKAZÓWKA: koszt_przejazdu = dystans * (spalanie / 100) * cena_paliwa

# miasto_a = input("Miasto A: ")
# miasto_b = input("Miasto B: ")
# dystans = float(input(f"Dystans {miasto_a}-{miasto_b}: "))
# cena_paliwa = float(input("Cena paliwa: "))
# spalanie = float(input("Spalanie na 100 km: "))
#
# koszt = dystans * (spalanie/100) * cena_paliwa
# print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.0f} PLN")

miasto_a = input('Podaj miejsce startu')
miasto_b = input('Podaj miejsce docelowe')
dystans = float( input(f'Podaj gystanas między {miasto_a} i {miasto_b}'))
cena_paliwa= float(input("Podaj cene paliwa"))
spalanie = float(input("Podaj spalanie na 100 km"))
koszt = dystans * (spalanie/100) * cena_paliwa
print(f"Koszt przejazdu między {miasto_a} i {miasto_b} wynosi {koszt:.2f}.pln")