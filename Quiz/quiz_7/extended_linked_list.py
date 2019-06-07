# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if len(self) < 3:
            return

        min_number = self.head.value
        node = self.head
        while node:
            if node.value < min_number:
                min_number = node.value
            node = node.next_node
        number_index = self.index_of_value(min_number)

        sorted_list = LinkedList()

        while len(sorted_list) < len(self):
            node = self.head
            for i in range(number_index):
                node = node.next_node
            sorted_list.append(node.value)
            number_index -= 1
            if number_index < 0:
                number_index = len(self) - 1
            node = self.head
            for i in range(number_index):
                node = node.next_node
            if len(sorted_list) < len(self):
                sorted_list.append(node.value)
            number_index += 3
            if number_index > len(self) - 1:
                number_index -= len(self)
 
        node_self = self.head
        node_sorted = sorted_list.head
        while node_sorted:
            node_self.value = node_sorted.value
            node_self = node_self.next_node
            node_sorted = node_sorted.next_node
