#We fill our dictionary with the words' frequency of occurence in the text.

def remplir_dico(dico,liste):
    for c in liste :
        dico[c] = dico.get(c,0) + 1
    return(dico)
    
# There, we only keep words whose frequencies are more than 3 occurences    
    
def nettoie_dico(dico):
    h = {}
    for c in dico.keys():
        if dico[c] > 3:
            h[c] = dico[c]
    return(h)
    
    
#function givng the highest number of occurences of a word in a text
def max (dico) :
	max=0
	for mot in dico :
		if dico[mot]>max :
			max=dico[mot]
	return(max)
