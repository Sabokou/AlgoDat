# Imports für die Grundfunktionen des Dijkstra Algorithmus
import matplotlib.pyplot as plt
import functools
from random import randint, choice
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D

#Imports für die GUI
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np





#Nötige Funktionen für Dijkstra Algorithmus definieren

## Definition des reinen Dijkstra Algorithmus
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

## Definition der Hilfsfunktion Pythagoras -> diese errechnet die Distanz zwischen 2 Knotenpunkten
###Die Funktion wird in der Funktion ErstelleVerbindgungsliste genutzt
def Pythagoras2D(Punkt1, Punkt2):
    distanz = round(sqrt(((Punkt1[0]-Punkt2[0])**2 + (Punkt1[1] - Punkt2[1])**2)))
    if distanz == 0:
        return 1
    else:
        return distanz
def Pythagoras3D(Punkt1, Punkt2):
    distanz = round(sqrt(((Punkt1[0]-Punkt2[0])**2 + (Punkt1[1] - Punkt2[1])**2+ (Punkt1[2] - Punkt2[2])**2)))
    if distanz == 0:
        return 1
    else:
        return distanz

## Definition der Funktion ErstelleKoordinatenliste -> erstellt eine Koordinatenliste mit zufälligen Knotenkoordinaten
def ErstelleKoordiantenliste2D(knotenzahl = 8):
    koordinatenliste = dict()
    for i in range(knotenzahl):
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(koordinatenliste)
    return koordinatenliste
def ErstelleKoordinatenliste3D(knotenzahl = 8):
    koordinatenliste = dict()
    for i in range(knotenzahl):
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(koordinatenliste)
    return koordinatenliste

## Definition der Funktion ErstelleVerbindungsliste 
### nutzt die erstellte Koordinatenliste, um die entsprechenden Kanten zwischen den Knoten zufällig zu generieren
### ruft dabei die oben definierte Hilfsfunktion Pythagoras auf 
def ErstelleVerbindungsliste2D(koordinatenliste, knotenzahl = 8):
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
            distanz = Pythagoras2D(koordinatenliste[i], koordinatenliste[verbindung])
            verbindungsliste[i] = verbindungsliste[i] + [(verbindung, distanz)]
            verbindungsliste[verbindung] = verbindungsliste[verbindung] + [(i, distanz)]
    print(verbindungsliste)
    return verbindungsliste
def ErstelleVerbindungsliste3D(koordinatenliste, knotenzahl = 8):
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

## Definition der Hilfsfunktion connectpoint für die Funktion ShowPlot
### Zeichnet die Kanten zwischen den einzelnen Knoten
def connectpoints2D(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],':ko')
def connectpoints3D(x,y,z,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    z1, z2 = z[p1], z[p2]
    ax.plot([x1,x2],[y1,y2],[z1, z2], ':ko')

## Definition der Funktion ShowPlot
### nutzt die Hilfsfunktion connectpoints
### zeichnet den kompletten Graphen
def ShowPlot2D(koordinatenliste, verbindungsliste, weg, knotenzahl = 8):
    xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
    yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]

    for i in verbindungsliste.keys():
        for n in range(len(verbindungsliste[i])):
            connectpoints2D(xCoord, yCoord, i, verbindungsliste[i][n][0])

    plt.axis([-1, knotenzahl * 5 + 1, -1, knotenzahl * 5 + 1])

    for i in range(knotenzahl):
        plt.text(xCoord[i]-0.5, yCoord[i], str(i))

    plt.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')

    plt.show()
def ShowPlot3D(koordinatenliste, verbindungsliste, weg, knotenzahl = 8):
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

# Funktionsaufrufe
def Funktionsaufruf2D():
    koordinatenliste = ErstelleKoordiantenliste2D()
    verbindungsliste = ErstelleVerbindungsliste2D(koordinatenliste)
    knotenzahl = 8
    startkoordinate = randint(0,knotenzahl)
    endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

    weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
    print(weg)
    print ("Distance:",distanz)
    ShowPlot2D(koordinatenliste, verbindungsliste, weg, knotenzahl=8)
    return koordinatenliste, verbindungsliste, weg, knotenzahl, startkoordinate, endkoordinate, distanz
