import sys
import os
width, height =os.get_terminal_size()
width = width - 1
balance =0
warehouse = {}
logs = []

                            
availabe_actions =["saldo", "sprzedaz","zakup","konto","magazyn","przeglad","stop"] 


if (len(sys.argv) == 4 and sys.argv[1]=="saldo") or (len(sys.argv) == 2 and sys.argv[1]=="saldo"):
     logs.append(sys.argv[1:])
     balance = int(sys.argv[2])
elif (len(sys.argv) == 5 and sys.argv[1]=="sprzedaz") or warehouse :
     print("\nMagazyn jest pusty\n")
     exit()
elif (len(sys.argv) == 5 and sys.argv[1]=="zakup") or balance :
     print("\nBrak salda\n")
     exit()

while True:
     print(f"Dozwolone akcje: {availabe_actions}\n")
     action = input("Wybierz akcje: ")
     temp_log = []
     if action == "saldo":
          new_balance = int(input("Podaj wartość salda: "))
          balance += new_balance
          comments = input("Komentarz: ")
          logs.append([action, new_balance, comments])
          print(f"\nWartość salda: {balance} \n")
          continue
     elif action == "sprzedaz":
          #empty warehause
          if not warehouse :
               print("\nMagazyn jest pusty proszeę zakupić toawr.\n")
               continue
          prd_id = input("Nazwa towaru: ")
          if not prd_id in warehouse:
               print("\nBrak towaru  w magazanie, proszę towar  wybrać z poniższej listy:  ")
               for key in warehouse:
                    print(f"{key} - {warehouse[key]} sztuk" )
               continue

     #    Sprawdzenie magazymanu
          # if not warehouse.get(action,0) :
          #      print("\nBrak towaru  w magazanie, proszę twowr z poniższej listy:  ")
          #      for key in warehouse:
          #           print(f"{key} - ilość: - {warehouse[key]}" )
          #      continue
          prd_prize = int(input("Cena produktu: "))
          prd_qty = int(input("Ile produktów: "))
          #remove item from warehouse
          if (warehouse[prd_id] - prd_qty) < 0:
               print(f"Chcesz sprzedać {prd_qty} {prd_id} w magazynie tylko {warehouse[prd_id]}/n ")
          warehouse[prd_id] -= prd_qty   
          balance += prd_prize * prd_qty
          logs.append([action, prd_id, prd_prize, prd_qty])
          print(f"\nSaldo wynosi: {balance}\n")
          continue
     elif action == "zakup":
          if balance <= 0:
               print("\nSaldo wynosi: 0. Nie można kupić towaru\n ")          
          prd_id = input("Nazwa towaru: ")
          prd_prize = int(input("Cena produktu: "))
          prd_qty = int(input("Ile produktów: "))
          if prd_prize * prd_qty > balance:
               print(f"\nNie mozna dokonac zakupu. Za małe saldo: {balance}\n")
               continue
          balance -= prd_prize * prd_qty
          if prd_id in warehouse:
               #add quntity to warehouse
               warehouse[prd_id] += prd_qty          
          else:
               #add item to warehouse
               warehouse[prd_id] = prd_qty
          logs.append([action, prd_id, prd_prize, prd_qty])
          print(f"\nSaldo wynosi: {balance}\n")
          continue
     elif action == "konto":
          print(f"\nSaldo wynosi: {balance}\n")
          continue
     elif action == "magazyn":
          if warehouse:
               print("Towar w magazynie.")
               for key in warehouse:
                    print(f"\n {key} - {warehouse[key]} sztuk\n" )
          else:
               print("\nMagazyn pusty.\n")
          print(f"\nSaldo wynosi: {balance}\n")
          continue
     elif action == "przeglad":
          if logs:
               for count, value in enumerate(logs):
                    print(f"Log nr {count} {value}")
          else:
               print("\nBrak logu\n")

          continue
     elif action == "stop":
          print("\nKoniec.")
          print(f"\nSaldo wynosi: {balance}\n")
          exit()

