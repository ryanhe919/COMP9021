# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    '''
    >>> LL = ExtendedLinkedList([49, 97, 53, 5, 33, 65, 62, 51, 38, 61])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    5, 53, 65, 33, 51, 62, 61, 38, 97, 49
    >>> LL = ExtendedLinkedList([49, 97, 53, 5])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    5, 53, 97, 49
    >>> LL = ExtendedLinkedList([49, 97, 53, 5, 33, 65])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    5, 53, 65, 33, 97, 49
    >>> LL = ExtendedLinkedList([49, 97, 53, 5, 33, 65, 62, 51])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    5, 53, 65, 33, 51, 62, 97, 49
    >>> LL = ExtendedLinkedList([73, 4, 54, 61, 73, 1, 26, 59, 62, 35])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    1, 73, 59, 26, 35, 62, 4, 73, 61, 54
    >>> LL = ExtendedLinkedList([49, 97, 53, 5, 33, 65, 62, 51, 38, 61, 45, 74])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    5, 53, 65, 33, 51, 62, 61, 38, 74, 45, 97, 49
    >>> LL = ExtendedLinkedList([73, 4, 54, 61, 73, 1, 26, 59, 62, 35, 83, 20])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    1, 73, 59, 26, 35, 62, 20, 83, 4, 73, 61, 54
    >>> LL = ExtendedLinkedList([92, 87, 98, 19, 33, 86, 81, 12, 41, 73, 21, 3, 52, 52, 9, 13])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    3, 21, 52, 52, 13, 9, 87, 92, 19, 98, 86, 33, 12, 81, 73, 41
    >>> LL = ExtendedLinkedList([69, 37, 78, 3, 79, 83, 26, 32, 6, 50, 48, 82, 17, 10, 59, 0])
    >>> ExtendedLinkedList.rearrange(LL)
    >>> ExtendedLinkedList.print(LL)
    0, 59, 37, 69, 3, 78, 83, 79, 32, 26, 50, 6, 82, 48, 10, 17

    
    '''
    def __init__(self, L = None):
        super().__init__(L)


    def rearrange(self):
        min_number = self.head.value
        node = self.head
        while node:
            if node.value < min_number:
                min_number = node.value
            node = node.next_node
        number_index = self.index_of_value(min_number)
        # find the minimum number in this list
        
        length_of_list = 0
        node = self.head
        while node:
            length_of_list += 1
            node = node.next_node
        #compute the length of list
        
        sorted_list = []
        node = self.head
        for i in range(number_index):
            node = node.next_node
        sorted_list.append(node.value)      
        #sort list
        while len(sorted_list) < length_of_list:
            number_index = number_index - 1
            if number_index < 0:
                number_index = length_of_list - 1
            node = self.head
            for i in range(number_index):
                node = node.next_node
            sorted_list.append(node.value)
            if len(sorted_list) == length_of_list:
                break
            number_index = number_index + 3
            if number_index > length_of_list - 1:
                number_index -= length_of_list
            node = self.head
            for i in range(number_index):
                node = node.next_node
            sorted_list.append(node.value)
        node = self.head
        self.head.value = sorted_list[0]
        for e in sorted_list[1:]:
            node.next_node.value = e
            node = node.next_node

if __name__ == '__main__':
    import doctest
    doctest.testmod()
