import sys
balance =0
warehouse = {}
logs = []

availabe_actions =["saldo", "sprzedaz","zakup","konto","magazyn","przeglad"] 

while True:
    print(f"Dozwolone akcje: {availabe_actions}")
    action = ("Podaj rodzaj akcji: ")
    if sys.argv[1] == "saldo":
        print("Dopisz saldo")
    elif sys.argv[1] == "sprzedaz":
        print("Dopisz sprzedaz")    
    elif sys.argv[1] == "zakup":
        print("Dopisz zakup") 
    elif sys.argv[1] == "konto":
        print("Dopisz konto") 
    elif sys.argv[1] == "magazyn":
        print("Dopisz magazyn") 
    elif sys.argv[1] == "przeglad":
        print("Dopisz przeglad") 
    else:
        if sys.argv[1] == True:
            action = input("Podaj rodzaj akcji: ")

