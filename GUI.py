"""
Autoren:    Alina Buss      (4163246)
            Phillip Lange   (5920414)
"""

#region Imports
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
#endregion

#Nötige Funktionen für Dijkstra Algorithmus definieren
#region Dijkstra-Algorithmus
## Definition des reinen Dijkstra Algorithmus, der sich an dem Pseudocode orientiert
def dijkstra(verbindungsliste,start,ende):
    distanz = dict()
    herkunftsliste = dict()
    warteschlange = list()
    for i in verbindungsliste.keys():                                                                               # initialisiert Distanzliste mit "unendlich" für jeden Index
        distanz[i] = float('inf')                                                                    
        herkunftsliste[i] = 0                                                                                       # initialisiert Dictionary mit Distanzen zu vorherigen Sachen mit 0
        warteschlange.append(i)                                                                                     # Liste mit allen Knotennamen
    
    distanz[start] = 0                                                                                              # Distanz zum Startpunkt ist 0
    while len(warteschlange) != 0:                                                                                  # so lange Elemente vorhanden sind:
        minimum = min(warteschlange, key=lambda x: distanz[x])                                                      # wähle Knoten aus wo die Distanz am kleinsten ist
        warteschlange.remove(minimum)                                                                               # entfernt Element, damit es nicht nochmal überprüft werden kann
        for verbindung, strecke in verbindungsliste[minimum]:
            alternative = distanz[minimum] + strecke                                                                # Distanz aus kürzestem Weg + neue kürzeste Route zum nächsten Knoten
            if alternative < distanz[verbindung]:                                                                   # Wenn neue Route kleiner der alten ist
                distanz[verbindung] = alternative                                                                   # setze Distanz zu neuem Knoten als Distanz
                herkunftsliste[verbindung] = minimum                                                                # merke dir den Punkt, den du vorher angesteuert hast
    
    weg = [ende]                                                                                                    # Erstellt die Liste, die später den optimalen Weg zeigt                                                                 
    temporaer = ende                                                                                                # Wird als Hilfsvariable genutzt um sicher zu stellen, dass zumindest Start- und Endknoten im Weg stehen
    while temporaer != start:                                                                                          
        weg.append(herkunftsliste[temporaer])                                                                       # Fügt aus der Herkunftsliste hinzu, wie man zu temporaer kam
        temporaer = herkunftsliste[temporaer]                                                                       # Der neue Punkt von dem der Herkunftsknoten bestimmt werden soll ist der gerade hinzugefügte
    weg.reverse()                                                                                                   # Der Weg wird rückkwärts aufgebaut und muss deswegen noch gedreht werden
    return weg, distanz[ende]
#endregion

#region Berechnung der Kantenlängen
## Definition der Hilfsfunktion Pythagoras -> diese errechnet die Distanz zwischen 2 Knotenpunkten
### Pythagoras2D berechnet die Distanz zwischen den Knoten innerhalb eines zweidimensionalen Koordinatensystem
def Pythagoras2D(Punkt1, Punkt2):
    """
        Nutzt die euklidische Norm auf zweidimensionalen Ortsvektoren der jeweiligen Punkte im die Distanz zwischen ihnen zu bestimmen
        Das Ergebnis wird gerundet für Übersichtlichkeit und sollte es somit zu 0 werden sei es stattdessen 1 
    """
    distanz = round(sqrt(((Punkt1[0]-Punkt2[0])**2 + (Punkt1[1] - Punkt2[1])**2)))
    if distanz == 0:
        return 1
    else:
        return distanz

### Pythagoras3D berechnet die Distanz zwischen den Knoten innerhalb eines dreidimensionalen Koordinatensystem
def Pythagoras3D(Punkt1, Punkt2):
    """
        Nutzt die euklidische Norm auf dreidimensionale Ortsvektoren der jeweiligen Punkte im die Distanz zwischen ihnen zu bestimmen
        Das Ergebnis wird gerundet für Übersichtlichkeit und sollte es somit zu 0 werden sei es stattdessen 1 
    """
    distanz = round(sqrt(((Punkt1[0]-Punkt2[0])**2 + (Punkt1[1] - Punkt2[1])**2+ (Punkt1[2] - Punkt2[2])**2)))
    if distanz == 0:
        return 1
    else:
        return distanz
#endregion

