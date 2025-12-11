import time
import networkx as nx
import matplotlib.pyplot as plt
start_time = time.time()

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
print(lines)
G = nx.DiGraph()
count = 0
count2 = 0

for line in lines:
    fro, to = line.split(':')
    for neighbour in to.split():
        G.add_edge(fro, neighbour)

def count_paths(G : nx.DiGraph, source : str, destination : str):
    topo_order = list(nx.topological_sort(G))
    paths = {node: 0 for node in G.nodes}
    paths[source] = 1
    for node in topo_order:
        if paths[node] > 0:
            for neighbour in G.successors(node):
                paths[neighbour] += paths[node]
    return paths[destination]

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

plt.figure(figsize=(16, 12), dpi=400)
pos = nx.spring_layout(G, k=0.9)
nx.draw(G, pos, with_labels=True, node_color='red', edge_color='gray', node_size=50, font_size=4, width=0.2)
plt.title("Device Graph")
plt.savefig("graph.png", format="png", dpi=400)
plt.show()

count = count_paths(G, 'you', 'out')
p1 = count_paths(G, 'svr', 'dac') * count_paths(G, 'dac', 'fft') * count_paths(G, 'fft', 'out')
p2 = count_paths(G, 'svr', 'fft') * count_paths(G, 'fft', 'dac') * count_paths(G, 'dac', 'out')
print(p1, p2, p1 + p2)
count2 = p1 + p2
print(count)
print(count2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
with open('sol.txt', "a") as f:
    f.write(f"{int(time.time())}: P1: {count} P2: {count2}\n")