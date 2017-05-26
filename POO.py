import os

############Les classes
class Personne:
	"""Classe définissant une personne caractérisée par:
	- son nom
	- son prénom
	- son âge
	- son lieu de résidence"""
	
	def __init__(self, nom, prenom): #méthode constructeur
									 #!!! Le premier parametre DOIT etre self !!!
									 #Le reste est libre
		"""pour l'instant, on ne va définir qu'un seul attribut"""
		self.nom = "Dupont"
		self.prenom = "Jean"
		self.age = 33
		self.lieu_residence = "Paris"
		
jean = Personne("Dupont", "Jean")
jean #<__main__.Personne object at 0x00B42570>
jean.nom #'Dupont'
jean.prenom #'Jean'

jean.lieu_residence = "Berlin" #Jean déménage

bernard = Personne("Micado", "Bernard") #nom='Micado', prenom='Bernard', age=33

###Les attributs de classe (les attributs d'objet sont spécicifique à l'instance de l'objet
###							les attributs de classe sont propres à la classe et communs
###							à toutes les instances de cette classe) 
class Compteur:
	"""Cette classe possède un attibut de classe qui s'incrémente à chaque
	fois que l'on crée un objet de ce type"""
	#On crée les attributs de classe après la docstring et avant le constructeur
	objets_crees = 0 #le compteur vaut 0 au départ
	def __init__(self):
		"""à chaque fois qu'on crée un objet, on incrémente le compteur"""
		Compteur.objets_crees += 1

a = Compteur()
Compteur.objets_crees	# =1
b =  Compteur()
Compteur.objets_crees	# =2
	#!!! a.objets_crees = 2 et b.objets_crees = 2 !!!

	
###Les méthodes
class TableauNoir:
	"""Classe définissant une surface sur laquelle on peut écrire,
	que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
	est 'surface'"""
	
	def __init__(self):
		"""par défaut, notre surface est vide"""
		self.surface = ""
	def ecrire(self, message_a_ecrire):
		"""Méthode permettant d'écrire sur la surface du tableau.
		Si la surface n'est pas vide, on saute une ligne avant de rajouter
		le message à écrire"""
		if self.surface != "":
			self.surface += "\n"
			self.surface += message_a_ecrire
	def lire(self):
		"""Cette méthode se charge d'afficher, grâce à print,
		la surface du tableau"""
		print(self.surface)
			
tab = TableauNoir()
tab.surface	# ''
tab.ecrire("Coucou, tu veux")
tab.ecrire("voir")
tab.surface	# "Coucou, tu veux\nVoir"

	# !!! Ecrire tab.ecrire(...) revient à écrire TableauNoir.ecrire(tab, ...)
	# !!! D'où le 'self' dans la définition de la méthode 'ecrire'
	# !!! Parfois on trouve 's' à la place de 'self' mais c'est à éviter
		
###Méthodes de classe
class Compteur:
	"""Cette classe possède un attibut de classe qui s'incrémente à chaque
	fois que l'on crée un objet de ce type"""
	#On crée les attributs de classe après la docstring et avant le constructeur
	objets_crees = 0 #le compteur vaut 0 au départ
	def __init__(self):
		"""à chaque fois qu'on crée un objet, on incrémente le compteur"""
		Compteur.objets_crees += 1
	def combien(cls):
		"""Méthode de classe affichant combien d'objets ont été créés"""
		print("jusqu'à présent, {} objets ont été créés.".format(cls.objets_crees))
	combien = classmethod(combien)
	
Compteur.combien()	#Jusqu'à présent, 0 objets ont été crées.
a=Compteur()
Compteur.combien()	#" " " " " " " "  1 " " " " " " " " " " 
b=Compteur()
a.combien()			#" " " " " " " "  2 " " " " " " " " " " 
					#on peut appeler une méthode de classe également depuis
					#un objet instancié sur la classe
					
#Méthodes statiques
class Test:
	"""Une classe de test tout simplement"""
	def afficher():
		"""fonction chargée d'afficher quelque chose"""
		print("On affiche la même chose")
		print("peu importe les données de l'objet ou de la classe")
	afficher = staticmethod(afficher)

Test.afficher()
a = Test()
a.afficher()	#appel depuis la classe ou l'instance, ça renvoie la même chose
		
####Introspection
dir(a)	#dir (...) retourne sous forme de liste, toutes les méthodes et attributs
			#accessibles depuis la classe ou l'objet passé en paramètre
a.__dict__ #l'attribut __dict__ contient un dictionnaire des attribut:valeur
			# !!! attention, en modifiant un attribut de ce dictionnaire par affectation
			# !!! (a.__dict__[xxx] = yyy), on modifie la valeur de a.xxx
			
############Les propriétés
##Les propriétés sont constitué d'un ensemble de méthodes appelées lors de l'accès à des attributs

class Personne:
	"""Classe définissant une personne caractérisée par :
	-son nom
	-son prénom
	-son âge-son lieu de résidence"""
	
	def __init__(self, nom, prenom):
		self.nom = nom
		self.prenom = prenom
		self.age = 33
		self._lieu_residence = "Paris"	# !!! l'attribut commence par un '_' !!!
										# ça signifie que PAR CONVENTION, on accèdera pas
										# à cet attribut en dehors de la classe
										
	def _get_lieu_residence(self):
		"""Méhotde qui sera appelée quand on souhaitera accéder en lecture à
		l'attribut "_lieu_residence'"""
		
		print("On accède à l'attribut 'lieu_residence' (sans '_' !!!) !")
		return self._lieu_residence
	def _set_lieu_residence(self, nouvelle_residence):
		"""Méthode appelée quand on souhaite modifier le lieu de résidence"""
		print("Attention, {} déménage à {}".format(self.prenom, nouvelle_residence))
		self._lieu_residence = nouvelle_residence
		
	#cablage de l'attribut lieu_residence (SANS '_' !!!) à une propriété
	lieu_residence = property(_get_lieu_residence, _set_lieu_residence)
					#On passe à la fonction property les méthodes à appeler en cas de,
					#dans l'ordre : lecture de l'attribut, écriture de l'attribut, suppression
					#de l'attribut, help sur l'attribut.
					#Chacun de ces paramètres est facultatif

jean = Personne("Micado", "Jean")
jean.nom 		#'Micado'
jean.prenom		#'Jean'
jean.age		#33
						#!!!!!!!!!!!!
jean.lieu_residence	#"On accède à l'attribut lieu_residence"
						#'Paris'
jean._lieu_residence = "Anvers"	#il ne faut pas y accéder directement car on a mis un '_'
print(jean.__dict__)			#mais ça marche quand même : _lieu_residence = "Anvers"
jean.lieu_residence = "Berlin"	#"Attention, Jean déménage à Berlin"
print(jean.__dict__)			#là on passe par la méthode set et c'est bien l'attribut, 
								#avec '_', qui est modifié !
jean.lieu_residence		#"On accède à l'attribut lieu_residence"
						#'Paris'
						#!!!!!!!!!!!!

os.system("pause")



