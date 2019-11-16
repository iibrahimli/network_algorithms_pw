import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("cities_in_az.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Destiny',
                            edge_attr=True, create_using=nx.DiGraph)

# add 'visited' attribute to each node
attribute_for_nodes(G, 'visited', False)

print(nx.shortest_path(G, source='Baku', target='Kurdamir', weight='Hours'))