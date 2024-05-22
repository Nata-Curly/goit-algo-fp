import uuid
import networkx as nx
import matplotlib.pyplot as plt


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


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {}

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

    add_heap_nodes(heap, heap_root, pos)

    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}
    colors = [node[1]["color"] for node in heap.nodes(data=True)]

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


draw_heap(root)
