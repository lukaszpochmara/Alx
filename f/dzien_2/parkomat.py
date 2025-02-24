'''
Godzina parkowania kosztuje 3 zł
Program pyta, ile godzin parkowania opłaca klient.
Wylicza kwotę do zapłaty, a następnie W PĘTLI prosi o wrzucenie kolejnej monety
aż zostanie opłacona wymagana suma.

W przypadku, gdy ktoś wpłaci za dużo, automat "wydaje resztę".
'''

godzina= 3

ile_h = int(input('Ile godzin opłacasz'))

suma = godzina * ile_h

print("Do zapłaty będzie:",suma)

wplacono = 0
while wplacono < suma:
    print(f'Do tej pory wpłacono 3{wplacono}, pozostało jeszcze {suma- wplacono}.')
    moneta= int(input('Wrzuć monetę: '))
    wplacono = wplacono+ moneta

    if moneta == 1 or moneta == 2 or moneta == 5:
        suma += moneta

    if wplacono> suma:
        print(f"Należy się resta{wplacono- suma}")
print('Dziękujemy za opłacenie parkingu')

