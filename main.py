#Générateur de mot de passe automatique

import string
import random

def valider_entier(message):
    while True :
        try:
            n=int(input(message))
        except ValueError:
            print("Ce n'est pas un nombre !")
            continue
        else :
            if n > 0:
                break
            else : print("Ce nombre n'est pas strictement positif !")
    return n

def mot_de_passe() :
    #Toutes les lettre, chiffres et caractères spéciaux
    all_caractere = string.ascii_letters + string.digits + string.punctuation

    #Récupère et assure la validité de l'entrée du nombre de mot de passe voulu
    number = valider_entier("Combien de mots de passe voulez-vous générer ?: ")

    for i in range (1, number+1):
        # Récupère et assure la validité de l'entrée de la longueur du mot de passe
        longueur = valider_entier("Entrer la longueur du mot de passe "  + str(i) + ": " )

        password = "".join(random.choices(list(all_caractere), k=longueur))
        print(">>MDP n" + str(i) + ": " + password)


#Test
mot_de_passe()

#c'est bon

