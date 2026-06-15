from typing import Any
from collections import deque
import heapq


class Graph:
    """
    Représentation d'un graphe utilisant une liste d'adjacence.

    Chaque sommet pointe vers une liste de tuples :
    (voisin, poids)

    Exemple :
        {
            "A": [("B", 1), ("C", 2)],
            "B": [("D", 1)]
        }

    Attributes:
        _adj:
            Dictionnaire représentant les connexions du graphe.

        directed:
            Indique si le graphe est orienté.
            True → arêtes à sens unique
            False → arêtes bidirectionnelles
    """

    def __init__(self, directed: bool = True) -> None:
        """
        Initialise un graphe vide.

        Args:
            directed:
                True si le graphe est orienté.
        """
        self._adj: dict[Any, list[tuple[Any, int]]] = {}
        self.directed: bool = directed

    @property
    def adj(self) -> dict[Any, list[tuple[Any, int]]]:
        """
        Retourne la structure d'adjacence.

        Lecture uniquement.
        """
        return self._adj

    # ------------------------------------------------------------------ #
    #  Propriétés utilitaires                                              #
    # ------------------------------------------------------------------ #

    @property
    def node_count(self) -> int:
        """Retourne le nombre de sommets."""
        return len(self._adj)

    @property
    def edge_count(self) -> int:
        """Retourne le nombre d'arêtes."""
        total = sum(len(voisins) for voisins in self._adj.values())
        return total if self.directed else total // 2

    def has_node(self, node: Any) -> bool:
        """Retourne True si le sommet existe dans le graphe."""
        return node in self._adj

    def has_edge(self, u: Any, v: Any) -> bool:
        """Retourne True si une arête existe entre u et v."""
        return any(voisin == v for voisin, _ in self._adj.get(u, []))

    # ------------------------------------------------------------------ #
    #  Ajout / suppression                                                 #
    # ------------------------------------------------------------------ #

    def add_node(self, node: Any) -> None:
        """
        Ajoute un sommet au graphe.

        Si le sommet existe déjà, rien n'est fait.

        Args:
            node:
                Valeur représentant le sommet.
        """
        if node not in self._adj:
            self._adj[node] = []

    def add_edge(
        self,
        u: Any,
        v: Any,
        weight: int = 1
    ) -> None:
        """
        Ajoute une arête entre deux sommets.

        Si un sommet n'existe pas, il est créé automatiquement.
        Si l'arête existe déjà, elle est ignorée.

        Args:
            u:      Sommet source.
            v:      Sommet destination.
            weight: Poids de l'arête. Par défaut = 1.
        """
        self.add_node(u)
        self.add_node(v)

        # CORRECTION : éviter les doublons
        if not self.has_edge(u, v):
            self._adj[u].append((v, weight))

        if not self.directed and not self.has_edge(v, u):
            self._adj[v].append((u, weight))

    def remove_node(self, node: Any) -> None:
        """
        Supprime un sommet et toutes ses arêtes associées.

        Args:
            node: Sommet à supprimer.

        Raises:
            KeyError: Si le sommet n'existe pas.
        """
        if node not in self._adj:
            raise KeyError(f"Le sommet '{node}' n'existe pas.")

        del self._adj[node]

        for voisins in self._adj.values():
            voisins[:] = [(v, w) for v, w in voisins if v != node]

    def remove_edge(self, u: Any, v: Any) -> None:
        """
        Supprime l'arête entre u et v.

        Args:
            u: Sommet source.
            v: Sommet destination.

        Raises:
            KeyError: Si l'arête n'existe pas.
        """
        if not self.has_edge(u, v):
            raise KeyError(f"L'arête '{u}' → '{v}' n'existe pas.")

        self._adj[u] = [(voisin, w) for voisin, w in self._adj[u] if voisin != v]

        if not self.directed:
            self._adj[v] = [(voisin, w) for voisin, w in self._adj[v] if voisin != u]

    # ------------------------------------------------------------------ #
    #  Affichage                                                           #
    # ------------------------------------------------------------------ #

    def display(self) -> None:
        """
        Affiche la structure du graphe.

        Exemple :
            A → [('B', 1), ('C', 2)]
            B → [('D', 1)]
        """
        for node in self._adj:
            print(node, "→", self._adj[node])

    # ------------------------------------------------------------------ #
    #  Parcours DFS                                                        #
    # ------------------------------------------------------------------ #

    def dfs(self, node: Any) -> None:
        """
        Lance un parcours DFS depuis un sommet donné.

        Args:
            node: Sommet de départ.
        """
        visited: set[Any] = set()
        self._dfs(node, visited)

    def _dfs(self, node: Any, visited: set[Any]) -> None:
        """
        Implémentation récursive du DFS.

        Args:
            node:    Sommet courant.
            visited: Ensemble des sommets déjà visités.
        """
        if node in visited:
            return

        visited.add(node)
        print(node)

        for voisin, _ in self._adj.get(node, []):
            self._dfs(voisin, visited)

    def dfs_all(self) -> None:
        """
        Parcourt complètement le graphe en utilisant DFS.

        Garantit que tous les sommets seront visités même
        si le graphe contient plusieurs composantes séparées.
        """
        # CORRECTION : indentation du corps de méthode corrigée
        visited: set[Any] = set()

        for node in self._adj:
            if node not in visited:
                self._dfs(node, visited)

    # ------------------------------------------------------------------ #
    #  Parcours BFS (nouveau)                                              #
    # ------------------------------------------------------------------ #

    def bfs(self, node: Any) -> None:
        """
        Lance un parcours BFS depuis un sommet donné.

        Explore les sommets niveau par niveau (en largeur).

        Args:
            node: Sommet de départ.
        """
        if node not in self._adj:
            return

        visited: set[Any] = set()
        queue: deque[Any] = deque([node])
        visited.add(node)

        while queue:
            current = queue.popleft()
            print(current)

            for voisin, _ in self._adj.get(current, []):
                if voisin not in visited:
                    visited.add(voisin)
                    queue.append(voisin)

    def bfs_all(self) -> None:
        """
        Parcourt complètement le graphe en utilisant BFS.

        Garantit que tous les sommets seront visités même
        si le graphe contient plusieurs composantes séparées.
        """
        visited: set[Any] = set()

        for node in self._adj:
            if node not in visited:
                queue: deque[Any] = deque([node])
                visited.add(node)

                while queue:
                    current = queue.popleft()
                    print(current)

                    for voisin, _ in self._adj.get(current, []):
                        if voisin not in visited:
                            visited.add(voisin)
                            queue.append(voisin)

    # ------------------------------------------------------------------ #
    #  Détection de cycle                                                  #
    # ------------------------------------------------------------------ #

    def _has_cycle_dfs(
        self,
        node: Any,
        visited: set,
        rec_stack: set
    ) -> bool:
        """
        Détection de cycle en DFS pour graphe orienté.

        Args:
            node:      Sommet courant.
            visited:   Sommets déjà explorés globalement.
            rec_stack: Sommets dans le chemin DFS actuel.
        """
        # CORRECTION : indentation corrigée
        visited.add(node)
        rec_stack.add(node)

        for voisin, _ in self._adj.get(node, []):
            if voisin not in visited:
                if self._has_cycle_dfs(voisin, visited, rec_stack):
                    return True
            elif voisin in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    def _has_cycle_undirected(
        self,
        node: Any,
        visited: set,
        parent: Any
    ) -> bool:
        """
        Détection de cycle en DFS pour graphe non-orienté.

        Args:
            node:    Sommet courant.
            visited: Sommets déjà visités.
            parent:  Sommet depuis lequel on est arrivé.
        """
        visited.add(node)

        for voisin, _ in self._adj.get(node, []):
            if voisin not in visited:
                if self._has_cycle_undirected(voisin, visited, node):
                    return True
            elif voisin != parent:
                # On a trouvé un voisin déjà visité qui n'est pas le parent → cycle
                return True

        return False

    def detect_cycle(self) -> bool:
        """
        Détecte s'il existe un cycle dans le graphe.

        Gère automatiquement les graphes orientés et non-orientés.

        Retour :
            True  → cycle détecté
            False → aucun cycle
        """
        visited: set = set()

        if self.directed:
            rec_stack: set = set()
            for node in self._adj:
                if node not in visited:
                    if self._has_cycle_dfs(node, visited, rec_stack):
                        return True
        else:
            # CORRECTION : logique séparée pour les graphes non-orientés
            for node in self._adj:
                if node not in visited:
                    if self._has_cycle_undirected(node, visited, None):
                        return True

        return False

    # ------------------------------------------------------------------ #
    #  Tri topologique (nouveau)                                           #
    # ------------------------------------------------------------------ #

    def topological_sort(self) -> list[Any]:
        """
        Retourne un tri topologique du graphe orienté acyclique (DAG).

        Le tri topologique garantit que pour toute arête u → v,
        u apparaît avant v dans le résultat.

        Returns:
            Liste des sommets dans l'ordre topologique.

        Raises:
            ValueError: Si le graphe contient un cycle ou n'est pas orienté.
        """
        if not self.directed:
            raise ValueError("Le tri topologique nécessite un graphe orienté.")

        if self.detect_cycle():
            raise ValueError("Le tri topologique nécessite un graphe acyclique (DAG).")

        visited: set[Any] = set()
        stack: list[Any] = []

        def _dfs_topo(node: Any) -> None:
            visited.add(node)
            for voisin, _ in self._adj.get(node, []):
                if voisin not in visited:
                    _dfs_topo(voisin)
            stack.append(node)

        for node in self._adj:
            if node not in visited:
                _dfs_topo(node)

        return stack[::-1]

    # ------------------------------------------------------------------ #
    #  Dijkstra et plus court chemin                                       #
    # ------------------------------------------------------------------ #

    def dijkstra(self, start: Any) -> tuple[
        dict[Any, float],
        dict[Any, Any]
    ]:
        """
        Calcule les plus courtes distances depuis un sommet de départ.

        Utilise l'algorithme de Dijkstra.

        Args:
            start: Sommet source.

        Returns:
            tuple :
                (distances, parents)

            distances :
                coût minimal depuis start

            parents :
                permet de reconstruire les chemins optimaux
        """
        distance: dict[Any, float] = {
            node: float("inf")
            for node in self._adj
        }

        parent: dict[Any, Any] = {}
        visited: set[Any] = set()
        pq: list[tuple[float, Any]] = []

        distance[start] = 0
        heapq.heappush(pq, (0, start))

        while pq:
            dist_u, u = heapq.heappop(pq)

            if u in visited:
                continue

            visited.add(u)

            for v, weight in self._adj.get(u, []):
                new_dist = dist_u + weight

                if new_dist < distance[v]:
                    distance[v] = new_dist
                    parent[v] = u
                    heapq.heappush(pq, (new_dist, v))

        return distance, parent

    def shortest_path(self, start: Any, end: Any) -> tuple[
        list[Any],
        float
    ]:
        """
        Retourne le plus court chemin entre deux sommets.

        Args:
            start: Sommet départ.
            end:   Sommet arrivée.

        Returns:
            (chemin, distance)

        Raises:
            KeyError: Si start ou end n'existe pas dans le graphe.
        """
        # CORRECTION : vérification des sommets avant accès au dictionnaire
        if start not in self._adj:
            raise KeyError(f"Le sommet de départ '{start}' n'existe pas.")
        if end not in self._adj:
            raise KeyError(f"Le sommet d'arrivée '{end}' n'existe pas.")

        distances, parent = self.dijkstra(start)

        if distances[end] == float("inf"):
            return [], float("inf")

        path: list[Any] = []
        current = end

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()

        return path, distances[end]


# ---------------------------------------------------------------------- #
#  Exemple d'utilisation                                                   #
# ---------------------------------------------------------------------- #

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