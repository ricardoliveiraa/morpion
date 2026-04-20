class Morpion():
    def __init__(self):
        self.jeu=[
            ["","",""],
            ["","",""],
            ["","",""]
        ]
    
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
        Renvoie une liste de tuples qui corresponde à toutes les cases dis^ponibles pour jouer dessus
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
        self.jeu[case[0]][case[1]] = joueur

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
            return True,self.jeu[0][0]
        
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


#Programme principal
if __name__ == "__main__":
    morpion=Morpion()
    utilisateur="O"
    ia="X"

    print(morpion)
    print(morpion.possibilites())