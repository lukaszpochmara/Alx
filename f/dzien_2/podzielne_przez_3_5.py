'''
Napisz program wypisujący wszystkie liczby od 1 do 100,
podzielne przez 3 lub podzielne przez 5.
Wypisz także jak dużo takich liczb wystąpiło w tym przedziale.
'''
liczby=set()

for i in range(1,101):
    if i % 3 ==0 or i % 5 ==0:
        liczby.add(i)

print(liczby)
print(f'Liczb podzielnych przez 3 i 5 w przedziale od 1 do 100 jest {len(liczby)}')