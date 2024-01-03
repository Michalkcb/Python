from aplikacja import Application

aplikacja = Application()
aplikacja.wypisz()
while True:
    print('-' * 30)
    print(
        'Co chcesz zrobić? [w-wypisz, d-dodaj, z-oznacz jako zrobione, q-zakończ]: '
    )
    polecenie = input('Napis "w", "d", "z", lub "q": ')
    if polecenie == 'w':
        aplikacja.wypisz()
    elif polecenie == 'd':
        aplikacja.dodaj()
    elif (polecenie == 'z'):
        aplikacja.oznacz_jako_zrobione()
    elif (polecenie == 'q'):
        quit()
    else:
        print('Nie rozumiem :((')