import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("cities_in_az.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Destiny', edge_attr=True)

# add 'visited' attribute to each node
attribute_for_nodes(G, 'visited', False)

# nx.draw_networkx(G, with_labels=True)
# plt.show()

orig, dest = 'Baku', 'Kurdamir'
path = any_path(G, orig, dest)
cost = path_cost(G, path, 'Hours')

print("origin:", orig)
print("destination:", dest)
print("path:", " -> ".join(path))
print("cost: {:.2f}".format(cost))