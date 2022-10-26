class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


class Linked:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_at_head(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node is not None:
            current_node = current_node.pointer
            current_node.pointer = new_node


link = Linked()
link.insert_at_head(2)
print(link.get_head())
