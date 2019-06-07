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


def replace_possiable_dot_to_star(row, column, grid):
    if grid[row][column] == 1:
        grid[row][column] = '*'
        if row:
            replace_possiable_dot_to_star(row - 1, column, grid)
        if row < 9:
            replace_possiable_dot_to_star(row + 1, column, grid)
        if column:
            replace_possiable_dot_to_star(row, column - 1, grid)
        if column < 9:
            replace_possiable_dot_to_star(row, column + 1, grid)
    return grid

def breath_first_search(tree, root):
    queue = Queue()
    path_list = []
    queue.enqueue([root])
    while not queue.is_empty():
        path = queue.dequeue()
        path_list.append(path)
        print(path)
        if len(path) == 1 and path[0] in tree:
            if (path[0][0], path[0][1] + 1) in tree[path[0]]:
                queue.enqueue(path + [(path[0][0], path[0][1] + 1)])
            if (path[0][0] + 1, path[0][1]) in tree[path[0]]:
                queue.enqueue(path + [(path[0][0] + 1, path[0][1])])
        if len(path) > 1 and path[0] in tree:
            if path[-1][0] - path[-2][0] == 0 and path[-1][1] - path[-2][1] == 1:
                if ((path[-1][0] - 1, path[-1][1]) in tree[path[-1]]) and ((path[-1][0] - 1, path[-1][1]) not in path):
                    queue.enqueue(path + [(path[-1][0] - 1, path[-1][1])])
                if ((path[-1][0], path[-1][1] + 1) in tree[path[-1]]) and ((path[-1][0], path[-1][1] + 1) not in path):
                    queue.enqueue(path + [(path[-1][0], path[-1][1] + 1)])
                if ((path[-1][0] + 1, path[-1][1]) in tree[path[-1]]) and ((path[-1][0] + 1, path[-1][1]) not in path):
                    queue.enqueue(path + [(path[-1][0] + 1, path[-1][1])])

            if path[-1][0] - path[-2][0] == 0 and path[-1][1] - path[-2][1] == -1:
                if ((path[-1][0] + 1, path[-1][1]) in tree[path[-1]]) and ((path[-1][0] + 1, path[-1][1]) not in path):
                    queue.enqueue(path + [(path[-1][0] + 1, path[-1][1])])
                if ((path[-1][0], path[-1][1] - 1) in tree[path[-1]]) and ((path[-1][0], path[-1][1] - 1) not in path):
                    queue.enqueue(path + [(path[-1][0], path[-1][1] - 1)])
                if ((path[-1][0] - 1, path[-1][1]) in tree[path[-1]]) and ((path[-1][0] - 1, path[-1][1]) not in path):
                    queue.enqueue(path + [(path[-1][0] - 1, path[-1][1])])

            if path[-1][0] - path[-2][0] == 1 and path[-1][1] - path[-2][1] == 0:
                if ((path[-1][0], path[-1][1] + 1) in tree[path[-1]]) and ((path[-1][0], path[-1][1] + 1) not in path):
                    queue.enqueue(path + [(path[-1][0], path[-1][1] + 1)])
                if ((path[-1][0] + 1, path[-1][1]) in tree[path[-1]]) and ((path[-1][0] + 1, path[-1][1]) not in path):
                    queue.enqueue(path + [(path[-1][0] + 1, path[-1][1])])
                if ((path[-1][0], path[-1][1] - 1) in tree[path[-1]]) and ((path[-1][0], path[-1][1] - 1) not in path):
                    queue.enqueue(path + [(path[-1][0], path[-1][1] - 1)])

            if path[-1][0] - path[-2][0] == -1 and path[-1][1] - path[-2][1] == 0:
                if ((path[-1][0], path[-1][1] - 1) in tree[path[-1]]) and ((path[-1][0], path[-1][1] - 1) not in path):
                    queue.enqueue(path + [(path[-1][0], path[-1][1] - 1)])
                if ((path[-1][0] - 1, path[-1][1]) in tree[path[-1]]) and ((path[-1][0] - 1, path[-1][1]) not in path):
                    queue.enqueue(path + [(path[-1][0] - 1, path[-1][1])])
                if ((path[-1][0], path[-1][1] + 1) in tree[path[-1]]) and ((path[-1][0], path[-1][1] + 1) not in path):
                    queue.enqueue(path + [(path[-1][0], path[-1][1] + 1)])


    return path_list
#        if path[-1] in tree:
#            for i in tree[path[-1]]:
#                if i not in path:
#                    queue.enqueue(path + [i])

def choose_path(path_list):
    length = len(path_list[-1])
    for i in range(1, len(path_list) + 1):
        if len(path_list[-i]) == length:
            path = path_list[-i]
    return path

def leftmost_longest_path_from_top_left_corner():
    tree = {}
    global grid
    if grid[0][0] == 1:
        grid = replace_possiable_dot_to_star(0, 0, grid)
    else:
        return None
##    print()
##    for i in range(len(grid)):
##        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))
    for i in range(10):
        for j in range(10):
            if grid[i][j] == '*':
                tree.update({(i , j): []})
                if j:
                    if grid[i][j - 1] == '*':
                        tree[(i, j)].append((i, j - 1))
                if i:
                    if grid[i - 1][j] == '*':
                        tree[(i, j)].append((i - 1, j))
                if i < 9:
                    if grid[i + 1][j] == '*':
                        tree[(i, j)].append((i + 1, j))
                if j < 9:
                    if grid[i][j + 1] == '*':
                        tree[(i, j)].append((i, j + 1))

    path_list = breath_first_search(tree, (0, 0))
 #    path = choose_path(path_list)
 #    return path


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
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')

