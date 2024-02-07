import heapq

class Graph:
    def __init__(self):
        # Ініціалізуємо словник вершин графа
        self.vertices = {}

    def add_vertex(self, vertex):
        # Додаємо нову вершину до графа
        self.vertices[vertex] = {}

    def add_edge(self, start_vertex, end_vertex, weight):
        # Додаємо ребро між двома вершинами з вагою
        self.vertices[start_vertex][end_vertex] = weight

    def dijkstra(self, start_vertex):
        # Ініціалізуємо словник для зберігання найкоротших відстаней
        shortest_paths = {vertex: float('inf') for vertex in self.vertices}
        shortest_paths[start_vertex] = 0
        priority_queue = [(0, start_vertex)]  # Використовуємо бінарну купу для оптимізації

        while priority_queue:
            current_weight, current_vertex = heapq.heappop(priority_queue)

            # Якщо поточний шлях від початкової вершини коротший, ігноруємо його
            if current_weight > shortest_paths[current_vertex]:
                continue

            # Отримуємо найкоротші шляхи для сусідів поточної вершини
            for neighbor, weight in self.vertices[current_vertex].items():
                path_weight = current_weight + weight

                # Якщо знайдено коротший шлях до сусіда, оновлюємо його
                if path_weight < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = path_weight
                    heapq.heappush(priority_queue, (path_weight, neighbor))

        return shortest_paths

def print_shortest_paths(shortest_paths, start_vertex):
    # Виводимо найкоротші відстані від заданої вершини
    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"From {start_vertex} to {vertex}: {distance}")

if __name__ == "__main__":
    # Створюємо граф та додаємо вершини та ребра
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'E', 3)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('D', 'E', 3)
    graph.add_edge('C', 'E', 1)

    # Знаходимо найкоротші шляхи та виводимо результати
    shortest_paths = graph.dijkstra('A')
    print_shortest_paths(shortest_paths, 'A')
