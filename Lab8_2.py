import random
import string


etoile="**************************\n"
print("",etoile,"Générateur de mot de passe\n",etoile)


def mdp_random(longeur_mdp,min,maj,ponctuation,chiffre):

    all = ''

    # En cherchant un peu sur internet, j'ai trouvé qu'on pouvait au lieu de créer 4 dictionnaires utiliser le paquet string :

    if min:
        all += string.ascii_lowercase
    if maj:
        all += string.ascii_uppercase
    if ponctuation:
        all += string.punctuation
    if chiffre:
        all += string.digits

    if not all:
        print("Veuillez sélectionner au moins un type de caractères.")
        return

    mdp = ''.join(random.choice(all) for i in range(longeur_mdp))
    return mdp


longeur_mdp=int(input(print("Saisir la longueur du mot de passe : ")))

min = input("Inclure des lettres minuscules (Sasir 'Oui' ou 'Non') : ").strip().lower() == "oui"
maj = input("Inclure des lettres majuscules (Sasir 'Oui' ou 'Non') : ").strip().lower() == "oui"
ponctuation = input("Inclure des ponctuations (Sasir 'Oui' ou 'Non') : ").strip().lower() == "oui"
chiffre = input("Inclure des chiffres (Sasir 'Oui' ou 'Non') : ").strip().lower() == "oui"



print("Le mot de passe est :",mdp_random(longeur_mdp,min,maj,ponctuation,chiffre))