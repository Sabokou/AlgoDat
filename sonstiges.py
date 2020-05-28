import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

# Aufgabe 1

CSV = pd.read_csv("C:\\Users\\alina\\Desktop\\Duales Studium\\Uni Mannheim\\Theoriephase\\2.Semester\\Data Science Fundamentals\\Data Visualization\\Extra\\exercise_studentScores-2.csv")
print(CSV)

# Aufgabe 2

print(CSV.dtypes)

#Aufgabe 3

print(len(CSV.index))

# Aufgabe 4
print(CSV.max())

# Aufgabe 5

print(CSV.sum()/len(CSV.index))

#Aufgabe 6

plt.plot(CSV["Homework1"], CSV["Group Project"], "o")
plt.show()

#Aufgabe 7

plt.plot(CSV["Homework1"], CSV["Homework2"], "o")
plt.show()

#Aufgabe 8

plt.plot(CSV["First exam"], CSV["Group Project"], "o")
plt.show()

#Aufgabe 9

plt.suptitle("Vergleich zwischen 3 Notenverteilung")

plt.subplot(1,2,1)
plt.plot(CSV["Homework1"], CSV["Group Project"], "bo")
plt.title("Hausaufgaben 1 vs. Gruppenaufgabe")
plt.xlabel("Hausaufgabe 1")
plt.ylabel("Gruppenaufgabe")
plt.axis(xmax=60, ymax =70)

plt.subplot(1,2,2)
plt.plot(CSV["Homework1"], CSV["Homework2"], "ro")
plt.title("Hausaufgaben 1 vs. Hausaufgabe 2")
plt.xlabel("Hausaufgabe 1")
plt.ylabel("Hausaufgabe 2")


plt.show()


# Aufgabe 10

std = np.std(CSV[1:])
mean = np.mean(CSV[1:])

mean.plot(kind = "bar", yerr = std)
plt.show()
 