rubriques=["1-fournitures","2-nourritures","3-cosmétique","4-foire aux livres","5-Au revoir!"]
print(" bonjour! Bienvenue dans Golden Store!")
while(True):
    print(rubriques)
    option=int(input("entrer votre choix: "))
    if(option==1):
        print("vous etes dans la rubrique fournitures")
    elif(option==2):
        print("vous etes dans la rubrique nourritures")
    elif(option==3):
        print("vous etes dans la rubrique cosmétique")
    elif(option==4):
        print("vous etes dans la rubrique foire aux livres")
    elif(option==5):
        print("Au revoir!")
        break
    else:
        print("error!")
        break
    
    
    

