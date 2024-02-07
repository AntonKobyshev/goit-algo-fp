class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Клас, що реалізує вузли однонаправленого списку
class LinkedList:
    def __init__(self):
        self.head = None

    # Метод, який реверсує список
    def reverse(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    # Метод, який вставляє новий вузол у відсортований порядок
    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    # Метод, який об'єднує два відсортовані списки в один
    def merge_sorted_lists(self, list2):
        merged_list = LinkedList()
        current1 = self.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.sorted_insert(Node(current1.data))
                current1 = current1.next
            else:
                merged_list.sorted_insert(Node(current2.data))
                current2 = current2.next

        while current1:
            merged_list.sorted_insert(Node(current1.data))
            current1 = current1.next

        while current2:
            merged_list.sorted_insert(Node(current2.data))
            current2 = current2.next

        return merged_list

    # Метод, що відображає елементи списку
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Основна функція
if __name__ == "__main__":
    # Створення першого списку та вставлення елементів у відсортованому порядку
    linked_list = LinkedList()
    linked_list.sorted_insert(Node(7))
    linked_list.sorted_insert(Node(3))
    linked_list.sorted_insert(Node(5))
    linked_list.sorted_insert(Node(1))

    print("Original list:")
    linked_list.display()

    # Реверсування першого списку
    linked_list.reverse()
    print("Reversed list:")
    linked_list.display()

    # Створення другого списку та вставлення елементів у відсортованому порядку
    linked_list2 = LinkedList()
    linked_list2.sorted_insert(Node(4))
    linked_list2.sorted_insert(Node(8))
    linked_list2.sorted_insert(Node(2))
    linked_list2.sorted_insert(Node(6))

    print("Second list:")
    linked_list2.display()

    # Об'єднання та відображення відсортованих списків
    merged_list = linked_list.merge_sorted_lists(linked_list2)
    print("Merged sorted lists:")
    merged_list.display()
