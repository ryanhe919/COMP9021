from stack_adt import *
from collections import defaultdict

our_tree = {1: [2, 4, 5], 2: [3], 5: [6, 11, 13], 6: [7, 8, 10], 8: [9], 11:[12]}
# Depth-First Search

def explore_tree_DFS(tree, root):
    stack = Stack()
    stack.push(root)
    while not stack.is_empty():
        path = stack.pop()
        print(path)
        if path in tree:
            for e in reversed(tree[path]):
                stack.push(e)

##
##def explore_tree_DFS(tree):
##    stack = Stack()
##    stack.push(([],tree))
##    while not stack.is_empty():
##        path, tree = stack.pop()
##        print(path)
##        if tree:
##            for e in reversed(list(tree.keys())):
##                stack.push((path + [e], tree[e]))

explore_tree_DFS(our_tree, 1)


