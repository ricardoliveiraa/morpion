# Importation 
from jeux import *
# Prog Principal
if __name__ == "__main__":
    
    def demande_case(plateau):
        print(plateau)
        ligne = int(input("Choisissez l'indice d'une ligne : "))
        colonne = int(input("Choisissez l'indice d'une colonne : "))
        return (ligne, colonne)
    
    def verification_case_valide(case):
        assert len(case) == 2
        assert type(case) == tuple
        assert case[0] <= 2 and case[0] >= 0
        assert case[1] <= 2 and case[1] >= 0

    def commencer_simulation():
        # Variables qui créer le jeu
        j_utilisateur = "O"
        j_ia = "X"
        plateau = Morpion()
        fin_simulation = False
        while fin_simulation == False : 
            # Tour de l'utilisateur de jouer : 
            case = demande_case(plateau)
            verification_case_valide(case)
            plateau.jouer(j_utilisateur, case)
            print(plateau)

            # Vérification si la partie se termine :
            fin_simulation = plateau.fin_jeu()[0]

            if fin_simulation == False : 
                # Tour de l'IA de jouer : 
                #plateau.jouer(j_ia, min_max(plateau, 9, j_ia))
                print(plateau)
                
            # Vérification si la partie se termine :
            fin_simulation = plateau.fin_jeu()[0]

        # Annonce de la fin de partie :
        gagnant= plateau.fin_jeu[1]
        if gagnant == j_ia :
            print("Vous avez perdu, retentez votre chance ;).")
        elif gagnant == j_utilisateur:
            print("Bien joué ! Vous avez gagné.")
        else : 
            print("Match nul.")


commencer_simulation()