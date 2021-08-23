"""
Une calculatrice à 6 opérations:
1-Addition
2-Soustraction
3-Multiplication
4-Division
5-Modulo(reste)
6-Exposant
"""


# Fonction addition
def addition():
    somme = nbre1 + nbre2
    return somme


# Fonction soustraction
def soustraction():
    soustraire = nbre1 - nbre2
    return soustraire    

# Fonction  multiplication
def multiplication():
    produit = nbre1 * nbre2
    return produit    

# Fonction  division
def division():
    rapport = nbre1 / nbre2
    return rapport   

# Fonction modulo(reste)
def modulo():
    reste = nbre1 % nbre2
    return reste    

# Fonction exposant
def exposant():
    puissance = nbre1 ** nbre2
    return puissance    


#Message qui qui sert de guide à l'utilisateur
print("\nBienvenue dans notre mini-calculatrice ! \nPressez 'a' pour l'addition, \n 's' pour la soustration , \n m pour la multiplication, \n 'd' pour la division, \n 'r' pour le reste \n 'e' pour l'exposant et 'q' pour quitter. Merci !")


while True:

    # saisie qui fait référence au choix de l'utilisateur
    choix=input("\nÀ présent, faites le choix de votre opération : ")


    # liste qui vérifie le choix de l'utilisateur
    verificateur=["a","s","m","d","r","e","q"]

    # Une sorte d'alertement au cas où l'utilisateur ferait un mauvais choix
    while choix not in verificateur:
        print("\nErreur ! vous avez fait autrement.")
        choix=input("\nr Réessayez, S.V.P évitez de faire des choix qui sont hors de la liste ci-pécédente  : ")

    # option qui permet à l'utilisateur d'abandonner le programme
    if choix == "q":
        print("\nAu revoir !")
        break


    # Les nombres entrés par l'utilisateur
    nbre1=int(input("\nLe premier : \n"))
    nbre2=int(input("\nLe second : \n"))

    
    # Les calculs selon le choix de l'utilisateur
    if choix == "a":
        print(addition())
    elif choix == "s":
        print(soustraction())        
    elif choix == "m":
        print(multiplication())
    elif choix == "d":
        print(division()) 
    elif choix == "r":
        print(modulo())
    elif choix == "e":
        print(exposant())                                 