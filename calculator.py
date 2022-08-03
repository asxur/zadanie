
import logging
logging.basicConfig(level=logging.INFO)

def calculator(number):
    if number == 1:
        logging.info("  Wybrałeś Dodawanie, podaj prosze 2 liczby ")
        no1 = float(input("Podaj składnik 1: "))
        no2 = float(input("Podaj składnik 2: "))
        logging.info(f"Dodaje {no1} i {no2}")
        print("Wynik twojego dzialania to : ", no1 + no2)
    elif number == 2:
        logging.info("  Wybrałeś Odejmowanie, podaj prosze 2 liczby ")
        no1 = float(input("Podaj składnik 1: "))
        no2 = float(input("Podaj składnik 2: "))
        print("Wynik twojego dzialania to : ", no1 - no2)
    elif number == 3:
        logging.info("  Wybrałeś Mnożenie, podaj prosze 2 liczby ")
        no1 = float(input("Podaj składnik 1: "))
        no2 = float(input("Podaj składnik 2: "))
        print("Wynik twojego dzialania to : ", no1 * no2)
    elif number == 4:
        logging.info("  Wybrałeś Dzielenie, podaj prosze 2 liczby ")
        no1 = float(input("Podaj składnik 1: "))
        no2 = float(input("Podaj składnik 2: "))
        print("Wynik twojego dzialania to : ", no1 / no2) 
    else:
        logging.info("Podałeś złą liczbę!")  
    exit()

if __name__ == "__main__":
    numbers_value = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie \n"))
    numbers = numbers_value
    calculate = calculator(numbers)
    print(calculate)