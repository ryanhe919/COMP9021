# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def breath_first_search(tree, root):
    path_list = []
    queue = Queue()
    queue.enqueue([root])
    while not queue.is_empty():
        path = queue.dequeue()
        print(path)
        path_list.append(path)
        if path[-1] in tree:
            for i in tree[path[-1]]:
                if i not in path:
                    queue.enqueue(path + [i])

def leftmost_longest_path_from_top_left_corner():
    tree = {}
    global grid
    if grid[0][0] == 0:
        return None
    for i in range(10):
        for j in range(10):
            tree.update({(i , j): []})
            if j:
                if grid[i][j - 1] == '1':
                    tree[(i, j)].append((i, j - 1))
            if i:
                if grid[i - 1][j] == '1':
                    tree[(i, j)].append((i - 1, j))
            if j < 9:
                if grid[i][j + 1] == '1':
                    tree[(i, j)].append((i, j + 1))
            if i < 9:
                if grid[i + 1][j] == '1':
                    tree[(i, j)].append((i + 1, j))
    print(tree)

provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
##print()
##for i in range(len(grid)):
##        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           
