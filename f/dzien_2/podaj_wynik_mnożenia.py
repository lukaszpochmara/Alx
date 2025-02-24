'''
Program losuje dwie liczby całkowite (np. z zakresu 1-20), i pyta się jaki jest wynik mnożenia tych liczb.

"Ile to jest 3 x 4 ?"

Użytkownik ma podać odpowiedź. Jeśli nie uda się za pierwszym razem, to program pozwala na kolejne próby.
Na końcu informuje, w której próbie udało się podać poprawny wynik.
'''

from random import randint

liczba1 = randint(1,20)
liczba2 = randint(1,20)
poprawny_wynik= liczba1 * liczba2


lp=0
while True:
    wynik = float(input(f'Ile to jest {liczba1} x {liczba2}?'))
    lp += 1
    if wynik ==poprawny_wynik:
        (print("Poprawna odpowiedz"))
        break
print(f'Poprawny wynik udało się w {lp}')