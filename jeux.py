from time import time
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
        Renvoie une liste de tuples qui corresponde à toutes les cases vides
        """
        res=[]
        for i in range(3):
            for j in range(3):
                if self.jeu[i][j] == "":
                    res.append((i,j))
        return res

    def jouer(self,joueur,case):
        """
        Remplis la case du plateau avec le symbole d'un joueur donné en paramètre
        Args:
            joueur (str): Symbole du joueur
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
        Renvoie le symbole du vainqueur ou alors None s'il n'y a pas de vainqueur
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
        
        #Résultat s'il n'y a pas de vainqueur
        else:
            return False,None

    def fin_jeu(self):
        """
        Renvoie l'état du jeu, s'il y a victoire, égalité ou si le jeu continue
        """
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
        
#----------------------------- Algorithme MinMax-----------------------------------
def coups_prochains_possibles(plateau,joueur):
    """
    Renvoie une liste comportant les coups possibles fait par le joueur en paramètre lors de son tour
    Args:
        plateau (Objet : Morpion): plateau actuel
        joueur (str): symbole du joueur
    """
    situations=[]
    coups_possibles=plateau.possibilites()
    for coup in coups_possibles:
        prochain_plateau=Morpion([ligne[:] for ligne in plateau.jeu])
        prochain_plateau.jouer(joueur,coup)
        situations.append(prochain_plateau)
    return situations            

compteur = 0

def min_max(plateau,profondeur,joueur):
    """
    Renvoie la valeur minmax : le score de la branche
    Args:
        plateau (Objet : Morpion): plateau actuel
        profondeur (int) : maximum d'appel de la fonction récursive 
        joueur (str): symbole du joueur
    """
    #Compteur pour départager en cas d'égalité
    global compteur
    compteur += 1

    #Attribue un score à un plateau s'il représente une situation finale de jeu
    if plateau.fin_jeu()[0] or profondeur == 0:
        return plateau.evaluer()

    #Attribue un score à un plateau s'il représente une situation finale de jeu
    if joueur == "X":
        suivants = coups_prochains_possibles(plateau, "X")
        return max([min_max(suivant, profondeur-1, "O") for suivant in suivants])

    #Attribue un score pour une branche partant d'un coup de l'IA
    else:
        suivants = coups_prochains_possibles(plateau, "O")
        return min([min_max(suivant, profondeur-1, "X") for suivant in suivants])


# -------------------------- ALPHABETA ----------------------------------------
def alpha_beta(plateau,alpha,beta,profondeur,joueur):
    """
    Renvoie le score de la branche en utilisant alphabeta (amélioration de minmax) 
    Args:
        plateau (Objet : Morpion): plateau actuel
        alpha (int) : valeur permettant de bloquer la recherche dans une branche inutile dans un min
        beta (int) : valeur permettant de bloquer la recherche dans une branche inutile dans un max
        profondeur (int) : maximum d'appel de la fonction récursive 
        joueur (str): symbole du joueur qui va jouer après
    """
    #Compteur pour départager en cas d'égalité
    global compteur
    compteur += 1

    #Attribue un score à un plateau s'il représente une situation finale de jeu
    if plateau.fin_jeu()[0] or profondeur == 0:
        return plateau.evaluer()

    #Attribue un score pour une branche partant d'un coup de l'utilisateur
    if joueur == "O":
        suivants = coups_prochains_possibles(plateau, "O")
        v = float("inf")
        for prochain in suivants:
            v = min(v,alpha_beta(prochain,alpha,beta,profondeur-1,"X"))
            if alpha >= v:
                return v
            beta = min(beta,v)
    
    #Attribue un score pour une branche partant d'un coup de l'IA
    else:
        suivants = coups_prochains_possibles(plateau, "X")
        v = -float("inf")
        for prochain in suivants:
            v = max(v,alpha_beta(prochain,alpha,beta,profondeur-1,"O"))
            if v>=beta:
                return v
            alpha = max(alpha,v)
    return v

def meilleur_coup(plateau):
    """
    Renvoie le meilleur coup à jouer pour X (l'IA)
    sous la forme d'un tuple (i, j)
    Args:
        plateau (Objet : Morpion): plateau actuel
    """
    global compteur
    meilleur_score = -float("inf")
    meilleur_coup = None
    rapidite = float("inf")

    # On teste tous les coups possibles
    for coup in plateau.possibilites():
        compteur = 0

        # copie du plateau
        copie = Morpion([ligne[:] for ligne in plateau.jeu])

        # X joue ce coup
        copie.jouer("X", coup)

        # on évalue la suite avec minmax
        score = alpha_beta(copie,-float("inf"),float("inf"), 9, "O")

        # si meilleur score : on garde
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = coup
            rapidite = compteur
        # Si c'est le même score mais en moins de coups
        elif score == meilleur_score and compteur<rapidite:
            meilleur_score = score
            meilleur_coup = coup
            rapidite = compteur
        
    return meilleur_coup

#-----------------------Programme principal------------------------------
if __name__ == "__main__":
    #Dans le jeu on va supposer que X correspond au programme et O l'utilisateur
    print(Morpion([["O", "X", "O"], ["", "X", ""], ["", "", "O"]]))
    print(Morpion([["O", "X", "O"], ["", "X", "X"], ["", "", "O"]]))

    t1=time()
    min_max(Morpion(),9,"O")
    t2=time()

    print("Minmax a pris ce temps pour trouver la meilleur branche avec un plateau vide : ", str(t2-t1))
    
    t1=time()
    alpha_beta(Morpion(),-float("inf"),float("inf"),9,"O")
    t2=time()

    print("Alphabeta a pris ce temps pour trouver le meilleur branche avec un plateau vide : ", str(t2-t1))