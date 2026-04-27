# Importation 
from time import time
from jeux import *
def demande_case(plateau):
    """
    Demande l'indice de la ligne et de la colonne à jouer
    Renvoie le tuple de la case à jouer
    Args : 
        plateau (Objet : Morpion) : plateau actuel
    """
    print(plateau)
    print("Cases vides restantes : " + str(plateau.possibilites()))
    ligne = int(input("Choisissez l'indice d'une ligne : "))
    colonne = int(input("Choisissez l'indice d'une colonne : "))
    return (ligne, colonne)

def verification_case_valide(case, plateau):
    """
    Vérifie si la case donnée par le joueur est valide
    Args : 
        case (tuple) : case donnée par le joueur
        plateau (Objet : Morpion) : plateau actuel
    """
    assert len(case) == 2
    assert type(case) == tuple
    assert case[0] <= 2 and case[0] >= 0
    assert case[1] <= 2 and case[1] >= 0
    assert case in plateau.possibilites(), "Cette case a déjà été choisi"

def fin_de_partie(plateau, j_utilisateur, j_ia):
    """
    Renvoie un message de fin de partie en fonction de l'état du jeu : Egalité ou Victoire
    et en annonçant le vainqueur en cas de Victoire
    Args : 
        plateau (Objet : Morpion) : plateau actuel
        j_utilisateur (str) : symbole de l'utilisateur
        j_ia (str) : symbole de l'ia
    """
    print(plateau)
    gagnant= plateau.fin_jeu()[1]
    if gagnant == j_ia :
        print("Vous avez perdu, retentez votre chance ;).")
    elif gagnant == j_utilisateur:
        print("Bien joué ! Vous avez gagné.")
    else : 
        print("Match nul.")

def commencer_simulation():
    """
    Lancement d'une partie de Morpion contre l'IA
    L'utilisateur joue en premier
    """
    # Variables qui créer le jeu
    j_utilisateur = "O"
    j_ia = "X"
    plateau = Morpion()
    fin_simulation = False

    while fin_simulation == False : 
        # Tour de l'utilisateur de jouer : 
        case = demande_case(plateau)
        verification_case_valide(case, plateau)
        plateau.jouer(j_utilisateur, case)
        print(plateau)

        # Vérification si la partie se termine :
        fin_simulation = plateau.fin_jeu()[0]

        if fin_simulation == False : 
            # Tour de l'IA de jouer : 
            plateau.jouer(j_ia, meilleur_coup(plateau))
            
        # Vérification si la partie se termine :
        fin_simulation = plateau.fin_jeu()[0]

    # Annonce de la fin de partie :
    fin_de_partie(plateau, j_utilisateur, j_ia)
    
# Prog Principal
if __name__ == "__main__":

    #commencer_simulation()

    t1=time()
    min_max(Morpion(),9,"O")
    t2=time()

    print("Minmax a pris ce temps pour trouver la meilleur branche avec un plateau vide : ", str(t2-t1))
    
    t1=time()
    alpha_beta(Morpion(),-float("inf"),float("inf"),9,"O")
    t2=time()

    print("Alphabeta a pris ce temps pour trouver le meilleur branche avec un plateau vide : ", str(t2-t1))