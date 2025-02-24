# Napisz program, który na ekran wypisuje tabliczkę mnożenia 10×10

#* użytkownik podaje liczbę wierszy i liczbę kolumn, a program wyświetla
# tabl. mno. o tych wymiarach



for w in range(1,11):
    for k in range(1,11):
        print(f'{w * k :3}' , end=' ')
    print()