import networkx as nx

# read edge list from file
edges = []
with open('data/edge_list.txt', 'r') as f:
    for line in f:
        u, v, w = line.strip().split()
        edges.append((int(u), int(v)))

# create graph from edges
graph = nx.Graph(edges)

# write graph in GML format
nx.write_gml(graph, 'data/train_bombing.gml')