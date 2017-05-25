"""mon docstring du module multipli contenant la fonction table"""

import os

def table(nb, max=10):
    """coucou, tu veux voir ma Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

#Le code qui suit ne sera executé que si multiplie.py est lancé directement
#Lors d'un import ce code ne sera pas executé (car la variable __name__ != __main__ )
if __name__ == "__main__":
    table(4)
    os.system("pause")