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
    def merge_sort(self, head):
        # Сортуємо список методом злиття
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left_half = self.merge_sort(head)
        right_half = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left_half, right_half)
        return sorted_list

    def sorted_merge(self, left_half, right_half):
        # Зливаємо два відсортованих підсписки
        result = None

        if left_half is None:
            return right_half
        if right_half is None:
            return left_half

        if left_half.data <= right_half.data:
            result = left_half
            result.next = self.sorted_merge(left_half.next, right_half)
        else:
            result = right_half
            result.next = self.sorted_merge(left_half, right_half.next)

        return result

    def get_middle(self, head):
        # Знаходимо середину списку
        if head is None:
            return head

        slow_pointer = head
        fast_pointer = head

        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.sorted_insert(Node(7))
    linked_list.sorted_insert(Node(3))
    linked_list.sorted_insert(Node(5))
    linked_list.sorted_insert(Node(1))

    print("Original list:")
    linked_list.display()

    linked_list.reverse()
    print("Reversed list:")
    linked_list.display()

    linked_list2 = LinkedList()
    linked_list2.sorted_insert(Node(4))
    linked_list2.sorted_insert(Node(8))
    linked_list2.sorted_insert(Node(2))
    linked_list2.sorted_insert(Node(6))

    print("Second list:")
    linked_list2.display()

    merged_list = linked_list.merge_sorted_lists(linked_list2)
    print("Merged sorted lists:")
    merged_list.display()
