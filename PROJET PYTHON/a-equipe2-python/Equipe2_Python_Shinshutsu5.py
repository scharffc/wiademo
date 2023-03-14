print("Ohayo")
app="Bienveznue dans Shinshutsu5,une application conçue pour les orphelins handicapés en Afrique"
print(app)
print("Voici nos differentes rubriques")
rubriques = ["1- DIVERTISSEMENT", "2- ACTUALITES,","3_RENSEIGNEMENTS",
             "4_ASSISTANCE PSYCHOLOGIQUE","5_COURS A DOMICILE"]
print(rubriques)
question=input("Sur quelle plateforme voulez vous vous rendre ?")
if(question=="1"):
    print("Vous avez choisi Divertissement.['Musique','Film','Jeux','BD','Danse']")
elif(question=="2"):
     print("Vous avez choisi Actualité.['Santé','Education','Sport','Economie','Culture']")
elif(question=="3"):
    print("Vous avez choisi Renseignement.")
elif(question=="4"):
    print("Vous avez choisi ASSISTANCE PSYCHOLOGIQUE.")
elif(question=="5"):
    print("Vous avez choisi COURS A DOMICILE.")
else:
    print("Veuillez choisir parmi les chiffres dans le menu")
print("Merci")
