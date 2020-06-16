#---------Imports-------- 
import matplotlib.pyplot as plt
import functools
from random import randint, choice
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D

def dijkstra(verbindungsliste,start,ende):
    distanz = dict()
    herkunftsliste = dict()
    warteschlange = list()
    for i in verbindungsliste.keys():                                                                               #initialisiert Distanzliste mit "unendlich"
        distanz[i] = float('inf')                                                                    
        herkunftsliste[i] = 0                                                                                       #initialisiert Dictionary mit Distanzen zu vorherigen Sachen mit 0
        warteschlange.append(i)                                                                                     #Liste mit allen Knotennamen
    
    distanz[start] = 0                                                                                              #Distanz zum Startpunkt ist 0
    while len(warteschlange) != 0:                                                                                  #so lange Elemente vorhanden sind:
        minimum = min(warteschlange, key=lambda x: distanz[x])                                                      #wähle Knoten aus wo die Distanz am kleinsten ist
        warteschlange.remove(minimum)                                                                               #entfernt Element, damit es nicht nochmal überprüft werden kann
        for verbindung, strecke in verbindungsliste[minimum]:
            alternative = distanz[minimum] + strecke                                                                #Distanz aus kürzestem Weg + neue kürzeste Route zum nächsten Knoten
            if alternative < distanz[verbindung]:                                                                   #Wenn neue Route kleiner der alten ist
                distanz[verbindung] = alternative                                                                   #setze Distanz zu neuem Knoten als Distanz
                herkunftsliste[verbindung] = minimum                                                                #merke dir den Punkt, den du vorher angesteuert hast
    weg = [ende]
    temporaer = ende
    while temporaer != start:
        weg.append(herkunftsliste[temporaer])
        temporaer = herkunftsliste[temporaer]
    weg.reverse()
    return weg, distanz[ende]

def Pythagoras3D(Punkt1, Punkt2):
    distanz = round(sqrt(((Punkt1[0]-Punkt2[0])**2 + (Punkt1[1] - Punkt2[1])**2+ (Punkt1[2] - Punkt2[2])**2)))
    if distanz == 0:
        return 1
    else:
        return distanz

def ErstelleKoordinatenliste3D(knotenzahl=8):
    koordinatenliste = dict()
    for i in range(knotenzahl):
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(koordinatenliste)
    return koordinatenliste

def ErstelleVerbindungsliste3D(koordinatenliste, knotenzahl=8):
    verbindungsliste = dict()
    for i in koordinatenliste.keys():
        verbindungsliste[i] = list()
    for i in koordinatenliste.keys():
        if knotenzahl < 20:
            k = randint(1,2)
        else: 
            k= randint(1, knotenzahl // 10 + 1)
        genutzteverbindungsliste = []
        for j in range(k):
            verbindung = choice([n for n in range(knotenzahl) if (n != i) and (n not in genutzteverbindungsliste)])
            genutzteverbindungsliste.append(verbindung)
            distanz = Pythagoras3D(koordinatenliste[i], koordinatenliste[verbindung])
            verbindungsliste[i] = verbindungsliste[i] + [(verbindung, distanz)]
            verbindungsliste[verbindung] = verbindungsliste[verbindung] + [(i, distanz)]
    print(verbindungsliste)
    return verbindungsliste

def connectpoints3D(x,y,z,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    z1, z2 = z[p1], z[p2]
    ax.plot([x1,x2],[y1,y2],[z1, z2], ':ko')

def ShowPlot3D(koordinatenliste, verbindungsliste, weg, knotenzahl=8):
    xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
    yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]
    zCoord=[koordinatenliste[k][2] for k in sorted(koordinatenliste)]

    for i in verbindungsliste.keys():
        for n in range(len(verbindungsliste[i])):
            connectpoints3D(xCoord, yCoord, zCoord, i, verbindungsliste[i][n][0])

    for i in range(knotenzahl):
        ax.text(xCoord[i]-0.5, yCoord[i], zCoord[i], str(i))

    ax.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg],[koordinatenliste[n][2] for n in weg], '-r')

    plt.show()
    


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    knotenzahl = 12
    koordinatenliste = ErstelleKoordinatenliste3D(knotenzahl)
    verbindungsliste = ErstelleVerbindungsliste3D(koordinatenliste, knotenzahl)
    startkoordinate = randint(0,knotenzahl)
    endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

    weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
    print(weg)
    print ("Distance:",distanz)
    ShowPlot3D(koordinatenliste, verbindungsliste, weg, knotenzahl) 