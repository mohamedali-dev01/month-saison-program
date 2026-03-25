m = int(input("saisir un nombre entre (1-12):"))

match m:
    
    
    case 1|2|12 :
        print("hiver")
    case 3|4|5 :
        print("printemps")
    case 6|7|8 :
        print("ete")
    case 9|10|11 :
        print("automne")
    case _:
        print("erreur")
    