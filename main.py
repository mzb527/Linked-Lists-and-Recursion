class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def sum_recursive(self, node):
        if node is None:
            return 0
        return node.data + self.sum_recursive(node.next)

    def reverse_recursive(self, prev, current):
        if current is None:
            self.head = prev
            return
        next_node = current.next
        current.next = prev
        self.reverse_recursive(current, next_node)

    def search_recursive(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self.search_recursive(node.next, target)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Initialize the linked list
ll = LinkedList()
ids = [101, 202, 303, 404, 505]
for id in ids:
    ll.insert_at_front(id)

# Display the initial list
print("Original Linked List:")
ll.print_list()

# Sum all IDs using recursion
total_sum = ll.sum_recursive(ll.head)
print(f"Sum of all IDs: {total_sum}")

# Reverse the linked list using recursion
ll.reverse_recursive(None, ll.head)
print("Reversed Linked List:")
ll.print_list()

# Search for an ID using recursion
search_id = 303
found = ll.search_recursive(ll.head, search_id)
print(f"Is ID {search_id} present? {'Yes' if found else 'No'}")