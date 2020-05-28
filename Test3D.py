import matplotlib.pyplot as plt
import functools
from random import randint, choice
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D


def ErstelleKoordinatenliste(knotenzahl = 8):
    koordinatenliste = dict()
    for i in range(knotenzahl):
        koordinatenliste[i] = [randint(1, 5*knotenzahl), randint(1, 5*knotenzahl), randint(1, 5*knotenzahl)]
    print(koordinatenliste)
    return koordinatenliste

koordinatenliste = ErstelleKoordinatenliste()


xCoord=[koordinatenliste[k][0] for k in sorted(koordinatenliste)]
yCoord=[koordinatenliste[k][1] for k in sorted(koordinatenliste)]
zCoord=[koordinatenliste[k][2] for k in sorted(koordinatenliste)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(xCoord, yCoord, zCoord)
plt.show()