#region Erstellung der Koordinaten
## Definition der Funktion ErstelleKoordinatenliste2D -> erstellt eine Koordinatenliste mit zufälligen Knotenkoordinaten im zweidimensionalen Raum
def ErstelleKoordiantenliste2D(knotenzahl = 8):
    # Die Koordianten werden in einem Dictionary gespeichert mit der Indexzahl als Schlüssel und den Koordianten als Tupel
    koordinatenliste = dict()
    # Die Knotenzahl gibt vor wie viele Knoten erzeugt werden
    for i in range(knotenzahl):
        # Da der Schlüssel der Index ist wird jedes mal 2 zufällige Ganzzahlen generiert und als Tupel dem Schlüssel zugewiesen
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(f"Koordinatenliste: {koordinatenliste}\n")
    return koordinatenliste

## Definition der Funktion ErstelleKoordinatenliste3D -> erstellt eine Koordinatenliste mit zufälligen Knotenkoordinaten im dreidimensionalen Raum
def ErstelleKoordinatenliste3D(knotenzahl = 8):
    koordinatenliste = dict()
    for i in range(knotenzahl):
        # Da der Schlüssel der Index ist werden jedes mal 3 zufällige Ganzzahlen generiert, die die x1-, x2- & x3-Werte bilden und als Tupel dem Schlüssel zugewiesen werden
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(f"Koordinatenliste: {koordinatenliste}\n")
    return koordinatenliste
#endregion

#region Erstellung der Kantenlisten
## Definition der Funktion ErstelleVerbindungsliste 
### nutzt die erstellte Koordinatenliste, um die entsprechenden Kanten zwischen den Knoten zufällig zu generieren
### ruft dabei die oben definierte Hilfsfunktion Pythagoras auf 
#### ErstelleVerbindungsliste2D generiert die Kanten für den zweidimensionalen Raum
def ErstelleVerbindungsliste2D(koordinatenliste, knotenzahl = 8):
    """
        Initialisiert ein Dictionary mit sämtlichen Keys aus der Koordinatenliste und weißt ihnen eine Liste zu mit allen zufällig gewählten Verbindungen
        Diese Verbindungen sind alle gerichtet, welches bedeutet, dass z.B. 1 -> 3 generiert werden kann aber nicht im folgenden 3 -> 1
    """
    #Initialisierung des Dictionaries
    verbindungsliste = dict()
    for i in koordinatenliste.keys():
        verbindungsliste[i] = list()
    #Für jeden Schlüssel werden dann eine zufällige Menge an Verbindungen erstellt
    for i in koordinatenliste.keys():
        #Wir haben uns entschieden bei einer höhreren Anzahl an Knoten die Menge an zugelassenen Verbinduungen zu erhöhen von max. 2 auf eine linear wachsende Funktion
        if knotenzahl < 20:
            k = randint(1,2)
        else: 
            k= randint(1, knotenzahl // 10 + 1)
        genutzteverbindungsliste = []
        # basierend auf der erzeugten Verbindungszahl k werden zufällig gerichtete Verbindungen erstellt
        for j in range(k):
            # choice wählt aus der Liste der möglichen Verbindungen eine aus
            # die Liste der möglichen Verbindugen sind alle, die noch nicht genutzt wurden, nicht der Punkt selber ist oder bereits exisitert
            verbindung = choice([n for n in range(knotenzahl) if (n != i) and (n not in genutzteverbindungsliste)])
            genutzteverbindungsliste.append(verbindung)
            # zum jeweiligen Verbindungsknoten wird automatisch auch die 
            distanz = Pythagoras2D(koordinatenliste[i], koordinatenliste[verbindung])
            verbindungsliste[i] = verbindungsliste[i] + [(verbindung, distanz)]
            verbindungsliste[verbindung] = verbindungsliste[verbindung] + [(i, distanz)]
    print("Verbindungen:", verbindungsliste)
    return verbindungsliste


#### ErstelleVerbindungsliste3D generiert die Kanten für den dreidimensionalen Raum
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
    print("Verbindungen:", verbindungsliste)
    return verbindungsliste
#endregion

#region Plot-Klasse für GUI
# Integration unseres Plotes in die GUI
## Insgesamt existieren drei Klassen von Plots, die in die GUI integriert werden können: 
##  ein leerer Anfangsplot, ein befüllter zweidimensionaler Plot und ein befüllter dreidimensionaler Plot

###Definition des leeren Anfangsplot
####Alle Plots erben von FigureCanvas
class CanvasLeer(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        #Definition der Figurart - hier zweidimensionaler Plot ohne Inputs
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)

        #Aufruf der FigureCanvas-Oberklasse
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


###Definition des befüllten zweidimensionalen Plots
class Canvas2D(FigureCanvas):
    #Initialisierung des 2D-Plots
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100, knotenzahl=8):
        #Definition der Figurart - hier zweidimensionaler Plots -> Inputs folgen
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)

        #Aufruf der FigureCanvas-Oberklasse
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        #Aufruf der folgenden plot2D-Funktionen -> diese integriert die Knoten-, Kanten- und Weginputs in den bisher leeren zweidimensionalen Plots 
        self.plot2D(knotenzahl)
        
    #Definition der plot2D-Funktion ->ruft die oben definierten Dijkstra-Funktionen für den zweidimensionalen Raum auf
    #   ->Die Knoten, Kanten und der kürzeste Weg, die durch die Dijkstra-Funktionen generiert wurden, werden in den zweidimensionalen Plot integriert
    def plot2D(self, knotenzahl):
        # Definition als zweidimensionaler Subplot
        axe = self.figure.add_subplot(111)

        #Aufruf der Dijkstra Funktionen ->Knoten und Koordinaten werden generiert
        koordinatenliste = ErstelleKoordiantenliste2D(knotenzahl)
        verbindungsliste = ErstelleVerbindungsliste2D(koordinatenliste, knotenzahl = knotenzahl)
        startkoordinate = randint(0,knotenzahl)
        endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

        #Der kürzeste Weg wird berechnet
        weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
        print(f"\nWeg: {weg}")
        print (f"Distanz: {distanz}")

        #Vorbereitung der x- und y-Koordinatenlisten, die geploted werden sollen
        xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
        yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]
        
        #Iteration über die Verbindungliste, um alle zusammengehörigen Kanten und Knotten zu plotten
        ##Betrachtung jedes einzelnen Keys in der Verbindungliste
        for i in verbindungsliste.keys():
            #Iteration über die mit dem Key verbundenen Knoten
            for n in range(len(verbindungsliste[i])):
                #Definition der x- und y-Koordinaten des Keys und seinem verbundenen Knoten
                x1, x2 = xCoord[i], xCoord[verbindungsliste[i][n][0]]
                y1, y2 = yCoord[i], yCoord[verbindungsliste[i][n][0]]
                #Knoten und Kanten des Keys mit seinem Nachbar werden hier geplottet
                axe.plot([x1,x2],[y1,y2],':ko')

        #Hier wird der letztendliche kürzeste Weg aus dem Dijkstra-Algorithmus mit rot gezeichnet
        axe.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')

        #Beschriftung aller Knoten
        for i in range(knotenzahl):
            axe.text(xCoord[i]-1, yCoord[i], str(i))
        
        # Der String beinhaltet alle relevanten Daten, die für die Laufzeit des Algorithmus wichtig waren
        xlabel = "Startknoten: "+ str(startkoordinate) + ", Endknoten: "+ str(endkoordinate) + ", Weg: "+ str(weg)+ ", Distanz: "+ str(distanz)
        # Der Titel wird genutzt um Informationen über die Berechnung des Dijkstra-Algorithmus anzuzeigen
        axe.set_title("Dijkstra\n" + xlabel)

