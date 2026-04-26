# Importation 
from jeux import *
# Prog Principal
if __name__ == "__main__":
    
    def demande_case(plateau):
        print(plateau)
        print("Cases vides restantes : " + str(plateau.possibilites()))
        ligne = int(input("Choisissez l'indice d'une ligne : "))
        colonne = int(input("Choisissez l'indice d'une colonne : "))
        return (ligne, colonne)
    
    def verification_case_valide(case, plateau):
        assert len(case) == 2
        assert type(case) == tuple
        assert case[0] <= 2 and case[0] >= 0
        assert case[1] <= 2 and case[1] >= 0
        assert case in plateau.possibilites(), "Cette case a déjà été choisi"

    def fin_de_partie(plateau, j_utilisateur, j_ia):
        print(plateau)
        gagnant= plateau.fin_jeu()[1]
        if gagnant == j_ia :
            print("Vous avez perdu, retentez votre chance ;).")
        elif gagnant == j_utilisateur:
            print("Bien joué ! Vous avez gagné.")
        else : 
            print("Match nul.")
    
    def commencer_simulation_premier(): 
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

    def commencer_simulation_deuxieme(): 
        # Variables qui créer le jeu
        j_utilisateur = "O"
        j_ia = "X"
        plateau = Morpion()
        fin_simulation = False

        while fin_simulation == False : 
            # Tour de l'IA de jouer : 
            plateau.jouer(j_ia, meilleur_coup(plateau))
            
            # Vérification si la partie se termine :
            fin_simulation = plateau.fin_jeu()[0]

            if fin_simulation == False : 
                # Tour de l'utilisateur de jouer : 
                case = demande_case(plateau)
                verification_case_valide(case, plateau)
                plateau.jouer(j_utilisateur, case)
                print(plateau)
                
            # Vérification si la partie se termine :
            fin_simulation = plateau.fin_jeu()[0]

        # Annonce de la fin de partie :
        fin_de_partie(plateau, j_utilisateur, j_ia)
#----------------------------IA VS IA---------------------------------
    def commencer_simulation_ia():
        # Variables qui créer le jeu
        j_ia1 = "O"
        j_ia2 = "X"
        plateau = Morpion()
        fin_simulation = False
        while fin_simulation == False : 
            # Tour de l'utilisateur de jouer : 
            print(plateau)
            plateau.jouer(j_ia1, meilleur_coup(plateau))
            print(plateau)

            # Vérification si la partie se termine :
            fin_simulation = plateau.fin_jeu()[0]

            if fin_simulation == False : 
                # Tour de l'IA de jouer : 
                plateau.jouer(j_ia2, meilleur_coup(plateau))
                
            # Vérification si la partie se termine :
            fin_simulation = plateau.fin_jeu()[0]

        # Annonce de la fin de partie :
        print(plateau)
        gagnant= plateau.fin_jeu()[1]
        if gagnant == j_ia1 :
            print("L'ia 1 a gagné.")
        elif gagnant == j_ia2:
            print("L'ia 2 a gagné")
        else : 
            print("Match nul.")

    #commencer_simulation_ia() # Problème : l'IA 1 laisse gagner l'IA 2
    commencer_simulation_premier()