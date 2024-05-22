
class Animal:

    def __init__(self, nom, nourriture_preferee):
        self.nom = nom
        self.nourriture_preferee = nourriture_preferee

    def __str__(self):
        return f"{self.nom} aime manger {self.nourriture_preferee}"


class Zoo:

    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def nourrir_animaux(self):
        for animal in self.animaux:
            print(f"Vous nourrissez {animal.nom} avec {animal.nourriture_preferee}")

    def afficher_animaux(self):
        print("Animaux dans le zoo :\n")
        for animal in self.animaux:
            print(animal)


lion = Animal("Lion", "viande")
elephant = Animal("Éléphant", "herbe")
singe = Animal("Singe", "fruits")

zoo = Zoo()

zoo.ajouter_animal(lion)
zoo.ajouter_animal(elephant)
zoo.ajouter_animal(singe)

print("\n---------------------------------------------\n")

zoo.afficher_animaux()

print("\n---------------------------------------------\n")

zoo.nourrir_animaux()

print("\n---------------------------------------------\n")
