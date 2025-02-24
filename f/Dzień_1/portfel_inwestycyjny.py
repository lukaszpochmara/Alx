# Zadanie 4
# Stwórz program, który pobiera od użytkownika informacje o jego portfelu inwestycyjnym,
# takie jak ilość posiadanych akcji i cena zakupu.
# Następnie użyj instrukcji warunkowych, aby obliczyć całkowitą wartość portfela oraz ewentualne zyski lub straty,
# w zależności od aktualnej ceny akcji.
#
# Aktualna cena za akcję: 10 USD.
#
# Należy wyświetlić
# 1) Całkowitą, aktualną wartość portfela
# 2) Wartość zysku lub straty (jeżeli jest strata to "Strata": "... PLN", jeżeli zysk to "Zysk": "... PLN"
#
# Wersja rozszerzona - niech Python losuje aktualną cenę akcji od 5 do 20 USD
# (podpowiedź - użyj modułu random).
#
import random

ilosc_akcji = int(input("Podaj ilość posiadanych akcji"))
cena_zakupu= float(input("Podaj cenę zakupu akcji"))

aktualna_cena = random.randint(0,20)

calkowita_wartosc_zakupu = ilosc_akcji * cena_zakupu
wartosc_portfela= ilosc_akcji * aktualna_cena

zysk =  wartosc_portfela -calkowita_wartosc_zakupu

if zysk >0:
    print(f"Zysk został osiągnięty i wynosi{zysk}.zł")
elif zysk == 0:
    print(f"Nie osiągnięto zysku{zysk}.zł")
else:
    print(f'Strata wynosi{zysk}.zł')

print(f"Aktualna cena akcji wynosi {aktualna_cena}zł")