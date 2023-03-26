# prerequisites
import os 
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt  


import numpy as np
import networkx as nx

def transform_list(lst):
    mapping = {}
    counter = 1
    result = []
    for elem in lst:
        if elem not in mapping:
            mapping[elem] = counter
            counter += 1
        result.append(mapping[elem])
    return result

def newman_fast_greedy(G):
    # Initialize community assignments for each node
    communities = {i: i for i in G.nodes()}
    
    # Initialize modularity value
    Q = 0
    best_Q = -1
    # Initialize list of communities
    community_list = list(communities.values())
    
    while len(community_list) > 1:
        # Compute modularity gain for all possible merges
        modularity_gain = {}
        for i in community_list:
            for j in community_list:
                if i != j:
                    modularity_gain[(i, j)] = compute_modularity_gain(G, communities, i, j)
        
        # Find the best merge according to modularity gain
        best_merge = max(modularity_gain, key=modularity_gain.get)
        merge_gain = modularity_gain[best_merge]
        
        # Merge the two communities
        new_community = min(best_merge)
        old_community = max(best_merge)
        for node in communities:
            if communities[node] == old_community:
                communities[node] = new_community
        
        # Update modularity value and community list
        Q += merge_gain

        print(Q)
        
        community_list.remove(old_community)

        if Q > best_Q:
            best_Q=Q
            best=list(communities.values())
    
    return best, best_Q

def compute_modularity_gain(G, communities, c1, c2):
    # Compute the change in modularity resulting from merging communities c1 and c2
    delta_Q = 0
    nodes_c1 = [n for n in communities if communities[n] == c1]
    nodes_c2 = [n for n in communities if communities[n] == c2]
    E_c1c2 = sum([1 for (u, v) in G.edges() if (u in nodes_c1 and v in nodes_c2) or (u in nodes_c2 and v in nodes_c1)])
    E_c1 = sum([G.degree(n) for n in nodes_c1])
    E_c2 = sum([G.degree(n) for n in nodes_c2])
    m = 2 * G.number_of_edges()
    delta_Q = (2*E_c1c2/m) - ((E_c1/m) * (E_c2/m))
    return delta_Q

def plotNetwork(G, communities,title):
    np.random.seed(29)  # to freeze the graph's view (networks uses a random view)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(20, 10)) 
    plt.title(title)
    nx.draw_networkx_nodes(G, pos, node_size=500, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.4)
    #nx.draw_networkx_labels(G, pos,bbox=dict(edgecolor='black', boxstyle='round,pad=0.1'),verticalalignment='top')
    nx.draw_networkx_labels(G, pos,verticalalignment='top')
    plt.show()


network_files = ['data/science.gml','data/london_bars.gml','data/proteine.gml','data/zebra.gml','data/corporate_club.gml','data/iceland.gml','data/train_bombing.gml','data/karate.gml','data/dolphins.gml','data/football.gml','data/krebs.gml']


for network_file in network_files:
    file_name = os.path.basename(network_file)
    G = nx.read_gml(network_file,label='id')
    # Call the Newman fast algorithm for community detection
    communities, modularity = newman_fast_greedy(G)
    colors=transform_list(communities)
    title=os.path.splitext(file_name)[0]
    plotNetwork(G,colors,title)
  # Print the results
    print("Community assignments:", communities)
    print("Best Modularity value:", modularity)

