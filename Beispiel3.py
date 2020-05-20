import matplotlib.pyplot as plt
import functools
from random import randint

#dict to label points
mylabel = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}

#dict to derive coordinates
mylabel2 = {
         'A':(randint(1,10),randint(1,10)),
         'B':(randint(1,10),randint(1,10)),
         'C':(randint(1,10),randint(1,10)),
         'D':(randint(1,10),randint(1,10)),
         'E':(randint(1,10),randint(1,10)),
         'F':(randint(1,10),randint(1,10)),
         'G':(randint(1,10),randint(1,10)),
         'H':(randint(1,10),randint(1,10))
           }
#Adjancency and State Matrix
Adj_Matrix = [[0, 20, 0, 0, 0, 0, 15, 0],
             [20, 0, 8, 9, 0, 0, 0, 0],
             [0,  8,  0,  6, 15, 0, 0, 10],
             [0, 9, 6, 0, 7, 0, 0, 0],
             [0, 0, 15, 7, 0, 22, 18, 0],
             [0, 0, 0, 0, 22, 0, 0, 0],
             [15, 0, 0, 0, 18, 0, 0, 0],
             [0, 0, 10, 0, 0, 0, 0, 0]]

xCoord=[mylabel2[k][0] for k in sorted(mylabel2)]
yCoord=[mylabel2[k][1] for k in sorted(mylabel2)]
plt.plot(xCoord, yCoord, 'bo')
plt.axis([-1, 11, -1, 11])

for i in range(8):
    plt.text(xCoord[i]-0.5, yCoord[i], mylabel[i+1])

for i in range(8):
    for j in range(8):
        if Adj_Matrix[i][j]:
            plt.plot([xCoord[i], xCoord[j]],[yCoord[i], yCoord[j]], 'b')

"""
#Dijkstra Algorithm
def dijkstra(graph,start,target):
    inf = functools.reduce(lambda x,y: x+y,(i[1] for u in graph for i
in graph[u]))
    dist = dict.fromkeys(graph,inf)
    prev = dict.fromkeys(graph)
    q = list(graph.keys())
    dist[start] = 0
    while q:
        u = min(q, key=lambda x: dist[x])
        q.remove(u)
        for v,w in graph[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    #”way”
    trav = []
    temp = target
    while temp != start:
        trav.append(prev[temp])
        temp = prev[temp]
    trav.reverse()
    trav.append(target)
    return " -> ".join(trav),dist[target]

graph = {
    'A' : [('B', randint(1,20)), ('G', randint(1,20))],
    'B' : [('A', randint(1,20)),('C', randint(1,20)), ('D', randint(1,20))],
    'C' : [('B', randint(1,20)),('D', randint(1,20)), ('E', randint(1,20)), ('H', randint(1,20))],
    'D' : [('B', randint(1,20)),('C', randint(1,20)),('E', randint(1,20))],
    'E' : [('C', randint(1,20)),('D', randint(1,20)),('F', randint(1,20)),('G', randint(1,20))],
    'F' : [('E', randint(1,20))],
    'G' : [('A', randint(1,20)),('E', randint(1,20))],
    'H' : [('C', randint(1,20))]
    }
traverse, dist = dijkstra(graph,'F','H')
print( traverse)
#Drawing of coordinates
mydrawing = traverse.split('-> ')
plt.plot([ mylabel2[n.rstrip()][0] for n in mydrawing ],[
mylabel2[n.rstrip()][1] for n in mydrawing])
print ("Distance:",dist)"""
plt.show()
