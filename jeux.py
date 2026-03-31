class Morpion():
    def __init__(self):
        jeu=["" for _ in range(9)]
        utilisateur="O"
        ia="X"
    
    def afficher_jeu(self):
        print(self.jeu[0] + " | " + self.jeu[1] + " | " + self.jeu[2])
        print("---------")
        print(self.jeu[3] + " | " + self.jeu[4] + " | " + self.jeu[5])
        print("---------")
        print(self.jeu[6] + " | " + self.jeu[7] + " | " + self.jeu[8])