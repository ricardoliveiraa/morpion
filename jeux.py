class Morpion():
    def __init__(self):
        self.jeu=[
            ["","",""],
            ["","",""],
            ["","",""]
        ]
        self.utilisateur="O"
        self.ia="X"
    
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

    def verifier_victoire(self):
        """
        Pour vérifier les vainqueurs ont a fait quelque chose de plus originel que simplement des if et else 
        On remplace les X par des 3 et les 0 par 3 
        Ont fait les sommes des lignes, colonnes et diagonales : Si somme=9 (X vainqueur) et somme=15 (O vainqueur) 
        """
        pass

    def fin_jeu(self):
        pass


#Programme principal
if __name__ == "__main__":
    morpion=Morpion()
    print(morpion)
    print(morpion.possibilites())