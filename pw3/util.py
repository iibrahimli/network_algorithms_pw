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


def degree_of_connectivity(G, v):
    """
    Compute the degree of connectivity of a vertex v
    """
    if isinstance(G, nx.Graph):
        return len(G.edges(v))
    elif isinstance(G, nx.DiGraph):
        return len(G.in_edges(v)) + len(G.out_edges(v))
    else:
        raise TypeError("check type of G")


def shortest_paths(G, v, attr=None):
    """
    Get list of shortest paths from v to all other nodes
    """
    sp = []
    for node in G.nodes:
        if node == v: continue
        sp.append(nx.shortest_path(G, source=v, target=node, weight=attr))
    return sp


def closeness_centrality(G, v, attr=None):
    """
    Compute the closeness centrality of a vertex v
    """
    sp = shortest_paths(G, v, attr=attr)
    return sum(map(len, sp)) / len(sp)


def betweenness_centrality(G, v, attr=None):
    """
    Compute the betweenness centrality of a vertex v
    """
    if isinstance(G, nx.Graph):
        vertices = list(G.nodes)
        n_appearances = 0
        for i1 in range(len(vertices)):
            for i2 in range(i1+1, len(vertices)):
                sp = nx.shortest_path(G, source=vertices[i1], target=vertices[i2], weight=attr)
                if v in sp:
                    n_appearances += 1
        return n_appearances
    elif isinstance(G, nx.DiGraph):
        vertices = list(G.nodes)
        n_appearances = 0
        for i1 in range(len(vertices)):
            for i2 in range(len(vertices)):
                if i1 == i2: continue
                sp = nx.shortest_path(G, source=vertices[i1], target=vertices[i2], weight=attr)
                if v in sp:
                    n_appearances += 1
        return n_appearances
    else:
        raise TypeError("check type of G")


def network_density(G):
    """
    Compute the network density
    """
    if isinstance(G, nx.Graph):
        n_vert = len(G.nodes)
        n_edges = len(G.edges)
        return (n_edges) / (n_vert * (n_vert - 1))
    elif isinstance(G, nx.DiGraph):
        n_vert = len(G.nodes)
        n_edges = len(G.edges)
        return (2 * n_edges) / (n_vert * (n_vert - 1))
    else:
        raise TypeError("check type of G")


def network_diameter(G, attr=None):
    """
    Compute the network diameter
    """
    if isinstance(G, nx.Graph):
        max_path_len = float('-inf')
        vertices = list(G.nodes)
        for i1 in range(len(vertices)):
            for i2 in range(i1+1, len(vertices)):
                sp = nx.shortest_path(G, source=vertices[i1], target=vertices[i2], weight=attr)
                sp_len = path_cost(G, sp, attr=attr)
                if sp_len > max_path_len:
                    max_path_len = sp_len
        return max_path_len
    elif isinstance(G, nx.DiGraph):
        max_path_len = float('-inf')
        vertices = list(G.nodes)
        for i1 in range(len(vertices)):
            for i2 in range(len(vertices)):
                if i1 == i2: continue
                sp = nx.shortest_path(G, source=vertices[i1], target=vertices[i2], weight=attr)
                sp_len = path_cost(G, sp, attr=attr)
                if sp_len > max_path_len:
                    max_path_len = sp_len
        return max_path_len
    else:
        raise TypeError("check type of G")


def network_avg_path_len(G, attr=None):
    """
    Compute the network average path length
    """
    if isinstance(G, nx.Graph):
        avg_path_len = 0.0
        count = 0
        vertices = list(G.nodes)
        for i1 in range(len(vertices)):
            for i2 in range(i1+1, len(vertices)):
                sp = nx.shortest_path(G, source=vertices[i1], target=vertices[i2], weight=attr)
                sp_len = path_cost(G, sp, attr=attr)
                avg_path_len += sp_len
                count += 1
        return avg_path_len / count
    elif isinstance(G, nx.DiGraph):
        avg_path_len = 0.0
        vertices = list(G.nodes)
        count = 0
        for i1 in range(len(vertices)):
            for i2 in range(len(vertices)):
                if i1 == i2: continue
                sp = nx.shortest_path(G, source=vertices[i1], target=vertices[i2], weight=attr)
                sp_len = path_cost(G, sp, attr=attr)
                avg_path_len += sp_len
                count += 1
        return avg_path_len / count
    else:
        raise TypeError("check type of G")


def bellman_ford(G, source):
    """
    Bellman-Ford algorithm. Returns 2 dicts: distances and predecessors
    """

    dist = {}
    pred = {}

    for n in G.nodes:
        dist[n] = float('inf')
        pred[n] = None
    
    dist[source] = 0.0

    # relax edges
    for _ in range(len(G.nodes)):
        print("Node")

    return dist, pred