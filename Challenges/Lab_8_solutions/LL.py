from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicate(self):
        node = self.head
        new_list = []
        while node:
            if node.value not in new_list:
                new_list.append(node.value)
            node = node.next_node

        node = Node(new_list[0])
        self.head = node
        for i in new_list[1:]:
            node.next_node = Node(i)
            node = node.next_node
            
