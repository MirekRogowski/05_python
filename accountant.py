import sys
balance =0
warehouse = {}
logs = []

availabe_actions =["saldo", "sprzedaz","zakup","konto","magazyn","przeglad","stop"] 

while True:
    print(f"Dozwolone akcje: {availabe_actions}")
    if (len(sys.argv) == 4 and sys.argv[1]=="saldo") or (len(sys.argv) == 2 and sys.argv[1]=="saldo"):
        if len(sys.argv) == 4:
             logs.append(sys.argv[1:])
             balance = int(sys.argv[2]) 
        while True:
             print(f"Dozwolone akcje: {availabe_actions}")
             temp_date = input("Wprowadz dane: ")
             temp_log = []
             if temp_date == "saldo":
                  temp_log.append(temp_date)
                  temp_date = int(input("Podaj wartość salda: "))
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
                  exit()



               # print(logs)
               # print(f"Saldo: {balance}")
               # print("Dopisz saldo")
               # print(len(sys.argv))
               # exit()
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
        print("No arguments")
        print(logs)
        print(len(sys.argv))
        print(sys.argv)
        exit()

   
  

