# Creates a word cloud in HTML

def nuage(n,titre,couleur1,couleur2): #prend en paramètre un dictionnaire correspondant à un nuage, le titre du nuage en .html et les deux couleurs du nuage
	maxi=max(n)	#donne la fréquence d'apparition maximale des mots du texte
	with open(titre, "w") as f:
		f.write("""
			<html>
			<head><title>{titre}</title>
			</head>""".format(titre="Nuage de mots"))

		f.write("""<body>""")
		i=0 #on va compter le nombr de mots
		for m in n:
			taille=n[m]*20/maxi #la taille de la police est choisie de sorte que le mot le plus fréquent soit en police 20
			if i%5==0: #si le nombre de mots est divisible par 5
				f.write("<br><br/>") #on passe à la ligne (tous les cinq mots donc)
				if len(m)%2==0 : #pour mettre deux couleurs on teste si le mot est de longueur paire on l'écrit de la couleur1
					f.write("<font size={freq} color={couleur}>        {mot}        </font>".format(mot=m,freq=taille,couleur=couleur1))
				else: #sinon le mot est écrit avec la couleur2
					f.write("<font size={freq} color={couleur}>        {mot}        </font>".format(mot=m,freq=taille,couleur=couleur2))
			
				
			else: 
			
				if len(m)%2==0 :
					f.write("<font size={freq} color={couleur}>        {mot}        </font>".format(mot=m,freq=taille,couleur=couleur1))
				else:
					f.write("<font size={freq} color={couleur}>        {mot}       </font>".format(mot=m,freq=taille,couleur=couleur2))
			
			i=i+1	#on compte les mots affichés pour pouvoir passer à la ligne tous les cinq mots
		
		f.write("</body></html>")
