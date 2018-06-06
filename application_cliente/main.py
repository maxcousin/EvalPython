from donnees import getDonnees
from Graphique import *


data = getDonnees()
SuperbeGraphique = Graphique(data)
SuperbeGraphique.dessiner()
