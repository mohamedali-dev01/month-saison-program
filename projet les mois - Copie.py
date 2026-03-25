mois = ["janvier" , "fevrier" , "mars" , "avril" , "mai" , "juin" , "juillet" , "aout" , "septembre" , "octobre" , "novembre" , "decembre"]
num = int(input("entrer un numero (1-12):"))


for i in range(12) :
    if i + 1 == num :
        
        print("le mois correspondant est:", mois[i])
        