from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

      #  print('   ', ' '.join(str(int(grid[i][j])) for j in range(len(grid))))

def triangles_in_grid():
    if dim < 3:
        return {}
##################################################################################################################
    result = {}
    max_size = (dim + 1) // 2
    N1 = []
    N = []
    for size in range(2, max_size + 1):
        L1 = []
        for i in range(0, dim - size + 1):
            for j in range(size - 1, dim - size + 1):
                L1.append([grid[x][y] for x in range(i, i + size) for y in range(j - x + i, j + x - i + 1)])
        a = 0
        for i in range(0, len(L1)):
            if 0 not in L1[i]:
                a += 1
        if a == 0:
            break
        else:
            N1.append(a)
    if N1 != []:
        for b in range(0,len(N1) - 1):
            N.append(N1[b] - N1[b + 1])
        N.append(N1[len(N1)-1])
        N = sorted(list(zip(range(2, max_size + 1), N)), reverse = True)
        result.update({'N': N})
##################################################################################################################
    W1 = []
    W = []
    
    for size in range(2, max_size + 1):
        L2 = []
        a = 0
        for i in range(size - 1, dim - size + 1):
            for j in range(0, dim - size + 1):
                L2.append([grid[x][y] for y in range(j, j + size) for x in range(i - y + j, i + y - j + 1)])
        for i in range(0, len(L2)):
            if 0 not in L2[i]:
                a += 1
        if a == 0:
            break
        else:
            W1.append(a)
    if W1 != 0:
        for b in range(0,len(W1) - 1):
            W.append(W1[b] - W1[b + 1])
        W.append(W1[len(W1)-1])
        W = sorted(list(zip(range(2, max_size + 1), W)), reverse = True)
        result.update({'W': W})
    #return {'N': N, 'W': W}
##################################################################################################################
    S1 = []
    S = []
    for size in range(2, max_size + 1):
        L3 = []
        for i in range(size - 1, dim):
            for j in range(size - 1, dim - size + 1):
                L3.append([grid[x][y] for x in range(i - size + 1, i + 1) for y in range(j - i + x, j + i - x + 1)])
        a = 0
        for i in range(0, len(L3)):
            if 0 not in L3[i]:
                a += 1
        if a == 0:
            break
        else:
            S1.append(a)
    if S1 != []:
        for b in range(0,len(S1) - 1):
            S.append(S1[b] - S1[b + 1])
        S.append(S1[len(S1)-1])
        S = sorted(list(zip(range(2, max_size + 1), S)), reverse = True)
        result.update({'S': S})     
    #return {'N': N, 'W': W, 'S': S}
    #return {'N': N}
#################################################################################################################
    E1 = []
    E = []
    for size in range(2, max_size + 1):
        L4 = []
        for i in range(size - 1, dim - size + 1):
            for j in range(size - 1, dim):
                L4.append([grid[x][y] for y in range(j - size + 1, j + 1) for x in range(i - j + y, i + j - y + 1)])
        a = 0
        for i in range(0, len(L4)):
            if 0 not in L4[i]:
                a += 1
        if a == 0:
            break
        else:
            E1.append(a)
    if E1 != []:
        for b in range(0,len(E1) - 1):
            E.append(E1[b] - E1[b + 1])
        E.append(E1[len(E1)-1]) 
        E = sorted(list(zip(range(2, max_size + 1), E)), reverse = True)
        result.update({'E': E})
    return result
   
################################################################################################################
    #return {'N': N, 'W': W, 'S': S}
try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')

