# Written by *** for COMP9021


from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        queue = []
        if self.value is None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
            return
        else:
            queue.append(self.left_node)
            queue.append(self.right_node)
            while True:
                node = queue.pop(0)
                if node.value is None:
                    node.value = value
                    node.left_node = PriorityQueue()
                    node.right_node = PriorityQueue()
                    break
                else:
                    queue.append(node.left_node)
                    queue.append(node.right_node)
        self.sort_tree()

            
        
    def sort_tree(self):
        queue = []
        queue.append(self)
        list = []
        while True:
            node = queue.pop(0)
            if node.value is None:
                break
            else:
                list.append(node)
                queue.append(node.left_node)
                queue.append(node.right_node)
        for i in reversed(list):
            if i.left_node.value is not None:
                if i.value > i.left_node.value:
                    i.value, i.left_node.value = i.left_node.value, i.value
            if i.right_node.value is not None:
                if i.value > i.right_node.value:
                    i.value, i.right_node.value = i.right_node.value, i.value
 

        

            
        
##        if self.value < self.left_node.value:
##            self.value, self.left_node.value = self.left_node.value, self.value
##        if self.value < self.right_node.value:
##            self.value, self.right_node.value = self.right_node.value, self.value


        
