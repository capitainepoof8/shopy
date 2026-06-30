TVA = 0.18
panier = []
menu = [
    {"number":1,"name": "Tchebou Guinar", "price": 1500},
    {"number":2,"name": "Yassa Poullet", "price": 1500},
    {"number":3,"name": "Attieke poulet + Alloco", "price": 3000},
    {"number":4,"name": "Mafé", "price": 1000},
    {"number":5,"name": "Soupe Kandja", "price": 2000},
    {"number":6,"name": "Paella", "price": 2500}
]

print("\n===========welcome-to-shopy==============")

print("1- afficher le menus du jour")
print("2- suprimer un plat du menu")
print("3- liste tous les plas")
print("4- vide mon panier")
print("5- affiche la facture")
print("6- a bientot")


choix =input("entrez votre selection (1-6):")

if choix == "1":
        print("\n============== menus =============")
        for plat in menu:
            print(f"{plat['number']}- {plat['name']}: {plat['price']} FCFA")
        
        ajouter = input("Ajouter (numéro): ")
        if ajouter.isdigit():
            for plat in menu:
                if plat['number'] == int(ajouter):
                    panier.append(plat)
                    print(f" {plat['name']} ajouté")
                    break
                input("\nAppuyez sur Entrer pour continuer...")
elif choix == "2":
        print("\n============ PANIER =============")
        if panier:
            total = 0
            for plat in panier:
                print(f"- {plat['name']}: {plat['price']}")
                total += plat['price']
            print(f"TOTAL: {total} FCFA")
        else:
            print("Panier vide")  
      
