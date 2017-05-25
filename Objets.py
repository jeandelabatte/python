import os
import pickle

############Les listes
ma_liste=list() #crée une liste vide []
autre_liste=[1,5,3.5,"coucou",9,[],5] #crée une liste non vide avec 4 types d'objet: int, float, string et list
autre_liste[1]=6 #contrairement aux str, les listes sont "mutables" (on peut changer la valeur directement)
ma_liste.append(56) #ajout d'un élément en fin de liste
					# ! les méthodes de list modifient l'objet et ne renvoient rien
					# ! les méthodes de string ne modifient pas l'objet et renvoient le résultat
autre_liste.insert(2,99) #insertion de 99 à l'indice 2
del autre_liste[3] #delete l'élement d'indice 3
a=5
del a #marche aussi avec les variables "simples"
autre_liste.remove(9) #enlève le 1er élément "9" de la liste (qq soit son indice)

##parcours des listes: comme avec les str -> un while avec incrément d'indice ou un for element in xxxx
#il existe une autre manière:
for i, elt in enumerate(autre_liste):		#enumerate renvoie des tuples au format (indice, element)
	print("A l'indice {} se trouve {}".format(i, elt))
	
############Les tuples : des listes qu'on ne peut pas modifier
tuple_vide = ()
tuple_non_vide = (1,) #est équivalent à ce dessous
tuple_non_vide = 1,		#La virgule est obligatoire car sinon on déclare une variable "simple"
tuple_avec_plusieurs_valeurs=(1,2,5)

####conversions chaines/listes
ma_chaine="Bonjour à tous"
ma_chaine_split=ma_chaine.split(" ") #le séparateur par défaut est esp||tab||saut_ligne
print(ma_chaine_split)		#['Bonjour', 'à', 'tous']
" ".join(ma_chaine_split)		#retourne (sans affecter) )ma_chaine_split = ma_chaine

def afficher_flottant(nb_f):
	if type(nb_f) != float:
		raise TypeError("wrong type, plz use 'afficher_flottant' w/ a float")
	
	nb_f_str=str(nb_f)
	nb_f_split=nb_f_str.split(".")
	
	return nb_f_split[0]+','+(nb_f_split[1])[:3]	#[:3] -> les 3 premiers

print(afficher_flottant(5.69999))

####fonctions à nombre de paramètres non fixé
def fonction_inconnue(*param):		#place les paramètres dans un tuple 'param'
	foo=1
def fonction_inconnue_2(nom, prenom, *commentaires): #seul 'commentaires' sera dans un tuple
	foo=2												#(!doit se placer après les param standards)
def fonction_inconnue_3(*values, sep=' ', end='\n'): #(!mais avant les param 'nommés')
	foo=3

####transformer une liste ou un tuple en paramètres de fonction_inconnue
liste_de_parametres=[1, 4, 9, 16, 25, 36]
print(liste_de_parametres) #1 seul paramètre -> affiche la liste
print(*liste_de_parametres) #à converti la liste en paramètres -> affiche tous les paramètres

####list comprehension
##simple
liste_origine=[0,1,2,3,4,5]
[nb*nb for nb in liste_origine]	#[0,1,4,9,16,25]
##avec condition
liste_origine=liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[nb for nb in liste_origine if nb % 2 == 0] #[0,2,4,6,8,10]

############Les dictionnaires
mon_dico=dict()				#crée un dictionnaire vide {}
mon_dico["pseudo"]="xelacel"
mon_dico["pswrd"]="****"	#{'pswrd': '****', 'pseudo': 'xelacel}

autre_dico={'voiture':'roule', 'avion':'vole', 'bateau':'flotte'}	#clef:valeur
del autre_dico["voiture"]	#supprime la clef "voiture" et sa valeur
autre_dico.pop("bateau")	#comme del mais en plus retourne la valeur

mon_dico.keys()				#renvoie la liste des clefs
mon_dico.values()			#renvoie la liste des valeurs
mon_dico.items()			#renvoie un tuple (clef, valeur)
							#équivalent à la méthode enumerate pour les listes
							
####dictionnaires et paramètres de fonctions
##fonctions à nombre de paramètres <strong>nommés</strong> non fixés
def fonction_inconnue(**para_nommes):	#place les paramètres dans un dico "param_nommes"
	foo=1								#au format nom_param:valeur_param
def fonction_inconnue_supreme(*en_tuple, **en_dico):	#accepte n'importe quel type de
	foo=42												#paramètres, nommés ou non, dans
														#n'importe quel ordre et dans
														#n'importe quelle quantité
##passer des paramètres via un dictionnaire
parametres = { 'sep':" >> ", 'end':" -\n" }
print('un', 'exemple', "d'appel", **parametres)			#pour transmettre les parametres
														#il faut mettre **


############Les fichiers
mon_fichier=open("fichier.txt", 'r')	#r=read, w=write (écrase), a=append (à la suite)
										#b=binary
mon_fichier.read()						#renvoie le contenu du fichier dans un string
mon_fichier.close()

mon_fichier=open("file_to_write.txt",'w')	#attention ça écrase le contenu
mon_fichier.write("coucou !!!")
mon_fichier.close()

with open("file_to_write.txt", 'r') as mon_fichier:	#autre manière d'ouvrir un fichier
	mon_fichier.read()								#avantage: ça ferme automatiquement
													#le fichier à la fin du bloc
mon_fichier.closed						#pour vérifier si fichier fermé. Renvoie True

##enregistrer des objets dans des fichiers
#(grâce au module pickle)
score = {
	"joueur 1":    5,
	"joueur 2":    10,
	"joueur 3":    20,
	"joueur 4":    7,
}

with open('donnees', 'wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)				#enregistrement
	mon_pickler.dump(score)
	
with open('donnees', 'rb') as fichier:
	mon_depickler = pickle.Unpickler(fichier)	#recuperation
	score_recupere = mon_depickler.load()
	

############Portées des variables et références
##Portée des variables
#Une var définie dans une fonction n'est pas accessible en dehors
#Une var définie en dehors d'une fonction est accessibe en lecture
#dans la fonction mais si on tente une affectation on va écrire dans
#une copie locale et la variable d'origine ne sera pas modifiée
#=> pour modifier une variable définie en dehors de la fct (ou un 
#de ses paramètres), il faut utiliser une méthode de l'objet
#qu'on souhaite modifier (on peut également modifier ses attributs
#directement)

##Références
liste1 = [1,2,3]
liste2 = liste1

liste2.append(4)
liste1				#retourne [1,2,3,4]
#On crée des références sur le même objet, et si on utilise des méthodes
#on modifie l'objet pointé par les 2 références. Ca ne le fait pas avec
#des nombres car pas de méthodes de nombres (juste des affectations et 
#opérations) et avec les str car les méthodes de str ne modifient pas l'objet

liste1 = [1,2,3]
liste2 = list(liste1)	#méthode si on veut décoreller les 2 objets
id(liste1) != id(liste2)	#True
liste1 is liste2 			#False (compare les id)

##variables globales
#on déclarela var en dehors de toute fonction, puis dans la
#fonction appelante on la déclare avec le mot clef 'global'
i=0
def incr_i():
	"""Fonction d'incrémentation. Ici sert juste d'exemple pour les var globales"""
	global i
	i += 1
print(i)	#i vaut maintenant 1
	

os.system("pause")