def Funktionsaufruf3D():
    koordinatenliste = ErstelleKoordinatenliste3D()
    verbindungsliste = ErstelleVerbindungsliste3D(koordinatenliste)
    knotenzahl = 8
    startkoordinate = randint(0,knotenzahl)
    endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

    weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
    print(weg)
    print ("Distance:",distanz)
    ShowPlot3D(koordinatenliste, verbindungsliste, weg, knotenzahl=8) 

koordinatenliste = ErstelleKoordiantenliste2D()
verbindungsliste = ErstelleVerbindungsliste2D(koordinatenliste)
knotenzahl = 8
startkoordinate = randint(0,knotenzahl)
endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
print(weg)
print ("Distance:",distanz)
ShowPlot2D(koordinatenliste, verbindungsliste, weg, knotenzahl=8)

# Integration unseres Plotes in die GUI

class Canvas2D(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        
        self.plot2D()
        
 
## Neudefintion der obrigen ShowPlot - Funktion 
    def plot2D(self):
        axe = self.figure.add_subplot(111)

        xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
        yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]

        for i in verbindungsliste.keys():
            for n in range(len(verbindungsliste[i])):
                x1, x2 = xCoord[i], xCoord[verbindungsliste[i][n][0]]
                y1, y2 = yCoord[i], yCoord[verbindungsliste[i][n][0]]
                axe.plot([x1,x2],[y1,y2],':ko')
        axe.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')

        axe.axis([-1, knotenzahl * 5 + 1, -1, knotenzahl * 5 + 1])

        for i in range(knotenzahl):
            axe.text(xCoord[i]-0.5, yCoord[i], str(i))

        xlabel = "Startknoten: "+ str(startkoordinate) + ", Endknoten: "+ str(endkoordinate) + ", Weg: "+ str(weg)+ ", Distanz: "+ str(distanz)
        axe.set_title("Dijkstra")
        axe.set_xlabel(xlabel)

#class Canvas3D(FigureCanvas):
#    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
#        fig = Figure(figsize=(width, height), dpi=dpi)
#        self.axes = fig.add_subplot(1,1,1)
# 
#        FigureCanvas.__init__(self, fig)
#        self.setParent(parent)

        
#        self.plot3D()
        
 
## Neudefintion der obrigen ShowPlot - Funktion 
#    def plot3D(self):
#        ax2 = self.figure.add_subplot(111)

#        xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
#        yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]

#        for i in verbindungsliste.keys():
#            for n in range(len(verbindungsliste[i])):
#                x1, x2 = xCoord[i], xCoord[verbindungsliste[i][n][0]]
#                y1, y2 = yCoord[i], yCoord[verbindungsliste[i][n][0]]
#                ax2.plot([x1,x2],[y1,y2],':ko')
#        ax2.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')

#        ax2.axis([-1, knotenzahl * 5 + 1, -1, knotenzahl * 5 + 1])

#        for i in range(knotenzahl):
#            ax2.text(xCoord[i]-0.5, yCoord[i], str(i))

#        xlabel = "Startknoten: "+ str(startkoordinate) + ", Endknoten: "+ str(endkoordinate) + ", Weg: "+ str(weg)+ ", Distanz: "+ str(distanz)
#        ax2.set_title("Dijkstra")
#        ax2.set_xlabel(xlabel)


# Allgemeiner Code für den GUI - AUfbau 
## automatisch generiert
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.radioButton.setChecked(True)
        
        if self.radioButton.isChecked() == True:
            self.widget1 = Canvas2D(self.splitter, width=8, height=4)
            self.widget1.setObjectName("widget1")
#        else:
#            self.widget2 = Canvas3D(self.splitter, width=8, height=4)
#            self.widget2.setObjectName("widget2")
        
        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Dijkstra Algorithmus"))
        self.label_4.setText(_translate("MainWindow", "Graph-Design"))
        self.radioButton.setText(_translate("MainWindow", "2D"))
        self.radioButton_2.setText(_translate("MainWindow", "3D"))
        self.label_3.setText(_translate("MainWindow", "Anzahl an Knoten:"))
        self.pushButton.setText(_translate("MainWindow", "Graph generieren"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

         