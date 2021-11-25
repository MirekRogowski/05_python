import sys
import os
width, height =os.get_terminal_size()
width = width - 1
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
             print(f"Dozwolone akcje: {availabe_actions}\n")
             temp_date = input("Jaka akcja: ")
             temp_log = []
             if temp_date == "saldo":
                  temp_log.append(temp_date)
                  temp_date = input("Podaj wartość salda: ")
                  balance += int(temp_date)
                  temp_log.append(temp_date)
                  temp_date = input("Komentarz: ")
                  temp_log.append(temp_date)
                  logs.append(temp_log)
                  continue
             elif temp_date == "sprzedaz":
                  if not bool(warehouse) :
                       print("*"*width)
                       print("Magazyn jest pusty")
                       print("prosze wybrać akcję -zakup-")
                       print("*"*width)
                       continue
                  temp_log.append(temp_date)
                  temp_date = input("Sprzedaż 1 krok: ")
                  print("temp date", temp_date)
               #    temp_mag =warehouse.get(temp_date,0)
               #    print("Magazyn", temp_mag)
                  if not bool(warehouse) :
                       print("prosze wybrać akcję -zakup-")
                       continue
                  if not warehouse.get(temp_date,0) :
                       print("Brak towaru  w magazanie, proszę wybrać inny towar ")
                       print("W magazynie są dostępne: ")
                       for key in warehouse:
                            print(f"Towar - {key}. Wartość: - {warehouse[key]}" )
                       continue

                 


        
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
               #    while (balance + int(temp_prize)*int(temp_quantity))< 0 :
               #         print
                       


                  if temp_log[1] not in warehouse:
                       warehouse[temp_log[1]] = temp_log[2], temp_log[3]
                  else:
                    #    print("!"*80)
                       di_prize, di_qty = warehouse[temp_log[1]] 
                       new_prize = int(di_prize) + int(temp_prize)
                       new_qty = int(di_qty)  + int(temp_quantity)
                       warehouse[temp_log[1]] = str(new_prize), str(new_qty) 
                    #    print(f"Wartosći slownik", new_prize, new_qty)
                    #    print("!"*80)
               #    for key in warehouse:
               #         print(f"Klucz - {key}. Wartość: - {warehouse[key]}\n" )
                  logs.append(temp_log)
                  print("*"*width)
                  continue
             elif temp_date == "konto":
                  print("*"*width)
                  print(f"Saldo wynosi: {balance}")
                  print("*"*width)
                  continue
             elif temp_date == "magazyn":
                  if warehouse:
                       print("*"*width)
                       for key in warehouse:
                            print(f"Towar - {key}. Wartość: - {warehouse[key]}" )
                       print("*"*width)
                  else:
                       print("*"*width)
                       print("Magazyn pusty")
                       print("*"*width)
                  continue
             elif temp_date == "przeglad":
                  if logs:
                       print("*"*width)
                       for count, value in enumerate(logs):
                            print(f"Log nr {count} {value}")
                       print("*"*width)
                  else:
                       print("*"*width)
                       print("Brak logu")
                       print("*"*width)
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

   
  

