import random

class JeuDePendu:

    def __init__(self, liste_mots):
        self.mot_a_deviner = random.choice(liste_mots)
        self.lettres_trouvees = []
        self.lettres_proposees = []
        self.vies_restantes = 6

    def afficher_mot(self):
        mot_masque = ''.join(
            [lettre if lettre in self.lettres_trouvees else '_' for lettre in self.mot_a_deviner]
        )
        return mot_masque

    def proposer_lettre(self, lettre):
        if lettre in self.lettres_proposees:
            print("Vous avez déjà proposé cette lettre.")
            return
        self.lettres_proposees.append(lettre)

        if lettre in self.mot_a_deviner:
            self.lettres_trouvees.append(lettre)
            
            if all(l in self.lettres_trouvees for l in self.mot_a_deviner): # renvoie True si tous les éléments de l'itérable sont vrais 
                print(f"Vous avez deviné le mot: {self.mot_a_deviner}")
                return True
            else:
                return f"Bien joué! Le mot: {self.afficher_mot()}"
        else:
            self.vies_restantes -= 1
            if self.vies_restantes == 0:
                print(f"Vous avez perdu, le mot était: {self.mot_a_deviner}")
                return True
            else:
                print(f"Il vous reste {self.vies_restantes} vies. Le mot: {self.afficher_mot()}")
                return


liste_mots = ["python", "assistante", "administrative", "salaire", "pokemon", "ordinateur", "programmation", "jeu", "pendu"]

jeu = JeuDePendu(liste_mots)

print("Bienvenue au jeu du pendu!")

while True:
    print(jeu.afficher_mot())
    lettre = input("Proposez une lettre: ").lower()
    resultat = jeu.proposer_lettre(lettre)

    if resultat == True:
        break
