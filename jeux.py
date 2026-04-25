class Morpion():
    def __init__(self,jeu=[["","",""],["","",""],["","",""]]):
        self.jeu=jeu
    
    def __str__ (self):
        msg=""
        for k in range(3):
            ligne=""
            for i in self.jeu[k]:
                if i == "":
                    ligne += " _ |"
                else:
                    ligne += " " + i + " |"
            msg += ligne[:-1] + "\n"
        return msg
        
    def possibilites(self):
        """
        Renvoie une liste de tuples qui corresponde à toutes les cases disponibles pour jouer dessus
        """
        res=[]
        for i in range(3):
            for j in range(3):
                if self.jeu[i][j] == "":
                    res.append((i,j))
        return res

    def jouer(self,joueur,case):
        """_summary_

        Args:
            joueur (str): Soit "X" soit "O" tout ça est géré dans la méthode général du jeu
            case (tuple): coordonnées de la case à jouer
        """
        i,j=case
        self.jeu[i][j] = joueur

    def est_rempli(self):
        """
        Vérifie si le morpion est rempli s'il n'y a plus de coups possibles à jouer
        """
        return self.possibilites() == []

    def verifier_vainqueur(self):
        """
        On vérifie toutes les possibilités de victoire 
        Renvoye le symbole du vainqueur ou alors None 
        """
        #Verification des lignes
        if self.jeu[0][0]==self.jeu[0][1]==self.jeu[0][2]!="":
            return True,self.jeu[0][0]
        elif self.jeu[1][0]==self.jeu[1][1]==self.jeu[1][2]!="":
            return True,self.jeu[1][0]
        elif self.jeu[2][0]==self.jeu[2][1]==self.jeu[2][2]!="":
            return True,self.jeu[2][0]

        #Verification des colonnes
        elif self.jeu[0][0]==self.jeu[1][0]==self.jeu[2][0]!="":
            return True,self.jeu[0][0]
        elif self.jeu[0][1]==self.jeu[1][1]==self.jeu[2][1]!="":
            return True,self.jeu[0][1]
        elif self.jeu[0][2]==self.jeu[1][2]==self.jeu[2][2]!="":
            return True,self.jeu[0][2]

        #Verification des diagonales
        elif self.jeu[0][0]==self.jeu[1][1]==self.jeu[2][2]!="":
            return True,self.jeu[0][0]
        elif self.jeu[0][2]==self.jeu[1][1]==self.jeu[2][0]!="":
            return True,self.jeu[0][2]
        
        #Résultat si il n'y a pas de vainqueur
        else:
            return False,None

    def fin_jeu(self):
        vainqueur=self.verifier_vainqueur()
        if vainqueur[0]:
            return True,vainqueur[1]
        elif self.est_rempli():
            return True,"Egalite"
        else:
            return False,"Continue"

    def evaluer(self):
        """
        Evalue le plateau actuel qui est une situation finale et attribut un score à ce plateau 
        """
        self.situation = self.fin_jeu()[1]
        if self.situation == "X":
            return 100
        elif self.situation == "O":
            return -100
        else:
            return 0
        
# Algorithme MinMax

def coups_prochains_possibles(plateau,joueur):
    """
    Renvoye un eliste comportant les coups possibles fait par l'adversaire dans son prochain coup
    """
    situations=[]
    coups_possibles=plateau.possibilites()
    for coup in coups_possibles:
        prochain_plateau=Morpion([ligne[:] for ligne in plateau.jeu])
        prochain_plateau.jouer(joueur,coup)
        situations.append(prochain_plateau)
    return situations            

def min_max(plateau,profondeur,joueur):
    """
    Renvoye la valeur minmax (score de la branche de l'arbre de possibilités à choisir)
    """
    if plateau.fin_jeu()[0] or profondeur == 0:
        return plateau.evaluer()

    if joueur == "X":
        suivants = coups_prochains_possibles(plateau, "X")
        return max([min_max(suivant, profondeur-1, "O") for suivant in suivants])
    else:
        suivants = coups_prochains_possibles(plateau, "O")
        return min([min_max(suivant, profondeur-1, "X") for suivant in suivants])

def meilleur_coup(plateau):
    """
    Renvoie le meilleur coup à jouer pour X (l'IA)
    sous la forme d'un tuple (i, j)
    """
    meilleur_score = -float("inf")
    meilleur_coup = None

    # On teste tous les coups possibles
    for coup in plateau.possibilites():
        # copie du plateau
        copie = Morpion([ligne[:] for ligne in plateau.jeu])

        # X joue ce coup
        copie.jouer("X", coup)

        # on évalue la suite avec minmax
        score = min_max(copie, 9, "O")

        # si meilleur score : on garde
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = coup

    return meilleur_coup


#Programme principal
if __name__ == "__main__":
    #Dans le jeu on va supposer que X correspond au programme et O l'utilisateur
    morpion=Morpion([["X","","O"],["","X",""],["X","O","O"]])


    print(min_max(morpion,9,"X"))
    print(meilleur_coup(morpion))