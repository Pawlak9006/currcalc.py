import requests
from datetime import datetime

print("Kalkulator Walut")

waluta = input("Podaj walute: ").upper() # upper = WIELKIE LITERY



if waluta == "PLN":
    print("1 PLN = 1 PLN") 
else:        
    dzisiaj = datetime.today().strftime('%Y-%m-%d')
    print(" ")

    adres = f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzisiaj}/?format=json"

    strona = requests.get(adres)

    if strona.status_code == 200:
        dane = strona.json()
        if 'rates' in dane:
            kurs = dane['rates'][0]['mid']
            
            print(f"1 {waluta} = {kurs} PLN w dniu {dzisiaj}")
            odpowiedz = input("chcesz podać ilość do wymiany? Tak/Nie : ")
            # print(odpowiedz)
            
            if odpowiedz == "Tak" or odpowiedz == "tak":
                while True:
                    ilosc = input(f"Podaj ilość: ")
                    try:
                        ilosc = float(ilosc)
                        if ilosc <= 0:
                            print("Podaj Kwotę większą niż 0 dzbanku ^^")
                        else:
                            break
                    except ValueError:
                        print("Hey podaj liczbę, It is NEED TO BE A NUMBER OVER 0 !")


                wynik = kurs * ilosc
                # print(f"1 {waluta} = {kurs} PLN ")
                print(f"{ilosc} {waluta} = {wynik} PLN w dniu {dzisiaj}")
            else:
                print(f"1 {waluta} = {kurs} PLN na dzień {dzisiaj}")
        else:
            print("Nie znaleziono kursu dla danej waluty")
    else:
        print(f"Nie można pobrać danych dla {waluta}")



