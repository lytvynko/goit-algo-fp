import matplotlib.pyplot as plt
import networkx as nx
import uuid

class Node:
    def __init__(self, value, color="skyblue"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())

def build_heap_from_array(array):
    nodes = [Node(val) for val in array]
    n = len(array)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

def draw_heap(root):
    if root is None:
        print("Heap is empty")
        return

    tree = nx.DiGraph()
    pos = {}
    def add_edges(node, x=0, y=0, layer=1):
        if node:
            pos[node.id] = (x, y)
            tree.add_node(node.id, value=node.value, color=node.color)
            if node.left:
                tree.add_edge(node.id, node.left.id)
                add_edges(node.left, x - 1 / 2 ** layer, y - 1, layer + 1)
            if node.right:
                tree.add_edge(node.id, node.right.id)
                add_edges(node.right, x + 1 / 2 ** layer, y - 1, layer + 1)
    add_edges(root)

    colors = list(nx.get_node_attributes(tree, 'color').values())
    labels = nx.get_node_attributes(tree, 'value')

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos, labels=labels, with_labels=True, node_size=2500, node_color=colors, font_weight='bold', arrowstyle='-|>', arrowsize=10)
    plt.show()

heap_array = [0, 4, 1, 5, 10, 3]
heap_root = build_heap_from_array(heap_array)
draw_heap(heap_root)