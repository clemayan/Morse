#/ : espace
# * écart entre chaque lettre
#À gauche : un point °
#À droite : un tiret -

# classe Noeud
class Noeud:
    def __init__(self, valeur, gauche = None, droit = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit


    def __str__(self):
        return str(self.valeur)

# fonction hauteur
# la hauteur de la racine est ici de 1
# remplacer 0 par -1 si on souhaite une hauteur de 0 pour la racine
def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))

#################### Code pour afficher l'arbre
import networkx as nx
import matplotlib.pyplot as plt

def repr_graph(arbre, size=(8,8), null_node=False):
    """
    size : tuple de 2 entiers. Si size est int -> (size, size)
    null_node : si True, trace les liaisons vers les sous-arbres vides
    """
    def parkour(arbre, noeuds, branches, labels, positions, profondeur, pos_courante, pos_parent, null_node):
        if arbre is not None:
            noeuds[0].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            profondeur -= 1
            labels[pos_courante] = str(arbre.valeur)
            branches[0].append((pos_courante, pos_parent))
            pos_gauche = pos_courante - 2**profondeur
            parkour(arbre.gauche, noeuds, branches, labels, positions, profondeur, pos_gauche, pos_courante, null_node)
            pos_droit = pos_courante + 2**profondeur
            parkour(arbre.droit, noeuds, branches, labels, positions, profondeur, pos_droit, pos_courante, null_node)
        elif null_node:
            noeuds[1].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            branches[1].append((pos_courante, pos_parent))


    if arbre is None:
        return

    branches = [[]]
    profondeur = hauteur(arbre)
    pos_courante = 2**profondeur
    noeuds = [[pos_courante]]
    positions = {pos_courante: (pos_courante, profondeur)}
    labels = {pos_courante: str(arbre.valeur)}

    if null_node:
        branches.append([])
        noeuds.append([])

    profondeur -= 1
    parkour(arbre.gauche, noeuds, branches, labels, positions, profondeur, pos_courante - 2**profondeur, pos_courante, null_node)
    parkour(arbre.droit, noeuds, branches, labels, positions, profondeur, pos_courante + 2**profondeur, pos_courante, null_node)

    mon_arbre = nx.Graph()

    if type(size) == int:
        size = (size, size)
    plt.figure(figsize=size)

    nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[0], node_color="pink", node_size=900, edgecolors="black") #changement de la taille des cercles
    nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[0], edge_color="black", width=1) #traits reliants les noeuds
    nx.draw_networkx_labels(mon_arbre, positions, labels)

# branches vides en gris
    if null_node:
        nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[1], node_color="White", node_size=50, edgecolors="grey") #fils qui n'existent pas
        nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[1], edge_color="grey", width=1)

    ax = plt.gca()
    ax.margins(0.01)
    plt.axis("off")
    plt.show()
    plt.close()

#création d'un arbre
d = Noeud('d',None,None) #None pas necessaire
a = Noeud('a',None,None)
c = Noeud('c',None,None)
rg = Noeud('1',a,None)
rd= Noeud('2',c,d)
arbre1 = Noeud('racine',rg,rd)
#repr_graph(arbre1,(4,5),True) #les fils gris n'existent pas

## à faire 1 :
#représentation de l'abre morse en majuscule
interro = Noeud('?')
guille = Noeud('"')
point = Noeud('.')
moins = Noeud('-')
ptvir = Noeud(';')
excla = Noeud('!')
parf = Noeud(')')
vir = Noeud(',')
deuxpts = Noeud(':')
aro = Noeud('@')
apo = Noeud("'")
under = Noeud('_')
dollar = Noeud('$')
VGG = Noeud('', None, dollar)

Eaig = Noeud('É')
Ccedille = Noeud('Ç')
VG = Noeud('', VGG) #fils gauche du noeud V
esper = Noeud('&')
Aac = Noeud('À', aro)
ZD = Noeud('', None, vir) #fils droit du noeud Z
paro = Noeud('(', None, parf)
CD = Noeud('', ptvir, excla) #fils droit du noeud C
Egr = Noeud('È', guille)
UDG = Noeud('', interro, under) #fils gauche du fils droit du noeud U
zero = Noeud('0')
un = Noeud('1', apo)
deux = Noeud('2')
trois = Noeud('3')
quattre = Noeud('4')
cinq = Noeud('5')
six = Noeud('6', None, moins)
sept = Noeud('7')
huit = Noeud('8', deuxpts)
neuf = Noeud('9')
egale = Noeud('=')
plus = Noeud('+', None, point)
div = Noeud('/')

