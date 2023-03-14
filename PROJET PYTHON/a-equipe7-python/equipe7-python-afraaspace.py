etape1=input("entrer votre nom : ")
print("Bienvenue",etape1," dans notre complexe AFRAA'S space.")
print()
print("Notre complexe comprend trois destinations : \n Boutique, Espace de conseils capillaires et Restaurant." )
destination=int(input("entrer votre destination: \n 1 pour aller au Restaurant\n 3 pour espace de conseils capillaires\n 2 pour la Boutique "))
if(destination==1):
    print("Bienvenue dans notre restaurant.Nous allons vous présenter notre menu:")
    choix = input("Choisir un entrée /n A pour akaras  /n B pour  pastels /  ")
    if (choix =="A"):
                  print("nous allons vous servir vos akaras dans 5 mn")
    elif (choix =="B"):
                  print("nous allons vous servir vos pastels dans 5 mn")
    choix1 = input("Choisir un plat de résistance /n G pour garba  /n D pour djollof rice  /  ")              
    if (choix1 =="G"):
                    print("nous allons vous servir votre garba dans 5 mn")
    elif (choix1 =="D"):
                   print("nous allons vous servir votre djollof rice dans 5 mn")
    choix2 =input("Choisir un dessert /n T pour thiakry /n F pour bissap")
    if (choix =="T"):
                   print("nous allons vous servir votre thiakry dans 5 mn")
    elif(choix2 =="F"):
                print("nous allons vous servir votre bissap dans 5 mn")
elif(destination==2):
    print("produits /n robes en wax /n pantalons en wax /n toth bag wax /n bracelets de perles ")
elif(destination==3):
    print("bienvenue dqns notre espace de conseils capillaires")