###Definition des befüllten dreidimensionalen Plots
class Canvas3D(FigureCanvas):
    #Initialisierung des 3D-Plots
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100, knotenzahl=8):
        #Definition der Figurart - hier dreidimensionaler Plots -> Inputs folgen
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)

        #Aufruf der FigureCanvas-Oberklasse
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        #Aufruf der folgenden plot3D-Funktionen -> diese integriert die Knoten-, Kanten- und Weginputs in den bisher leeren dreidimensionalen Plots 
        self.plot3D(knotenzahl)
        
 #Definition der plot3D-Funktion ->ruft die oben definierten Dijkstra-Funktionen für den dreidimensionalen Raum auf
    #   ->Die Knoten, Kanten und der kürzeste Weg, die durch die Dijkstra-Funktionen generiert wurden, werden in den dreidimensionalen Plot integriert
    def plot3D(self, knotenzahl):
        # Definition als dreidimensionaler Subplot
        ax2 = self.figure.add_subplot(111, projection='3d')

        #Aufruf der Dijkstra Funktionen ->Knoten und Koordinaten werden generiert
        koordinatenliste = ErstelleKoordinatenliste3D(knotenzahl)
        verbindungsliste = ErstelleVerbindungsliste3D(koordinatenliste, knotenzahl = knotenzahl)
        startkoordinate = randint(0,knotenzahl)
        endkoordinate = choice([n for n in range(knotenzahl) if (n !=  startkoordinate)])

        #Der kürzeste Weg wird berechnet
        weg, distanz = dijkstra(verbindungsliste,startkoordinate, endkoordinate)
        print(f"\nWeg: {weg}")
        print (f"Distanz: {distanz}")

        #Vorbereitung der x-,y- und z-Koordinatenlisten, die geploted werden sollen
        xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
        yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]
        zCoord=[koordinatenliste[k][2] for k in sorted(koordinatenliste)]

        #Iteration über die Verbindungliste, um alle zusammengehörigen Kanten und Knotten zu plotten
        ##Betrachtung jedes einzelnen Keys in der Verbindungliste
        for i in verbindungsliste.keys():
            #Iteration über die mit dem Key verbundenen Knoten
            for n in range(len(verbindungsliste[i])):
                #Definition der x-, y- und z-Koordinaten des Keys und seinem verbundenen Knoten
                x1, x2 = xCoord[i], xCoord[verbindungsliste[i][n][0]]
                y1, y2 = yCoord[i], yCoord[verbindungsliste[i][n][0]]
                z1, z2 = zCoord[i], zCoord[verbindungsliste[i][n][0]]
                #Knoten und Kanten des Keys mit seinem Nachbar werden hier geplottet
                ax2.plot([x1,x2],[y1,y2],[z1,z2],':ko')

        #Hier wird der letztendliche kürzeste Weg aus dem Dijkstra-Algorithmus mit rot gezeichnet        
        ax2.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg],[koordinatenliste[n][2] for n in weg], '-r')

        #Beschriftung aller Knoten
        for i in range(knotenzahl):
            ax2.text(xCoord[i]-1, yCoord[i]+1, zCoord[i]+0.5, str(i))

        # Der String beinhaltet alle relevanten Daten, die für die Laufzeit des Algorithmus wichtig waren
        xlabel = "Startknoten: "+ str(startkoordinate) + ", Endknoten: "+ str(endkoordinate) + ", Weg: "+ str(weg)+ ", Distanz: "+ str(distanz)
        # Der Titel wird genutzt um Informationen über die Berechnung des Dijkstra-Algorithmus anzuzeigen
        ax2.set_title("Dijkstra\n" + xlabel)
