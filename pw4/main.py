import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util import *


data = pd.read_csv("sample_network.csv")

G = nx.from_pandas_edgelist(data, source='Source', target='Sink',
                            edge_attr=True, create_using=nx.Graph)

