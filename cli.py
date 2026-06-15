from design_graph import Graph
if __name__ == "__main__":
    g = Graph(directed=True)

    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)

    print("=== Structure du graphe ===")
    g.display()

    print(f"\nSommets : {g.node_count}, Arêtes : {g.edge_count}")

    print("\n=== DFS depuis A ===")
    g.dfs("A")

    print("\n=== BFS depuis A ===")
    g.bfs("A")

    print("\n=== Cycle détecté ?", g.detect_cycle())

    print("\n=== Tri topologique ===")
    print(g.topological_sort())

    print("\n=== Plus court chemin A → D ===")
    chemin, distance = g.shortest_path("A", "D")
    print(f"Chemin : {chemin}, Distance : {distance}")



