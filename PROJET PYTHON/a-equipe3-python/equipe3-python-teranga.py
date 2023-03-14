print("Karibu (Bienvenue en swahili)")
rub=["1-Quizz capitales" , "2-Gastronomie africaine" , "3-Que faire de ses restes" , "4-quitter"]
while(True):
    print("Voici le menu")
    print(rub)
    option=int(input('Choisissez une option: '))
    if (option==1):
        print("Bienvenue dans le quizz des capitales des pays africains")
        print("Commencons le quizz !")
        reponse=input("quelle est la capitale du Senegal ?")
        if(reponse=="Dakar" or reponse=="dakar"):
            print("Diadieuf (bravo en wolof) !")
            print("Saviez vous que le Senegal figure dans le top 10 des pays ayant les plus grandes reserves de gaz au monde")
        else:
            print("Danga dioum (tu t'es trompe en wolof!")
    elif (option==2):
        print("Bienvenue dans le menu Gastronomie africaine")
        print("Commençons !")
    elif (option==3):
        print("Bienvenue dans le menu Que faire de ses restes")
        print("Commençons !")
    elif (option==4):
        break
    else:
        print("veuillez bien saisir les valeurs correspondantes au menu")
    reponse = input("voulez-vous reprendre ? Tapez oui ou non")
    if(reponse != "oui" and reponse != 'Oui' and reponse != 'o'):
        break
print("MERCI et AU REVOIR")
