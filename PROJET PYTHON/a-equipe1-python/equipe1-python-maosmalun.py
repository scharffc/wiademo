
print("Bienvenue sur MAOS MALUN, l'application qui vous permettra de gérer votre budget convenablement")
nom=input("entrez votre nom s'il vous plait:")
print("Salut",nom)
print("Dans la vie de tous les jours, nous rencontrons tous et toutes des soucis pour gérer notre argent")
print("C'est la raison pour laquelle 4 jeunes entrepreneuses ont crée MAOS MALUN pour vous faciliter la vie")
budget=int(input("veuillez entrer le montant de votre budget:"))
if( budget<=200000):
    print("vous devrez dépenser pour la nourriture:",str(budget*40/100))
    print(" pour les loisirs:",str(budget*5/100))
    print(" pour le transport:",str(budget*15/100))
    print(" pour la santé et l'hygiène:",str(budget*10/100))
    print(" pour les factures:",str(budget*20/100))
    print(" et enfin vous devrez économiser:",str(budget*10/100))
else:
    print("vous devrez dépenser pour la nourriture:",str(budget*35/100))
    print(" pour les loisirs:",str(budget*10/100))
    print(" pour le transport:",str(budget*10/100))
    print(" pour la santé et l'hygiène:",str(budget*8/100))
    print(" pour les factures:",str(budget*20/100))
    print(" et enfin vous devrez économiser:",str(budget*17/100))
print(nom,"nous espérons que vous allez gérer l'argent comme nous vous l'avons recommandé")
note=int(input("veuillez noter l'application sur 10:"))
if(note<5):
    print("nous nous excusons du désagremment que vous avez eu à avoir")
elif(note>=5 and note<8):
    print("merci nous apporterons des changements necessaires pour une utilisation maximale de l'application")
else:
    print("nous vous remercions infiniment")
print("AU REVOIR ,A LA PROCHAINE")

