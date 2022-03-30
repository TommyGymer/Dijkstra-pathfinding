from pyvis.network import Network

net = Network()

graph = {
    "A": {"B": 4, "D": 5, "C": 6},
    "B": {"A": 4, "C": 3},
    "C": {"B": 3, "D": 1, "A": 6},
    "D": {"A": 5, "C": 1}
}

nodes = graph.keys()
net.add_nodes(nodes)

for node, edges in graph.items():
    for end, weight in edges.items():
        net.add_edge(node, end, weight=weight)

net.show("graph.html")