H = Noeud('H', cinq, quattre)
V = Noeud('V', VG, trois)
F = Noeud('F', Eaig)
L = Noeud('L', esper, Egr)
P = Noeud('P', None, Aac)
J = Noeud('J', None, un)
B = Noeud('B', six, egale)
X = Noeud('X', div)
C = Noeud('C', Ccedille, CD)
Y = Noeud('Y', paro)
Z = Noeud('Z', sept, ZD)
Q = Noeud('Q')
UD = Noeud('', UDG, deux) #Noeud vide fils droit du noeud U
RD = Noeud('', plus, None) #fils droit du noeud R
OG = Noeud('', huit, None) #fils gauche du noeud O
OD = Noeud('', neuf, zero) #fils droit du noeud O
S = Noeud('S', H, V)
U = Noeud('U', F, UD)
R = Noeud('R', L, RD)
W = Noeud('W', P, J)
D = Noeud('D', B, X)
K = Noeud('K', C, Y)
G = Noeud('G', Z, Q)
O = Noeud('O', OG, OD)
I = Noeud('I', S, U)
A = Noeud('A', R, W)
N = Noeud('N', D, K)
M = Noeud('M', G, O)
E = Noeud('E', I, A)
T = Noeud('T', N, M)

ab_rac = Noeud('start', E, T)
repr_graph(ab_rac,(14,7),True)



## à faire 2 :
print("à faire 2 : décoder lettre")
def decode_lettre(arbre, code):
    """
    : arbre: objet de la class Noeud
    : code: de type str
    renvoie la lettre décodée
    """
    for i in code: #chaque caractère de la chaine de caractère
        if i == "-":
            arbre = arbre.droit #change de racine et entre dans le sous arbre droit
        if i == "°":
            arbre = arbre.gauche
    return arbre.valeur #lettre décodée

print("-°-° :",decode_lettre(ab_rac,'-°-°')," \n")

# m = '-°-°'
# m = list(m)
# print(m)



## à faire 3 :
print("à faire 3 : encoder lettre et message")
def encode_lettre(lettre,chemin,arbre):
    """
    : lettre: de type str
    : arbre: objet de la class Noeud
    renvoie la lettre encodée en morse
    """
    if arbre is None:
         return ""
    # elif arbre.valeur == lettre: #le noeud est la lettre à encoder
    #     return chemin #étapes lettre encodée
    elif arbre.valeur == lettre.upper(): #le noeud est la lettre à encoder, upper permet de mettre les lettres en majuscule et eviter des problèmes possibles
        return chemin #étapes lettre encodée
    else:
        chg = encode_lettre(lettre, chemin + "°", arbre.gauche)
        chd = encode_lettre(lettre, chemin + "-", arbre.droit)
    return chg + chd

#tests lettres et caractères particuliers ajoutés à l'arbre
print("R :",encode_lettre('R',"",ab_rac))
print("S :",encode_lettre('S',"",ab_rac))
print("O :",encode_lettre('O',"",ab_rac))
print("C :",encode_lettre('C',"",ab_rac))
print("D :",encode_lettre('D',"",ab_rac))
print("E :",encode_lettre('E',"",ab_rac))
print("? :",encode_lettre('?',"",ab_rac))
print(". :",encode_lettre('.',"",ab_rac))
print(", :",encode_lettre(',',"",ab_rac))
print('" :',encode_lettre('"','',ab_rac))
print("- :",encode_lettre('-',"",ab_rac))
print("; :",encode_lettre(';',"",ab_rac))
print("( :",encode_lettre('(',"",ab_rac))
print(") :",encode_lettre(')',"",ab_rac))
print(", :",encode_lettre(',',"",ab_rac))
print(": :",encode_lettre(':',"",ab_rac))
print("$ :",encode_lettre('$',"",ab_rac))
print("' :",encode_lettre("'","",ab_rac))
print("_ :",encode_lettre('_',"",ab_rac))
print("& :",encode_lettre('&',"",ab_rac))
print("É :",encode_lettre('É',"",ab_rac))
print("È :",encode_lettre('È',"",ab_rac))
print("À :",encode_lettre('À',"",ab_rac))
print("Ç :",encode_lettre('Ç',"",ab_rac),"\n")


