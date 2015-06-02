# Looking for a word in an ordered list
def cherche_dicho (mot, m) :
    a = 0
    b = len (mot)-1
    nb = 0
    while a < b :
        nb += 1
        p = (a+b)/2
        if mot [p] == m : return p,nb
        elif mot [p] > m : b = p-1
        else : a = p+1
    return -1,nb

def kill_stop_words_bis(list_dep,list_stop):
    liste = []
    for a in list_dep:
        (position, nbiter) = cherche_dicho(a, list_dep)
        if position=-1:
                liste.append(a)
    return liste
