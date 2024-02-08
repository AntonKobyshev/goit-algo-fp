from collections import deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid

# Клас, що представляє вузол бінарного дерева
class Node:
    def __init__(self, key, color="lightblue"):
        self.left = None
        self.right = None
        self.val = key 
        self.color = color 
        self.id = str(uuid.uuid4())  

# Функція, що додає ребра та вершини до графа для відображення бінарного дерева
def add_edges_combined(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            add_edges_combined(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            add_edges_combined(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерев обходу у глибину та у ширину
def draw_trees_combined(dfs_root, bfs_root):
    dfs_tree = nx.DiGraph()
    dfs_pos = {}
    dfs_tree = add_edges_combined(dfs_tree, dfs_root, dfs_pos)

    bfs_tree = nx.DiGraph()
    bfs_pos = {}
    bfs_tree = add_edges_combined(bfs_tree, bfs_root, bfs_pos)

    dfs_colors = [node[1]["color"] for node in dfs_tree.nodes(data=True)]
    dfs_labels = {node[0]: node[1]["label"] for node in dfs_tree.nodes(data=True)}

    bfs_colors = []
    for node in bfs_tree.nodes(data=True):
        if node[1]["label"] is not None:
            bfs_colors.append(node[1]["color"])

    bfs_labels = {node[0]: node[1]["label"] for node in bfs_tree.nodes(data=True)}

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    nx.draw(
        dfs_tree,
        pos=dfs_pos,
        labels=dfs_labels,
        arrows=False,
        node_size=1200,
        node_color=dfs_colors,
        cmap=plt.cm.Blues, 
    )
    plt.title("DFS Tree") 
    plt.subplot(1, 2, 2)
    nx.draw(
        bfs_tree,
        pos=bfs_pos,
        labels=bfs_labels,
        arrows=False,
        node_size=1200,
        node_color=bfs_colors,
        cmap=plt.cm.Blues, 
    )
    plt.title("BFS Tree")  
    plt.tight_layout()
    plt.show()


# Функція обходу у глибину дерева
def dfs(root):
    visited = set()
    stack = [root]
    dfs_order = []
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.add(node)
            dfs_order.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return dfs_order

# Функція обходу у ширину дерева
def bfs(root):
    visited = set()
    queue = deque([root])
    bfs_order = []
    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.add(node)
            bfs_order.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return bfs_order

def update_node_colors_by_order_new(root, order):
    color_palette = plt.cm.Blues  # Використовуємо палітру кольорів
    max_order = len(order)
    for idx, val in enumerate(order):
        node = find_node(root, val)
        if node:
            color_intensity = idx / max_order
            node.color = color_palette(color_intensity)[:3]  # Беремо лише перші три значення RGB

def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    left_search = find_node(root.left, val)
    if left_search:
        return left_search
    return find_node(root.right, val)

def copy_tree(node):
    if node is None:
        return None
    new_node = Node(node.val)
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)
    return new_node

def build_heap_tree(heap, i=0):
    if i < len(heap):
        node = Node(heap[i])
        node.left = build_heap_tree(heap, 2 * i + 1)
        node.right = build_heap_tree(heap, 2 * i + 2)
        return node
    return None

def main():
    heap_array = [1, 5, 4, 7, 10, 12, 24, 11, 7, 1, 2, 5, 13, 17, 8]
    heapq.heapify(heap_array)
    root = build_heap_tree(heap_array)

    dfs_order = dfs(root)
    dfs_tree_root = copy_tree(root)
    update_node_colors_by_order_new(dfs_tree_root, dfs_order)

    bfs_order = bfs(root)
    bfs_tree_root = copy_tree(root)
    update_node_colors_by_order_new(bfs_tree_root, bfs_order)

    draw_trees_combined(dfs_tree_root, bfs_tree_root)

if __name__ == "__main__":
    main()
