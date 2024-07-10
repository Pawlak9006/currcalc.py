import requests
from datetime import datetime

print("Kalkulator Walut")

waluta = input("Podaj walute: ").upper() # upper = WIELKIE LITERY



if waluta == "PLN":
    print("1 PLN = 1 PLN") 
else:
    ilosc = float(input(f"Podaj ilość: "))
    
    dzisiaj = datetime.today().strftime('%Y-%m-%d')
    print(" ")

    adres = f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzisiaj}/?format=json"

    strona = requests.get(adres)

    if strona.status_code == 200:
        dane = strona.json()
        if 'rates' in dane:
            kurs = dane['rates'][0]['mid']
            wynik = kurs * ilosc
            print(f"1 {waluta} = {kurs} PLN ")
            print(f"{ilosc} {waluta} = {wynik} PLN w dniu {dzisiaj}")
        else:
            print("Nie znaleziono kursu dla danej waluty")
    else:
        print(f"Nie można pobrać danych dla {waluta}")
