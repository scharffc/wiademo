print("Benvenue sur notre plateforme")
rubriques = ["1- Entreprenariat", "2- santé","3-quitter"]
print(rubriques)
response = input("Qu'est ce qui vous interesse")
if(response=="1"):
    response1 = input("avez vous de l'experience sur l'Entreprenariat?")
    if(response1=="oui"):
        print("Choisissez votre niveau:")
        print ("niveau1: un projet realisé")
        print ("niveau2: plus d'un projet realisé")
      
    else:
        print("TESproject vous permettra de vous perfectionner")
elif(response=="2"):
    print("")
else:
    print("Au revoir")
    

