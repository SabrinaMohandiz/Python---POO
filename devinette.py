import random

class JeuDeDevinette:

    def __init__(self):
        self.nb_deviner = random.randint(1, 100)
        self.nb_essais = 0

    def deviner(self, proposition):
        self.nb_essais += 1
        if proposition < self.nb_deviner:
            return "Trop petit"
        elif proposition > self.nb_deviner:
            return "Trop grand"
        else:
            return True



devinette = JeuDeDevinette()

print("Devinez le nombre entre 1 et 100")

while True:
    try:
        proposition = int(input("Entrez votre proposition: "))
        resultat = devinette.deviner(proposition)
        if resultat == True:
            print(f"Vous avez deviné le nombre {devinette.nb_deviner} en {devinette.nb_essais} essais.")
            break
        print(resultat)

    except ValueError:
        print("Veuillez entrer un nombre valide.")
