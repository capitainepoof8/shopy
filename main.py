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





def ajouter():
    ajouter = input("\nAjouter au panier (numéro) ou Entrée pour revenir : ")
    if ajouter.isdigit():
        
        trouve = False
        for plat in menu:
            if plat['number'] == int(ajouter):
                panier.append(plat)
                print(f"-> {plat['name']} ajouté au panier")
                trouve = True
               
        if not trouve:
            print("Numéro invalide.")
    
    
def afficher_menu(menu):
    print("=============== menu du jour ==============")
    if menu:
        for plat in menu:
            print(f"{plat['number']}- {plat['name']}: {plat['price']} FCFA")
        else:
            print("votre panier est vide")
        ajouter()
        return menu
             
             
             
def suprimer_plat():
    print("")

def lister_plats(menu):
    print



def menu_principal():
    print("\n===========welcome-to-shopy==============")
    while True:
        print("\n1- afficher le menu du jour")
        print("2- suprimer un plat du menu")
        print("3- liste tous les plats")
        print("4- vide mon panier")
        print("5- affiche la facture")
        print("6- a bientot")
 
        choix = input("entrez votre selection (1-6): ")
 
        if choix == "1":
            afficher_menu(menu)
        elif choix == "2":
            suprimer_plat(menu)
        elif choix == "3":
            lister_plats(menu)
        elif choix == "4":
            vider_panier(panier)
        elif choix == "5":
            afficher_facture(panier)
        elif choix == "6":
            print("\nA bientôt !")
            break
        else:
            print("Choix invalide, entrez un chiffre entre 1 et 6.")
 
def main():
    
    menu
    
    
menu_principal()