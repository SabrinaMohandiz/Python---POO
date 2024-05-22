import random

class Carte:

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f" - {self.valeur} de {self.couleur}"

    def __repr__(self):
        return self.__str__()


class PaquetDeCartes:

    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Coeur', 'Carreaux', 'Trèfles', 'Piques']

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in self.valeurs for couleur in self.couleurs]
        self.melanger()

    def melanger(self):
        random.shuffle(self.paquet)

    def distribuer(self):
        if len(self.paquet) > 0:
            return self.paquet.pop()
        else:
            return None

    def __str__(self):
        return ''.join('[ ' + str(carte) + ' ] - ' for carte in self.paquet)

    def __repr__(self):
        return self.__str__()

paquet = PaquetDeCartes()

print("\n---------------------------------------------\n")
print("Paquet de cartes mélangé:\n")
print(paquet)
print("\n---------------------------------------------\n")

paquet.melanger()

print("\nDistribution de 8 cartes:")
for _ in range(8):
    carte = paquet.distribuer()
    print(carte)

paquet.melanger()

print("\n---------------------------------------------\n")

print("Paquet de cartes restant:\n")
print(paquet)

print("\n---------------------------------------------\n")