#endregion

#region GUI
# Allgemeiner Code für den GUI - AUfbau 
## automatisch generiert
class Ui_MainWindow(object):
    """
        Klasse repräsentiert die GUI und alle inkludierten Objekte
    """
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
        self.lineEdit.setText("8")
        
        self.verticalLayout.addWidget(self.lineEdit)
        
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.verticalLayout.addWidget(self.line_3)
        
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button_clicked)
        
        self.verticalLayout.addWidget(self.pushButton)
        
        self.radioButton.setChecked(True)
        
        self.widget0 = CanvasLeer(self.splitter, width=8, height=4)
        self.widget0.setObjectName("widget0")

        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def deletePriorWidgets(self):
        """
            Um zu verhindern, dass mehrere Graphen im rechten Teil der GUI erzeugt werden entfernt diese Methode bereits erzeugte Widgets.
            Da nicht zu jedem Zeitpuntk alle Widgets initalisiert sind muss über Try/Except die einzelnen Befehle ausgeführt werden.
        """
        try:
            self.widget0.setParent(None)
        except:
            pass

        try:
            self.widget1.setParent(None)
        except:
            pass
        
        try:          
            self.widget2.setParent(None)
        except:
            pass
    
    def button_clicked(self):
        """
            Eventhandler für den Button
            Überprüft, welcher Radiobutton markiert wurde und ruft dem entsprechend die Erstellfunktion für 2D- oder 3D Graphen auf 
        """
        
        # Löschung vorher erstellten Widgets
        self.deletePriorWidgets()
        # Exception Handling für den Fall, dass der Nutzer keine Zahl eingibt
        try:
            knoten = int(self.lineEdit.text())
        except:
            knoten = 8

        print(f"Anzahl Knoten: {knoten}")
        
        if self.radioButton.isChecked() == True:
            self.widget1 = Canvas2D(self.splitter, width = 8, height = 4, knotenzahl = knoten)
            self.widget1.setObjectName("widget1")
        else:
            self.widget2 = Canvas3D(self.splitter, width = 8, height = 4, knotenzahl = knoten)
            self.widget2.setObjectName("widget2")

    def retranslateUi(self, MainWindow):
        """
            Standard-Element von PyQT5 GUIs
            Kann genutzt werden um Mehrsprachigkeit der GUI zu gewährleisten
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Dijkstra Algorithmus"))
        self.label_4.setText(_translate("MainWindow", "Graph-Design"))
        self.radioButton.setText(_translate("MainWindow", "2D"))
        self.radioButton_2.setText(_translate("MainWindow", "3D"))
        self.label_3.setText(_translate("MainWindow", "Anzahl an Knoten:"))
        self.pushButton.setText(_translate("MainWindow", "Graph generieren"))
#endregion

#region Main-Call
"""
    Die folgende Region wird dazu genutzt um die GUI zu initaliseren, welches den Programmfluss eventbasiert bestimmt
"""
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
#endregion