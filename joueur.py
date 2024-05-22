from de import De

class Joueur:

    def __init__(self, nom, solde_initial):
        self.nom = nom
        self.solde = solde_initial
        self.position = 0

    def payer(self, montant):
        if montant > self.solde:
            print(f"{self.nom} n'a pas assez d'argent pour payer {montant} -> Solde actuel : {self.solde}")
            return False
        else:
            self.solde -= montant
            print(f"{self.nom} a payé {montant} -> Solde restant : {self.solde}")
            return True

    def recevoir(self, montant):
        self.solde += montant
        print(f"{self.nom} a reçu {montant} ->  Solde actuel : {self.solde}")


class Case:

    def __init__(self, nom, cout):
        self.nom = nom
        self.cout = cout

    def atterir(self, joueur):
        print(f"{joueur.nom} atterrit sur {self.nom} avec un coût de {self.cout}")
        joueur.payer(self.cout)


# Définir quelques cases pour le plateau
cases = [
    Case("Case Départ", 0),
    Case("Boulevard de Belleville", 60),
    Case("Rue de Boul", 100),
    Case("Avenue de la République", 140),
    Case("Gare de Lyon", 200),
    Case("Gare du Nord", 200),
    Case("Boulevard des Capucines", 280),
    Case("Avenue des Champs-Élysées", 400)
]

# Créer des joueurs
joueur1 = Joueur("Sabrina1", 1500)
joueur2 = Joueur("Sabrina2", 1500)

# Initialiser le dé
de = De()

# Fonction pour avancer un joueur et gérer l'atterrissage sur une case
def avancer_joueur(joueur, lancer_de, cases):
    joueur.position = (joueur.position + lancer_de) % len(cases)
    case = cases[joueur.position]
    case.atterir(joueur)

# Simulation 3 tours
for tour in range(3):
    print(f"Tour {tour + 1}:")
    print("\n---------------------------------------------\n")
    for joueur in [joueur1, joueur2]:
        print(f"\nJoueur: {joueur.nom}")
        lancer = de.lancer()
        print(f"{joueur.nom} lance le dé et obtient {lancer}")
        avancer_joueur(joueur, lancer, cases)
        print("\n---------------------------------------------\n")
