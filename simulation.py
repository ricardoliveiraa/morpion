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
        # Au tour de l'utilisateur de jouer : 
        case = demande_case(plateau)
        verification_case_valide(case)
        plateau.jouer(j_utilisateur, case)
        print(plateau)

        # Au tour de l'IA de jouer : 
        


commencer_simulation()