#UTF8
from random import *
def clear_grille():
    """
    cree une grille vierge
    """
    global cell 
    haut = 10  # hauteur du tableau
    larg = 10  # largeur du tableau
   
    cell = [[0 for ligne in range(larg)] for tableau in range(haut)]
    for hauteur in range(10):
        for largeur in range(10):
            print(cell[hauteur][largeur],end='\t')
    
    
def tour():
    """
    tour comprenant la determination du nombre de voisins vivants de chaque cellule et l'application des regles
    """
    etat=[[0 for ligne in range(10)] for tableau in range(10)]
    for ligne in range(10):
        for col in range(10):
            etat[ligne][col]=cell[ligne][col]
    
            
    temp= [[0 for ligne in range(10)] for tableau in range(10)]
    nb_voisins=0
    for ligne in range(10):
        for col in range(10):
            if etat[ligne][(col-1)%10]==1:
                nb_voisins+=1
            if etat[ligne][(col+1)%10]==1:
                nb_voisins+=1
            if etat[(ligne+1)%10][(col-1)%10]==1:
                nb_voisins+=1
            if etat[(ligne+1)%10][col]==1:
                nb_voisins+=1
            if etat[(ligne+1)%10][(col+1)%10]==1:
                nb_voisins+=1
            if etat[(ligne-1)%10][(col-1)%10]==1:
                nb_voisins+=1
            if etat[(ligne-1)%10][col]==1:
                nb_voisins+=1
            if etat[(ligne-1)%10][(col+1)%10]==1:
                nb_voisins+=1

            if etat[ligne][col] == 1 and nb_voisins < 2:                
                temp[ligne][col] = 0           
            if etat[ligne][col] == 1 and (nb_voisins == 2 or nb_voisins == 3):                
                temp[ligne][col] = 1          
            if etat[ligne][col] == 1 and nb_voisins > 3:                
                temp[ligne][col] = 0         
            if etat[ligne][col] == 0 and nb_voisins == 3:                
                temp[ligne][col] = 1
                
            cell[ligne][col] = temp[ligne][col]
            nb_voisins=0
            
    for hauteur in range(10):
        for largeur in range(10):
            print(cell[hauteur][largeur],end='\t')
    print()    


def config_aleatoire():
    """
    remplis la grille de facon aleatoire
    """
    for hauteur in range(10):
        for largeur in range(10):
            cell[hauteur][largeur]=randint(0,1)
    for hauteur in range(10):
        for largeur in range(10):
            print(cell[hauteur][largeur],end='\t')
    print('configuration fini')
    
    
def config_manuelle():
    """
    remplis la grille manuellement
    """
    nb_modif=int(input("choisir un nb de modifications: "))

    for config in range(nb_modif):
        ligne=int(input("quelle ligne ? "))
        colonne=int(input("quelle colonne ? "))
        cell[ligne][colonne]=1
        for hauteur in range(10):
            for largeur in range(10):
                print(cell[hauteur][largeur],end='\t')
    print("configuration finie")


#programme principale 
def main():
    clear_grille()
    
    erreur=True
    while (erreur == True):
        config=input("choisir une config aleatoire ou manuelle : ")
        if config=='aleatoire' :
            erreur=False
            config_aleatoire()
        elif config=='manuelle' :
            erreur=False
            config_manuelle()
        else:
            erreur=True

    for longueur in range(10):
        tour()
        print('tour : ',longueur+1)
    print("fin de la partie")
    

main()

            