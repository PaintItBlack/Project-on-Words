def remplir_dico(dico,liste):
    for c in liste :
        dico[c] = dico.get(c,0) + 1
    return(dico)
    
    
    
def nettoie_dico(dico):
    h = {}
    for c in dico.keys():
        if dico[c] > 3:
            h[c] = dico[c]
    return(h)
    
    
#fonction donnant la fréquence maximale d'apparition d'un mot dans le dictionnaire
def max (dico) :
	max=0
	for mot in dico :
		if dico[mot]>max :
			max=dico[mot]
	return(max)
