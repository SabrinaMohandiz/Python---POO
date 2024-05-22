import random

class De:

    def lancer(self):
        return random.randint(1, 6)


de = De()
resultat = de.lancer()
print(f"Résultat du lancer de dé: {resultat}")