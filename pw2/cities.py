import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("cities_in_az.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Destiny',
                            edge_attr=True, create_using=nx.DiGraph)

print("shortest path Baku -> Imishli")
print(" * without weights:", nx.shortest_path(G, source='Baku', target='Imishli'))
print(" * with weights:", nx.shortest_path(G, source='Baku', target='Imishli', weight='Hours'))
# 3.1.3: the total weight for path Baku -> Shamakhi -> Imishli is higher that the other,
#        while the number of nodes needed to travel is lower


nx.add_path(G, ['Baku', 'Imishli'])
G.edges['Baku', 'Imishli']['Hours'] = 1.29

print()
print("shortest path Baku -> Imishli")
print(" *", nx.shortest_path(G, source='Baku', target='Imishli', weight='Hours'))
print("shortest path Imishli -> Baku")
print(" *", nx.shortest_path(G, source='Imishli', target='Baku', weight='Hours'))
# 3.1.5: again, the weight for direct route from Baku to Imishli is lower than others,
#        but from Imishli to Baku the total weight is less by going through 2 more vertices
