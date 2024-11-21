'''fonction pour liste de Syracuse'''
#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    '''syr_plot'''
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }})
    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()# fig.write_html('fig.html', include_plotlyjs='cdn') #######################
def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """# votre code ici
    l = [ ]
    l.append(n)
    while l[-1]!=1:
        if l[-1]%2==0:
            l.append(l[-1]/2)
        else :
            l.append(l[-1]*3+1)
    return l
def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: le temps de vol""" # votre code ici
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse
    Args:l (list): la suite de Syracuse
    Returns:int: le temps de vol en altitude"""
    # votre code ici
    n =0
    for i,k in enumerate(l):
        if k<l[0]:
            n=i
            break
    return n-1

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse
    Args:l (list): la suite de Syracuse
    Returns:int: l'altitude maximale"""
    # votre code ici
    return max(l)
#### Fonction principale


def main():
    '''main'''
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(78)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
