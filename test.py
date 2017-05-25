import math	#importe tout math et le place dans un nouveau namespace nommé 'math'
			#les appels se font alors en math.xxx (math.sqrt(5), ...)
### from math import sqrt #-> n'importe que sqrt et le place dans le namespace courant (pas 'math')
### from math import *    #-> importe tout math et met tout dans le namespace courant
import os
from multiplie import *


print("coucou")
a=1
#while 1:
#	a=0

def multiplie_7(n):
	return 7*n

def table_7():
	i=0
	while i<7:
		print(i, " x 7 = ", multiplie_7(i))
		i=i+1

table_7()

####passage de paramètres et valeurs par défaut
def fonc(a=1, b=2, c=3, d=4, e=5):
	print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)

fonc()
fonc(4)
fonc(b=8, d=5)
fonc(b=35, c=48, a=4, e=9)

####On ne peut pas surcharger une fonction en python
def exemple():
    print("Un exemple d'une fonction sans paramètre")

exemple()

def exemple(): # On redéfinit la fonction exemple
    print("Un autre exemple de fonction sans paramètre")

exemple()

####fonctions lambda	x:f(x)
f = lambda x: x*x
print("le carré de 5 est ", f(5));

table(8, 12)

####forme minimale (à éviter) -> try: bloc à essayer		except: bloc a executer en cas d'erreur
annee = input()
try:
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")

####forme complète -> try: blabla	except <type de l'exception>: blabla	else: blabla	finally: blabla
try:
	resultat = numerateur / denominateur
except NameError:
	print("La variable numerateur ou denominateur n'a pas été définie")
except TypeError:
	print("La variable numerateur ou denominateur ne connait pas la division")
except ZeroDivisionError:
	print("La variable denominateur est égale à 0")
else:	#si aucun des except n'est executé
    print("Le résultat obtenu est", resultat)
finally:	#executé qu'il y ai eu des erreurs ou non
	print("coucou")

####lever une exception grâce à assert <test>
print("entrer un chiffre inférieur à 10 (ou supérieur si vous êtes un ouf)")
var=input()
var=int(var)
assert var <= 10

####lever une exception directement grâce à raise <type de l'exception>(<message à afficher>)
print("voulez-vous lever une exception ? [y/n]")
var=input()
if var == 'y' or var == 'Y':
	raise ValueError("vous avez décidé de lever une exception")
else:
	print("vous faites là un choix avisé")
	
####Formater les chaines de char
prenom="Paul"
nom="Dupont"
age=21
print("Je m'appelle {0} {1} et j'ai {2} ans".format(prenom, nom, age))

date="Dimanche 24 juillet 2011"
heure="17:00"
print("cela s'est produit le {} à {}.".format(date, heure)) #pas obligé de mettre les indices

adresse="""
 {no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse) #on peut aussi mettre les noms des variables
	
os.system("pause")