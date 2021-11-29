import sys
balance =0
warehouse = {}
logs = []
                            
availabe_actions = ["saldo", "sprzedaz", "zakup", "stop", "konto", "magazyn", "przeglad"] 

while True:
     action = input("Wybierz akcje: \n")
     temp_log = []
     if action == "saldo":
          new_balance = int(input("Podaj wartość salda: "))
          balance += new_balance
          comments = input("Komentarz: ")
          logs.append([action, new_balance, comments])
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
          prd_prize = int(input("Cena produktu: "))
          prd_qty = int(input("Ile produktów: "))
          #remove item from warehouse
          if (warehouse[prd_id] - prd_qty) < 0:
               print(f"\nChcesz sprzedać {prd_qty} {prd_id} w magazynie {warehouse[prd_id]}\n ")
               continue
          warehouse[prd_id] -= prd_qty   
          balance += prd_prize * prd_qty
          logs.append([action, prd_id, prd_prize, prd_qty])
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
          continue
     elif action == "stop":
          logs.append([action])
          break
     else:
          print(f"\nDostępne akcje: {availabe_actions[:3]}")
          print("\nNiedozwolna akcja")
          exit("exit")
if (len(sys.argv) == 4 and sys.argv[1]=="saldo") or (len(sys.argv) == 2 and sys.argv[1]=="saldo"):
     logs.append(sys.argv[1:])
     # add balance
     balance += int(sys.argv[2])
     #print logs
     for row in logs:
          for line in row:
               print(line)
     print("--- >>> saldo")
elif (len(sys.argv) == 5 and sys.argv[1]=="sprzedaz"):
     logs.append(sys.argv[1:])
     #subtract the item 
     warehouse[prd_id] -= int(sys.argv[4])  
     #add balance
     balance += int(sys.argv[4]) * int(sys.argv[4])
     #print logs
     for row in logs:
          for line in row:
               print(line)
     print("--- >>> sprzedaz")
elif (len(sys.argv) == 5 and sys.argv[1]=="zakup"):
     logs.append(sys.argv[1:])
     #add the item 
     warehouse[prd_id] += int(sys.argv[4])  
     #add balance
     balance -= int(sys.argv[4]) * int(sys.argv[4])
     #print logs
     for row in logs:
          for line in row:
               print(line)
     print("--- >>> zakup")
elif (len(sys.argv) == 2 and sys.argv[1]=="konto"):
     print(f"\nSaldo wynosi: {balance}\n")
     print("--- >>> konto")
elif (len(sys.argv) > 1 and sys.argv[1] == "magazyn"):
     logs.append(sys.argv[1:])
     n = len(sys.argv)
     print("Stan magazynu: ")
     for i in range(2, n):
          prd_id = sys.argv[i]
          if prd_id in warehouse:
               print(f"{prd_id} : {warehouse[prd_id]} sztuk" )
          else:
               print(f"{prd_id} : brak poyzcji w magazynie")
     print("--- >>> magazyn")
elif (len(sys.argv) == 4 and sys.argv[1]=="przeglad"):
     logs.append(sys.argv[1:])
     first = int(sys.argv[2])
     last = int(sys.argv[3])
     if first < 1 :
          first = 1
     if last > len(logs) :
          last = len(logs)
     while first <= last:
          print(f"Akcja nr {first} - {logs[first-1]}")
          first += 1
     print("--- >>> przeglad")
else:
     print("\nKoniec")
     exit()