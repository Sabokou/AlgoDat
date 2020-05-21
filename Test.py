
#---------Imports-------- 
import matplotlib.pyplot as plt
import functools
from random import randint, choice
from math import sqrt

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

def Pythagoras(Punkt1, Punkt2):
    distanz = round(sqrt(((Punkt1[0]-Punkt2[0])**2 + (Punkt1[1] - Punkt2[1])**2)))
    if distanz == 0:
        return 1
    else:
        return distanz

def ErstelleKoordiantenliste(knotenzahl = 8):
    koordinatenliste = dict()
    for i in range(knotenzahl):
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(koordinatenliste)
    return koordinatenliste

def ErstelleVerbindungsliste(koordinatenliste, knotenzahl = 8):
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
            distanz = Pythagoras(koordinatenliste[i], koordinatenliste[verbindung])
            verbindungsliste[i] = verbindungsliste[i] + [(verbindung, distanz)]
            verbindungsliste[verbindung] = verbindungsliste[verbindung] + [(i, distanz)]
    print(verbindungsliste)
    return verbindungsliste

def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    return x1, x2, y1,y2
   #plt.plot([x1,x2],[y1,y2],':ko')

def ShowPlot(koordinatenliste, verbindungsliste, weg, knotenzahl = 8):
    xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
    yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]

    for i in verbindungsliste.keys():
        for n in range(len(verbindungsliste[i])):
            connectpoints(xCoord, yCoord, i, verbindungsliste[i][n][0])

    plt.axis([-1, knotenzahl * 5 + 1, -1, knotenzahl * 5 + 1])

    for i in range(knotenzahl):
        plt.text(xCoord[i]-0.5, yCoord[i], str(i))
    
    return x1, x2, y1, y2

    #plt.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')

    #plt.show()
    


koordinatenliste = ErstelleKoordiantenliste()
verbindungsliste = ErstelleVerbindungsliste(koordinatenliste)
knotenzahl = 8
startkoordinate = randint(0,knotenzahl)
endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
print(weg)
print ("Distance:",distanz)
#ShowPlot(koordinatenliste, verbindungsliste, weg, knotenzahl=8) 


xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]



from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
 
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        title = "Matplotlib Embeding In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500
 
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
 
        self.MyUI()
 
 
    def MyUI(self):
 
        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)
 
        button = QPushButton("Click Me", self)
        button.move(100, 450)
 
        button2 = QPushButton("Click Me Two", self)
        button2.move(250, 450)
 
 
class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        self.plot()
 
 
    def plot(self):
        ax = self.figure.add_subplot(111)
        for i in verbindungsliste.keys():
            for n in range(len(verbindungsliste[i])):
                x1, x2 = xCoord[i], xCoord[verbindungsliste[i][n][0]]
                y1, y2 = yCoord[i], yCoord[verbindungsliste[i][n][0]]
                ax.plot([x1,x2],[y1,y2],':ko')
        ax.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')
 
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()