## à faire 3 :
def encode_message(message, arbre):
    """
    : message: de type str
    : arbre: objet de la class Noeud
    renvoie le message encodé en morse
    """
    mess = "" #variable qui contiendra le message final en morse
    #print("message :", message,":")
    for i in message:
        #print(encode_lettre(i,"",arbre))
        if i == " ":
            mess = mess + "/*" #un espace est représenté par un /
        else:
            mess = mess + encode_lettre(i,"",arbre) + "*" #chaque lettre est séparée par un *
    return mess #message encodé en morse

#tests
print("sos :",encode_message("sos",ab_rac)) #minuscule
print("SOS :",encode_message("SOS",ab_rac)) #majuscule
print("SoS :",encode_message("SoS",ab_rac)) #mélange
print("Portez ce vieux whisky au juge blond qui fume :",encode_message("Portez ce vieux whisky au juge blond qui fume",ab_rac)) #toutes les lettres
print("BrAVO, jeuNE PAdAWAN LA NSI EST AvEc tOI ! :",encode_message("BrAVO, jeuNE PAdAWAN LA NSI EST AvEc tOI !",ab_rac)," \n") #majuscule, minuscule, espace, ponctuation
#print('−°°°*°−°*°−*°°°−*−−−*−−°°−−*/*°−−−*°*°°−*−°*°*/*°−−°*°−*−°°*°−*°−−*°−*−°*/*°−°°*°−*/*−°*°°°*°°*/*°*°°°*−*/*°−*°°°−*°*−°−°*/*−*−−−*°°*/*−°−°−−*') #verification site



## à faire 4 :
print("à faire 4 : décoder message")
def decode_message(message_code, arbre):
    """
    : message_code: de type str
    : arbre: objet de la class Noeud
    renvoie le message décodé
    """
    decode = "" #variable qui contiendra le message final décodé
    #print("message :",message_code)
    lettres = message_code.split("*") #liste avec chaque lettres du message
    #print(lettres)
    del lettres[-1] #supprime le dernier élément de la liste ''
    #print(lettres)
    for i in range(len(lettres)):
        #print(lettres[i])
        if lettres[i]== "/":
            decode = decode + " " #/ correspond à un espace ajout d'un espace au message final
            #print("result",decode)
        else :
            l = decode_lettre(ab_rac,lettres[i]) #lettre décodée
            #print(type(l))
            decode = decode + l #ajout lettre décodée au message final
            #print("result",decode)
    return decode

print("°°°*---*°°°* :",decode_message("°°°*---*°°°*", ab_rac)," \n")
#phrase = "hello world"
#print(list(phrase.split(" ")))
#print(list(phrase.split("o")))



## à faire 5 :
print("à faire 5 :")
message = '-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*'
print(message, ":",decode_message(message,ab_rac),"\n","\n")

print("dico #######################################################################################################################################","\n")
## à faire 6 :
print("à faire 6 :")
def dictionnaire(arbre,chemin,dico):
    if arbre is not None:
        if arbre.valeur != "":
            dico[arbre.valeur] = chemin
        dictionnaire(arbre.gauche,chemin + "°",dico)
        dictionnaire(arbre.droit,chemin + "-",dico)
    return dico

#print(dictionnaire(ab_rac,'',{}))
dic = dictionnaire(ab_rac,'',{})
print(dic,"\n")
#print("test",dic["E"])

#La fonction est-elle récursive ? si oui, préciser la condition d'arrêt.
    #Oui, il s'agit d'une fonction recursive car c'est une fontion faisant appel à elle même.
    #La fontion s'arrête lorsque la focntion est passé par tous les noeuds de l'arbre. La fonction est un parcours préfixe qui s'arrêt lorque l'arbre est vide.
#La fonction parcours l'arbre, de quel parcours s'agit-il ?
    #Il s'agit d'un parcours préfixe.

print("decoder lettre :")
def decode_lettre_dic(arbre, code):
    """
    : arbre: de type dict
    : code: de type str
    renvoie la lettre décodée
    """
    for i in arbre :
        #print(i) #les clefs du dictionnaire
        if arbre[i] == code: #valeur de la clef = code recherché
            return i #renvoie la clef, la lettre décodée

print("-°-° :",decode_lettre_dic(dic,'-°-°'),"\n")


print("encoder lettre et message:")
def encode_lettre_dic(lettre,arbre):
    """
    : lettre: de type str
    : arbre: de type dict
    renvoie la lettre encodée en morse
    """
    if lettre == " ": #espace représenté par /
        return "/"
    else :
        return arbre[lettre.upper()] #met en majuscule la lettre recherchée

