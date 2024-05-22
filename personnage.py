class Personnage:

    def __init__(self, nom, sante, degats):
        self.nom = nom
        self.sante = sante
        self.degats = degats

    def attaquer(self, autre_personnage):

        autre_personnage.sante -= self.degats
        print(f"{self.nom} attaque {autre_personnage.nom} et lui inflige {self.degats} dégâts")

        if autre_personnage.sante <= 0:
            print(f"{autre_personnage.nom} a été vaincu par {self.nom}")
        else:
            print(f"{autre_personnage.nom} a maintenant {autre_personnage.sante} points de santé")

    def est_vivant(self):
        return self.sante > 0


# Créer deux personnages
personnage1 = Personnage("Guerrier", 100, 20)
personnage2 = Personnage("Mage", 80, 25)

# Boucle de jeu au tour par tour
tour = 1
while personnage1.est_vivant() and personnage2.est_vivant():
    print(f"\n--- Tour {tour} ---\n")
    if tour % 2 != 0:
        personnage1.attaquer(personnage2)
    else:
        personnage2.attaquer(personnage1)
    tour += 1
    print("\n--------------")


print("\nLe combat est terminé")
