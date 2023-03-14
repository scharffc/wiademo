print("Bienvenue sur notre plateforme fagarou mo gën fadju!")
print("Quelle est votre langue?")
print("1 = Wolof, 2 = Anglais, 3 = Français")
option = int(input("Choisissez une langue:"))
if(option == 1):
    print("no toudou?")
    tour = input("Bindal sa tour: ")
    print("Lane nga done?")
    print("1=Goor")
    print("2=jiggen")
    sexe = int(input("tannal ci niar yi: "))
    print ("Niaata att nga am")
    att = int(input("Dougueleul sa att: "))
    print("No dissé")
    diss = int(input("dougueleul sa dissay: "))
    print("Nane nga tolou")
    ndiol = int(input("Dougueuleul sa ndiolay: "))
    def imc(p,t):
        imc = p/(t**2)
        return(imc)
    val = imc(diss,ndiol)
    print("Sa IMC mongui tolou ci: ", val)
    if (val < 18.5):
        print("Danga sew lol ci sa att té lolou bakhoul")
        print("Ioe naka ngay doundé")
        print("1= dangay faral di lekk lou niin , 2= dangay faral di lekk lou saff soukeur torop, 3= Faralo di yeungeul sa yaram, 4= do lekk lou beuri")
        tam = int(input("tanal bene: "))
        if (tam == 1):
            print("Lou niin bakhoul ci sa wergu yaram wakhoumalak ioe mi nga khamné danga sew lool.")
            print("Motakh nga wara gen lekk niam you melni niébé, haricots, lentilles..., niam you am guerté tamit dina bakh ci ioe, beurre,fromage, bo tamé di lekk yoyoudinga gueneu diss té lolou mo gen ci sa wergu ")
        elif(tam == 2):
            print("Lou saf soukeur bakhna wayé lou eup tourou soukeur bou eup day indi diabete té bobou febar ray domou adama you bari")
    
    
    
            
    
