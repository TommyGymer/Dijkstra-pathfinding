from pyvis.network import Network
import math
import time

net = Network()

class node():
    index = None
    label = None
    dist = math.inf
    heuristic = 0
    total = math.inf
    prev = None
    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return f"<node {self.label} i: {self.index} dist: {self.dist} heuristic: {self.heuristic} total: {self.total} prev: {self.prev}>"

# graph = {
#     "A": {"B": 4, "C": 6},
#     "B": {"A": 4, "C": 3},
#     "C": {"B": 3, "D": 1, "A": 6},
#     "D": {"C": 1}
# }

graph = {
    "A": {"B": 3, "D": 25, "I": 12},
    "B": {"A": 3, "C": 5},
    "C": {"B": 5, "D": 14, "E": 6},
    "D": {"A": 25, "C": 14, "E": 7},
    "E": {"C": 6, "D": 7, "F": 8, "G": 16},
    "F": {"I": 7, "E": 8, "G": 9},
    "G": {"E": 16, "F": 9, "H": 11},
    "H": {"J": 23, "G": 11},
    "I": {"A": 12, "J": 10, "F": 7},
    "J": {"I": 10, "H": 23},
}

nodes = graph.keys()
net.add_nodes(nodes)

for n, edges in graph.items():
    for end, weight in edges.items():
        net.add_edge(n, end, weight=weight)

#net.show("graph.html")

print("starting pathfinding")
start_t = time.time()

start = "A"
end = "H"

cnode = start
data = {}

for n in graph.keys():
    #index, from start, heuristic, prev node
    data[n] = node(n)

i = 1
while True:
    if not data[cnode].prev:
        #this must be the first node
        data[cnode].dist = 0
        data[cnode].total = 0
    data[cnode].index = i
    for n, dist in graph[cnode].items():
        if data[n].index:
            continue
        if data[n].dist > data[cnode].dist + dist:
            data[n].dist = data[cnode].dist + dist
            data[n].total = data[n].dist + data[n].heuristic
            data[n].prev = cnode
    i += 1
    cnodes = [(node, obj) for node, obj in data.items() if not obj.index]
    cnodes.sort(key=lambda x: x[1].total)
    cnode = cnodes[0][0]
    #need to sort the items in data which do not have and index by the total dist and then chose the closest
    if cnode == end:
        break

#[print(f"{n}: {o}") for n, o in data.items()]

route = [cnode]
total_dist = data[cnode].total

while True:
    cnode = data[cnode].prev
    route.append(cnode)
    if cnode == start:
        break

route.reverse()

print(route)
print(total_dist)

end_t = time.time()

print(f"finished pathfinding in {(end_t - start_t) * 1000}ms")
