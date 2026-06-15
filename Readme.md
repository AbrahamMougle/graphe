# 🗺️ Graph — Bibliothèque Python de graphes

Implémentation orientée objet d'un graphe en Python, couvrant les structures de données, les algorithmes de parcours, la détection de cycles et le calcul de plus courts chemins.

---

## 📋 Table des matières

- [Aperçu](#aperçu)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation rapide](#utilisation-rapide)
- [API complète](#api-complète)
- [Algorithmes implémentés](#algorithmes-implémentés)
- [Exemples](#exemples)

---

## Aperçu

Ce projet implémente une classe `Graph` générique basée sur une **liste d'adjacence**. Elle supporte les graphes **orientés** et **non-orientés**, avec des arêtes pondérées.

**Fonctionnalités principales :**

- Ajout / suppression de sommets et d'arêtes
- Parcours en profondeur (DFS) et en largeur (BFS)
- Détection de cycle (orienté et non-orienté)
- Plus court chemin par l'algorithme de Dijkstra
- Tri topologique (DAG)
- Propriétés utilitaires : `node_count`, `edge_count`, `has_node`, `has_edge`

---

## Structure du projet

```
graph/
└── graph.py       # Classe Graph et tous les algorithmes
```

---

## Installation

Aucune dépendance externe requise. Le projet utilise uniquement la bibliothèque standard Python.

```bash
# Python 3.10+ recommandé
python graph.py
```

---

## Utilisation rapide

```python
from graph import Graph

# Graphe orienté (par défaut)
g = Graph(directed=True)

g.add_edge("A", "B", weight=1)
g.add_edge("A", "C", weight=4)
g.add_edge("B", "C", weight=2)
g.add_edge("C", "D", weight=1)

# Affichage
g.display()

# Plus court chemin
chemin, distance = g.shortest_path("A", "D")
print(chemin)    # ['A', 'B', 'C', 'D']
print(distance)  # 4
```

---

## API complète

### Création

| Méthode                    | Description                             |
| -------------------------- | --------------------------------------- |
| `Graph(directed=True)`     | Crée un graphe orienté ou non-orienté   |
| `add_node(node)`           | Ajoute un sommet                        |
| `add_edge(u, v, weight=1)` | Ajoute une arête entre `u` et `v`       |
| `remove_node(node)`        | Supprime un sommet et toutes ses arêtes |
| `remove_edge(u, v)`        | Supprime l'arête entre `u` et `v`       |

### Interrogation

| Méthode / Propriété | Description                              |
| ------------------- | ---------------------------------------- |
| `has_node(node)`    | Vérifie si un sommet existe              |
| `has_edge(u, v)`    | Vérifie si une arête existe              |
| `node_count`        | Nombre de sommets                        |
| `edge_count`        | Nombre d'arêtes                          |
| `adj`               | Dictionnaire d'adjacence (lecture seule) |
| `display()`         | Affiche le graphe dans le terminal       |

### Parcours

| Méthode     | Description                          |
| ----------- | ------------------------------------ |
| `dfs(node)` | Parcours en profondeur depuis `node` |
| `dfs_all()` | DFS sur toutes les composantes       |
| `bfs(node)` | Parcours en largeur depuis `node`    |
| `bfs_all()` | BFS sur toutes les composantes       |

### Algorithmes

| Méthode                     | Description                               |
| --------------------------- | ----------------------------------------- |
| `detect_cycle()`            | Détecte un cycle (orienté et non-orienté) |
| `dijkstra(start)`           | Distances minimales depuis `start`        |
| `shortest_path(start, end)` | Plus court chemin entre deux sommets      |
| `topological_sort()`        | Tri topologique (DAG uniquement)          |

---

## Algorithmes implémentés

### DFS — Depth-First Search

Parcours récursif en profondeur. Explore une branche complète avant de passer à la suivante.

```
Complexité : O(V + E)
```

### BFS — Breadth-First Search

Parcours en largeur par file d'attente (`deque`). Explore les sommets niveau par niveau.

```
Complexité : O(V + E)
```

### Détection de cycle

- **Graphe orienté** : pile de récursion (`rec_stack`) — détecte les arêtes arrière.
- **Graphe non-orienté** : DFS avec suivi du parent — évite de traiter l'arête retour comme un cycle.

```
Complexité : O(V + E)
```

### Dijkstra

Calcule les plus courtes distances depuis un sommet source. Utilise un tas binaire (`heapq`) pour sélectionner efficacement le sommet de plus faible coût à chaque étape.

> ⚠️ Ne fonctionne qu'avec des **poids positifs**.

```
Complexité : O((V + E) log V)
```

### Tri topologique

Ordre linéaire des sommets d'un DAG (graphe orienté acyclique) tel que pour toute arête `u → v`, `u` précède `v`. Basé sur un DFS post-ordre inversé.

```
Complexité : O(V + E)
```

---

## Exemples

### Graphe non-orienté et détection de cycle

```python
g = Graph(directed=False)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)  # Crée un cycle

print(g.detect_cycle())  # True
```

### Tri topologique sur un DAG

```python
g = Graph(directed=True)
g.add_edge("cours", "tp")
g.add_edge("tp", "examen")
g.add_edge("cours", "projet")

print(g.topological_sort())
# ['cours', 'tp', 'examen', 'projet']  (ou variante valide)
```

### Dijkstra — distances depuis un sommet

```python
g = Graph(directed=True)
g.add_edge("A", "B", 1)
g.add_edge("A", "C", 4)
g.add_edge("B", "C", 2)
g.add_edge("C", "D", 1)

distances, _ = g.dijkstra("A")
print(distances)
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

## Auteur

Projet réalisé en Python dans le cadre d'un apprentissage des structures de données et algorithmes sur les graphes.
