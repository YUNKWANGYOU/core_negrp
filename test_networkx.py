import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()
graph.add_nodes_from((1,2,3,4,5))
graph.add_edges_from([(1,2), (1,3),(1,4),(3,5)])

nx.draw(graph)
plt.show()