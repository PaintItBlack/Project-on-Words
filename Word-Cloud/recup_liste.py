def recup_liste (chemin):
    with open (chemin, "r") as f : # ouverture d'un fichier
        l = []
        for row in f.readlines():
            for a in row.strip('\n').strip('.').strip(',').split(' '):
                l.append(a.lower())
        return l
