import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("airports.csv")

G = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)

dist, pred = bellman_ford(G, 'CRP')