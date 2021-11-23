import sys
balance =0
warehouse = {}
logs = []

availabe_actions =["saldo", "sprzedaz","zakup","konto","magazyn","przeglad"] 

while True:
    print(f"Dozwolone akcje: {availabe_actions}")
    if len(sys.argv) > 1 and sys.argv[1]=="saldo":
        print("Dopisz saldo")
        exit()
    elif len(sys.argv) > 1 and sys.argv[1]== "sprzedaz":
         print("Dopisz sprzedaz") 
         exit()   
    elif len(sys.argv) > 1 and sys.argv[1]== "zakup":
         print("Dopisz zakup") 
         exit()
    elif len(sys.argv) > 1 and sys.argv[1]== "konto":
         print("Dopisz konto") 
         exit()
    elif len(sys.argv) > 1 and sys.argv[1]== "magazyn":
         print("Dopisz magazyn") 
         exit()
    elif len(sys.argv) > 1 and sys.argv[1]== "przeglad":
         print("Dopisz przeglad") 
         exit()
    else:
        print("No arguments")
        exit()

   
  

