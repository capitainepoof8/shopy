TVA = 0.18
panier = []
menu = [
    {"number":1,"name": "Tchebou Guinar", "price": 1500},
    {"number": 1, "name": "Tchebou Guinar", "price": 1500},
    {"number": 2, "name": "Yassa Poullet", "price": 1500},
    {"number": 3, "name": "Attieke poulet + Alloco", "price": 3000},
    {"number": 4, "name": "Mafé", "price": 1000},
    {"number": 5, "name": "Soupe Kandja", "price": 2000},
    {"number": 6, "name": "Paella", "price": 2500}
]





def ajouter():
    ajouter = input("\nAjouter au panier (numéro) ou Entrée pour revenir : ")

    if ajouter == "":
        return

    if not ajouter.isdigit():
        print("Numéro invalide.")
        return

    plat_trouve = None
    for plat in menu:
        if plat['number'] == int(ajouter):
            plat_trouve = plat

    if plat_trouve is None:
        print("Numéro invalide.")
        return

    quantite_valide = False
    while not quantite_valide:
        try:
            quantite = int(input("Quantité : "))
            if quantite <= 0:
                print("La quantité doit être supérieure à 0.")
            else:
                quantite_valide = True
        except ValueError:
            print("Entrez un nombre entier valide.")

    # verifie si le plat est deja dans le panier
    deja_present = False
    for article in panier:
        if article['number'] == plat_trouve['number']:
            article['quantite'] = article['quantite'] + quantite
            deja_present = True
            print(f"-> quantité mise à jour pour {plat_trouve['name']}")

    if not deja_present:
        nouvel_article = {
            "number": plat_trouve['number'],
            "name": plat_trouve['name'],
            "price": plat_trouve['price'],
            "quantite": quantite
        }
        panier.append(nouvel_article)
        print(f"-> {plat_trouve['name']} ajouté au panier")


def afficher_menu(menu):
    print("=============== menu du jour ==============")
    if not menu:
        print("le menu est vide")
        return

    for plat in menu:
        print(f"{plat['number']}- {plat['name']}: {plat['price']} FCFA")

    ajouter()


def suprimer_plat(panier):
    if not panier:
        print("\nvotre panier est vide")
        return

    lister_plats(panier)

    numero = input("\nEntrez le numéro du plat à supprimer : ")

    if not numero.isdigit():
        print("Numéro invalide.")
        return

    trouve = False
    for article in panier:
        if article['number'] == int(numero):
            panier.remove(article)
            print(f"-> {article['name']} supprimé du panier")
            trouve = True
            break

    if not trouve:
        print("Ce plat n'est pas dans le panier.")


def lister_plats(panier):
    if not panier:
        print("\nvotre panier est vide")
        return

    print("\n--- CONTENU DU PANIER ---")
    for article in panier:
        print(f"{article['number']}- {article['name']} x{article['quantite']} - {article['price']} FCFA/u")


def vider_panier(panier):
    panier.clear()
    print("\nvotre panier a été vidé")


def afficher_facture(panier):
    if not panier:
        print("\nvotre panier est vide, aucune facture à afficher")
        return

    print("=============== merci d'avoir passé commande ===================")
    print("====================== votre facture ==========================")

    montant_ht = 0
    for article in panier:
        sous_total = article['price'] * article['quantite']
        montant_ht = montant_ht + sous_total
        print(f"{article['name']} x{article['quantite']} = {sous_total} FCFA")

    montant_tva = montant_ht * TVA
    montant_ttc = montant_ht + montant_tva

    print(f"\nMontant HT  : {montant_ht} FCFA")
    print(f"TVA (18%)   : {montant_tva} FCFA")
    print(f"Montant TTC : {montant_ttc} FCFA")


def menu_principal():
    print("\n===========welcome-to-shopy==============")
    while True:
        print("\n1- afficher le menu du jour")
        print("2- suprimer un plat du panier")
        print("3- liste tous les plats du panier")
        print("4- vide mon panier")
        print("5- affiche la facture")
        print("6- a bientot")

        choix = input("entrez votre selection (1-6): ")

        if choix == "1":
            afficher_menu(menu)
        elif choix == "2":
            suprimer_plat(panier)
        elif choix == "3":
            lister_plats(panier)
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
    menu_principal()


if __name__ == "__main__":
    main()