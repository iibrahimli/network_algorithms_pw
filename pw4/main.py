import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("sample_network.csv")

G = nx.from_pandas_edgelist(data, source='Source', target='Sink',
                            edge_attr=True, create_using=nx.Graph)


# nx.draw_networkx(G, with_labels=True)
# plt.show()

v = 23
print(f"stats for network (and node {v})")
print(f" * degree of connectivity:       {degree_of_connectivity(G, v)}")
print(f" * closeness centrality:         {closeness_centrality(G, v, attr='Kbps_AVG'):.3f}")
print(f" * betweenness centrality:       {betweenness_centrality(G, v, attr='Kbps_AVG')}")
print(f" * network density:              {network_density(G):.3f}")
print(f" * network diameter:             {network_diameter(G, attr='Kbps_AVG'):.3f}")
print(f" * network average path length:  {network_avg_path_len(G, attr='Kbps_AVG'):.3f}")


max_flow = edmonds_karp(G, 2, 100, attr='Kbps_AVG')

print("Max flow:", max_flow)