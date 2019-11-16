import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("airports.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)

# add 'visited' attribute to each node
attribute_for_nodes(G, 'visited', False)

print("shortest path (Distance) CRP -> BOI and vice versa")
print(" *", nx.shortest_path(G, source='CRP', target='BOI', weight='Distance'))
print(" *", nx.shortest_path(G, source='BOI', target='CRP', weight='Distance'))

print()
print("shortest path (AirTime) CRP -> BOI and vice versa")
print(" *", nx.shortest_path(G, source='CRP', target='BOI', weight='AirTime'))
print(" *", nx.shortest_path(G, source='BOI', target='CRP', weight='AirTime'))

v = 'LAX'
print()
print(f"stats for {v}")
print(f" * degree of connectivity:  {degree_of_connectivity(G, v)}")
print(f" * closeness centrality:    {closeness_centrality(G, v, attr='Distance'):.2f}")
print(f" * betweenness centrality:  {betweenness_centrality(G, v, attr='Distance'):.2f}")
