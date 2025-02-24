# ######
# ## IF
# ######
#
# #################
# # if warunek:
# # kod, który się wykonuje, gdy warunek daje True
# #################
#
# # UWAGA! Pamiętajmy, że kod wewnątrz if musi być we wcięciu - wcięcie to tabulator lub 4 spacje
#
#
# temperatura = float(input("Podaj temperature"))
# if temperatura >=30:
#     print('Gorąco')
#
#
# # Zadanie 2 - sprawdzenie czy użytkownik jest pełnoletni
# # Pobierz od użytkownika informację o rok urodzenia i wypisz "Jesteś dorosły", jeżeli
# # użytkownik jest faktycznie pełnoletni
#
#
# from datetime import datetime
#
# wiek= int(input("Podaj rok urodzenia"))
# if datetime.now().year- wiek>18:
#     print('Jestś pełnoletni')
#
# # Zadanie 3
# # Określ, czy podana liczba jest dodatnia, ujemna lub równa zero.
# # Liczbę pobieramy z inputa.
#
#
# liczba = int(input("Podaj liczbę"))
#
# if liczba > 0:
#     print("Liczba większa od zera")
# elif liczba < 0:
#     print("Liczba jest niejsza od zera")
# else:
#     print("Liczba jest równa zero")


# Zadanie 3
# Napisz program w Pythonie, który symuluje proces weryfikacji dwuetapowej dla użytkownika.
# Użytkownik powinien wprowadzić swój login i hasło. Następnie program powinien sprawdzić,
# czy podane dane są poprawne.

# Jeśli są poprawne, program powinien "wygenerować" kod weryfikacyjny.
# Użytkownik będzie musiał podać ten kod, aby potwierdzić swoją tożsamość.

# Jeśli kod zostanie wprowadzony poprawnie, program wyświetli komunikat potwierdzający pomyślne zalogowanie.
# Jeśli jednak login, hasło lub kod weryfikacyjny zostanie wprowadzony nieprawidłowo,
# program powinien wyświetlić odpowiedni komunikat o błędzie.

# Prawidłowe dane do weryfikacji
# poprawny_login = "uzytkownik123"
# poprawne_haslo = "haslo123"
# poprawny_kod_weryfikacyjny = "123456"

# Np. login="uzytkownik123" haslo="zlehaslo" -> dostajemy komunikat "Zły login lub hasło"
# Np. login="uzytkownik123" haslo="haslo123" kod_weryfik="333333" -> komunikat: "Zły kod weryfikacyjny"
# Np. jeżeli wszystko poprawne (login, haslo, kod) to komunikat "Zalogowano poprawnie"

# Te dane powinny przyjść z bazy (tutaj maksymalnie upraszamy)
# Ponadto - hasło powinno przyjść w postaci niejawnej :)

# POPRAWNY_LOGIN = "uzytkownik123"
# POPRAWNE_HASLO = "haslo123"
# POPRAWNY_KOD = "123456"
#
# login = input("Podaj login: ")
# haslo = input("Podaj haslo: ")

# 1szy sposób
# Sprawdzenie poprawnosci loginu i hasla
# if login == POPRAWNY_LOGIN and haslo == POPRAWNE_HASLO:
#     print("Pierwszy etap logowania udany! W celu dokonczenia weryfikacji, podaj kod weryfikacyjny")
#     # UWAGA!
# Nie możemy dokonać konwersji wprowadzonego kodu na int, ponieważ może być kod mający na początku 0
# np. 012345. Wtedy po konwersji czyli int("012345") dostaniemy 12345 - zero zostanie "zjedzone"
#     kod = input("Podaj kod weryfikacyjny")
#     if kod == POPRAWNY_KOD:
#         print("Zalogowano poprawnie!")
#     else:
#         print("Zły kod weryfikacyjny")
# else:
#     print("Błędny login lub hasło")

# 2gi sposób
# if login != POPRAWNY_LOGIN or haslo != POPRAWNE_HASLO:
#     print("Błędny login lub hasło")
# elif input("Podaj kod weryfikacyjny: ") == POPRAWNY_KOD:
#     print("Zalogowano poprawnie!")
# else:
#     print("Błędny kod weryfikacyjny")


# Prawidłowe dane do weryfikacji
poprawny_login = "uzytkownik123"
poprawne_haslo = "haslo123"
poprawny_kod_weryfikacyjny = "123456"


login = input("Podaj login")
haslo = input('Podaj hasło')


if login == poprawny_login and haslo == poprawne_haslo:
    print(f"Wprowadzono poprawny login i haslo, kod weryfkacyjny to:{poprawny_kod_weryfikacyjny}")

kod= input("Podaj kod weryfikacyjny")

if kod== poprawny_kod_weryfikacyjny:
    print('Zalogowano pomyślnie')
else:
    print('Kod nie jest poprawny')

