def mini(Tab,index_debut):
    """détermine le rang de l'élément le plus petit du début au dernier élément du tableau Tab"""
    minimum = Tab[index_debut]
    index_mini = index_debut
    taille = len(Tab)
    for i in range(index_debut,taille):
        if minimum > Tab[i]:
            minimum = Tab[i]
            index_mini = i
    return index_mini

def tri_selection(Tab):
    taille = len(Tab)
    for i in range(taille-1):
        index_du_min = mini(Tab,i)
        truc = Tab[i]
        Tab[i] = Tab[index_du_min]
        Tab[index_du_min] = truc
    return Tab

tableau = [8,4,9,2,5]
print(tri_selection(tableau))