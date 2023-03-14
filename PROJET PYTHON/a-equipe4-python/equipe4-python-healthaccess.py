liste_option1=["ventoline" ,"corticoides" ,"bronchodilatateurs"]
liste_option2=["efferalgan" ,"paracétamol" ,"panadol"]
liste_option3=["parégorique" ,"doliprane" ,"spasfon"]
age=int(input("Entrez votre age: "))
if (age>=0 and age<=3):
    print("Le patient est un bébé!")
elif (age>=3 and age<=20):
    print("Le patient est un enfant!")
elif(age>=20 and age<=60):
    print("Le patient est un adulte!")
elif(age>60):
    print("Le patient est un sénior!")
print("Que ressentez-vous?")
symptômes=["1.problémes respiratoires" ,"2.maux de tête" ,"3.maux de ventre"]
print(symptômes)
option=int(input("Entrez votre réponse: "))
if (option==1):
    print("Vous souffrez d'asthme!")
    print("Nous vous proposons ces médicaments: " , liste_option1)
elif (option==2):
    print("Vous souffrez de surmenage!")
    print("Nous vous proposons ces médicaments: " , liste_option2)
elif (option==3):
    print("Vous souffrez de fortes diarrhées")
    print("Nous vous proposons ces médicaments: " , liste_option3)
else:
    print("Nous ne reconnaisons pas vos symtomes")
print("Prenez Soin de vous ! Au revoir !")