#test lettres
print("R :",encode_lettre_dic('R',dic))
print("S :",encode_lettre_dic('S',dic))
print("O :",encode_lettre_dic('O',dic))
print("C :",encode_lettre_dic('C',dic))
print("D :",encode_lettre_dic('D',dic))
print("! :",encode_lettre_dic('!',dic))
print("; :",encode_lettre_dic(';',dic))
print(" :",encode_lettre_dic(' ',dic))
print("E :",encode_lettre_dic('E',dic),"\n")

def encode_message_dic(message,arbre):
    """
    : message: de type str
    : arbre: de type dict
    renvoie le message encodé en morse
    """
    mess = "" #variable qui contiendra le message final en morse
    #print("message", message,":")
    for i in message:
        #print(i)
        #print(encode_lettre_dic(i,ab_rac))
        mess = mess + encode_lettre_dic(i,arbre) + "*" #chaque lettre est séparée d'un espace représenté par un *
    return mess

#tests
print("sos :",encode_message_dic("sos",dic)) #minuscule
print("SOS :",encode_message_dic("SOS",dic)) #majuscule
print("SoS :",encode_message_dic("SoS",dic)) #mélange
print("BrAVO jEuNE PAdAWAN LA NSI EST AvEc tOI :",encode_message_dic("BrAVO jEuNE PAdAWAN LA NSI EST AvEc tOI",dic),"\n") #majuscule, minuscule, espace

print("decoder message :")
def decode_message_dic(message_code,arbre):
    """
    : message_code: de type str
    : arbre: de type dict
    renvoie le message décodé
    """
    decode = "" #variable qui contiendra le message décodé
    #print(message_code)
    lettres = message_code.split("*") #liste avec chaque lettres du message codé
    #print(lettres)
    del lettres[-1] #supprime le dernier élément de la liste ('')
    #print(lettres)
    for i in range(len(lettres)):
        #print(lettres[i])
        if lettres[i]== "/":
            decode = decode + " " #/ correspond à un espace
            #print("result",decode)
        else :
            #print(decode)
            decode = decode + decode_lettre_dic(dic,lettres[i]) #ajout de la lettre décodée au message
            #print("result",decode)
    #print(message_code, ":")
    return decode

message = '-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*'
print(message, ":", decode_message_dic(message,dic),"\n","\n")

print("timeit #######################################################################################################################################","\n")
import timeit

print("Exemple :'BRAVO JEUNE PADAWAN LA NSI EST AVEC TOI' :","\n")
#arbre encodage
debut1 = timeit.default_timer()# debut du "chrono"
encode_message("BRAVO JEUNE PADAWAN LA NSI EST AVEC TOI",ab_rac)
fin1 = timeit.default_timer()
duree1 = fin1 - debut1
print("L'encodage avec une structure d'arbre dure",duree1,"secondes")
#arbre décodage
debut2 = timeit.default_timer()
decode_message('-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*',ab_rac)
fin2 = timeit.default_timer()
duree2 = fin2 - debut2
print("Le décodage avec une structure d'arbre dure",duree2,"secondes")

#dictionnaire encodage
debut1_dic = timeit.default_timer()# debut du "chrono"
encode_message_dic("BRAVO JEUNE PADAWAN LA NSI EST AVEC TOI",dic)
fin1_dic = timeit.default_timer()
duree1_dic = fin1_dic - debut1_dic
print("L'encodage avec une srtucture de dictionnaire dure",duree1_dic,"secondes")
#dictionnaire décodage
debut2_dic = timeit.default_timer()
decode_message_dic('-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*',dic)
fin2_dic = timeit.default_timer()
duree2_dic = fin2_dic - debut2_dic
print("Le décodage avec une structure de dictionnaire dure",duree2_dic,"secondes","\n","\n")

print("timeit moyenne encodage ########################################################################################################################""\n")
#Rouge et noir
with open ("RN.txt","r", encoding = "utf-8") as fichier : #ouvrir le fichier txt contenant le texte à encoder en utf8
    rn = "" #chaine de caractère contenat les lignes du fichier texte
    #print(fichier)
    for i in fichier:
        rn = rn + i
    #print(rn) #affiche le contenu du fichier en str
    #print(type(rn))

#arbre encodage
debut = timeit.default_timer()# debut du "chrono"
encode_message(rn,ab_rac)
fin = timeit.default_timer()
duree = fin - debut
print("RN arbre :",duree,"secondes")
#dictionnaire encodage
debut_dic = timeit.default_timer()# debut du "chrono"
encode_message_dic(rn,dic)
fin_dic = timeit.default_timer()
duree_dic = fin_dic - debut_dic
print("RN dico :",duree_dic,"secondes")


#Divina Commedia
with open ("Divina_Commedia.txt","r", encoding = "utf-8") as fichier : #ouvrir le fichier txt contenant le texte à encoder en utf8
    dc = ""
    for i in fichier:
        dc = dc + i

    #print(dc) #affiche le contenu du fichier en str
    #print(type(dc))

#arbre encodage
debut2 = timeit.default_timer()# debut du "chrono"
encode_message(dc,ab_rac)
fin2 = timeit.default_timer()
duree2 = fin2 - debut2
print("Divina Commedia arbre :",duree2,"secondes")
#dictionnaire encodage
debut_dic2 = timeit.default_timer()# debut du "chrono"
encode_message_dic(dc,dic)
fin_dic2 = timeit.default_timer()
duree_dic2 = fin_dic2 - debut_dic2
print("Divina Commedia dico :",duree_dic2,"secondes")


#Avatar
with open ("Avatar.txt","r", encoding = "utf-8") as fichier : #ouvrir le fichier txt contenant le texte à encoder en utf8
    av = ""
    for i in fichier:
        av = av + i

    #print(av) #affiche le contenu du fichier en str
    #print(type(av))

#arbre encodage
debut3 = timeit.default_timer()# debut du "chrono"
encode_message(av,ab_rac)
fin3 = timeit.default_timer()
duree3 = fin3 - debut3
print("Avatar arbre :",duree3,"secondes")
#dictionnaire encodage
debut_dic3 = timeit.default_timer()# debut du "chrono"
encode_message_dic(av,dic)
fin_dic3 = timeit.default_timer()
duree_dic3 = fin_dic3 - debut_dic3
print("Avatar dico :",duree_dic3,"secondes","\n")


moyearbre = (duree + duree2 + duree3)/3
print("En moyenne, la structure de l'arbre met", moyearbre,"secondes à encoder un fichier txt.")
moydic = (duree_dic + duree_dic2 + duree_dic3)/3
print("En moyenne, la structure du dictionnaire met", moydic,"secondes à encoder un fichier txt.")

if moydic > moyearbre: #dic plus lent que l'arbre
    print("La structure dictionnaire est",moydic/moyearbre,"fois plus lente que la structure d'arbre.","\n","\n")
else: #arbre plus lent que dictionnaire
    print("La structure d'arbre est",moyearbre/moydic,"fois plus lente que la structure de dictionnaire.","\n","\n")


print("timeit moyenne decodage #############################################################################################################################""\n")
#Rouge et noir
with open ("RN_decode.txt","r", encoding = "utf-8") as fichier : #ouvrir le fichier txt contenant le texte à encoder en utf8
    rnd = "" #chaine de caractère contenat les lignes du fichier texte
    #print(fichier)
    for i in fichier:
        rnd = rnd + i
    #print(rnd) #affiche le contenu du fichier en str
    #print(type(rnd))

#arbre decodage
debut_decode = timeit.default_timer()# debut du "chrono"
decode_message(rnd,ab_rac)
fin_decode = timeit.default_timer()
duree_decode = fin_decode - debut_decode
print("RN arbre :",duree_decode,"secondes")
#dictionnaire decodage
debut_dic_decode = timeit.default_timer()# debut du "chrono"
decode_message_dic(rnd,dic)
fin_dic_decode = timeit.default_timer()
duree_dic_decode = fin_dic_decode - debut_dic_decode
print("RN dico :",duree_dic_decode,"secondes")


#Divina Commedia
with open ("Divina_Commedia_decode.txt","r", encoding = "utf-8") as fichier : #ouvrir le fichier txt contenant le texte à encoder en utf8
    dcd = ""
    for i in fichier:
        dcd = dcd + i

    #print(dcd) #affiche le contenu du fichier en str
    #print(type(dcd))

#arbre decodage
debut2_decode = timeit.default_timer()# debut du "chrono"
decode_message(dcd,ab_rac)
fin2_decode = timeit.default_timer()
duree2_decode = fin2_decode - debut2_decode
print("Divina Commedia arbre :",duree2_decode,"secondes")
#dictionnaire decodage
debut_dic2_decode = timeit.default_timer()# debut du "chrono"
decode_message_dic(dcd,dic)
fin_dic2_decode = timeit.default_timer()
duree_dic2_decode = fin_dic2_decode - debut_dic2_decode
print("Divina Commedia dico :",duree_dic2_decode,"secondes")


#Avatar
with open ("Avatar_decode.txt","r", encoding = "utf-8") as fichier : #ouvrir le fichier txt contenant le texte à encoder en utf8
    avd = ""
    for i in fichier:
        avd = avd + i

    #print(avd) #affiche le contenu du fichier en str
    #print(type(avd))

#arbre decodage
debut3_decode = timeit.default_timer()# debut du "chrono"
decode_message(avd,ab_rac)
fin3_decode = timeit.default_timer()
duree3_decode = fin3_decode - debut3_decode
print("Avatar arbre :",duree3_decode,"secondes")
#dictionnaire decodage
debut_dic3_decode = timeit.default_timer()# debut du "chrono"
decode_message_dic(avd,dic)
fin_dic3_decode = timeit.default_timer()
duree_dic3_decode = fin_dic3_decode - debut_dic3_decode
print("Avatar dico :",duree_dic3_decode,"secondes","\n")


moyearbre_decode = (duree_decode + duree2_decode + duree3_decode)/3
print("En moyenne, la structure de l'arbre met", moyearbre_decode,"secondes à décoder un fichier txt.")
moydic_decode = (duree_dic_decode + duree_dic2_decode + duree_dic3_decode)/3
print("En moyenne, la structure du dictionnaire met", moydic_decode,"secondes à décoder un fichier txt.")

if moydic_decode > moyearbre_decode: #dic plus lent que l'arbre
    print("La structure dictionnaire est",moydic_decode/moyearbre_decode,"fois plus lente que la structure d'arbre.","\n","\n")
else: #arbre plus lent que dictionnaire
    print("La structure d'arbre est",moyearbre_decode/moydic_decode,"fois plus lente que la structure de dictionnaire.","\n","\n")

print("affichage utlisateur ######################################################################################################################""\n")
def menu():
    """affiche un menu gérant le choix de l'utilisateur pour encoder ou décoder un message en morse"""
    print("structure :","\n","1- arbre","\n","2- dictionnaire","\n")
    choix1 = input("Quel est votre choix ? (pour quitter entrez stop) ")
    print()
    if choix1 == "stop" :
       return #arrete le programme
    elif choix1 == "1": #arbre
        print("action :","\n","1- encoder message","\n","2- décoder message","\n")
        choix2 = input("Quel est votre choix ? (pour quitter entrez stop, pour retourner au menu entrez retour) ")

        if choix2 == "stop" :
            return
        elif choix2 == "retour" :
            menu()
        elif choix2 == "1": #encodage
            message1 = input("Que voulez-vous encoder ? ")
            if len(message1) > 1 : #le message est au moins un mot
                print(encode_message_dic(message1, dic), "\n")
            else : #évite * pour séparer les lettres au cas où le message n'est qu'une seule lettre
                print(encode_lettre_dic(message1, dic), "\n")
            menu() #retour au menu
        elif choix2=="2":#décodage
            message2 = input("Que voulez-vous décoder ? ")
            print(decode_message(message2, ab_rac), "\n")
            menu() #retour au menu
        else:
            print("Erreur : le choix n'est pas possible !")
            return menu()

    elif choix1 == "2": #arbre
        print("action :","\n","1- encoder message","\n","2- décoder message","\n")
        choix2 = input("Quel est votre choix ? (pour quitter entrez stop, pour retourner au menu entrez retour) ")

        if choix2 == "stop" :
            return
        elif choix2 == "retour" :
            menu()
        elif choix2 == "1": #encodage
            message3 = input("Que voulez-vous encoder ? ")
            if len(message3) > 1 : #le message est au moins un mot
                print(encode_message_dic(message3, dic), "\n")
            else : #évite * pour séparer les lettres au cas où le message n'est qu'une seule lettre
                print(encode_lettre_dic(message3, dic), "\n")
            menu()
        elif choix2=="2": #décodage
           message4 = input("Que voulez-vous décoder ? ")
           print(decode_message_dic(message4, dic), "\n")
           menu()
        else:
            print("Erreur : le choix n'est pas possible !")
            return menu()
    else: #autre caractère
        print("Erreur : le choix n'est pas possible !")
        return menu()

menu()
