import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def generate_color(index, total):
    intensity = int(100 * index / total)
    return f"#12{(50 + intensity):2x}{(155 + intensity):02x}"


def dfs(node, visited, colors, order):
    if node is not None:
        visited.add(node.id)
        order.append(node.id)
        if node.left and node.left.id not in visited:
            dfs(node.left, visited, colors, order)
        if node.right and node.right.id not in visited:
            dfs(node.right, visited, colors, order)


def bfs(node, visited, colors, order):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        visited.add(current.id)
        order.append(current.id)
        if current.left and current.left.id not in visited:
            queue.append(current.left)
        if current.right and current.right.id not in visited:
            queue.append(current.right)


def draw_heap(heap_root, traversal="dfs"):
    heap = nx.DiGraph()
    pos = {}

    # Додавання всіх вузлів у граф перед підрахунком вузлів
    add_heap_nodes(heap, heap_root, pos)

    # Визначення загальної кількості вузлів у дереві
    total_nodes = heap.number_of_nodes()

    # Виклик функції обходу залежно від обраного методу
    colors = {}
    visited = set()
    order = []
    if traversal == "dfs":
        dfs(heap_root, visited, colors, order)
    elif traversal == "bfs":
        bfs(heap_root, visited, colors, order)

    # Оновлення кольорів у графі
    for i, node_id in enumerate(order):
        color = generate_color(i + 1, total_nodes)
        heap.nodes[node_id]["color"] = color

    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}
    colors = [node[1]["color"] for node in heap.nodes(data=True)]

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def add_heap_nodes(heap, heap_node, pos, layer=1, x=0, y=0):
    if heap_node is not None:
        heap.add_node(heap_node.id, label=heap_node.val, color=heap_node.color)
        pos[heap_node.id] = (x, y)
        if heap_node.left:
            heap.add_edge(heap_node.id, heap_node.left.id)
            add_heap_nodes(
                heap, heap_node.left, pos, layer + 1, x - 1 / 2**layer, y - 1
            )
        if heap_node.right:
            heap.add_edge(heap_node.id, heap_node.right.id)
            add_heap_nodes(
                heap, heap_node.right, pos, layer + 1, x + 1 / 2**layer, y - 1
            )


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

draw_heap(root, traversal="dfs")  # обхід у глибину
draw_heap(root, traversal="bfs")  # обхід у ширину
