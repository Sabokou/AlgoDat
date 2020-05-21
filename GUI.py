# -*- coding: utf-8 -*-

import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

import Main

class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        #self.zeichne()
 
 
    def zeichne(self):

        
        # xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
        # yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]

        # for i in verbindungsliste.keys():
        #     for n in range(len(verbindungsliste[i])):
        #         Main.connectpoints(xCoord, yCoord, i, verbindungsliste[i][n][0])

        # plt.axis([-1, knotenzahl * 5 + 1, -1, knotenzahl * 5 + 1])

        # for i in range(knotenzahl):
        #     plt.text(xCoord[i]-0.5, yCoord[i], str(i))

        # plt.plot([koordinatenliste[n][0] for n in weg ],[koordinatenliste[n][1] for n in weg], '-r')

        # plt.show()
        Main.plt.show()  

        # x = np.array([50, 30,40])
        # labels = ["Apples", "Bananas", "Melons"]
        # ax = self.figure.add_subplot(111)
        # ax.pie(x, labels=labels)

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
        
        
        self.widget1 = Canvas(self.splitter, width=8, height=4)
        self.widget1.setObjectName("widget1")
        
        
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

         