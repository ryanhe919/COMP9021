# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint
from copy import deepcopy

dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

# Possibly define other functions

def replace_1_by_star(i, j, grid1):
    if grid1[i][j] == 1:
        grid1[i][j] = '*'
        if i:
            replace_1_by_star(i - 1, j, grid1)
        if i < dim - 1:
            replace_1_by_star(i + 1, j, grid1)
        if j:
            replace_1_by_star(i, j - 1, grid1)
        if j < dim - 1:
            replace_1_by_star(i, j + 1, grid1)
    return grid1

def replace_0_by_star(i, j, grid1):
    if grid1[i][j] == 0:
        grid1[i][j] = '*'
        if i:
            replace_0_by_star(i - 1, j, grid1)
        if i < dim - 1:
            replace_0_by_star(i + 1, j, grid1)
        if j:
            replace_0_by_star(i, j - 1, grid1)
        if j < dim - 1:
            replace_0_by_star(i, j + 1, grid1)
    return grid1
def replace_0_by_star_2(i, j, grid2):
    if grid2[i][j] == 0:
        grid2[i][j] = '*'
        if i:
            replace_1_by_star_2(i - 1, j, grid2)
        if i < dim - 1:
            replace_1_by_star_2(i + 1, j, grid2)
        if j:
            replace_1_by_star_2(i, j - 1, grid2)
        if j < dim - 1:
            replace_1_by_star_2(i, j + 1, grid2)
    return grid2
def replace_1_by_star_2(i, j, grid2):
    if grid2[i][j] == 1:
        grid2[i][j] = '*'
        if i:
            replace_0_by_star_2(i - 1, j, grid2)
        if i < dim - 1:
            replace_0_by_star_2(i + 1, j, grid2)
        if j:
            replace_0_by_star_2(i, j - 1, grid2)
        if j < dim - 1:
            replace_0_by_star_2(i, j + 1, grid2)
    return grid2
try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0
# Replace this comment with your code
grid1 = deepcopy(grid)
if grid[0][0] == 1:
    grid1 = replace_1_by_star(0, 0, grid1)
else:
    grid1 = replace_0_by_star(0, 0, grid1)

for i in range(dim):
    for j in range(dim):
        if grid1[i][j] == '*':
            size_of_largest_homogenous_region_from_top_left_corner += 1
'''
print()
for i in range(dim):
    print('   ', ' '.join(str(grid1[i][j]) for j in range(dim)))
'''

print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code
for i in range(dim):
    for j in range(dim):
        if grid[i][j] == 0:
            sum1 = 0
            grid2 = deepcopy(grid)
            grid2 = replace_0_by_star_2(i, j, grid2)
            for x in range(dim):
                for y in range(dim):
                    if grid2[x][y] == '*':
                      sum1 += 1
                      if sum1 > max_size_of_region_with_checkers_structure:
                          max_size_of_region_with_checkers_structure = sum1
'''
print()
for i in range(dim):
    print('   ', ' '.join(str(grid2[i][j]) for j in range(dim)))
'''
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )


