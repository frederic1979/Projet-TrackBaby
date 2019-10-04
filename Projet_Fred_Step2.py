# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv
import numpy

# Récupération des mesures dans les fichiers à faire
# Affichage des graphiques à faire

###################################  Poids
# initialisation des variables
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []


# lecture du CSV (mesures) et incrémentation des mes 2 listes (x et y), avec chgt de ligne à chaque ';'
with open('/home/bnp-renault-003/Bureau/python-project-trackbaby/mesures.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    
    for row in plots:
        if row[0]!='Mois' : #on élimine le cas de la 1ere ligne qui contient du str
            x.append(int(row[0]))
            y.append(float(row[1]))

#idem mais avec les valeurs du fichier des constantes
with open('/home/bnp-renault-003/Bureau/python-project-trackbaby/poids-age-garcon-0-60-light.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    
    for row in plots:
        if row[0]!='Month' :
            x1.append(int(row[0]))
            y1.append(float(row[1]))
            x2.append(int(row[0]))
            y2.append(float(row[2]))
            x3.append(int(row[0]))
            y3.append(float(row[3]))
            x4.append(int(row[0]))
            y4.append(float(row[4]))
            x5.append(int(row[0]))
            y5.append(float(row[5]))
# on décide de la position de notre 1er graph sur une grille de 1 ligne, 3 col, et 1ere pos
plt.subplot(1,3,1)
# scatter pour avoir des pts sur le graph / plot pour une trace / K pour le noir / Label pour les légende dans le graph
plt.scatter(x,y,color=['k'])
plt.plot(x1,y1, label='5% poids')
plt.plot(x2,y2, label='25% poids')
plt.plot(x3,y3, label='50% poids')
plt.plot(x4,y4, label='75% poids')
plt.plot(x5,y5, label='95% poids')

# on place des légendes sur les axes x et y, et le titre / la fct legend / Grid pour avoir grille
plt.xlabel('Age en mois')
plt.ylabel('Poids en kg')
plt.title('Hello You\nVoici le graph ONE')
plt.legend()
plt.grid()


###################################################     taille
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []


with open('/home/bnp-renault-003/Bureau/python-project-trackbaby/mesures.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    
    for row in plots:
        if row[0]!='Mois' :
            x.append(int(row[0]))
            y.append(float(row[2]))


with open('/home/bnp-renault-003/Bureau/python-project-trackbaby/taille-age-garcon-0-60-light.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    
    for row in plots:
        if row[0]!='Month' :
            x1.append(int(row[0]))
            y1.append(float(row[1]))
            x2.append(int(row[0]))
            y2.append(float(row[2]))
            x3.append(int(row[0]))
            y3.append(float(row[3]))
            x4.append(int(row[0]))
            y4.append(float(row[4]))
            x5.append(int(row[0]))
            y5.append(float(row[5]))


plt.subplot(1,3,2)

plt.scatter(x,y,color=['k'])
plt.plot(x1,y1, label='5% taille')
plt.plot(x2,y2, label='25% taille')
plt.plot(x3,y3, label='50% taille')
plt.plot(x4,y4, label='75% taille')
plt.plot(x5,y5, label='95% taille')


plt.xlabel('Age en mois')
plt.ylabel('Taille en cm')
plt.title('Hello You\nVoici le Graph TWO')
plt.legend()
plt.grid()


################################## Perim

x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []


with open('/home/bnp-renault-003/Bureau/python-project-trackbaby/mesures.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    
    for row in plots:
        if row[0]!='Mois' :
            x.append(int(row[0]))
            y.append(float(row[3]))


with open('/home/bnp-renault-003/Bureau/python-project-trackbaby/perim-cra-age-garcon-0-60-light.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    
    for row in plots:
        if row[0]!='Month' :
            x1.append(int(row[0]))
            y1.append(float(row[1]))
            x2.append(int(row[0]))
            y2.append(float(row[2]))
            x3.append(int(row[0]))
            y3.append(float(row[3]))
            x4.append(int(row[0]))
            y4.append(float(row[4]))
            x5.append(int(row[0]))
            y5.append(float(row[5]))


plt.subplot(133)

plt.scatter(x,y,color=['k'])
plt.plot(x1,y1, label='5% perim cranien')
plt.plot(x2,y2, label='25% perim cranien')
plt.plot(x3,y3, label='50% perim cranien')
plt.plot(x4,y4, label='75% perim cranien')
plt.plot(x5,y5, label='95% perim cranien')


plt.xlabel('Age en mois')
plt.ylabel('Perim cranien')
plt.title('Hello You\nVoici le graph THREE')
plt.legend()
plt.grid()

plt.show()