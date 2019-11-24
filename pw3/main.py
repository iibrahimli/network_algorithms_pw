import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("airports.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True,
                            create_using=nx.DiGraph)


print(" *** Bellman-Ford ***")
print()

dist, pred = bellman_ford(G, 'CRP', attr='Distance')
sp = get_shortest_path_from_pred(pred, 'CRP', 'BOI')
print("CRP -> BOI shortest path by distance:", dist['BOI'], sp)
dist, pred = bellman_ford(G, 'CRP', attr='AirTime')
sp = get_shortest_path_from_pred(pred, 'CRP', 'BOI')
print("CRP -> BOI shortest path by air time:", dist['BOI'], sp)

print()
dist, pred = bellman_ford(G, 'BOI', attr='Distance')
sp = get_shortest_path_from_pred(pred, 'BOI', 'CRP')
print("BOI -> CRP shortest path by distance:", dist['CRP'], sp)
# dist, pred = bellman_ford(G, 'BOI', attr='AirTime')
# sp = get_shortest_path_from_pred(pred, 'BOI', 'CRP')
# print("BOI -> CRP shortest path by air time:", dist['CRP'], sp)


print()
print()
print(" *** Dijkstra ***")
print()

dist, pred = dijkstra(G, 'CRP', attr='Distance')
sp = get_shortest_path_from_pred(pred, 'CRP', 'BOI')
print("CRP -> BOI shortest path by distance:", dist['BOI'], sp)
dist, pred = dijkstra(G, 'CRP', attr='AirTime')
sp = get_shortest_path_from_pred(pred, 'CRP', 'BOI')
print("CRP -> BOI shortest path by air time:", dist['BOI'], sp)

print()
dist, pred = dijkstra(G, 'BOI', attr='Distance')
sp = get_shortest_path_from_pred(pred, 'BOI', 'CRP')
print("BOI -> CRP shortest path by distance:", dist['CRP'], sp)
# dist, pred = dijkstra(G, 'BOI', attr='AirTime')
# sp = get_shortest_path_from_pred(pred, 'BOI', 'CRP')
# print("BOI -> CRP shortest path by air time:", dist['CRP'], sp)