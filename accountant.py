import sys
balance =0
warehouse = {}
logs = []

start_actions = ["saldo", "sprzedaz","zakup"]   
print(f"Dozwolone akcje: {start_actions }")
                            
availabe_actions =["saldo", "sprzedaz","zakup","konto","magazyn","przeglad","stop"] 

while True:
    if (len(sys.argv) == 4 and sys.argv[1]=="saldo") or (len(sys.argv) == 2 and sys.argv[1]=="saldo"):
        if len(sys.argv) == 4:
             logs.append(sys.argv[1:])
             balance = int(sys.argv[2])
        while True:
             print(f"Dozwolone akcje: {availabe_actions}")
             temp_date = input("Jaka akcja: ")
             temp_log = []
             if temp_date == "saldo":
                  temp_log.append(temp_date)
                  temp_date = input("Podaj wartość salda: ")
                  balance += int(temp_date)
                  temp_log.append(temp_date)
                  temp_date = input("Komentarz: ")
                  temp_log.append(temp_date)
                  print(f"Dane tymczasow: {temp_log}")
                  logs.append(temp_log)
                  print(f"Saldo wynosi: {balance}")

                  print(temp_date)
                  print(f"dane tymczasowe {len(temp_date)}, {temp_date}")
                  print(logs)
                  continue
             elif temp_date == "sprzedaz":
                  temp_log.append(temp_date)
                  temp_date = input("Sprzedaż: ")
                  #while do testowania magazynu
                  temp_log.append(temp_date)
                  temp_date = input("Cena produktu: ")
                  temp_log.append(temp_date)
                  temp_quantity = input("Ile produktów: ")
                  temp_log.append(temp_quantity)
                  temp_log.append(str(balance))
                  balance += int(temp_date)*int(temp_quantity)
                  temp_log.append(str(balance))
                  print(f"Dane tymczasow: {temp_log}")
                  #dane poprawne
                  logs.append(temp_log)
                  print(f"Saldo wynosi: {balance}")

                  print(temp_date)
                  print(f"dane tymczasowe {len(temp_date)}, {temp_date}")
                  print(logs)
                  continue
             elif temp_date == "zakup":
                  temp_log.append(temp_date)
                  temp_date = input("Nazwa towaru ")
                  #while do testowania magazynu
                  temp_log.append(temp_date)
                  temp_prize = input("Cena produktu: ")
                  temp_log.append(temp_prize)
                  temp_quantity = input("Ile produktów: ")
                  temp_log.append(temp_quantity)
                  balance -= int(temp_prize)*int(temp_quantity)

                  if temp_log[1] not in warehouse:
                       warehouse[temp_log[1]] = temp_log[2], temp_log[3]
                  else:
                       print("!"*80)
                       di_prize, di_qty = warehouse[temp_log[1]] 
                       di_prize += temp_prize
                       di_qty  += temp_quantity
                       warehouse[temp_log[1]] = di_prize,di_qty 

                       print(f"Wartosći slownik", di_prize, di_qty)
                       print("!"*80)
                  for key in warehouse:
                       print(f"Klucz - {key}. Wartość: - {warehouse[key]}" )
                  print(f"Magazyn -zawartość: {warehouse}")
                  
               #    print(f"Wartości w magazynie 932187493 {warehouse.keys()}")

                  logs.append(temp_log)
                  print(f"Saldo wynosi 02: {balance}")

                  print(f"dane tymczasowe 03: ile elementów {temp_log}.")
                  print(logs)
                  continue
             elif temp_date == "konto":
                  print(f"Saldo wynosi: {balance}")
                  continue
             elif temp_date == "magazyn":
                  if warehouse:
                       print(f"Magazyn -zawartość: {warehouse}")
                  else:
                       print("Magazyn pusty")
                  continue

             elif temp_date == "stop":
                  print("Do widzenia")
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
    elif len(sys.argv) > 1 and sys.argv[1]== "stop":
         print("Dopisz stop") 
         exit()
    else:
        print("Wpisz prawidłową akcje")
        exit()

   
  

