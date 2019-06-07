# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
        

    def rearrange(self, step):
        # Replace pass above with your code
        node = self.head
        length = len(self)
        #print(len(self))
        
        new_list = LinkedList()


                
        node = self.head
        for i in range(step - 1):
            node = node.next_node
        
        # new_list.append(node.value)
        count = step - 1

            


        # new_node = node
        # print(new_node.value)
        for i in range(length):
            new_list.append(node)
            for j in range(step):
                count += 1

            if count >= length:
                count = count - length
            node = self.head
            for j in range(count):
                node = node.next_node

        '''
         while new_node:
            print(new_node.value)
            new_node = new_node.next_node
        
        current_node = self.head
        new_node = new_list.head
        for i in range(length):
            temp_node = self.head
            for j in range(new_node.value):
                temp_node = temp_node.next_node
            new_node = new_node.next_node

            print(temp_node.value)
            current_node = temp_node
            current_node = current_node.next_node

       # new_node = new_list.head
       # print(new_node.value)

        node = self.head
        new_node = new_list.head
        node = new_node.value
        print(node.value)
        while node.next_node.next_node:
            node.next_node = node.next_node.next_node
             
        node = self.head
        while node:
            print(node.value)
            node = node.next_node
        '''

        

        new_node = new_list.head
        while new_node:
            print(new_node.value)
            new_node = new_node.next_node
        new_node = new_list.head
        self.head = new_list.head.value
        a = self.head
        while new_node and new_node.next_node:
            new_node = new_node.next_node
            a.next_node = new_node.value
            a = a.next_node


        
