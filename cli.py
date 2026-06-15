from design_graph import Graph
g = Graph(directed=True)



g.add_edge("A","B",10)
g.add_edge("A","C",8)
g.add_edge("B","C",3)
g.add_edge("B","D",5)
g.add_edge("B","F",7)
g.add_edge("C","D",5)
g.add_edge("C","F",7)
g.add_edge("D","E",5)
g.add_edge("D","F",3)
g.add_edge("E","F",3)
g.add_edge("E","G",10)
g.add_edge("F","G",8)


path, distance = g.shortest_path(
    "A",
    "G"
)

print(path)
print(distance)


