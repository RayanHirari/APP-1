
def produit_filtre(csv_manip, produit):
    """
    Cette fonction cree une liste de liste uniquement avec un produit specifique.

    Parametres:
    csv_manip(list): liste de liste du csv que je veux trier.
    produit(str): Nom du produit que je cherche.
    Renvoi:
    csv_produit(list):liste de liste; les sous listes sont composees forcement des infos du produit souhaite.
    """
    #initier ma variable que je veux renvoyer
    csv_produit = []

    #parcourir ligne par ligne dans csv entree
    for ligne in csv_manip:
        if ligne[1] == produit: #si je trouve le produit au niveau de l'index 1 de la ligne
            csv_produit.append(ligne)

    return csv_produit

def date_filtre(csv_manip, date):
    """
    Cette fonction cree une liste de liste uniquement avec une date specifique.

    Parametres:
    csv_manip(list): liste de liste du csv que je veux trier.
    date(str): date que je cherche.
    Renvoi:
    csv_date(list):liste de liste; les sous listes sont composees forcement des infos de la date souhaite.
    """
    #initier ma variable que je veux renvoyer
    csv_date = []

    #parcourir ligne par ligne dans csv entree
    for ligne in csv_manip:
        if ligne[4] == date: #si je trouve la date au niveau de l'index 4 de la ligne
            csv_date.append(ligne)

    return csv_date

def prix_filtre(csv_manip, prix):
    
    """
    Cette fonction cree une liste de liste uniquement avec un prix specifique.

    Parametres:
    csv_manip(list): liste de liste du csv que je veux trier.
    prix(str): prix que je cherche. faites en sorte qu'il soit un float converti en str.
    Renvoi:
    csv_prix(list):liste de liste; les sous listes sont composees forcement des infos du prix souhaite.
    """
    #initier ma variable que je veux renvoyer
    csv_prix = []

    #parcourir ligne par ligne dans csv entree
    for ligne in csv_manip:
        if float(ligne[3]) == prix: #si je trouve le prix au niveau de l'index 3 de la ligne
            csv_prix.append(ligne)

    return csv_prix

def quantmin_filtre(csv_manip, quantite):
    """
    Cette fonction cree une liste de liste avec un quantite minimum specifique.

    Parametres:
    csv_manip(list): liste de liste du csv que je veux trier.
    quantite(int): Nom du produit que je cherche. 
    Renvoi:
    csv_produit(list):liste de liste; les sous listes sont composees forcement des infos du produit souhaite.
    """
    #initier ma variable que je veux renvoyer
    csv_quantmin = []
    #parcourir ligne par ligne dans csv entree
    for ligne in csv_manip:
        if int(ligne[2]) >= quantite: #si je trouve la bonne quantite au niveau de l'index 1 de la ligne
            csv_quantmin.append(ligne)

    return csv_quantmin

def quantmax_filtre(csv_manip, quantite):
    """
    Cette fonction cree une liste de liste avec un quantite minimum specifique.

    Parametres:
    csv_manip(list): liste de liste du csv que je veux trier.
    quantite(int): Nom du produit que je cherche. 
    Renvoi:
    csv_produit(list):liste de liste; les sous listes sont composees forcement des infos du produit souhaite.
    """
    #initier ma variable que je veux renvoyer
    csv_quantmax = []
    #parcourir ligne par ligne dans csv entree
    for ligne in csv_manip:
        if int(ligne[2]) <= quantite: #si je trouve la bonne quantite au niveau de l'index 1 de la ligne
            csv_quantmax.append(ligne)

    return csv_quantmax
