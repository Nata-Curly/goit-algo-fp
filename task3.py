import networkx as nx
import heapq


G = nx.Graph()

G.add_nodes_from(
    ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Nik", "Natalia"]
)

G.add_edge("Alice", "Bob", weight=9)
G.add_edge("Alice", "Charlie", weight=5)
G.add_edge("Alice", "Frank", weight=3)
G.add_edge("Alice", "David", weight=5)
G.add_edge("Alice", "Emma", weight=3)
G.add_edge("Bob", "David", weight=4)
G.add_edge("Bob", "Nik", weight=4)
G.add_edge("Bob", "Natalia", weight=5)
G.add_edge("Charlie", "David", weight=3)
G.add_edge("Charlie", "Emma", weight=1)
G.add_edge("David", "Emma", weight=2)
G.add_edge("David", "Frank", weight=5)
G.add_edge("Emma", "Frank", weight=6)
G.add_edge("Frank", "Charlie", weight=3)
G.add_edge("Nik", "Natalia", weight=7)
G.add_edge("Nik", "Charlie", weight=8)
G.add_edge("Nik", "Alice", weight=3)
G.add_edge("Natalia", "Alice", weight=7)


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, data in graph[current_vertex].items():
            weight = data["weight"]
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


distances = dijkstra(dict(G.adj), "Alice")

print("\nНайкоротші відстані:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
