import uuid
import heapq
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
    
     # Додає ребра та вершини до графа для відображення бінарної купи.
    
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root):
   
    #Візуалізує бінарну купу за допомогою графічної бібліотеки NetworkX.
    
    heap_graph = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap_graph = add_edges(heap_graph, heap_root, pos)

    colors = [node[1]["color"] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(heap_array):
    """
    Побудова бінарної купи з вхідного масиву.
    """
    heapq.heapify(heap_array)
    nodes = [Node(val) for val in heap_array]
    root = nodes[0]
    for i in range(len(heap_array)):
        if 2 * i + 1 < len(heap_array):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(heap_array):
            nodes[i].right = nodes[2 * i + 2]
    return root


if __name__ == "__main__":
    heap_array = [1, 5, 4, 7, 10, 12, 24, 11, 7, 1, 2, 5, 10, 11, 2]

    heap_tree_root = build_heap_tree(heap_array)

    draw_heap(heap_tree_root)
