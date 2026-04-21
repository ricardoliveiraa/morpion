# Importation 
from jeux import *
# Prog Principal
if __name__ == "__main__":
    
    def demande_case(plateau):
        print(plateau)
        ligne = int(input("Choisissez l'indice d'une ligne : "))
        colonne = int(input("Choisissez l'indice d'une colonne : "))
        print((ligne, colonne))
        return (ligne, colonne)
    
    def verification_case_valide(case):
        assert len(case) == 2
        assert type(case) == tuple
        assert case[0] <= 2 and case[0] >= 0
        assert case[1] <= 2 and case[1] >= 0

    def commencer_simulation():
        plateau = Morpion()
        case = demande_case(plateau)
        verification_case_valide(case)

commencer_simulation()