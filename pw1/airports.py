import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("airports.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)

# add 'visited' attribute to each node
attribute_for_nodes(G, 'visited', False)

# nx.draw_networkx(G, with_labels=True)
# plt.show()

orig, dest = 'LAX', 'ISP'
path = any_path(G, orig, dest)
dist_cost = path_cost(G, path, 'Distance')
airtime_cost = path_cost(G, path, 'AirTime')

print("origin:", orig)
print("destination:", dest)
print("path:", " -> ".join(path))
print("distance cost: {:.2f}".format(dist_cost))
print("air time cost: {:.2f}".format(airtime_cost))