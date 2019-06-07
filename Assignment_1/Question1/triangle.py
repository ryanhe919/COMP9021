# Written by *** for COMP9021
import sys
import copy
file_name = input('which data file do you want to use? ')
try:
    with open(f'{file_name}', 'r') as file:
        triangle_list = file.readlines()
    file.closed
except FileNotFoundError:
    print('Dont\'t find file. ')
    sys.exit()

for i in range(len(triangle_list)):
    triangle_list[i] = triangle_list[i].replace(' ', '')
    triangle_list[i] = triangle_list[i].replace('\n', '')
    triangle_list[i] = list(triangle_list[i])
    for j in range(len(triangle_list[i])):
        triangle_list[i][j] = int(triangle_list[i][j])

sum_list = []
for _ in range(len(triangle_list)):
    sum_list.append([0, [], 1])
for i in range(len(triangle_list) - 1, -1, -1):
    for j in range(i + 1):
        sum_list[j][0] += triangle_list[i][j]
        sum_list[j][1].insert(0, triangle_list[i][j])
    for j in range(i):
        if sum_list[j][0] == sum_list[j + 1][0]:
            sum_list[j][2] += sum_list[j + 1][2]
        if sum_list[j][0] < sum_list[j + 1][0]:
            sum_list[j] = copy.deepcopy(sum_list[j+1])

print(sum_list)
print(f'The largest sum is: {sum_list[0][0]}')
print(f'The number of paths yielding this sum is: {sum_list[0][2]}')
print(f'The leftmost path yielding this sum is: {sum_list[0][1]}')


