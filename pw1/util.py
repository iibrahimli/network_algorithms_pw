import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def attribute_for_nodes(G, attribute, default_value):
    """
    Create an attribute for every node in G and set it with default value;
    If called again, reset all nodes’ attribute to default value
    """
    for g in G.nodes.keys():
        G.nodes[g][attribute] = default_value


def any_path(G, origin, destination):
    """
    Finds any path from origin to destination (strings)
    Returns a list of node labels from origin to destination
    """

    def dfs_path(G, orig, dest, path):
        """
        Depth-first search to find a path
        """
        
        # path.append(orig)
        G.nodes[orig]['visited'] = True

        for neighbor in G.neighbors(orig):

            if G.nodes[neighbor]['visited']:
                continue

            if neighbor == dest:
                G.nodes[neighbor]['visited'] = True
                path.append(neighbor)
                return
            
            dfs_path(G, neighbor, dest, path)
            if G.nodes[dest]['visited']:
                path.append(neighbor)
                return

    path = []
    dfs_path(G, origin, destination, path)
    return [origin] + path[::-1]


def path_cost(G, path, attr):
    """
    Calculate total cost for the given path and attribute
    """

    return sum([G.edges[n1, n2][attr] for n1, n2 in zip(path[:-1], path[1:])])