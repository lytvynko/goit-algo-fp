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

def add_edges(node, tree=None, pos={}, x=0, y=0, layer=1):
    if tree is None:
        tree = nx.DiGraph()
    if node:
        pos[node.id] = (x, y)
        tree.add_node(node.id, value=node.value, color=node.color)
        if node.left:
            tree.add_edge(node.id, node.left.id)
            add_edges(node.left, tree, pos, x - 1 / 2 ** layer, y - 1, layer + 1)
        if node.right:
            tree.add_edge(node.id, node.right.id)
            add_edges(node.right, tree, pos, x + 1 / 2 ** layer, y - 1, layer + 1)
    return tree, pos

def interpolate_color(start_color, end_color, factor: float):
    """Інтерполює між двома кольорами з заданим фактором."""
    start_r, start_g, start_b = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:], 16)
    end_r, end_g, end_b = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:], 16)

    r = int(start_r + (end_r - start_r) * factor)
    g = int(start_g + (end_g - start_g) * factor)
    b = int(start_b + (end_b - start_b) * factor)

    return f'#{r:02x}{g:02x}{b:02x}'

def traversal_update_colors(node, visited_order, tree, start_color="#000000", end_color="#FFFFFF", method='dfs'):
    if method == 'dfs':
        dfs(node, visited_order, tree, start_color, end_color)
    else:
        bfs(node, visited_order, tree, start_color, end_color)

def dfs(node, visited_order, tree, start_color, end_color):
    if node and node.id not in visited_order:
        visited_order[node.id] = len(visited_order) + 1
        factor = len(visited_order) / len(tree.nodes)
        node.color = interpolate_color(start_color, end_color, factor)
        if node.left:
            dfs(node.left, visited_order, tree, start_color, end_color)
        if node.right:
            dfs(node.right, visited_order, tree, start_color, end_color)

def bfs(node, visited_order, tree, start_color, end_color):
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        if current_node.id not in visited_order:
            visited_order[current_node.id] = len(visited_order) + 1
            factor = len(visited_order) / len(tree.nodes)
            current_node.color = interpolate_color(start_color, end_color, factor)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

def draw_tree_with_traversal(root, method='dfs'):
    tree, pos = add_edges(root)
    visited_order = {}
    traversal_update_colors(root, visited_order, tree, "#000000", "#FFFFFF", method)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['value'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos, labels=labels, with_labels=True, node_size=2500, node_color=colors, font_weight='bold', arrowstyle='-|>', arrowsize=10)
    plt.title(f"Tree Traversal: {method.upper()}")
    plt.show()

# Створення та візуалізація бінарної купи з масиву
heap_array = [0, 4, 1, 5, 10, 3]
heap_root = build_heap_from_array(heap_array)

# Візуалізація обходу в глибину
draw_tree_with_traversal(heap_root, 'dfs')

# Візуалізація обходу в ширину
draw_tree_with_traversal(heap_root, 'bfs')